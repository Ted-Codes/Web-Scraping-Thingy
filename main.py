from bs4 import BeautifulSoup
import requests
import webbrowser

username = input("Input youtube username: ")
link = "https://www.youtube.com/@" + username

r = requests.get(link)
r_text = r.text

soup = BeautifulSoup(r_text, features="html.parser")

object_link = soup.find(property="og:image")
dirty_link = str(object_link)
clean_link = dirty_link.split('"')[1]
print("Link:" + clean_link)

webbrowser.open_new(clean_link)

print("Status Code: " + str(r.status_code))
