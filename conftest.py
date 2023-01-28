import json
import pytest
import selenium.webdriver


@pytest.fixture
def configuration_opt():
    with open('config.json',"r",encoding="utf8") as config_file:
        configuration = json.load(config_file)
    assert configuration['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(configuration['implicit_wait'], int)
    assert configuration['implicit_wait'] > 0
    return configuration


@pytest.fixture
def browser(configuration_opt):
    if configuration_opt['browser'] == 'Firefox':
        browser_opt = selenium.webdriver.Firefox()
    elif configuration_opt['browser'] == 'Chrome':
        browser_opt = selenium.webdriver.Chrome()
    elif configuration_opt['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        browser_opt = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{configuration_opt["browser"]}" is not supported')
    browser_opt.implicitly_wait(configuration_opt['implicit_wait'])
    yield browser_opt
    browser_opt.quit()
