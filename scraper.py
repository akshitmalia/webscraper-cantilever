import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "http://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Lists to store data
titles = []
prices = []
ratings = []

# Loop through each book on the page
for book in soup.select('article.product_pod'):
    titles.append(book.h3.a['title'])
    prices.append(book.select_one('.price_color').text)
    rating_class = book.select_one('.star-rating')['class'][1]
    ratings.append(rating_class)

# Store into DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

# Save as CSV
df.to_csv('books.csv', index=False)
print("Scraping complete. Data saved to books.csv")

