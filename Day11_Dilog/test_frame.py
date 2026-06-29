import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_iframe(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    all_frames = page.frames
    print("Total frames found:", len(all_frames))

    # =========================================================================
    #APPROACH 1: Using frame_locator() with CSS selector (Sabse Best & Easy)
    # =========================================================================
    # : Frame ke andar jaane ke liye frame_locator() use
    frame1 = page.frame_locator("frame[src='frame_1.html']")
    
    inputbox = frame1.locator("input[name='mytext1']")
    inputbox.fill("welcome")

    # 3: Input box me text check karne ke liye 'to_have_value' hota hai,
    expect(inputbox).to_have_value("welcome")


    # =========================================================================
    #  APPROACH 2: Using page.frame(url="...") (Agar URL pata ho)
    # =========================================================================
    # Agar aap page.frame() use kar rahe ho, toh poora URL ya uska hissa (regex) dena hota hai
    # frame_by_url = page.frame(url=r".*frame_1.html")
    # inputbox2 = frame_by_url.locator("input[name='mytext1']")
    # inputbox2.fill("welcome again")


    page.wait_for_timeout(3000)