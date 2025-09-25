from selenium.webdriver.common.by import By

class CheckboxPage:
    def __init__(self, driver):
        """faz a inicializacao da pagina de checkbox"""
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"
        self.expand_all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.notes_checkbox = (By.XPATH, "//label[@for='tree-node-notes']")
        self.notes_input = (By.ID, "tree-node-notes")  
   

    def navigate(self):
        self.driver.get(self.url)

    def click_expand_all(self):
        expand = self.driver.find_element(*self.expand_all_button)
        expand.click()

    def check_notes_checkbox(self):
        notes_checkbox = self.driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
        notes_checkbox.click()
    
    def is_notes_checked(self):
        notes_input = self.driver.find_element(By.ID, "tree-node-notes")
        return notes_input.is_selected()