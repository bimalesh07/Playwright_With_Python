import pytest
from playwright.sync_api import Page, expect
import re

# ==============================================================================
# #1 USING XPATH: Jab text badal raha ho toh 'or' condition lagana
# ==============================================================================
def test_handle_dynamic_elements_xpath(page: Page):
    # Blog site 
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # Loop chalaya taaki 5 baar button daba sakein (START -> STOP -> START...)
    for i in range(5):
        #Note: XPath me 'or' lagakar humne bola ki chahe START likha ho ya STOP, dono ko pakad lo!
        button = page.locator("//button[text()='START' or text()='STOP']")
        button.click()
        page.wait_for_timeout(2000)


# ==============================================================================
# #2 REMEDY USING CSS SELECTOR: starts-with (^=) ka Most of Time we use This 
# ==============================================================================
def test_handle_dynamic_elements_css(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    for i in range(5):
        #Note: CSS selector me ^= ka matlab hota hai 'starts with'. 
        # Kyunki START aur STOP dono ki shuruat 'st' se hoti hai, toh dono catch ho jayenge!
        button = page.locator("button[name^='st']")
        button.click()
        page.wait_for_timeout(2000)


# ==============================================================================
# #3 REMEDY USING BUILT-IN LOCATOR: Regular Expression (Regex) ke sath
# ==============================================================================
def test_handle_dynamic_elements_builtin(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    for i in range(5):
        #re.compile(r'ST.*') ka matlab hai: Aisa button jiska naam 'ST' se shuru ho aur aage kuch bhi (.*) ho!
        button = page.get_by_role(role="button", name=re.compile(r'ST.*', re.IGNORECASE))
        button.click()
        page.wait_for_timeout(2000)