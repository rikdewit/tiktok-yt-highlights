from playwright.sync_api import sync_playwright
from getpass import getpass

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=907684893581-tprkr1koadektv2tn4p83se4vdtslecu.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.upload&state=QNRDJADG5wpDDWoHOrWGNJUcp2vw4F&access_type=offline")
    print(page.title())
    print("Please login to your google account which has a youtube account connected")
    email = input("Email: ")
    password = getpass()
    youtube_username = input("Youtube username: ")

    email = "rikdewit1997@gmail.com"
    password = "whatkindamusiccurrents"
    youtube_username = "Tiktok Highlight Reels"

    email_selector = 'input[type="email"]'
    password_selector = 'input[type="password"]'

    page.fill(email_selector, email)
    page.press(email_selector, "Enter")
    page.fill(password_selector, password)
    page.press(password_selector, "Enter")
    
    userlist_selector = "ul.OVnw0d"

    page.click("text=Tiktok Highlight Reels")
    page.wait_for_load_state("networkidle")
    page.press("text=Continue", "Enter")




    page.wait_for_load_state("networkidle")
    continue_button = page.query_selector_all("button")[2]
    continue_button.click()
    page.wait_for_load_state("networkidle")
    
    page.screenshot(path='screenshot.png')

    browser.close()