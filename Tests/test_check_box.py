from selenium.webdriver.common.by import By
from Pages.check_box_page import CheckboxPage

def test_check_box_page(driver):
    """Testa a funcionalidade da pagina de checkbox"""
    checkbox_page = CheckboxPage(driver)
    checkbox_page.navigate()
    checkbox_page.click_expand_all()
    checkbox_page.check_notes_checkbox()
    assert checkbox_page.is_notes_checked()

