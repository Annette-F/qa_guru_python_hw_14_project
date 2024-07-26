from selene import browser, have, be


def test_scroll_main_page():
    # Opened main page
    browser.open('/')

    # Scroll page down
    for _ in range(4):
        browser.element('.nav-home').element('.js-mnext').click()

    # Check element footer
    browser.element('.footer').should(be.present)

    # Scroll page up
    for _ in range(4):
        browser.element('.nav-home').element('.js-mprev').click()

    # Check element header
    browser.element('.header').should(be.present)


def test_career_page_requirements():
    # Open main page
    browser.open('/')

    # Open Career page
    browser.element('[href="/23310/"]').should(have.text('Карьера')).hover()
    browser.element('[href="/38819/"]').click()
    browser.element('.titlepage').should(have.text('Требования к кандидатам'))
