import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_product_view_sku(browser):
    """
    Test case WERT-1:Открытие деталей товара. Проверка артикула:
    """ 

        # запускаем браузер с указанными выше настройками

        # определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    browser.get(url=url)
        # ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
    # ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()
    # ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
        # проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"


@pytest.mark.smoke #метка для возможности запуска этого теста отдельго
def test_smoke():
    """
    Test case SMK-1:
     """ 
    # Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    #chrome_options.add_argument("--headless") # спец. режим "без браузера"  
    # устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
# а вот так с сохранением отчетов в формате allure
#pytest /Users/alex/Desktop/PythonProjects/TestQAStudioShop/tests/qa_studio_shop/test_smoke.py::test_product_view_sku --alluredir=my_allure_results 
#pytest /Users/alex/Desktop/PythonProjects/TestQAStudioShop/tests --alluredir=my_allure_results сразу для всех
# а вот так просто запуск тестов
#pytest /Users/alex/Desktop/PythonProjects/TestQAStudioShop/Tests/test_smoke.py::test_product_view_sku
# pytest -m smoke - запуск автотеста одного по метке
#./allure serve /Users/alex/Desktop/PythonProjects/TestQAStudioShop/my_allure_results команда для запуска allure из его папки bin
# /Users/alex/Desktop/PythonProjects/allure-2.19.0/bin/allure serve /Users/alex/Desktop/PythonProjects/TestQAStudioShop/my_allure_results сразу запуск allure