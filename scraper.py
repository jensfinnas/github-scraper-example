import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://www.expressen.se"
filename = "data/{}.csv".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
fieldnames = ["Heading", "URL"]

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for link in soup.find_all("a", href=True):
        href = link.get("href")
        heading = link.find("h2")

        if href and "/nyheter/" in href and heading:
            writer.writerow({"Heading": heading.text.strip(), "URL": href})

print("Data saved to:", filename)
