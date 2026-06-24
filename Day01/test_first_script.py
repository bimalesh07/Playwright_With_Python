from playwright.sync_api import expect, Page

def test_google_search_easy(page: Page):
    page.goto("https://google.com")
    search_box = page.get_by_title("Search")
    
    # Is line ko exact aise badal lo (www. aur slash lagakar):
    expect(page).to_have_url("https://www.google.com/")


