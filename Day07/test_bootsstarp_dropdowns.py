import pytest
from playwright.sync_api import sync_playwright, expect, Page

"""
================================================================================
PLAYWRIGHT DROPDOWN NOTE
================================================================================
1) Selected dropdowns - having 'select' tag
   Options are embedded in 'option' tags.
   RULE: In par direct .click() nahi chalta! Hamesha .select_option() use karo.

2) Bootstrap dropdown - having div/button tag. Some time visible options, some time not.
   Options are embedded inside the 'div', 'ul', or 'li' tags.
   RULE: Pehle main button par .click() karke dropdown open karo, 
            phir andar ke option par direct .click() chala do.

3) Hidden dropdowns - options are hidden from the DOM until clicked.

KEY TAKEAWAY:
If it's not a normal dropdown (no <select> tag), then we CANNOT use select_option() 
like index, value, or role. We have to use regular UI actions like .click().
================================================================================
"""

def test_bootstrapdropdown(page: Page):
    page.goto("https://practice.expandtesting.com/dropdown")

    # ------------------------------------------------------------------------
    # HANDING STANDARD SELECT DROPDOWN (#country)
    # ------------------------------------------------------------------------
    # Find all locators of dropdown options
    options = page.locator("#country > option")

    # Count of options
    count = options.count()
    
    # Assertion for counting the options
    expect(options).to_have_count(count) 

    # Loop chalakar target option select karna
    for i in range(count):
        text = options.nth(i).inner_text()
        if text == 'China':
            # options.nth(i).click() 
            # Note: Yeh hamesha TimeoutError dega kyunki <option> tags par click lock hota hai.
            
            #SAHI TARIKA: Main select element par jaakar label se select karo
            page.locator("#country").select_option(label=text)
            break
            
    # Verification: Check kiya ki kya select hui value sach me China ('CN') hai
    expect(page.locator("#country")).to_have_value("CN")
    
    page.wait_for_timeout(3000)

    # ------------------------------------------------------------------------
    # HOW TO HANDLE REAL BOOTSTRAP DROPDOWN (For your learning/practice)
    # ------------------------------------------------------------------------
    """
    # Agar website par div/button wala asli bootstrap dropdown handle karna ho:
    
    # Step 1: Pehle dropdown ke main button/div par click karke list kholo
    page.locator("button#bootstrap-dropdown-id").click()
    
    # Step 2: Andar ke saare elements (jo ab visible ho gaye hain) unhe pakdo
    bootstrap_options = page.locator(".dropdown-menu li a")
    
    # Step 3: Loop chalao aur direct .click() maaro (Kyunki yeh normal link/buttons hain)
    for opt in bootstrap_options.all():
        if opt.inner_text() == "China":
            opt.click() # YAHAN click() 100% perfect kaam karega!
            break
    """