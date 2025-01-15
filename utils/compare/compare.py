from deepdiff import DeepDiff

from typing import Any

from utils.logger.logger import file_logger


log = file_logger(__name__)


def is_eql(actual: dict[str, Any], expected: dict[str, Any]) -> bool:
    diff = DeepDiff(actual, expected)

    log.info("Начало сравнения фактического и ожидаемого словаря")
    if not diff:
        log.info("Словари одинаковые")
        return True
    else:
        log.error("Словари разные: %s", diff)
        return False
