import json
import pytest
import selenium.webdriver
from prettyconf import Configuration
from pages.configuration.properties import Properties


def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='staging', help='Environment'
    )


@pytest.fixture
def props(request) -> Configuration:
    args = {
        "env": request.config.getoption('--env')}
    return Properties.get_config(args)


@pytest.fixture
def config():
    with open('config.json', "r", encoding="utf8") as config_file:
        configuration = json.load(config_file)
    assert configuration['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(configuration['implicit_wait'], int)
    assert configuration['implicit_wait'] > 0
    return configuration


@pytest.fixture
def browser(config, props):
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
    browser_opt.set_window_size(1366,768)
    browser_opt.implicitly_wait(config['implicit_wait'])
    yield browser_opt
    browser_opt.quit()
