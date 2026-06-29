from playwright.sync_api import sync_playwright, expect , Page
import pytest

@pytest.mark.skip
def test_paginations_table(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages = True

    while has_more_pages:
        rows = page.locator('#example tbody tr').all()
        for row in rows:
            print(row.inner_text())
        
        next_button = page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")

        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_button.click()

# Filters row test
def test_fillters_rows(page: Page):
    #1
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    
    # 2. Dropdown ko uski sahi ID
    dropdown = page.locator("#dt-length-0")
    
    # [UI Assertion] Pehle check kiya ki dropdown dikh raha hai
    expect(dropdown).to_be_visible()
    
    # 3. Dropdown me se value="25" select ki
    dropdown.select_option(value="25")
    
    # [Value Assertion] Double check kiya ki 25 select hua ya nahi
    expect(dropdown).to_have_value("25")

    # 4. Table ke tbody ke andar ke saare 'tr' (rows) ko pakda
    rows = page.locator('#example tbody tr')
    
    # 5. [Assertion] Kyunki dropdown me 25 entries select hain, 
    # toh page par exact 25 rows hi dikhni chahiye!
    expect(rows).to_have_count(25) # ✅ 35 hata kar 25 kar diya hai
    
    print("\n[SUCCESS] Test pass ho gaya! Screen par exact 25 rows dikh rahi hain.")

