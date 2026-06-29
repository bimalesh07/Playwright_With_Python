import pytest
from playwright.sync_api import Page, expect

def test_copy_paste_and_validate(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html?m=1")
    page.wait_for_timeout(500)

    # Teeno input boxes ko validation ke liye variables me daal dete hain
    box1 = page.locator("#input1")
    box2 = page.locator("#input2")
    box3 = page.locator("#input3")

    # =========================================================================
    # STEP 1: Pehle Box Me Type Karo Aur Copy Karo
    # =========================================================================
    box1.click()
    page.keyboard.type("welcome")
    page.wait_for_timeout(500)

    # Pehle box ka saara text select kiya (Control + A)
    page.keyboard.press("Control+A")
    
    # Text ko clipboard me copy kiya (Control + C)
    page.keyboard.press("Control+C")
    page.wait_for_timeout(500)


    # =========================================================================
    # STEP 2: Tab Dabakar Box 2 Aur Box 3 Me Paste Karo
    # =========================================================================
    
    # --- BOX 2 ---
    page.keyboard.press("Tab") # Move to Box 2
    page.keyboard.press("Tab") # Move to Box 2
    page.keyboard.press("Control+V") # Paste the value
    page.wait_for_timeout(500)

    # --- BOX 3 ---
    page.keyboard.press("Tab") # Move to Box 3
    page.keyboard.press("Tab") # Move to Box 3
    page.keyboard.press("Control+V") # Paste the value
    page.wait_for_timeout(500)


    # =========================================================================
    # STEP 3: VALIDATION (Check kiya ki teeno me same value hai ya nahi)
    # =========================================================================
    # Input box ki value check karne ke liye hamesha 'to_have_value' use karte hain
    expect(box1).to_have_value("welcome")
    expect(box2).to_have_value("welcome")
    expect(box3).to_have_value("welcome")
    
    print("Makkhan Workflow! Teeno boxes successfully validate ho gaye!")