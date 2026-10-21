from playwright.sync_api import Page,expect

def test_login_page_loads(page:Page):
    page.goto("http://127.0.0.1:5500/login.html")
    
    expect(page.get_by_role("heading",name="Login")).to_be_visible()
    
    page.get_by_label("Username").fill("student101")
    page.get_by_label("Password").fill("test-password")
    
    page.get_by_role("button",name="Login").click()
    
    expect(page).to_have_url("http://127.0.0.1:5500/dashboard.html?username=student101&password=test-password")    
    expect(page.get_by_role("heading",name="Student Dashboard")).to_be_visible()