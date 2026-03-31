from lv.cebbys.languages.ctd.utility.logging import (
    get_logger,
)
from lv.cebbys.languages.ctd.ghidra.datatype import (
    DatatypeConnector,
)
from lv.cebbys.languages.ctd.loader import (
    CtdLoader,
)
from ghidra.program.flatapi import (  # type: ignore
    FlatProgramAPI,
)
from pyghidra import (
    get_current_interpreter,
    started,
)
from pathlib import (
    Path,
)
from time import (
    sleep,
)

logger = get_logger(__name__)


def tick(roots: list[Path]) -> None:
    if not started():
        logger.info("Ghidra is not started, cannot synchronize types")
        return

    database_path = Path("ctd_types.db").resolve()
    logger.info(f"Opening database connection at {database_path}")
    connector = DatatypeConnector(database_path)

    logger.info("Ghidra is started, synchronizing types...")
    try:
        api = get_interpreter()
        if api:
            program = api.currentProgram
            logger.info(f"Loading CTDs with {program}...")
            loader = CtdLoader(roots)
            definitions = list(loader.definitions.values())
            connector.synchronize(program, definitions)
    except BaseException as e:
        logger.error(f"Error during synchronization: {e}", exc_info=True)
    finally:
        connector.close()

    sleep(10)


def get_interpreter() -> "FlatProgramAPI|None":
    try:
        return get_current_interpreter()  # type: ignore
    except BaseException as e:
        logger.error(f"Error getting interpreter: {e}", exc_info=True)
        return None
