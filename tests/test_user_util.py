import pytest
from src.user_util import user_format


@pytest.fixture
def user_fixture():
    return [{"title": 'Frontend-разработчик', "url": 'https://hh.ru/v', "salary_from": 70000, "employer": 'Нордавинд'}]


def test_user_format(user_fixture):
    vacancies = user_format(user_fixture)
    for vacancy in vacancies:
        assert str(vacancy) == 'Frontend-разработчик (https://hh.ru/v)'
