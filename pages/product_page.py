class ProductPage:
    def __init__(self, page):
        self.page = page

    def wait_for_results(self):
        """
        Wait for search results or product list to appear
        """
        self.page.wait_for_selector("div.product-item", timeout=10000)

    # def add_simple_product_to_cart(self):
    #     """
    #     Add first simple product from search results
    #     """
    #     self.page.locator("input[value='Add to cart']").first.click()
    #     # Wait for cart to update
    #     self.page.wait_for_selector("span.cart-qty:not(:has-text('(0)'))", timeout=15000)

    def configure_computer(self):
        """
        Select options for configurable product
        """
        self.page.click("input#product_attribute_72_5_18_65")  # CPU
        self.page.click("input#product_attribute_72_6_19_91")  # RAM
        self.page.click("input#product_attribute_72_3_20_58")  # HDD
        self.page.click("input#product_attribute_72_8_30_95") # OS
        add_btn = self.page.locator("(//input[@id='add-to-cart-button-72'])[1]")
        add_btn.wait_for(state="visible", timeout=15000)
        add_btn.click()

    def add_configured_computer_to_cart(self):

        add_btn = self.page.locator("(//input[@value='Add to cart'])[1]")
        add_btn.wait_for(state="visible", timeout=15000)
        add_btn.click()
        self.configure_computer()  # select CPU, RAM, HDD, OS
        self.page.wait_for_selector("div.bar-notification.success", timeout=15000)

