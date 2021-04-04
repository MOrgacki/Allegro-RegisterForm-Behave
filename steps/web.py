from behave import *

from selenium.webdriver.support.ui import Select
import time

def choose_companyType(context, parameters):
    Select(context.driver.find_element_by_css_selector(
        "select[formcontrolname='legalForm']")).select_by_value(parameters['Company type'])
    if parameters['Company type'] == "3":
        context.driver.find_element_by_id("firstName").send_keys(parameters['First Name'])
        context.driver.find_element_by_id("lastName").send_keys(parameters['Last Name'])
    elif 4 <= int(parameters['Company type']) <= 12:
        context.driver.find_element_by_id("companyRegister").send_keys(parameters['KRS'])

    Select(context.driver.find_element_by_css_selector(
        "select[formcontrolname='state']")).select_by_value(parameters['Province'])


def choose_country(context,parameters):
    if parameters['Country Code'] == "PL":
        choose_companyType(context, parameters)
    elif parameters['Country Code'] == "-1":
        context.driver.find_element_by_id("countryName").send_keys(parameters['Custom country'])
        context.driver.find_element_by_css_selector("ul[class^='filterBox'] p").click()
        if parameters['Custom country'] == "Polska":
            choose_companyType(context, parameters)

    context.driver.find_element_by_id("name").send_keys(parameters['Company Name'])
    context.driver.find_element_by_id("taxId").send_keys(parameters['taxId'])
# "Constants"

SITE = 'https://allegro.pl.allegrosandbox.pl/rejestracja-konta-firmowego/nowe-konto'

# Givens


@given('Allegro registration page is displayed')
def step_impl(context):
    context.driver.get(SITE)
# Whens

@when('the company fills a basic data with')
def step_impl(context):
    parameters = context.table[0]
    context.driver.find_element_by_id("email").send_keys(parameters['E-mail'])
    context.driver.find_element_by_id("login").send_keys(parameters['Login'])
    context.driver.find_element_by_id("password").send_keys(parameters['Password'])
    context.driver.find_element_by_id("phone").send_keys(parameters['Phone'])


@when('chooses country code and fills following data about the company')
def step_impl(context):
    parameters = context.table[0]
    Select(context.driver.find_element_by_css_selector(
        "select[formcontrolname='countryCode']")).select_by_value(parameters['Country Code'])

    choose_country(context, parameters)


@when('completes company address')
def step_impl(context):
    parameters = context.table[0]
    context.driver.find_element_by_id("addressLine").send_keys(parameters['Address'])
    context.driver.find_element_by_id("city").send_keys(parameters['City'])
    context.driver.find_element_by_id("zipCode").send_keys(parameters['Zip Code'])

@when('accepts user agreement and submits a form')
def step_impl(context):
    context.driver.find_element_by_xpath("//form/div[2]/div/label").click()
    context.driver.find_element_by_id("submitFrom").click()
# Thens

# @then('result is shown for "{phrase}"')
# def step_impl(context, phrase):
#     result = context.driver.find_element_by_css_selector("p[class='m-type m-type--paragraph']").text
#     assert result == phrase
