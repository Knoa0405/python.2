import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
com_a_hrefs = []
com_titles = []
dic_data = {}
lst_dic = []

def front_page() :
  request = requests.get(alba_url)
  soup = BeautifulSoup(request.text,"html.parser")
  com_lst = soup.find_all("li",{"class":"impact"})
  for com_list in com_lst :
    com_a_tag = com_list.find("a",{"class":"goodsBox-info"})
    com_a_href = com_list.find("a")["href"]
    com_title = com_a_tag.find("span",{"class":"company"})
    com_a_hrefs.append(com_a_href)
    com_titles.append(com_title.string)

def put_url() :
  com_a_hrefs.reverse()
  com_a_href = com_a_hrefs.pop()
  com_a_hrefs.reverse()
  return com_a_href

def company_data(com_a_href) :
  lst = []
  print(f"Scrapping {com_a_href}")

  try :
    request = requests.get(f"{com_a_href}")
    soup = BeautifulSoup(request.text,"html.parser")
    com_tb= soup.find("tbody")
    com_row = com_tb.find_all("tr",{"class":""})

    for com_info in com_row :
      local_td = com_info.find("td",{"class":"local"})
      com_branch_td = com_info.find("td",{"class":"title"})
      time_td = com_info.find("td",{"class":"data"}) 
      pay_td = com_info.find("td",{"class":"pay"})
      regdate_td = com_info.find("td",{"class":"regDate"})

      if local_td and com_branch_td and time_td and pay_td and regdate_td :
        local = local_td.get_text().replace("\xa0"," ")
        com_branch_td = com_branch_td.find("span",{"class","company"})
        branch = com_branch_td.get_text()
        time = time_td.get_text()
        pay = pay_td.get_text()
        regdate = regdate_td.get_text()
        dic = {"local" : local ,"branch" : branch, "time" : time, "pay" : pay ,"regdate" : regdate}
        lst.append(dic)
  except :
    print("URL error or No list")
    
  return lst

def save_file() :
  for dic_key,dic_value in dic_data.items() :
    f = open(f'{dic_key}.csv', mode="w")
    writer = csv.writer(f)
    writer.writerow(["place","title","time","pay","date"])
    for dic_val in dic_value :
      writer.writerow(list(dic_val.values()))

def main() :
  # put_url 함수로 URL을 하나씩 넣어주고 company_data 함수에서
  # 나오는 값을 lst_dic 에 담아준다. 이후, for in zip 문으로 dic_data로 
  # company_title과 company_data를 묶어서 dic_data로 dict 형태로 저장한다.
  # 나중에 save 할 때 dic_data의 키와 값으로 csv파일의 제목과 data를 넣어준다.
  while True :
    if com_a_hrefs != [] :
      com_a_href = put_url()
      lst_dic.append(company_data(com_a_href))
      for com_title,com_data in zip(com_titles,lst_dic) : 
        dic_data[com_title] = com_data
    else :
      break

front_page()
# delete Wrong URL
del com_titles[-1]
del com_a_hrefs[-1]
main()
save_file()