import json
import pytest
import selenium.webdriver


@pytest.fixture
def config():
    with open('config.json',"r",encoding="utf8") as config_file:
        configuration = json.load(config_file)
    assert configuration['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(configuration['implicit_wait'], int)
    assert configuration['implicit_wait'] > 0
    return configuration


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        browser_opt = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        browser_opt = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        browser_opt = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    browser_opt.implicitly_wait(config['implicit_wait'])
    yield browser_opt
    browser_opt.quit()
