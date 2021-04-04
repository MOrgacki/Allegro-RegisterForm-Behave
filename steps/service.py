# """
# This module contains step definitions for service.feature.
# It uses the requests package:
# http://docs.python-requests.org/
# """
#
# import requests
#
# from behave import *
#
#
# # "Constants"
#
# SITE_API = 'https://edge.allegro.pl.allegrosandbox.pl/companies'
# querystring = {"dryRun":"true","include":"email"}
#
# # Whens
#
# @when('the DuckDuckGo API is queried with')
# def step_impl(context):
#     first_row = context.table[0]
#     payload = "{\"address\":{\"countryCode\":null},\"" \
#               "agreementTerms\":null,\"companyRegister\":null,\"" \
#               "email\":\"test\",\"firstName\":null,\"" \
#               "lastName\":null,\"login\":null,\"password\"" \
#               ":null,\"phone\":null,\"taxId\":null}"
#     headers = {
#         'Accept': "application/vnd.allegro.public.v1+json",
#         'Accept-Language': "pl",
#         'Content-Type': "application/vnd.allegro.public.v1+json",
#         'Referer': "https://allegro.pl.allegrosandbox.pl/rejestracja-konta-firmowego/nowe-konto",
#         'Sec-Fetch-Mode': "cors",
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "51d3c8d4-bd46-42e9-ae66-03c0cd4532e0,2fd73a66-da55-43ec-90af-add99d546549",
#         'Host': "edge.allegro.pl.allegrosandbox.pl",
#         'Accept-Encoding': "gzip, deflate",
#         'Content-Length': "180",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#         }
#     response = requests.request("POST", SITE_API, data=payload, headers=headers, params=querystring)
#     print(response.text)
#
# # Thens
#
# @then('the response status code is "200"')
# def step_impl(context):
#     assert context.response.status == 442
#
#