import pytest
from playwright.sync_api import sync_playwright, Playwright, Page, expect


"""bypass of auth then direct"""
@pytest.mark.skip
def test_authPopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("text=Congratulations")).to_be_visible()
    page.wait_for_timeout(5000)


"""Best Approch"""
def test_admin_auth(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    
    # Context banate waqt hi admin ke credentials pass kar diye
    context = browser.new_context(
        http_credentials={
            "username": "admin",     
            "password": "admin_password" 
        }
    )
    
    #new page
    page = context.new_page()

    # popup automatic bypass 
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    
    page.wait_for_timeout(3000)
    context.close()
    browser.close()