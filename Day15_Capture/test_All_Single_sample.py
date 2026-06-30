
def test_direct_context_style(context):
    
    # Ab is context se aap jitne chahe utne naye pages (tabs) bana sakte hai
    page1 = context.new_page()
    page1.goto("https://demowebshop.tricentis.com/")
    
    page2 = context.new_page()
    page2.goto("https://google.com")
    
    # Dono pages par normal automation karo...
    page1.locator("#newsletter-email").fill("test@email.com")



    """
   # pytest.ini autoamic video and screenshots and 
    
    [pytest]
    addopts = --headed
          --slowmo=500
          --video=on
          --screenshot=on
          --tracing=on
          --reruns 2
    
    """