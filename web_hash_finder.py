import mechanicalsoup
import requests

browser = mechanicalsoup.StatefulBrowser()
defaultUrl = "https://md5calc.com/hash"
browser.open(defaultUrl)

browser.select_form(selector='form')

encrypt_options = browser.get_current_page().findAll('option')
input_to_encrypt = ''

while not input_to_encrypt:
  try:
    input_to_encrypt = input("Digite o que deseja criptografar: \n")
    if not input_to_encrypt:
      raise ValueError
  except ValueError:
    print("O valor não pode ser nulo")

for option in encrypt_options:
  browser.open(defaultUrl + "/" + option["value"] + "/" + input_to_encrypt)
  calculator = browser.get_current_page().findAll(class_="hash-calculator")
  actual_hash = calculator[0].find('pre')
  print(option["value"], actual_hash.text)
  
  
