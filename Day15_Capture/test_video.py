import pytest
from playwright.sync_api import Playwright, expect,sync_playwright

def test_video_capture(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size ={"width":1024, "height":768}

    )
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    context.close()
    browser.close()