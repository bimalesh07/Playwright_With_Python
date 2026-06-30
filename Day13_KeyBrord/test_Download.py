import pytest
from playwright.sync_api import sync_playwright, expect, Page
import os

def test_download_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    # Text dala aur download link generate kiya
    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click() # Generates the link

    # =========================================================================
    # APPROACH 1: Expect Download (Industry Standard & Highly Recommended)
    # =========================================================================
    # Isme click hone aur download start hone ka jhanjhat Playwright khud manage karta hai
    with page.expect_download() as download_info:
        page.locator("#txtDownloadLink").click() # Click karne par download trigger hoga
        
    download = download_info.value
    # File ko apne folder me save kar liya
    download.save_as("downloads/testfile_standard.txt")
    # if we want file name as fiel then 
    #download.save_as("downloads/" + download.suggested_filename)


    # =========================================================================
    # APPROACH 2: Lambda Style (Jo aapne image me use kiya hai)
    # =========================================================================
    # Pehle event listener lagaya, fir click kiya
    # page.on("download", lambda download: download.save_as("downloads/testfile.txt"))
    # page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(3000)

    if os.path.exists("downloads/testfile.txt"):
        print("file exits,")
    else:
        print("File is not exists")