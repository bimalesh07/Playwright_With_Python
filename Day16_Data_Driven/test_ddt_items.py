import pytest
from playwright.sync_api import expect, Playwright, Page

search_itmes = ['laptop','Gift card','smartphone','monitor']

@pytest.mark.parametrize("item", search_itmes)
def test_search_item(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item) # we need to pass item name
    page.locator("input[value='Search']").click()


    #asserctions
    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item, ignore_case=True)