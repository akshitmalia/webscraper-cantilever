# Web Scraper with Flask Interface

This project was built as part of the Cantilever Cybersecurity Internship (Task 1).

It scrapes book data from a sample e-commerce website and displays it through a searchable web interface.

## Features
- Extracts book title, price, and rating
- Stores the data in a CSV file (`books.csv`)
- Displays the scraped data using a Flask web app
- Real-time search bar to filter books by title

## Technologies Used
- Python 3.13
- Requests
- BeautifulSoup4
- Pandas
- Flask

## Project Structure
webscraper-cantilever/
├── books.csv
├── scraper.py
├── app.py
├── templates/
│ └── index.html
├── static/


## How to Run
1. Open terminal and navigate to the project folder
2. Run the scraper script:
python scraper.py
3. Start the Flask web server:
python app.py
4. Open the browser and go to:
http://127.0.0.1:5000/


## Note
This project demonstrates how publicly available data can be collected and why implementing rate limits and scraping protection is essential in web applications.

