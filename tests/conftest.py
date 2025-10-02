import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    # Enable video recording for each test
    context = browser.new_context(record_video_dir="reports/videos/")
    page = context.new_page()
    yield page

    # Handle failures
    if request.node.rep_call.failed:
        # Attach screenshot
        screenshot_path = f"reports/{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach video
        video_path = page.video.path()
        page.close()  # video gets saved only after closing
        allure.attach.file(
            video_path,
            name="Failure Video",
            attachment_type=allure.attachment_type.WEBM
        )
    else:
        page.close()

    context.close()


# Hook to get test result (needed for failure detection)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
