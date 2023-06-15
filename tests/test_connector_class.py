import pytest
from src.connector_class import JsonConnector
import os


@pytest.fixture
def vacancies_fixture():
    return [{'title': 'Frontend-разработчик', 'url': 'https://hh.ru/vacancy/81910657', 'salary_from': 70000, 'employer': 'Нордавинд'}, {'title': 'Специалист службы поддержки', 'url': 'https://www.superjob.ru/vakansii/specialist-sluzhby-podderzhki-37984527.html', 'salary_from': 15000, 'employer': 'Яндекс/ООО "ЯНДЕКС"'}]

@pytest.fixture
def connector_fixture():
    test_connector = JsonConnector()
    test_connector.file_name = "test.json"
    return test_connector


def test_add_vacancies(vacancies_fixture, connector_fixture):
    connector_fixture.add_vacancies(vacancies_fixture)  # проверка записи в пустой файл
    connector_fixture.add_vacancies(vacancies_fixture)  # проверка записи в непустой файл
    assert os.stat(connector_fixture.file_name).st_size != 0
    connector_fixture.delete_vacancies()


def test_filter_vacancies(vacancies_fixture, connector_fixture):
    connector_fixture.add_vacancies(vacancies_fixture)
    assert connector_fixture.filter_vacancies("разработчик") == [{'title': 'Frontend-разработчик', 'url': 'https://hh.ru/vacancy/81910657', 'salary_from': 70000, 'employer': 'Нордавинд'}]
    connector_fixture.delete_vacancies()


def test_top_vacancies(vacancies_fixture, connector_fixture):
    connector_fixture.add_vacancies(vacancies_fixture)
    assert connector_fixture.top_vacancies(1) == [{'title': 'Frontend-разработчик', 'url': 'https://hh.ru/vacancy/81910657', 'salary_from': 70000, 'employer': 'Нордавинд'}]
    connector_fixture.delete_vacancies()


def test_delete_vacancies(vacancies_fixture, connector_fixture):
    connector_fixture.add_vacancies(vacancies_fixture)
    connector_fixture.delete_vacancies()
    assert os.stat(connector_fixture.file_name).st_size == 0
