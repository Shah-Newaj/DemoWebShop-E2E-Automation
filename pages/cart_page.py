class CartPage:
    def __init__(self, page):
        self.page = page

    def open_cart(self):
        # Open cart from header
        cart_link = self.page.locator("div.header-links a[href='/cart']").first
        cart_link.wait_for(state="visible", timeout=10000)
        cart_link.click()
        self.page.wait_for_url("**/cart", timeout=10000)
        self.page.wait_for_selector("div.page.shopping-cart-page", timeout=10000)

    def verify_item_in_cart(self):
        # Verify at least one item is in the cart
        self.page.wait_for_selector("table.cart tr.cart-item-row", timeout=10000)
        assert self.page.locator("table.cart tr.cart-item-row").count() > 0, "Cart is empty!"
