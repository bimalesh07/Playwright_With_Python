import pytest
from playwright.sync_api import sync_playwright, expect, Page

# =========================================================================
# 1. MOUSE HOVER (Dropdown Open Karna)
# =========================================================================
def test_mouse_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(500)

 
    pointme_btn = page.locator(".dropbtn")

    # Dropdown button ke upar mouse lekar gaye (Hover kiya)
    pointme_btn.hover()

    laptops = page.locator(".dropdown-content a:nth-child(2)")
    laptops.hover() # Laptops option ke upar hover kiya
    
    # Click karna ho toh direct click bhi maar sakte ho:
    # laptops.click()

    page.wait_for_timeout(3000)


# =========================================================================
# 2. MOUSE RIGHT CLICK (Context Menu Open Karna)
# =========================================================================
def test_mouse_rightclick(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(500)
    
    #Approach 1: Direct Page level par click karna ---
    # page.click("#box", button="right") # (Isme element variable nahi banta)

    #Approach 2: Locator Variable Banakar (Recommended & Clean) ---
    my_element = page.locator("#box")
    my_element.click(button="right") # button="right" likhte hi right click hoga

    page.wait_for_timeout(3000)


# =========================================================================
# 3. MOUSE DOUBLE CLICK (Text Copy Control)
# =========================================================================
# @pytest.mark.skip  # Agar skip hatana ho toh is line ko comment kar dena
def test_double_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(500)

    # --- Approach 1: Direct Selector Use Karke ---
    # page.double_click("//button[contains(text(),'Copy Text')]")

    # --- Approach 2: Locator Variable Banakar (Best Practice) ---
    double_btn = page.locator("//button[contains(text(),'Copy Text')]")
    double_btn.double_click() # Do baar fatafat click karega

    # Verification: Double click karne par text field2 me copy ho jata hai
    expect(page.locator("#field2")).to_have_value("Hello World!")

    page.wait_for_timeout(3000)


# =========================================================================
# DRAG AND DROP (Uthana Aur Patakna)
# =========================================================================
def test_drag_drop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(500)

    source = page.locator("#draggable") # Jise uthana hai
    

    target = page.locator("#droppable")  # Jahan drop karna hai

    # --- Approach 1: Manual Mouse Control (Not Recommended, lamba hai) ---
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #Approach 2: Direct Shortcut Method (Highly Recommended ) ---
    source.drag_to(target)
    
    expect(page.locator("#droppable p")).to_have_text("Dropped!")

    page.wait_for_timeout(3000)