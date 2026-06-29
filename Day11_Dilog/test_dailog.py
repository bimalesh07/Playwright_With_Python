import pytest
from playwright.sync_api import Page, expect

# =========================================================================
# 1. SIMPLE DIALOG (Sirf "OK" Button Hota Hai)
# =========================================================================
def test_dialog_simple(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(300)

    #Lambda expression: direct bina kisi function ke 1 line me accept (OK) kiya
    page.on("dialog", lambda dialog: dialog.accept()) 
    
    page.locator("#alertBtn").click() # Opens dialog
    page.wait_for_timeout(3000)


# =========================================================================
# 2.CONFIRM BOX WITH "OK" (Dono options hain, par hum OK dabayenge)
# =========================================================================
def test_dialog_confirm_ok(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(300)

    # .accept() matlab "OK" par click hoga
    page.on("dialog", lambda dialog: dialog.accept()) 
    
    page.locator("#confirmBtn").click() 
    
    # Validation: Check kiya ki UI par success text aaya ya nahi
    expect(page.locator("#demo")).to_have_text("You pressed OK!")
    page.wait_for_timeout(3000)


# =========================================================================
# 3. CONFIRM BOX WITH "CANCEL" (Dono options hain, par hum Cancel dabayenge)
# =========================================================================
def test_dialog_confirm_cancel(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(300)

    # .dismiss() matlab "Cancel" par click hoga
    page.on("dialog", lambda dialog: dialog.dismiss()) 
    
    page.locator("#confirmBtn").click() 
    
    # Validation: Check kiya ki Cancel wala text aaya
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(3000)


# =========================================================================
# 4. PROMPT BOX (Input field + Alert Text Check + OK/Cancel)
# =========================================================================
def test_dialog_prompt_with_input(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(300)

    # Complex logic ke liye lambda ki jagah alag se function bana kar register kiya
    def handle_prompt(dialog):
        # 1. Alert ke andar ka text verify kiya
        assert dialog.message == "Please enter your name:"
        
        # 2. Input box me text bhara aur OK (.accept) kiya
        dialog.accept("Bhai Amit")

    # Event register kiya function ke sath
    page.on("dialog", handle_prompt) 
    
    page.locator("#promptBtn").click() 
    
    # Validation: Check kiya ki hamara bhara hua naam screen par print hua ya nahi
    expect(page.locator("#demo")).to_contain_text("Hello Bhai Amit! How are you today?")
    page.wait_for_timeout(3000)