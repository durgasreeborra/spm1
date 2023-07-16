import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with the actual path to the ChromeDriver executable

# Selecting English as the Source Language and Entering Text
def test_select_source_language_and_enter_text():
    driver.get("durgasree.site/index.html")  # Replace with the actual file path

    # Wait for the source language select element to be present
    time.sleep(2)  # Wait for 2 seconds (adjust as needed)

    source_language_select = driver.find_element(By.CSS_SELECTOR, ".controls .row.from select")
    source_text_area = driver.find_element(By.CSS_SELECTOR, ".text-input .from-text")

    # Test Case 1:Select English as the source language
    source_language_code = "en"  # Replace with the desired source language code, for example, "en-GB" for English
    source_language_select.click()  # Open the select dropdown

    time.sleep(2)  # Wait for 1 second (adjust as needed)

    source_language_option = driver.find_element(By.CSS_SELECTOR, f".controls .row.from select option[value='{source_language_code}']")
    source_language_option.click()
    time.sleep(2)
    # test-case 2: Verify the selected language by checking the selected option's value
    selected_option = source_language_select.find_element(By.CSS_SELECTOR, "option:checked")
    assert selected_option.get_attribute("value") == source_language_code
    time.sleep(2)
    # Test Case 3:Enter text in the source text area
    text_to_translate = "Hello, how are you?"  # Replace with the desired text to translate
    source_text_area.clear()
    source_text_area.send_keys(text_to_translate)

    # Additional test steps for Test Case 1
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    target_language_select = driver.find_element(By.CSS_SELECTOR, ".controls .row.to select")
    translate_btn = driver.find_element(By.CSS_SELECTOR, "button")

    # Test Case 4:Select  the target language
    target_language_code = "es"  # Replace with the desired target language code, for example, "es-ES" for Spanish
    target_language_select.click()  # Open the select dropdown

    time.sleep(2)  # Wait for 1 second (adjust as needed)

    target_language_option = driver.find_element(By.CSS_SELECTOR, f".controls .row.to select option[value='{target_language_code}']")
    target_language_option.click()
    time.sleep(2)  
    #Test Case 5: Verify the selected target language by checking the selected option's value
    selected_option = target_language_select.find_element(By.CSS_SELECTOR, "option:checked")
    assert selected_option.get_attribute("value") == target_language_code

    #Test Case 6:Click the translate button
    translate_btn.click()

    # Additional test steps for Test Case 2
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)


# Run all the test cases
test_select_source_language_and_enter_text()

# Close the WebDriver
driver.quit()
