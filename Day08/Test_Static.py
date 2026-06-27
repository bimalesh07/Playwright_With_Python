import pytest
from playwright.sync_api import sync_playwright,expect,Page

def test_static_web_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #location table
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()


    #1 count total numbers of rows in a table
    row = table.locator('tr') # equals we alreday make table so we dont need to make locaters ful
    row_count = row.count()
    expect(row).to_have_count(row_count)

    print("Total numbers Of Rows in a table :", row_count)#7


    #2 count total numbers of columns/headers in table
    columns = row.locator("th") 
    columns_count = columns.count()
    expect(columns).to_have_count(columns_count)
    print("Numbers of columns/headres in a table:", columns_count) #4


    #3 Read all the data from 2nd row of the table in css index are not support when use xpaht we use xpath
    # second_row_cells = row.nth(2).locator("td")
    # second_row_texts = second_row_cells.all_inner_texts()
    # print("2nd row data====>", second_row_texts)
    # expect(second_row_cells).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    # #print with loops
    # for text in second_row_texts:
    #     print(text)

    
    #4 Read all  the data from the table(Exclusive headers)
    all_row_data = row.all()
    # for row in all_row_data[1:]:
    #    cols = row.locator('td').all_inner_texts()
    #    print(cols)
    
    #5 print Book Name where writen by  
    # for  row in all_row_data[1:]:
    #     auth_name = row.locator('td').nth(1).inner_text()
    #     if auth_name =="Amod":
    #         book_name = row.locator('td').nth(0).inner_text()
    #         print(f"Auth Name is: {auth_name} and Book Name is: {book_name}")

    #6 Calculate total price of all the books
    total_price =0
    for row in all_row_data[1:]:
        price = row.locator('td').nth(3).inner_text()
        total_price += int(price)
    print("Total Price of Table is: ", total_price)













