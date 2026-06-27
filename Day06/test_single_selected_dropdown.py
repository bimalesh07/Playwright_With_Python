import pytest
from playwright.sync_api import Page, expect

def test_dropwons(page: Page):
    # 1. Website par gaye
    page.goto("https://testautomationpractice.blogspot.com/")

    # 2. Dropdown element ko ek variable me store kar liya taaki baar-baar na likhna pade
    country_dropdown = page.locator("#country")

    # [UI Assertion] - Pehle check kiya ki dropdown UI par sahi-salamat dikh raha hai ya nahi
    expect(country_dropdown).to_be_visible()

    # 3. Index se 4th option select kiya (kyunki index 0 se shuru hota hai, toh 3 matlab 4th item)
    country_dropdown.select_option(index=3)
    
    # [Value Assertion] - Check kiya ki kya sahi me index 3 wali value select hui?
    # Note: testautomationpractice par index 3 par 'uk' hai, toh hum uski value check kar rahe hain
    expect(country_dropdown).to_have_value("uk") 
    
    page.wait_for_timeout(3000)

    # ------------------------------------------------------------------------
    # TARIKA 1: Without using .all() -> Direct text ki list nikalna
    # ------------------------------------------------------------------------
    dropdowns_options_locator = page.locator("#country > option")

    # Bina loop ke direct .all_text_contents() chalaya (Yeh strings ki list dega)
    all_names_list = dropdowns_options_locator.all_text_contents()
    
    print("\n--- Tarika 1 (Direct Text List) ---")
    for name in all_names_list:
        print(name)

    # [Python Assert] - Check kiya ki list khali toh nahi hai, kam se kam options hain na!
    assert len(all_names_list) > 0, "Dropdown me koi option hi nahi mila bhai!"

    # ------------------------------------------------------------------------
    # TARIKA 2: Using .all() -> Elements ki list banakar count aur loop chalana
    # ------------------------------------------------------------------------
    dropdowns_elements_list = page.locator("#country > option").all()
    
    # Total count nikal kar print kiya aur assert kiya
    total_options_count = len(dropdowns_elements_list)
    print(f"\nTotal dropdown options found: {total_options_count}")
    
    # [Assertion] - Check kiya ki dropdown me wahi total counts hain na jo expected hain
    expect(page.locator("#country > option")).to_have_count(total_options_count)

    print("\n--- Tarika 2 (Elements Loop) ---")
    for option in dropdowns_elements_list:
        # Loop ke andar har ek option ki UI visibility check ki
        expect(option).to_be_visible() 
        # Aur uska text print kiya
        print(option.text_content())
    
    page.wait_for_timeout(2000)