import requests

from bs4 import BeautifulSoup

from collections import Counter

url = "http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# print(soup.find_all("span", class_="text"))

# Count total number of quotes
quotes =soup.select("div.quote span.text")

print(f"the total number of quotes  found is {len(quotes)}")
# Count the number of unique authors
authors = soup.select("span small.author")

unique_authors = { author.get_text() for author in authors}

print(f"Total number of unique authors: {len(unique_authors)}")
# Find the author with the most quotes on the page
authors = soup.find_all("small", class_="author")

author_names = [author.get_text() for author in authors]

count_of_authors = Counter(author_names)

most_common, count = count_of_authors.most_common(1)[0]

print(f"The author with the most quotes is {most_common} with {count} quotes.")

# Count how many quotes contain the word “is” (case-insensitive)
quotes = soup.find_all("span", class_="text")

# Count quotes containing "is" (case-insensitive)
count_is = sum(1 for quote in quotes if "is" in quote.get_text().lower())

print("Number of quotes containing 'is':", count_is)

# List all tags that appear and how many times each appears
tags = soup.find_all("a", class_="tag")

tag_names = [tag.get_text().lower() for tag in tags]

target_tags = ["love", "inspirational", "life", "humor", 
               "books", "reading", "friendship", "friends", 
               "truth", "simile"]


tag_count = Counter(tag_names)


for t in target_tags:
    print(f"{t}: {tag_count.get(t, 0)}")