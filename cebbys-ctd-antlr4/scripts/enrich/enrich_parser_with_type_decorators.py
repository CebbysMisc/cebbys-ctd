import rich.console as Console
import rich.syntax as Syntax
import argparse as Argparse
import pathlib as Pathlib
import difflib as Difflib

CONSOLE = Console.Console()
SHOW_DIFF = True

def main():
    parser: Argparse.ArgumentParser
    args: Argparse.Namespace
    file_path: Pathlib.Path
    
    parser = Argparse.ArgumentParser(
        description="Enrich parser file with type decorators"
    )
    parser.add_argument(
        "file",
        type=str,
        help="Path to the parser file to enrich"
    )
    
    args = parser.parse_args()
    file_path = Pathlib.Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return
    
    if not file_path.is_file():
        print(f"Error: Path is not a file: {file_path}")
        return
    
    original = file_path.read_text("utf-8")
    modified = decorate(original)
    file_path.write_text(modified, "utf-8")

    if SHOW_DIFF:
        diff = "\n".join(Difflib.unified_diff(
            original.splitlines(),
            modified.splitlines(),
            lineterm=''
        ))
        syntax = Syntax.Syntax(
            diff, "diff", theme="ansi_dark", line_numbers=True
        )
        CONSOLE.print(syntax)

def decorate(content:str) -> str:
    header: list[str] = []
    lines: list[str] = content.splitlines()

    while len(content) > 0:
        line = lines.pop(0)
        header.append(line)
        if "class CtdParser ( Parser ):" in line:
            break

    header.insert(2, "import typing as Typing")

    for i in range(len(lines)):
        line = lines[i]
        if line.strip().startswith("def "):
            if "=None" in line:
                updated = line.replace("=None", "|None = None")
                lines[i] = updated
                line = updated


    i: int = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("def "):
            if _is_getter(i, lines):
                datatype = lines[i+1]
                datatype = datatype[datatype.index("(") + 1:datatype.index(")") - 2]
                line = line.replace("):", f") -> '{datatype}':")
                lines[i] = line
            elif _is_indexed_getter(i, lines):
                prefix = " " * line.index("d")
                name = line[line.index("d") + 4:line.index("(")]
                datatype = lines[i+2]
                datatype = datatype[datatype.index("(") + 1:datatype.index(")")]

                decorator = [
                    f"{prefix}@Typing.overload",
                    f"{prefix}def {name}(self) -> 'list[{datatype}]': ...",
                    f"{prefix}@Typing.overload",
                    f"{prefix}def {name}(self, i:int) -> '{datatype}': ...",
                ]
                decorator.reverse()
                for d in decorator:
                    lines.insert(i, d)
                i += len(decorator)

        i += 1
    
    return "\n".join(header) + "\n" + "\n".join(lines)

def _is_indexed_getter(i: int, lines:list[str]):
    return "if i is None:" in lines[i+1] and "getTypedRuleContexts" in lines[i+2] and "else:" in lines[i+3]

def _is_getter(i: int, lines:list[str]):
    return "return self.getTypedRuleContext" in lines[i+1]

if __name__ == "__main__":
    main()