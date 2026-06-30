import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page

# =========================================================================
# BROWSER CONTEXT & MULTI-PAGE AUTOMATION
# =========================================================================
def test_browsercontext(playwright: Playwright):
    # 1. Browser lunch
    browser = playwright.chromium.launch(headless=False)
    
    # 2. Isolated Incognito Window (Context) Banaya
    context = browser.new_context()

    # 3. Us context ke andar do alag-alag TABS (Pages) khole
    page1 = context.new_page()  # Tab 1
    page2 = context.new_page()  # Tab 2

    # --- Tab 1 Automation ---
    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    # --- Tab 2 Automation ---
    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")

    # Clean up: Context aur Browser ko close karna achhi practice hai
    context.close()
    browser.close()