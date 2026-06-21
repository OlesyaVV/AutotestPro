def test_check_page_title(page):
    # Фикстура `page` предоставляется автоматически плагином pytest-playwright
    page.goto("https://example.com")
    
    # Проверяем заголовок страницы
    assert page.title() == "Example Domain" 

def test_check_h1(page):
    page.goto("https://example.com")
    h1_locator = page.locator("h1")
# Проверка через expect (рекомендуемый способ ассертов в Playwright)
    from playwright.sync_api import expect

    expect(h1_locator).to_have_text('Example Domain')

def test_check_p(page):
    page.goto("https://example.com")
    locator = page.get_by_text('This domain is for use in documentation examples without needing permission. Avoid use in operations.')
    from playwright.sync_api import expect

    expect(locator).to_contain_text('domain is for use')

def hello():
    print("Hello World!")
    hello()

