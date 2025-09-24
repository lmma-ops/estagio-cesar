from selenium.webdriver.common.by import By
import time

def test_check_box(driver):
    driver.get("https://demoqa.com/checkbox")
    time.sleep(2)  # Wait for the page to load
    
    # Expand the tree
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()
    time.sleep(2)  # Wait for the tree to expand
    
    # Select the checkbox "Notes"
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
    notes_checkbox.click()
    time.sleep(2)  # Wait for the action to complete
    
    # Validate if checkbox was ticked
    notes_input = driver.find_element(By.ID, "tree-node-notes")
    assert notes_input.is_selected()
    time.sleep(2)

def test_check_box_command(driver):
    driver.get("https://demoqa.com/checkbox")
    time.sleep(2)  # Wait for the page to load
        
    # Expand the tree
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()
    time.sleep(2)  # Wait for the tree to expand
        
    # Select the checkbox "Notes"
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-commands']")
    notes_checkbox.click()
    time.sleep(2)  # Wait for the action to complete
        
    # Validate if checkbox was unticked
    notes_input = driver.find_element(By.ID, "tree-node-commands")
    assert notes_input.is_selected()
    time.sleep(2)