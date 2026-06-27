import pytest
from playwright.sync_api import Page, expect

def test_inputbox(page: Page):
    # Step 1: Website open karna
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # Step 2: Name wale input box ko uski ID (#name) se pakadna
    text_box = page.locator("#name")

    # --------------------------------------------------------------------------
    # KYUN USE KIYA? -> Takki confirm ho sake box sahi salamat screen par hai aur chal raha hai.
    # --------------------------------------------------------------------------
    expect(text_box).to_be_visible()  # Check kiya ki box dikh raha hai ya nahi
    expect(text_box).to_be_enabled()  # Check kiya ki box active (typing ke liye ready) hai ya nahi

    # --------------------------------------------------------------------------
    # KYUN USE KIYA? -> Check karne ke liye ki developer ne box me max 15 letters ki limit lagai hai ya nahi.
    # --------------------------------------------------------------------------
    # Yeh Playwright ka smart locator assertion hai (Auto-wait ke sath)
    expect(text_box).to_have_attribute("maxlength", "15")

    # --------------------------------------------------------------------------
    # KYUN USE KIYA? -> Agar hume limit ka pata lagakar use terminal me print karna ho.
    # --------------------------------------------------------------------------
    maxlength = text_box.get_attribute("maxlength") # Box ke andar se '15' nikal kar laya
    print("Is box me maximum itne letters aa sakte hain:", maxlength)

    # --------------------------------------------------------------------------
    # KYUN USE KIYA? -> Box ke andar apna naam type karne ke liye.
    # --------------------------------------------------------------------------
    text_box.fill("bimalesh") # Typing action

    # --------------------------------------------------------------------------
    # KYUN USE KIYA? -> Yeh check karne ke liye ki jo maine type kiya, kya woh sach me box me gaya?
    # --------------------------------------------------------------------------
    # Note: Kisi bhi input box ke andar likha hua text nikalne ke liye hamesha '.input_value()' use hota hai.
    entervalue = text_box.input_value() 
    print("Humne box me ye naam enter kiya hai:", entervalue)
    
    # chaho toh ispe bhi assertion laga sakte ho aise:
    assert entervalue == "bimalesh"