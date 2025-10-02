class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = "input#Email"
        self.password = "input#Password"
        self.login_btn = "input.button-1.login-button"

    def login(self, email, password):
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)
        self.page.wait_for_selector("a.ico-logout")
