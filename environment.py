from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.driver.quit()
