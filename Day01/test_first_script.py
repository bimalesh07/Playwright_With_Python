import re
from playwright.sync_api import expect, Page

def test_google_search_easy(page: Page):
    #Step 1: Google ki website par jaana
    page.goto("https://google.com")
    
    # --------------------------------------------------------------------------
    # NOTES FOR DAY 01:
    # Playwright me automatic wait (Auto-Wait) hota hai. Selenium ki tarah 
    # har line par 'WebDriverWait' lagane ki koi zaroorat nahi hai.
    # --------------------------------------------------------------------------

    #Step 2: Search Box ko uske title ("Search") se dhoodhna
    search_box = page.get_by_title("Search")
    
    #Step 3: Search Box me apna text fill karna (Selenium ka send_keys)
    search_box.fill("Playwright Python Automation")
    
    # Step 4: Keyboard ka 'Enter' button press karna search karne ke liye
    search_box.press("Enter")
    
    # hoda sa wait taaki result load ho jaye (Sirf dekhne ke liye, varna zaroorat nahi hai)
    page.wait_for_timeout(2000)

    # --------------------------------------------------------------------------
    # ASSERTION NOTES:
    # Playwright me hamesha 'expect()' ka use karke verify karte hain.
    # Google automatic 'google.com' ko 'www.google.com' me redirect karta hai,
    # isliye URL verification me 'www.' lagana zaroori hai.
    # --------------------------------------------------------------------------
    
    #  Step 5: Verify karna ki hum sahi page par hain ya nahi
    expect(page).to_have_url(re.compile(r"google\.com")) # Regex use kiya taaki redirect handle ho jaye

