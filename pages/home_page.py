BASE_URL = "https://demowebshop.tricentis.com/"

class HomePage:
    def __init__(self, page):
        self.page = page
        self.register_link = "a.ico-register"
        self.login_link = "a.ico-login"
        self.logout_link = "a.ico-logout"
        self.search_box = "input#small-searchterms"
        self.search_btn = "input[type='submit'][value='Search']"

    def navigate(self):
        self.page.goto(BASE_URL)

    def click_register(self):
        self.page.click(self.register_link)

    def click_login(self):
        self.page.click(self.login_link)

    def click_logout(self):
        self.page.click(self.logout_link)

    def search_product(self, product_name):
        self.page.fill(self.search_box, product_name)
        self.page.click(self.search_btn)
