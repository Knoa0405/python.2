from bs4 import BeautifulSoup
import requests



def stackoverflow (url) :
  language_list = []
  try :
    r = requests.get(f"{url}")
    soup = BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all("div",{"class":"grid--cell fl1"})
    if divs :
      for div in divs :
        title = div.find("a")
        company = div.find("h3",{"class":"mb4"})
        link = div.find("a")
        title = title.string
        company = company.find("span")
        link = link["href"]
        if title and company and link :
          stack_dic = {
            "title" : title,
            "company" : company.string.strip().replace("\r\n",""),
            "Link" : "https://stackoverflow.com"+link
          }
          language_list.append(stack_dic)
  except :
    pass
  return language_list

def wework (url) :
  language_list = []
  try :
    r = requests.get(f"{url}")
    soup = BeautifulSoup(r.text,"html.parser")
    uls = soup.find_all("ul")
    if uls :
      for ul in uls  :
        lis = ul.find_all("li")
        for li in lis :
          a_tag = li.find("a")
          if a_tag :
            company = a_tag.find("span",{"class":"company"})
            title = a_tag.find("span",{"class":"title"})
            link = a_tag["href"]
            if title and company and link :
              wework_dic = {
                "title" : title.string,
                "company" : company.string,
                "Link" : "https://weworkremotely.com"+link
              }
              language_list.append(wework_dic)
  except :
    pass
  return language_list

def remoteok (url) :
  language_list = []
  try :
    r = requests.get(f"{url}")
    soup = BeautifulSoup(r.text,"html.parser")
    tbody = soup.find("table")
    if tbody :
      trs = tbody.find_all("tr")
      for tr in trs :
        td = tr.find("td",{"class":"company position company_and_position"})
        if td :
          a_tag = td.find("a",{"class":"companyLink"})
          if a_tag :
            company = a_tag.find("h3")
            title = td.find("h2")
            link = a_tag["href"]
            if title and company and link :
              remote_dic = {
                "title" : title.string,
                "company" : company.string,
                "Link" : "https://remoteok.io"+link
              }
              language_list.append(remote_dic)
  except :
    pass
  return language_list
