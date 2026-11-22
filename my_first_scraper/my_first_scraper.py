import requests
import csv
import io
from bs4 import BeautifulSoup

def request_github_trending(url):
    responses = requests.get(url)
    return responses

def extract(page):
    soup = BeautifulSoup(page.text, "html.parser")
    repositories = soup.find_all("article") 
    return repositories 

def transform(html_repos):
    repositories_data = []

    for repo in html_repos:
        title = repo.find('h1')
        link = title.find('a')
        url = link['href']
        parts = url.strip('/').split('/')
        developer = parts[0]
        repository_name = parts[1]
        stars = repo.find('a', href=lambda href: href and href.endswith('/stargazers'))
        nbr_stars = int(stars.text.strip().replace(',',''))

        repositories_data.append({
            "developer": developer,
            "repository_name": repository_name,
            "nbr_stars": nbr_stars
        })
    return repositories_data

def format(repositories_data):
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["Developer", "Repository Name", "Number of Stars"])

    for repo in repositories_data:
        writer.writerow([
            repo["developer"],
            repo["repository_name"],
            repo["nbr_stars"]
        ])
    return output.getvalue().strip()

url = "https://storage.googleapis.com/qwasar-public/track-ds/trending_14_06_2022"
page = request_github_trending(url)
repositories = extract(page)
data = transform(repositories)
csv_data = format(data)

print(csv_data)
