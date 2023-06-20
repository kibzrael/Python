import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions", timeout=9000)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary", limit=10)
print(f"{len(questions)} Questions:")
for question in questions:
    print(question.select_one(".s-link").string)
    print(question.select_one(".s-post-summary--stats-item-number").string, " Votes")
