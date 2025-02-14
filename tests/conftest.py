import allure
import os

import pytest
from pytest_metadata.plugin import metadata_key

from dotenv import dotenv_values

from utils.logger.logger import file_logger


log = file_logger(__name__)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=".env.local")


def pytest_configure(config):
    config.stash[metadata_key]["Env"] = config.getoption("--env")
    del config.stash[metadata_key]["Packages"]
    del config.stash[metadata_key]["Plugins"]
    del config.stash[metadata_key]["JAVA_HOME"]


@allure.title("Загрузка конфигурационного файла")
@pytest.fixture(scope="session")
def env_config(pytestconfig):
    env = pytestconfig.getoption("--env")
    if not os.path.exists(env):
        log.error(f"Конфигурационный файл '{env}' не найден")
        raise FileNotFoundError()
    return dotenv_values(env)


@pytest.fixture(scope="session")
def test_case_ids_list():
    return []


@pytest.fixture(scope="function", autouse=True)
def test_case_id(request, test_case_ids_list):
    tc_id = request.node.get_closest_marker("test_case_id")
    if tc_id:
        tc_id_value = tc_id.args[0]
        test_case_ids_list.append(tc_id_value)
        return tc_id_value
    return None


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(3, "<th>Test case link</th>")
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(3, f"<td><a href='http://localhost/{report.tc_id}'>{report.tc_id}</a></td>")
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.tc_id = str(item.get_closest_marker("test_case_id").args[0])
