import pytest
from playwright.sync_api import Page, expect

def test_inner_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # 1. Pehle Bade Frame (Frame 3) ke andar ghuso URL se
    frame3 = page.frame(url=r".*frame_3.html")
    
    # Uske andar ka text box bharo
    frame3.locator("input[name='mytext3']").fill("Welcome")

    # 2. 🔥 JADU: Frame 3 ke andar baithe saare child frames ki list nikali
    all_child_frames = frame3.child_frames
    print("Total inner frames inside frame 3:", len(all_child_frames))

    # 3. Pehle inner frame (index 0) ko pakad liya
    inner_frame = all_child_frames[0]

    # 4. Us inner frame ke andar ka radio button select kiya aur verify kiya
    radio = inner_frame.get_by_label("I am a human")
    radio.check()
    
    expect(radio).to_be_checked() # Sateek Validation ✅
    page.wait_for_timeout(5000)