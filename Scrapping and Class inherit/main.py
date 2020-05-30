import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


os.system("clear")

url = "https://www.iban.com/currency-codes"

def default(url) :
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  table = soup.find('table',{'class':'table'})
  countries = table.select("tr > td:nth-of-type(1)")
  currencies = table.select("tr > td:nth-of-type(2)")
  alpha_3codes = table.select("tr > td:nth-of-type(3)")
  return countries,currencies,alpha_3codes

def set_list_cts(cts) :
  print("Welcome to CurrencyConvert PRO 2000 !")
  lst_cts = []
  for num,country in enumerate(cts) :
    country = (country.string).capitalize()
    print(f"# {num} {country}")
    lst_cts.append(country)
  print("\nWhere are you from ? Choose a country by number.\n")
  return lst_cts

def set_list_crcs(crcs) :
  lst_crcs = []
  for currency in crcs :
    if currency != "No universal currency" :
      lst_crcs.append(currency.string)
    else :
      lst_crcs.append("This isn't currency")
  return lst_crcs

def set_list_codes(codes) :
  lst_codes = []
  for code in codes :
    if code != "" :
      lst_codes.append(code.string)
    else :
      lst_codes.append("No Code")
  return lst_codes

# Variables
countries,currencies,alpha_3codes = default(url)
lst_crcs = set_list_crcs(currencies)
lst_codes = set_list_codes(alpha_3codes)
# ---------------------------------------------

lst_cts = set_list_cts(countries)

class Input_num :
  def inp(self) :
    try :
      self.num = int(input("# : "))
    except :
      print("That wasn't a number.")
      Input_num.inp(self)
    else :
      if self.num > len(lst_cts) :
        print("That's not exist.")
        Input_num.inp(self)
    return self.num

class Input_amt :
  def inp(self) :
    super().inp()
    self.num = int(input())

class Country :
  def __init__(self,num) :
    self.num = num

  def p(self):
    self.country = lst_cts[self.num]
    self.code = lst_codes[self.num]
    print(f"{self.country}")

class Amount(Country) :
  def __init__(self,num) :
    super().__init__(num)
  def p(self) :
    super().p()
    print("\nNow choose another country.\n")
    return self.code

class Converto(Country) :
  def __init__(self,num) :
    super().__init__(num)
  def p(self,code1) :
    super().p()
    print(f"\nHow many {code1} do you want to convert to {self.code}?")
    return self.code



number = Input_num()
num = number.inp()
amount = Amount(num)
code1 = amount.p()
num = number.inp()
converto = Converto(num)
code2 = converto.p(code1)

AMT = input()


def amount_convert() :
  CONV_URL = f"https://transferwise.com/gb/currency-converter/{code1}-to-{code2}-rate?amount={AMT}"
  request = requests.get(CONV_URL)
  soup = BeautifulSoup(request.text, 'html.parser')
  box = soup.find_all("div",{"class":"col-xs-7"})
  amt_btn = box[0].input['value']
  cvt_btn = box[1].input['value']
  amt = format_currency(amt_btn,code1, locale="ko_KR")
  cvt = format_currency(cvt_btn,code2, locale="ko_KR")
  print(f"{code1} {amt} is {cvt}")


amount_convert()
