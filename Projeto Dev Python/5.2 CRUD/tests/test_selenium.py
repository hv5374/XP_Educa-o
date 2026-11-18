from selenium import webdriver
import pytest

@pytest.mark.selenium
def test_selenium():
    driver = webdriver.Chrome()  # or any other browser driver
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()