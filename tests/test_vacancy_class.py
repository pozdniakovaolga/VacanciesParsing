import pytest
from src.vacancy_class import Vacancy


@pytest.fixture
def vacancy_fixture():
    return Vacancy('Frontend-разработчик', 'https://hh.ru/vacancy/81910657', 70000, 'Нордавинд')


def test___str__(vacancy_fixture):
    assert str(vacancy_fixture) == 'Frontend-разработчик (https://hh.ru/vacancy/81910657)'


def test___repr__(vacancy_fixture):
    assert repr(vacancy_fixture) == "Vacancy(Frontend-разработчик, https://hh.ru/vacancy/81910657, 70000, Нордавинд)"


def test_is_valid_title_empty(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.title = ""


def test_is_valid_title_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.title = 12


def test_is_valid_url_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.url = 12


def test_is_valid_url_start(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.url = "url"


def test_is_valid_salary_str(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.url = "abc"


def test_is_valid_employer_empty(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.employer = ""


def test_is_valid_employer_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.employer = 12


def test__gt__(vacancy_fixture):
    hh = Vacancy('Front', 'https://hh.ru/vacancy/81', 70, 'Норд')
    assert vacancy_fixture.__gt__(hh) == True


def test__lt__(vacancy_fixture):
    hh = Vacancy('Front', 'https://hh.ru/vacancy/81', 70, 'Норд')
    assert vacancy_fixture.__lt__(hh) == False
