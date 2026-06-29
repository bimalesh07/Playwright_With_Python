import pytest
from playwright.sync_api import sync_playwright, expect, Page

# =========================================================================
# Calendar me Month, Year aur Date select karne ke liye
# =========================================================================
def select_date(page, target_year, target_month, target_date, is_future):
    while True:
        current_month = page.locator('.ui-datepicker-month').text_content().strip()
        current_year = page.locator('.ui-datepicker-year').text_content().strip()

        # Agar target month aur year mil gaya, toh loop se bahar nikal jao
        if current_month == target_month and current_year == target_year:
            break

        if is_future == True:
            page.locator('.ui-icon.ui-icon-circle-triangle-e').click() # Future date ke liye (Next click)
            
        else:
            page.locator('.ui-icon.ui-icon-circle-triangle-w').click() # Past date ke liye (Prev click)
    

    # Calendar ke saare dates (td) ka loop chalayenge
    all_dates = page.locator(".ui-datepicker-calendar td a").all() # 'a' tag lagaya taaki direct text mile
    
    for dt in all_dates:
        date_text = dt.inner_text().strip()
        
        if date_text == target_date:
            dt.click() # Sahi date milte hi click karo
            break # Date mil gayi toh loop se bahar


# =========================================================================
# TEST CASE: Date Picker Automation
# =========================================================================
def test_date_picker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")

    #Approach 1: Ekdum seedha fill karna (Kafi hai agar kaam ho jaye) ---
    # date_input.fill("10/15/2025")
    # expect(date_input).to_have_value("10/15/2025")


    # Approach 2: Complex but we know for its Good (Loop chala kar select karna) ---
    is_future = True
    year = "2026"
    month = "October"
    date = "15"

    date_input.click() 
    
    # Function ko call kiya saari values dekar
    select_date(page, year, month, date, is_future)
    
    print("Selected date=========>", date_input.input_value())
    
    # Check kiya ki wahan sahi format me date aayi ya nahi
    # Note: Kuch websites par text select hone ke baad "10/15/2026" aata hai, format dekh lena UI par.
    expect(date_input).to_have_value("10/15/2026") 

    page.wait_for_timeout(5000)