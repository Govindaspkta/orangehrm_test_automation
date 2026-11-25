from playwright.sync_api import Page

LOGIN_PATH = "/web/index.php/auth/login"


def login(page: Page, base_url: str, username: str, password: str):
    page.goto(f"{base_url}{LOGIN_PATH}")
    page.locator('input[name="username"]').fill(username)
    page.locator('input[name="password"]').fill(password)
    page.locator('button[type="submit"]').click()
