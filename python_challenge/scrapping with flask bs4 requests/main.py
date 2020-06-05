import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
from urllib.parse import unquote

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]
app = Flask("DayEleven")

def url_req(reddit) :
  url = f"https://www.reddit.com/r/{reddit}/top/?t=month"
  req_top = requests.get(url, headers=headers)
  soup = BeautifulSoup(req_top.text, 'html.parser')
  a_tags = soup.find_all("a",{"data-click-id":"body"})
  votes = soup.find_all("button",{"aria-label":"upvote"})  
  for a_href,vote in zip(a_tags,votes) :
    vot = vote.find_next_sibling()
    h3 = a_href.select("a > div > h3")
    h3 = h3[0]
    ahref = a_href["href"]
    h3_href = {
    "h3" : h3.string,
    "ahref" : ahref,
    "reddit" : reddit,
    "vote" : vot.string
    }
    h3_href_lst.append(h3_href)
  

@app.route("/")
def home() :

  return render_template("home.html",subreddits = subreddits)

h3_href_lst = []

@app.route("/read")
def read() :
  lst = []
  for reddit in subreddits :
    val = request.args.get(f'{reddit}')
    if val == "on" :
      url_req(reddit)
      lst.append(f'{reddit}')
  return render_template("read.html",reddits = lst, h3_href_lst = h3_href_lst)



@app.route("/add")
def add() :
  addreddit = request.args.get("addreddit")
  addreddit = unquote(addreddit)
  r = requests.get(f"https://www.reddit.com/r/{addreddit}")
  print(r.status_code)
  if r.status_code == 502 :
    subreddits.append(addreddit)
    return redirect("/")
  elif "/r/" in addreddit :
    text = "Write the name without /r/"
    return render_template("error.html",error_text = text)
  else :
    text = "That subreddit does not exist"
    return render_template("error.html",error_text = text)
    
 

app.run(host="0.0.0.0")