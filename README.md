# DemoWebShop-E2E-Automation
🛒 DemoWebShop E2E Automation (Playwright + Pytest + Python + Allure)

DemoWebShop-Demo-Site-E2E-Automation/

Command to run the project...

    pytest -v --alluredir="AllureReports/reports" tests/test_demowebshop_e2e.py

This project contains end-to-end (E2E) test automation for Tricentis Demo Web Shop
 using:

Playwright (browser automation)

Pytest (test framework)

Allure (reporting)

Page Object Model (POM) for maintainability

📂 Project Structure
Magento-Demo-Site-E2E-Automation/
│
├── pages/               # Page Object Model classes
│   ├── home_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│
├── tests/
│   └── test_demowebshop_e2e.py   # Main E2E test
│
├── utils/
│   └── helpers.py      # Helper functions (e.g., random email generator)
│
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation


Run a specific test
pytest tests/test_demowebshop_e2e.py::test_demowebshop_add_to_cart --headed --alluredir=reports


✅ Test Flow

Open DemoWebShop homepage

Register a new user

Logout & login again

Search for product

Add product to cart

Open cart and verify item

Take screenshot & attach to Allure report

