import re
from playwright.sync_api import Page, expect

def test_xpath_locaters(page: Page):
    # 🌍 Sabse pehle website ka URL kholegan
    page.goto("https://demowebshop.tricentis.com/")

    # --------------------------------------------------------------------------
    # #1 Absolute xpath(full path) - Yeh lamba rasta hai, use nahi karna hai ❌
    # --------------------------------------------------------------------------
    # logo = page.locator("/html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")

    # --------------------------------------------------------------------------
    # #2 Relative Xpath: Chota aur badhiya rasta. Check kar rahe hain ki logo dikh raha hai ya nahi
    # --------------------------------------------------------------------------
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(2000)

    # --------------------------------------------------------------------------
    # #3 Dynamic Path: contains() ka use karke computer wale saare products ko ek sath pakda
    # --------------------------------------------------------------------------
    products = page.locator("//h2//a[contains(@href,'computer')]")
    
    # Kitne product mile, unka total count terminal me print karega (Count 1 se shuru hota hai)
    print("Total product mile:", products.count()) 
    
    # Verification check: confirm kar rahe hain ki count sahi hai ya nahi
    expect(products).to_have_count(products.count())

    # --------------------------------------------------------------------------
    # #4 Kisi ek single element ka text nikalne ke liye (first, last, nth)
    # --------------------------------------------------------------------------
    # .first use kiya -> Saare products me se sabse pehle product ka text nikalne ke liye
    first_product = products.first.text_content()
    print("Pehla computer product ye hai:", first_product)
    
    # .last use kiya -> Saare products me se sabse aakhri product ka text nikalne ke liye
    last_product = products.last.text_content()
    print("Aakhri computer product ye hai:", last_product)
    
    # .nth(2) use kiya -> Beech me se teesra product nikalne ke liye (Kyunki index 0 se shuru hota hai: 0=1st, 1=2nd, 2=3rd)
    nth_product = products.nth(2).text_content() 
    print("Teesra computer product (Index 2):", nth_product)

    # --------------------------------------------------------------------------
    # #5 Agar saare products ka text ek sath nikalna ho aur loop chalana ho
    # --------------------------------------------------------------------------
    # .all_text_contents() -> Ek hi baar me saare products ke naam ki ek list bana dega
    products_title = products.all_text_contents()
    print("Saare products ki list ek sath:", products_title)
    
    # Ab loop chalakar ek-ek product ka naam alag-alag line me print karenge
    print("Ek-ek karke product ka naam loop se print ho raha hai:")
    for i in products_title:
        print(i)
    
    # --------------------------------------------------------------------------
    # #6 XPath with starts-with(): Un links ko dhoodho jo '/build' se shuru hote hain
    # --------------------------------------------------------------------------
    building_products = page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Aise products jo /build se shuru hote hain unka count:", building_products.count())
    expect(building_products).to_have_count(building_products.count())

    # --------------------------------------------------------------------------
    # #7 XPath with text(): Direct screen par likhe huye 'Register' text se link ko dhoodha
    # --------------------------------------------------------------------------
    registration_link = page.locator("//a[text() = 'Register']")
    expect(registration_link).to_be_visible()

    # --------------------------------------------------------------------------
    # #8 XPath with last(): Follow us ke andar jo sabse aakhri (last) link hai use pakda
    # --------------------------------------------------------------------------
    google_link = page.locator("//div[@class='column follow-us']//li[last()]") 
    expect(google_link).to_have_text("Google+")

    # --------------------------------------------------------------------------
    # #9 XPath with position(): Follow us ke andar jo second (2nd) position par link hai use pakda
    # --------------------------------------------------------------------------
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")