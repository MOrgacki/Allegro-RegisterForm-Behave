@web
Feature: Sign-Up as company
  As a company,
  I want to have opportunity to register,
  So I fill a form.

  Scenario Outline: Positive registration for a polish company
    Given Allegro registration page is displayed
    When the company fills a basic data with
    | E-mail     |  Login   |Password    |Phone  |
    |mo@gmail.com| 1_org | Testing_mo1|+48500100100|
    And chooses country code and fills following data about the company
    |Country Code|Company type|Province      |First Name  |Last Name |KRS  |Company Name|taxId  |
    |PL          |<legalForm> |<countryState>| <firstName>|<lastName>|<KRS>|Testy SA    |3386379154|
    And completes company address
    |Address      |City   |Zip Code|
    |<addressLine>|<city> |<zipCode>|
    And accepts user agreement and submits a form
#    Then result is shown for "<phrase>"


    #(legalForm 2 => basic | legalForm 3 => basic + firstName, lastName  | legalForm <4:11> => basic + KRS)
    Examples: Polish form data
     |KRS        |legalForm|firstName|lastName|countryState  | addressLine   |city |zipCode|  phrase  |
     |           |     2   |Marcin   |Org |OP            |ul. ogórkowa 12|Opole|12-100 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |           |     3   |Marcin   |Łórgąćki|MP            |ul. testowa 12 |Kraków|10-100 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |0123456789 |     4   |         |        |MZ            |ul. fajna   1/2|Warszawa|47-100 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |9876543210 |     7   |         |        |PK            |ul. pusta 12   |Rzeszów|40-000 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |9999999999 |     11  |         |        |SK            |ul. krótka 12  |Katowice|02-500 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|


  Scenario Outline: Positive registration for a foreign company
    Given Allegro registration page is displayed
    When the company fills a basic data with
    | E-mail     |  Login   |Password    |Phone  |
    |mo@gmail.com| 1_org | Testing_mo1|+48500100100|
    And chooses country code and fills following data about the company
    |Country Code |Company Name |taxId  |
    |<countryCode>|Testowania|<taxId>|
    And completes company address
    |Address      |City  |Zip Code |
    |<addressLine>|<city>|<zipCode>|
    And accepts user agreement and submits a form
#    Then result is shown for "<phrase>"


     Examples: Foreign form data
     |countryCode|  taxId   | addressLine   | city  | zipCode |  phrase  |
     |GB         |3386379154|shiny 12   | London   |  10 200 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |US         |5663203178|beatiful 12| New York |  40 115 | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     |FR         |3554247112|źeli 12    | Paris    |  2555   | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|


Scenario Outline: Positive registration for custom type company
    Given Allegro registration page is displayed
    When the company fills a basic data with
    | E-mail     |  Login   |Password    |Phone  |
    |mo@gmail.com| 1_org | Testing_mo1|+48500100100|
    And chooses country code and fills following data about the company
    |Custom country |Country Code |Company type|Province      |First Name  |Last Name |KRS      |Company Name  |taxId  |
    |<customCountry>|-1           |<legalForm> |OP            | Marcin     |Org  |111111111|Testownia|<taxId>|
    And completes company address
    |Address      |City     |Zip Code  |
    |ul. testowa 12 | <city>  | <zipCode>|
    And accepts user agreement and submits a form
#    Then result is shown for "<phrase>"


     Examples: Foreign form data
     |customCountry|legalForm| taxId    |city| zipCode   |  phrase  |
     | Gambia      |         |6017749036|Birro|  002100  | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     | Polska      |    2    |7011167842|Łódz |  41-100  | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
     | Francja     |         |7617413552|Paris|  235     | Aby dokończyć rejestrację, potwierdź adres e-mail. Sprawdź pocztę i kliknij w przycisk w wiadomości.|
