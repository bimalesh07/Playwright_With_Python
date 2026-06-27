import pytest
from playwright.sync_api import  Page, expect


def test_multi_selected_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #selected Multiple from tech dropdown
    #page.locator('#colors').select_option(["Red","Blue","Green"]) #by lable
    #page.locator("#colors").select_option(label=["Red","Blue","Green"]) #by label


    # page.locator("#colors").select_option(value=["red","white", "green"]) #by values
    #page.locator("#colors").select_option(index=[4, 3]) #by index

    #count
    drowpdown_options = page.locator("#colors>option")
    expect(drowpdown_options).to_have_count(7)


    page.wait_for_timeout(5000)






