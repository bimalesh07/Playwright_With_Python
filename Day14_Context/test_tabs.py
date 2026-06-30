from playwright.sync_api import sync_playwright, expect, Page, Playwright

def test_handle_tabs(playwright: Playwright):
    # 🏎️ Spelling sahi ki: 'browser'
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parentpage = context.new_page()
    parentpage.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    # Register an event for handle tab
    with context.expect_page() as tabwindows:
        parentpage.locator("button:has-text('New Tab')").click()
    
    #'.value' ke aage se brackets () no use
    tab_value = tabwindows.value
    tab_value.wait_for_load_state()

    # '.pages' ke aage se brackets () no use
    all_page = context.pages
    print("Total pages of:", len(all_page))

    child_page = all_page[1]
    print("url of child page:", child_page.url)
    
   
    context.close()
    browser.close()