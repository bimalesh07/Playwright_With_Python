import pytest
from playwright.sync_api import expect, Page

def test_all_methods_demo(page: Page):
    # 1
    page.goto("https://demowebshop.tricentis.com/")

    # Saare products ke main locator ko pakda
    products = page.locator(".product-title")

    # ========================================================================
    # # 2) all_inner_texts() vs all_text_contents()
    # ========================================================================
    print("\n--- 2) ALL TEXT METHODS DEMO ---")
    
    # Bina kisi loop ke ek jhatke me saare visible names ki list mili
    product_names_inner = products.all_inner_texts()
    print("Direct Inner Texts List:", product_names_inner)

    # Saare names ki list mili (hidden + visible text aur extra spaces ke sath)
    product_names_content = products.all_text_contents()
    
    # Python ka .strip() jadu: Jo extra spaces/newlines (\n) text_contents lekar aaya tha, 
    # unhe saaf-suthra karne ke liye humne List Comprehension lagaya (Jaise aapki image me tha)
    products_names_trimmed = [text.strip() for text in product_names_content]
    print("Trimmed Text Contents List:", products_names_trimmed)


    # ========================================================================
    # # 3) all() Method
    # ========================================================================
    print("\n--- 3) ALL() METHOD WITH LOOPS DEMO ---")
    
    # products.all() lagane se hamein Locators (Elements) ki list milti hai, strings ki nahi!
    product_locators = products.all()

    # Pehle single index check kiya (Jaise image me tha)
    print("Index 0 wale locator ka text:", product_locators[0].inner_text())

    # FOR-EACH LOOP (Jo aapki image me blue color se highlited hai)
    # Yeh sabse clean tarika hai loop chalane ka
    print("\nUsing for-each loop:")
    for product_loc in product_locators:
        # Yahan aap .click() bhi kar sakte the, par hum abhi text print kar rahe hain
        print(product_loc.inner_text())


    # RANGE-LEN LOOP (Jo aapki image me sabse niche comment tha)
    # Yeh index-wise kaam karne ke liye use hota hai
    print("\nUsing range(len()) loop:")
    for i in range(len(product_locators)):
        print(f"Product {i+1}:", product_locators[i].inner_text())