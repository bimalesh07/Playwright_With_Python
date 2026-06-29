import pytest
from playwright.sync_api import sync_playwright, expect, Page

# =========================================================================
# FUNCTION 1: Pehle box/calendar me CHECK-IN date select karne ke liye
# =========================================================================
def select_checkin_date(page, year, month, day):
    while True:
        # Pehla calendar (.nth(0)) ka Month aur Year uthaya (Jaise: "October 2025")
        checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()
        
        # Split kiya space se -> current_month="October", current_year="2025"
        current_month, current_year = checkin_month_year.split(" ")

        # Agar sahi saal aur mahina mil gaya, toh loop se bahar niklo
        if current_month == month and current_year == year:
            break
        else:
            # Nahi mila toh "Next month" ka arrow click karte raho
            page.locator('button[aria-label="Next month"]').click()

    # Pehle calendar (.nth(0)) ki table ke saare 'td' (dates) nikale
    all_dates = page.locator('table.b8fcb0c66a tbody').nth(0).locator('td').all()
    
    # Loop chala kar sahi tareekh par click kiya
    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break


# =========================================================================
# FUNCTION 2: Doosre box/calendar me CHECK-OUT date select karne ke liye
# =========================================================================
def select_checkout_date(page, year, month, day):
    while True:
        #Panga: Ab hum doosra calendar dekh rahe hain, isliye lagaya .nth(1)
        checkout_month_year = page.locator("h3[aria-live='polite']").nth(1).inner_text()
        current_month, current_year = checkout_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator('button[aria-label="Next month"]').click() # Go to next month

    # Doosre calendar (.nth(1)) ki table me se saari tareekhein nikali
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(1).locator('td').all()
    
    for date in all_dates:
        if date.inner_text() == day:
            date.click()
            break


# =========================================================================
# MAIN TEST CASE: Booking.com Flow
# =========================================================================
def test_booking_Date_picker(page: Page):
    # 1. Website par gaye aur Date Picker box par click kiya
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click() # Clicked on date picker

    # 2. Apne dono functions ko target dates dekar call kiya
    select_checkin_date(page, year="2025", month="October", day="10")
    select_checkout_date(page, year="2025", month="November", day="5")

    # 3. UI par jo text ab dikh raha hai use confirm karne ke liye fetch kiya
    checkin_text = page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text = page.locator("span[data-testid='date-display-field-end']").inner_text