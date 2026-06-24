import re
from playwright.sync_api import Page, expect

def test_xpath_locaters(page: Page):
    # URL Open karna
    page.goto("https://demowebshop.tricentis.com/")

    # --------------------------------------------------------------------------
    # #1 Absolute XPath ( Not Recommended ❌)
    # --------------------------------------------------------------------------
    # logo = page.locator("/html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    
    # --------------------------------------------------------------------------
    # #2 Relative XPath (Standard Structure: //tagname[@attribute='value'])
    # --------------------------------------------------------------------------
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(2000)

    # --------------------------------------------------------------------------
    # #3 Dynamic XPath using contains() -> Partial match ke liye
    # --------------------------------------------------------------------------
    products = page.locator("//h2//a[contains(@href, 'computer')]")
    print("Total Product Count:", products.count()) 
    expect(products).to_have_count(products.count())

    # --------------------------------------------------------------------------
    # #4 Handling Single Element from Multiple Elements (first, last, nth)
    # --------------------------------------------------------------------------
    # .first -> List ka sabse pehla element uthane ke liye
    first_product = products.first.text_content()
    print("First Product Title:", first_product)
    
    # .last -> List ka sabse aakhri element uthane ke liye
    last_product = products.last.text_content()
    print("Last Product Title:", last_product)
    
    # .nth(index) -> Kisi beech ke element ko index se uthane ke liye (Index 0 se shuru hota hai)
    nth_product = products.nth(2).text_content() # Yaani 3rd product
    print("3rd Product Title (Index 2):", nth_product)

    # --------------------------------------------------------------------------
    # #5 Fetching All Texts at once & Looping
    # --------------------------------------------------------------------------
    # .all_text_contents() -> Saare elements ka text ek sath Python List me nikal leta hai
    products_title = products.all_text_contents()
    print("All Product Titles List:", products_title)
    
    # Looping -> Ek-ek karke text screen par print karne ke liye
    print("--- Printing titles using Loop ---")
    for title in products_title:
        print(title)
    
    # --------------------------------------------------------------------------
    # #6 XPath Functions: starts-with(), text(), position(), last()
    # --------------------------------------------------------------------------
    # A. starts-with() -> Jab attribute ka aage ka text fix ho aur piche ka badal raha ho
    building_products = page.locator("//h2//a[starts-with(@href, '/build')]")
    print("Count of building products:", building_products.count())
    expect(building_products).to_have_count(building_products.count())

    # B. text() -> Jab element ke andar likhe huye visible text se dhoodhna ho
    registration_link = page.locator("//a[text() = 'Register']")
    expect(registration_link).to_be_visible()

    # C. last() -> XPath ke andar directly aakhri element tak pahunchne ke liye
    google_link = page.locator("//div[@class='column follow-us']//li[last()]") 
    expect(google_link).to_have_text("Google+")

    # D. position() -> XPath ke andar specific index par switch karne ke liye (XPath me index 1 se shuru hota hai)
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")