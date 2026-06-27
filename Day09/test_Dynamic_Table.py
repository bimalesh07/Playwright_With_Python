import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_verify_chrome_cpu(page: Page):
    # 1. Target Website par gaye jahan dynamic tasks/CPU wali table hai
    page.goto("https://testautomationpractice.blogspot.com/")

    # 2. Table ke tbody element ka master locator banaya
    table = page.locator("#taskTable > tbody")

    # 3. .all() use karke saare row locators ki ek Python list banayi (Taaki loop chala sakein)
    rows = table.locator('tr').all()
    
    # Ek khali variable banaya taaki Chrome ka CPU load isme store kar sakein
    cpu_load = ""
    
    # 4. Loop chalakar har ek row ke andar check karna shuru kiya
    for row in rows:
        # nth(0) se sabse pehla column (Process/Browser Name) nikala
        process_name = row.locator("td").nth(0).inner_text() 
        
        if process_name == "Chrome":
            #JADU: :has-text('%') se seedhe wahi cell pakda jisme CPU percentage (%) hai if 
            """if same like MBS MB then we use re.complie for onely take MB ya what ever we want """
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print(f"\n[SUCCESS] Chrome mil gaya! CPU Load hai: {cpu_load}")
            break # Chrome milne ke baad loop ko yahin rok diya (Time bachane ke liye)
    
    # [Assertion] Final Validation
    # Pehle ensure kiya ki cpu_load khali nahi hai (yaani loop me Chrome mila tha)
    assert cpu_load != "", "Galti ho gayi bhai! Table me Chrome process mila hi nahi!"
    
    # Ab screen par jo alag se text likha hota hai (e.g., "Chrome CPU: 2.5%"), 
    # uske locator par check kiya ki kya hamari nikali hui cpu_load value usme match kar rahi hai ya nahi.
    # (Note: Agar website par exact class '.chrome_cpu' na ho, toh aap normal text locator bhi use kar sakte hain)
    # expect(page.locator("p:has-text('Chrome CPU')")).to_contain_text(cpu_load)
    
    expect(page.locator(".chrome-cpu")).to_contain_text(cpu_load)


