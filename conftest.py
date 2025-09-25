import pytest
from selenium import webdriver
import time
from pathlib import Path
import os
import pytest_html 

    
LOG_FILE = Path("test_durations.log")
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """executa o setup antes de cada teste e registra o tempo de duracao"""
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    print(msg)
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    """executa o teardown apos cada teste e registra o tempo de termino e duracao"""
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)

    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

def pytest_addoption(parser):
    """adiciona a opcao de linha de comando para selecionar o navegador"""
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")

@pytest.fixture
def driver(request):
    """cria a fixture do driver com base na opcao de linha de comando"""
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit() 

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """adiciona screenshots para o relatorio HTML em caso de falha"""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take screenshot
        driver = item.funcargs['driver']
        screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
        driver.save_screenshot(screenshot_file)
        # Add screenshot to the HTML report
        if screenshot_file:
            html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
           f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
    report.extra = extra