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
        logger.debug("Ghidra is not started, cannot synchronize types")
        return

    database_path = Path("ctd_types.db").resolve()
    logger.debug(f"Opening database connection at {database_path}")
    connector = DatatypeConnector(database_path)

    logger.debug("Ghidra is started, synchronizing types...")
    try:
        api = get_interpreter()
        if api:
            program = api.currentProgram
            logger.debug(f"Loading CTDs with {program}...")
            loader = CtdLoader(roots)
            definitions = list(loader.definitions.values())
            result = connector.synchronize(program, definitions)
            if not result:
                sleep(10)
    except BaseException as e:
        logger.error(f"Error during synchronization: {e}", exc_info=True)
        sleep(9)
    finally:
        connector.close()

    sleep(1)


def get_interpreter() -> "FlatProgramAPI|None":
    try:
        return get_current_interpreter()  # type: ignore
    except BaseException as e:
        logger.error(f"Error getting interpreter: {e}", exc_info=True)
        return None
