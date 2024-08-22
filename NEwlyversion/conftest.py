import pytest
from selenium import webdriver


@pytest.fixture
def Setup():
    driver = webdriver.Chrome()
    driver.get("https://automationpanda.com/2024/06/11/running-tests-in-a-java-maven-project/")
    driver.maximize_window()
    return driver


@pytest.fixture()
def Set_up():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(params=
[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com1", "Credence@123"),
    ("Credencetest@test.com", "Credence@1231"),
    ("Credencetest@test.com1", "Credence@1231")
])
def getedataforliggo(request):
    return request.param
