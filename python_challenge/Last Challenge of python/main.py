"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, request , redirect , render_template ,send_file
from scrapper import stackoverflow, wework, remoteok
import csv, time
from export_csv import save_to_file
import os.path
from urllib.parse import unquote

app = Flask("Remote Jobs")



@app.route("/")
def home () :
  return render_template("job_list.html")

db = {}


@app.route("/search")
def search () :
  search_input = request.args.get("term")
  search_input = unquote(search_input.lower())
  if search_input :
    url_list = [f'https://stackoverflow.com/jobs?r=true&q={search_input}',
                f'https://weworkremotely.com/remote-jobs/search?term={search_input}',
                f'https://remoteok.io/remote-dev+{search_input}-jobs'
                ]
    fromDb = db.get(search_input)
    if fromDb :
      language_list = fromDb
    else :
      language_list = stackoverflow(url_list[0]) + wework(url_list[1]) + remoteok(url_list[2])
      db[search_input] = language_list
      save_to_file(language_list,search_input)
  else :
    return redirect("/")
  return render_template("search_input.html",search_input = search_input,language_list = db[search_input],length = len(db[search_input]))

@app.route("/export/<search_input>")
def export(search_input) :
  try:
    search_input = search_input.lower()
    if not search_input :
      raise Exception()
    file = f'static/{search_input}.csv'
    if os.path.isfile(file) :
      file_name = f"static/{search_input}.csv"
      attachment_filename = f"{search_input}_jobs.csv"
      return send_file(file_name, attachment_filename = attachment_filename, as_attachment=True)
    else :
      redirect("/search")
  except :
    redirect("/")
      
app.run(host="0.0.0.0")


