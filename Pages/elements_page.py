from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        self.menu_check_box_id = (By.ID, "item-0")

    def navigate(self):
        self.driver.get(self.url)

    def is_check_box_css_is_visible(self):
        check_box_css = self.driver.find_element(By.CSS_SELECTOR, ".element-list.collapse.show li#item-0")
        return check_box_css.is_displayed()
    
    def is_check_box_id_visible(self):
        check_box_id = self.driver.find_element(By.ID, "item-0")
        return check_box_id.is_displayed()  
    
    def get_menu_check_box_id_text(self):
        return self.driver.find_element(*self.menu_check_box_id).text
    