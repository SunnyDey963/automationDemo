import time

from playwright.sync_api import Page,Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #it is like opening in incognito mode sperate private browser,
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#chromium headless mode, with 1 single context
def test_playwrightBasicsShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK23") # Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    time.sleep(5)

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser =playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK23")  # Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    time.sleep(5)

# web table automation:
# 1. identify the price colomn
# 2.  identify the banana row
# 3. extract the price of banana

def test_uiTable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            colValue = index
            print(f"price colvalue is {colValue}")
            break

    bananRow = page.locator("tr").filter(has_text="banana")
    expect(bananRow.locator("td").nth(colValue)).to_have_text("87")





