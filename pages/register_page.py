class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.gender_male = "input#gender-male"
        self.firstname = "input#FirstName"
        self.lastname = "input#LastName"
        self.email = "input#Email"
        self.password = "input#Password"
        self.confirm_password = "input#ConfirmPassword"
        self.register_btn = "input#register-button"

    def register(self, firstname, lastname, email, password):
        self.page.click(self.gender_male)
        self.page.fill(self.firstname, firstname)
        self.page.fill(self.lastname, lastname)
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.fill(self.confirm_password, password)
        self.page.click(self.register_btn)
        self.page.wait_for_selector("text=Your registration completed")
