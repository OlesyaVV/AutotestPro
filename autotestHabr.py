def test_burger_click(page):
    page.goto("https://habr.com/ru/feed/")
    burger = page.get_by_role("button", name="Toggle menu")
    burger.click()
    from playwright.sync_api import expect
    menu_item = page.get_by_role("link", name="Тестирование Тестирование")
    expect(menu_item).to_be_visible()
    menu_item.hover()
    terminology_item = page.get_by_role("link", name="Терминология IT")
    expect(terminology_item).to_be_visible()
    terminology_item.click()
    expect(page).to_have_url("https://habr.com/ru/hubs/terminator/articles/")
