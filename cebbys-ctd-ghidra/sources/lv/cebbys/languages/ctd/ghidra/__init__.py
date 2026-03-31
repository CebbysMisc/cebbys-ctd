from lv.cebbys.languages.ctd.ghidra.process.synchronize import (
    Synchronizer,
)
from pyghidra.launcher import (
    GuiPyGhidraLauncher,
)
from pyghidra import (
    open_program,
    gui,
)
from pathlib import (
    Path,
)
from atexit import (
    register,
)

GHIDRA_HOME = Path("C:/Tools/Ghidra/Ghidra 12.0.3").resolve()


def main(roots: list[Path]) -> None:
    global GHIDRA_HOME

    synchronizer = Synchronizer(roots)
    synchronizer.start()

    def on_exit():
        print("Exiting, stopping and joining threads")
        synchronizer.stop()
        synchronizer.join()
        print("Threads closed and joined successfully")

    register(on_exit)

    launcher = GuiPyGhidraLauncher(False, install_dir=GHIDRA_HOME)
    launcher.start()  # type: ignore
