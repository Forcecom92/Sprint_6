import allure
from pages.logo_page import LogoPage
from data import URL


class TestLogoPage:

    @allure.title('Проверка возврата на домашнюю страницу по клику на логотип Самоката')
    @allure.description('Кликаем на кнопку "Принять куки", далее на кнопку "Заказать", чтобы уйти с домашней страницы, а потом возвращаемся на нее обратно')
    def test_logo_scooter(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_cookie()
        logo_page.click_order_button()
        logo_page.click_logo_scooter()

        assert logo_page.get_current_url() == URL.FIRST_PAGE
