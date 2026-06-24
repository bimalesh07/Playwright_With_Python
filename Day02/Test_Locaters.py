import re
from playwright.sync_api import Page, expect

def test_verify_pwlocators(page: Page):
    # 🌍 Practice ke liye SauceDemo ya any open site sahi hai, but concept dekhne ke liye URL open kiya
    page.goto("https://demo.nopcommerce.com/") 
    page.wait_for_timeout(2000)

    # -------------------------------------------------------------
    # 1) get_by_alt_text() -> Image ke description se dhoodhna
    # -------------------------------------------------------------
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()
    
    # -------------------------------------------------------------
    # 2) get_by_text() -> Normal screen par likhe text ke liye
    # -------------------------------------------------------------
    expect(page.get_by_text("Welcome to our store")).to_be_visible() # Full exact match
    expect(page.get_by_text("Welcome to", exact=False)).to_be_visible() # Aadana-adhura (Partial) match
    expect(page.get_by_text(re.compile(r"Welcome to", re.IGNORECASE))).to_be_visible() # Regex se bina small/capital ke jhanjhat ke

    # -------------------------------------------------------------
    # 3) get_by_role() -> Element ke kaam/type (heading, button) ke hisab se
    # -------------------------------------------------------------
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(2000)
    expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # -------------------------------------------------------------
    # 4) get_by_label() -> Form ke input fields jahan aage <label> laga ho
    # -------------------------------------------------------------
    page.get_by_label("First name:").fill("bimalesh")
    page.get_by_label("Email:").fill("bimaleshk07@gmail.com")
    page.wait_for_timeout(1000)

    # -------------------------------------------------------------
    # 5) get_by_placeholder() -> Box ke andar jo halka sa text hota hai
    # -------------------------------------------------------------
    # FIX: 'Serach' ki spelling ko 'Search' kiya aur method se 's' hataya
    page.get_by_placeholder("Search store").fill("apple")

    # -------------------------------------------------------------
    # 6) get_by_title() -> Hover karne par jo extra tooltip text dikhta hai
    # -------------------------------------------------------------
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page Link")).to_have_text("Home")
    
    # FIX: 'html' ko capital 'HTML' kiya ya fir 'ignore_case=True' lagaya
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML", ignore_case=True)
    page.wait_for_timeout(1000)

    # -------------------------------------------------------------
    # 7) get_by_test_id() -> Yeh devlopers ka diya hua custom id hota hai (data-testid)
    # -------------------------------------------------------------
    # Note: Agar test page par data-testid="profile" hoga tabhi yeh chalega, rare use hota hai
    expect(page.get_by_test_id("profile")).to_have_text("Jhon Doee")