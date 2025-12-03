import requests

from bs4 import BeautifulSoup

# Scrape book information (title and price) from a website and perform basic analysis such as average price and most expensive book.
# Use the demo site: http://books.toscrape.com
# Count total number of books
# Calculate the average price
# Find the most expensive book

# url = "http://books.toscrape.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")


# print(soup.find("h1"))
# print(soup.find_all("h1"))

# articles = soup.select("div li article.product_pod")

# print(f"The number of books is {len(articles)}")


# prices = soup.select("div.product_price p.price_color")

# prices = [float(price.text[2:]) for price in prices]

# print(prices)

# print(f"Average price: {round(sum(prices) / len(prices), 2)}")

# titles_with_prices = {}

# print(articles)

# for article, price in zip(articles, prices):
#     title = article.select("h3 a ")[0]["title"]
#     titles_with_prices[title] = price 

# print(titles_with_prices)

# print(f"The most expensive book is {max(titles_with_prices, key=titles_with_prices.get)}")