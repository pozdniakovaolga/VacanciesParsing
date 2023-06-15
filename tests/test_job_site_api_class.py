import pytest
from src.job_site_api_class import HeadHunterAPI, SuperJobAPI


@pytest.fixture
def hh_fixture():
    return {'items': [{'id': '81910657', 'premium': False, 'name': 'Frontend-разработчик', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 70000, 'to': None, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2023-06-14T14:56:15+0300', 'created_at': '2023-06-14T14:56:15+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=81910657', 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/81910657?host=hh.ru', 'adv_response_url': None, 'alternate_url': 'https://hh.ru/vacancy/81910657', 'relations': [], 'employer': {'id': '1178506', 'name': 'Нордавинд', 'url': 'https://api.hh.ru/employers/1178506', 'alternate_url': 'https://hh.ru/employer/1178506', 'logo_urls': {'original': 'https://hhcdn.ru/employer-logo-original/1056714.png', '90': 'https://hhcdn.ru/employer-logo/5847497.png', '240': 'https://hhcdn.ru/employer-logo/5847498.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1178506', 'accredited_it_employer': True, 'trusted': True}, 'snippet': {'requirement': 'Знание JavaScript (ES6, node, webpack, Lodash, Moment.js, jQuery), HTML5, CSS3, <highlighttext>Python</highlighttext>, React, TypeScript, SCSS Modules. - ', 'responsibility': 'Разработка приложения, являющегося клиентской частью программного комплекса, и интеграция его с ядром программы.'}, 'contacts': None, 'schedule': None, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}}]}


@pytest.fixture
def sj_fixture():
    return {'objects': [{'canEdit': False, 'is_closed': False, 'id': 37984527, 'id_client': 3237849, 'payment_from': 15000, 'payment_to': 0, 'date_pub_to': 1687028103, 'date_archived': 0, 'date_published': 1686766503, 'address': None, 'profession': 'Специалист службы поддержки', 'work': None, 'compensation': None, 'candidat': 'К', 'metro': [], 'currency': 'rub', 'vacancyRichText': '<p>Каждый день', 'covid_vaccination_requirement': {'id': 1, 'title': 'Не важно'}, 'moveable': True, 'agreement': False, 'anonymous': False, 'is_archive': False, 'is_storage': False, 'type_of_work': {'id': 10, 'title': 'Неполный рабочий день'}, 'place_of_work': {'id': 2, 'title': 'Удалённая работа (на дому)'}, 'education': {'id': 0, 'title': 'Не имеет значения'}, 'experience': {'id': 1, 'title': 'Без опыта'}, 'maritalstatus': {'id': 0, 'title': 'Не имеет значения'}, 'children': {'id': 0, 'title': 'Не имеет значения'}, 'client': {'id': 3237849, 'title': 'Яндекс/ООО "ЯНДЕКС"', 'link': 'https://www.superjob.ru/clients/yandeks-ooo-yandeks-3237849/vacancies.html', 'industry': [], 'description': 'Поисковая система и интернет-портал.', 'vacancy_count': 17621, 'staff_count': 'более 5000', 'client_logo': 'https://public.superjob.ru/images/clients_logos.ru/3237849_daa40cb82b789026a6a0faa84128f2fd.jpg', 'address': None, 'addresses': [], 'url': 'https://yandex.ru', 'short_reg': False, 'is_blocked': False, 'registered_date': 1499948707, 'town': {'id': 4, 'title': 'Москва', 'declension': 'в Москве', 'hasMetro': True, 'genitive': 'Москвы'}}, 'languages': [], 'driving_licence': [], 'catalogues': [{'id': 33, 'title': 'IT, Интернет, связь, телеком', 'key': 33, 'positions': [{'id': 51, 'title': 'Системное администрирование', 'key': 51}, {'id': 57, 'title': 'Техническая поддержка', 'key': 57}, {'id': 60, 'title': 'Другое', 'key': 60}, {'id': 61, 'title': 'Начало карьеры, мало опыта', 'key': 61}, {'id': 503, 'title': 'Внедрение и сопровождение ПО', 'key': 503}]}], 'agency': {'id': 1, 'title': 'прямой работодатель'}, 'town': {'id': 4, 'title': 'Москва', 'declension': 'в Москве', 'hasMetro': True, 'genitive': 'Москвы'}, 'already_sent_on_vacancy': False, 'rejected': False, 'response_info': [], 'phone': None, 'phones': None, 'fax': None, 'faxes': None, 'client_logo': 'https://public.superjob.ru/images/clients_logos.ru/3237849_daa40cb82b789026a6a0faa84128f2fd.jpg', 'highlight': True, 'age_from': 0, 'age_to': 0, 'gender': {'id': 0, 'title': 'Не имеет значения'}, 'firm_name': 'Яндекс', 'firm_activity': 'Поисковая система и интернет-портал.', 'link': 'https://www.superjob.ru/vakansii/specialist-sluzhby-podderzhki-37984527.html', 'latitude': None, 'longitude': None}]}


def test_get_vacancies_hh():
    hh = HeadHunterAPI()
    assert type(hh.get_vacancies("python")) == dict


def test_clean_vacancies_hh(hh_fixture):
    hh = HeadHunterAPI()
    assert hh.clean_vacancies(hh_fixture) == [{'title': 'Frontend-разработчик', 'url': 'https://hh.ru/vacancy/81910657', 'salary_from': 70000, 'employer': 'Нордавинд'}]


def test_clean_vacancies_sj(sj_fixture):
    sj = SuperJobAPI()
    assert sj.clean_vacancies(sj_fixture) == [{'title': 'Специалист службы поддержки', 'url': 'https://www.superjob.ru/vakansii/specialist-sluzhby-podderzhki-37984527.html', 'salary_from': 15000, 'employer': 'Яндекс/ООО "ЯНДЕКС"'}]
