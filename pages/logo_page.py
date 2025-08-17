import allure
from data import URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoPage(BasePage):

    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    ORDER_UPPER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")

    @allure.step('Кликаем на кнопку Заказать сверху')
    def click_order_button(self):
        self.wait_and_find_element(self.ORDER_UPPER_BUTTON).click()

    @allure.step('Кликаем по лого Самокат')
    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step('Кликаем по лого Яндекс')
    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)

    @allure.step('Ожидаем пока страница станет Дзен')
    def wait_for_url_changes_dzen(self):
        self.wait_for_url_changes(URL.DZEN_PAGE)

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Кликаем на кнопку Заказать для перехода на другу страницу и клик на лого самоката, чтобы вернуться обратно домой')
    def click_order_and_click_logo_scooter_back(self):
        self.click_order_button()
        self.click_logo_scooter()
