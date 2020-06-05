import requests
import os

def Welcome() :
  return print("Welcome to IsItDown.py!\nplease write a URL or URLs you want to check. (separagted by comma)")

def url_split_valid(url) :
  urls = url.split(",")
  for url in urls :
    url = url.strip()
    url = url.lower()
    if "http://" in url :
      url = url
    elif "http://" not in url :
      url = f"http://{url}"
    try:
      r = requests.get(f"{url}")
      r_code = r.status_code
      if r_code == 200 :
        print(f"{url} is up!")
    except:
      print(f"{url} is down!")
      return

def url_valid(url) :
  if ".com" not in url :
    print(f"{url} is not a valid URl.")
  else :
    url_split_valid(url)
       
while True :
  Welcome()
  url = input()
  url_valid(url)
  answer =""
  while True:
    answer = input('Do you want to start over?(y/n): ')
    if answer in ("y","n") :
      break
    print("This is not invalid answer")
  if answer == "y" :
    os.system("clear")
    continue
  elif answer == "n" :
    print("ok,bye!")
    break


