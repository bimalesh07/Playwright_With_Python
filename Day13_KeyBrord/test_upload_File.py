import pytest
from playwright.sync_api import expect, Page

# 1. SINGLE FILE UPLOAD
def test_upload(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # File ka path variable me set kiya
    file_path = "upload/Test1.txt"

    # File set ki aur click kiya
    page.locator("#singleFileInput").set_input_files(file_path)
    page.locator("button:has-text('Upload Single File')").click()
    
    # Validation
    expect(page.locator("#singleFileStatus")).to_contain_text("Uploaded")


# 2. MULTIPLE FILES UPLOAD
def test_multiple_files(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # Saari files ko ek list [] me daal kar bhej diya
    multi_files = ["upload/Test1.txt", "upload/Test12.txt"]
    
    page.locator("#multipleFilesInput").set_input_files(multi_files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    # Validation
    expect(page.locator('#multipleFilesStatus')).to_contain_text("Test1.txt")
    expect(page.locator('#multipleFilesStatus')).to_contain_text("Test12.txt")