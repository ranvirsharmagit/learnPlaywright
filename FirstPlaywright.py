from playwright.sync_api import sync_playwright

def google_test():

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "google" in page.title()
        print(page.title())
        browser.close()
