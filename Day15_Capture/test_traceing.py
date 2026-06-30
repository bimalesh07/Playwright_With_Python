from playwright.sync_api import Playwright, expect
import pytest

def test_video_capture(playwright: Playwright):
    # 1. Browser aur Context chalu kiya
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # 2.(Trace) Shuru kiya: Photo aur HTML dono record honge
    context.tracing.start(screenshots=True, snapshots=True)
    
    # 3. Normal test case ka kaam kiya
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    # 4. (Trace) Band kiya aur saara data 'trace.zip' me save kar diya
    context.tracing.stop(path="trace.zip")

    # 5. Browser close kiya
    context.close()
    browser.close()

"""playwright show-trace trace.zip"""
"""python -m playwright show-trace trace.zip"""