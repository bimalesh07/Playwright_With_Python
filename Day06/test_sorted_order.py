import pytest
from playwright.sync_api import  Page, expect


def test_multi_selected_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Dropdown_options = page.locator("#colors>option") #unsorted list
    Dropdown_options =  page.locator("#animals>option") #sorted list

    options_text = [text.strip() for text in Dropdown_options.all_text_contents()]


    """#we check list are soreted or not so we take  original if sorted and we need sorted then fal if we want unsorted then pass this the way we check"""
    original_list = options_text.copy()
    sorted_List = sorted(original_list, reverse=True)  # reverse:true , Decending orders check

    print("Original List:", original_list)
    print("sorted_list:", sorted_List)

    if original_list == sorted_List:
        print("Dropwown is Sorted")
    else:
        print("Dropdowns are not sorted")




  
    page.wait_for_timeout(5000)
