import pytest
from selenium import webdriver
import requests

from urls import Urls
from faker import Faker



@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()


@pytest.fixture
def create_user_and_get_token():
    fake = Faker()
    """Создаёт пользователя через API и возвращает токен + данные, удаляем после теста"""
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    payload = {
        "email": email,
        "password": password,
        "name": name,
    }

    
    requests.post(
        Urls.REGISTER_USER,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    
    response = requests.post(
        Urls.LOGIN_USER,
        json={
            "email": email,
            "password": password,
        },
    )

    token = response.json().get("accessToken", "")

    yield {
        "email": email,
        "password": password,
        "name": name,
        "token": token,
    }

    
    if token:
        requests.delete(f"{Urls.MAIN_URL_API}auth/user", headers={"Authorization": token})

