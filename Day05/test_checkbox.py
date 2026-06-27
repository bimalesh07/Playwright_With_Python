import pytest
from playwright.sync_api import Page, expect

def test_checkbox(page: Page):
    # 🌍 Step 1: Sabse pehle website ka URL kholega
    page.goto("https://testautomationpractice.blogspot.com/")

    # """Select specific checkbox(sunday)"""
    # sunday_checkbox = page.get_by_label("Sunday")
    # sunday_checkbox.check()
    # expect(sunday_checkbox).to_be_checked()
    # page.wait_for_timeout(5000)

    """#2 Count numbers of Check boxes"""
    """expect is not work in element not a text value """
    """
    NOTE: Playwright locators do not return a standard Python list or array like Selenium. 
    Because of this, we cannot pass a group of elements directly into expect(). 
    The expect() assertion only works on a single locator element at a time. 
    To assert multiple elements (like checkboxes), we must loop through the list 
    and verify each element individually.
    """
    
    # step1, 
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []

    # step 2
    # for day in days:
    #     checkbox = page.get_by_label(day)
    #     checkboxes.append(checkbox)

    """Using list comprehension for single modern loops"""
    checkboxes = [page.get_by_label(day) for day in days]
    

    # Iska use isliye kiya taaki terminal me total count (7) print ho sake.
    print("Total numbers of checkbox", len(checkboxes))

    # #3 selected all the checkboxes and assert each check box is selected
    # Loop chalakar ek-ek checkbox ko pakda, use tick kiya aur expect se verify kiya.
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
    
    page.wait_for_timeout(2000)

    # #4 check last 3 boxes
    # Python slicing [-3:] use karke aakhri ke 3 checkboxes ko uncheck kiya.
    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        # FIX NOTES: 'not_to_be_attached' tab lagta hai jab element screen se gayab ho jaye.
        # Checkbox screen par hi hai, bas khali hua hai, isliye 'not_to_be_checked' use kiya.
        expect(checkbox).not_to_be_checked()
    
    # #5 toggle checkbox
    # Iska use isliye kiya: Agar tick hai toh hata do, agar khali hai toh tik laga do.
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    # #6 Randomly check checkboxes - check 1,3,6 checkboxes
    # Index number 1 (Monday), 3 (Wednesday), aur 6 (Saturday) wale box ko select karne ke liye.
    indexes = [1, 3, 6]
    for i in indexes:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()
    
    # #7 selected with checkbox based on the label/input by choice
    # Kisi ek din ka naam match karke use click karne ke liye.
    weekday = "Monday"
    for label in days:
        if label == weekday:
            checkbox_label = page.get_by_label(label)
            checkbox_label.click()
            expect(checkbox_label).to_be_checked()

    # ==========================================================================
    #  EXTRA BONUS ADDE
    # ==========================================================================
    
    """#8 Dropdown Selection (Select Tag): Desi bhasha me dropdown se option chunna"""
    # Kyun use kiya? -> Website par 'Country' select karne ka ek option hota hai.
    # Isko select karne ke liye hum .select_option() use karte hain.
    country_dropdown = page.locator("#country")
    
    # Humne dropdown me se 'India' ko select kiya uske value ya text se
    country_dropdown.select_option(label="India")
    
    # Verify kaise karein? -> expect se check kiya ki kya sach me 'India' select hua?
    expect(country_dropdown).to_have_value("india") # HTML me value small 'india' hai
    print("Dropdown se India select ho gaya successfully!")

    """#9 Radio Buttons Selection: Male/Female select karne ke liye"""
    # Kyun use kiya? -> Checkbox me multiple click ho sakte hain, par radio button me sirf ek hi select hota hai.
    # Isko select karne ke liye bhi .check() ka hi use hota hai.
    male_radio = page.get_by_label("Male", exact=True)
    male_radio.check()
    
    # Verify kiya ki radio button select hua ya nahi
    expect(male_radio).to_be_checked()
    print("Radio button se Male option check ho gaya!")



    """
    ================================================================================
     SMART NOTE: Playwright Ka `.all()` Method Kya Karta Hai?
    ================================================================================

    1. KYUN USE KARTE HAIN? 
    Website par agar ek jaise bohot saare elements hain (jaise saare checkboxes), 
    aur hume un sabhi par ek sath kaam karna hai bina unka naam (Sunday, Monday) alag se likhe.

    2. YEH KAAM KAISE KARTA HAIN?
    - Pehle hum CSS ya XPath se un saare elements ka ek master locator banate hain.
    - Fir us master locator ke aage `.all()` laga dete hain.
    - `.all()` lagate hi Playwright automatic un saare elements ko ek-ek karke ek 
     sahi Python List me badal kar hume de deta hai!

    3. ISKA ASLI FAYDA?
    Hume khud se lambi list (days = ['Sunday', 'Monday'...]) nahi banani padti. 
    Playwright khud hi saare elements dhoodh kar list taiyar kar deta hai aur hum 
    aaram se loop chalakar 'expect()' use kar sakte hain!
    """


# --------------------------------------------------------------------------
    # PRACTICAL EXAMPLE: CSS Selector + .all()
    # --------------------------------------------------------------------------
    # Step 1: CSS path se saare checkboxes ka master pointer pakda
    master_locator = page.locator("input[type='checkbox'][id$='day']")

    # Step 2: .all() lagakar Playwright se bola- "Bhai, in sabki ek Python List bana de"
    pure_elements_list = master_locator.all()
    print("Playwright ne .all() se kitne checkbox dhoodhe:", len(pure_elements_list))

    # Step 3: Ab bani-banayi list par loop chalao aur mast expect() lagao
    for box in pure_elements_list:
        box.check()                 
        expect(box).to_be_checked() 