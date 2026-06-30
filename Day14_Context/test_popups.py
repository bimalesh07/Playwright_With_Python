import pytest
from playwright.sync_api import sync_playwright, expect, Playwright

def test_handle_popups(playwright: Playwright):
    #PURPOSE: Heavy browser software engine start karna (Chrome/Chromium)
    browser = playwright.chromium.launch(headless=False)
    
    #PURPOSE: Ek safe, isolated aur private window (Incognito mode jaisa) banana
    context = browser.new_context()
    
    #PURPOSE: Us private window ke andar pehla primary tab (main page) open karna
    page = context.new_page()

    #PURPOSE: Main testing website par navigate karna jahan popup button hai
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html?m=1")
    
    # PURPOSE: 'with' block lagakar Playwright ka special target listener active karna.
    # Yeh script aur browser ki speed ko match (sync) karta hai taaki naya page miss na ho.
    # 'popup_info' ek temporary band dabba (holder) hai jo popup ki details catch karega.
    with context.expect_page() as popup_info:
        #  PURPOSE: Button click karna jo backend me automatic do (2) naye popups kholta hai
        page.locator("#PopUp").click() 
    
    #  PURPOSE: '.value' lagakar temporary dabbe ko unbox kiya aur asli active 
    # Browser Page/Tab ko nikal kar 'popup_page' variable me direct target lock kar diya.
    popup_page = popup_info.value
    
    # PURPOSE: Playwright ko bolna ki jab tak naya popup page poori tarah se load 
    # na ho jaye, tab tak test case ko aage mat badhana (Flaky/Fail hone se bachata hai).
    popup_page.wait_for_load_state()

    # PURPOSE: Browser context me filhal jitne bhi active tabs hain unki list check karna.
    # Note: Website ne do popups khole the (Selenium aur Playwright), par humare 'with' block ne
    # smart tarike se sirf sabse pehle wale single popup target ko capture kiya.
    all_pages = context.pages
    print("Total pages in context:", len(all_pages)) # Output: 2 (Ek main page + ek pehla captured popup)

    # PURPOSE: Captured popup tab ka actual web page title nikalna
    title = popup_page.title()
    print("New Popup Title:", title)

    # PURPOSE: Agar captured page ka title humare target se match karta hai toh action lena.
    # Isme bina kisi loop ke, direct single target page par script execute ho rahi hai.
    if "Playwright" in title:
        # PURPOSE: Naye khule hue target page ke andar jaakar 'Get started' button click karna
        popup_page.locator("a:has-text('Get started')").click() 
        
        # PURPOSE: Dynamic URL change hone ke baad naye page ka title strict verify karna
        expect(popup_page).to_have_title("Installation | Playwright")
        
        # PURPOSE: Kaam khatam hone par sirf is temporary popup wale tab ko close karna
        popup_page.close()

    # PURPOSE: Main page ko 2 seconds tak khula rakhna taaki hum visually verify kar sakein
    page.wait_for_timeout(2000)
    
    #PURPOSE: Pura browser window aur computer memory (RAM resources) ko safely cleanup karna
    context.close()
    browser.close()