import pytest
from playwright.sync_api import sync_playwright, expect , Page


def test_date_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input_date = page.locator("#datepicker")

    #Approch1
    input_date.fill("10/15/2025")
    expect(input_date).to_have_value("10/15/2025")

    #Approch2
    is_future = True
    year ="2025"
    month ="October"
    date = "15"
    



    page.wait_for_timeout(3000)

