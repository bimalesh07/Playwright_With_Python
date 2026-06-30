from playwright.sync_api import Page, expect
import datetime


def test_capture_my_screen(page): 

    page.goto("https://demowebshop.tricentis.com/")

    #Dynamic Time aur Date banaya (Filename unique rakhne ke liye)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    #PURE PAGE ka screenshot (Visible ya Full Page)
    # page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)

    #SPECIFIC ELEMENT (Logo) ka screenshot
    logo = page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshots/logo_{timestamp}.png")