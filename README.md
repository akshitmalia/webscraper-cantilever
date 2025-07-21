# Web Scraper with Flask Interface

This project was developed as part of the Cantilever Cybersecurity Internship (Task 1).

It scrapes book data from a demo e-commerce website ([books.toscrape.com](http://books.toscrape.com)) and displays it on a user-friendly web interface with search functionality.

---

## Features
- Scrapes book **title, price, and rating**
- Stores the data in a CSV file (`books.csv`)
- Displays the scraped data in a web interface built using Flask
- Provides real-time filtering using a search bar

---

## Technologies Used
- Python 3.13
- Flask
- Requests
- BeautifulSoup4
- Pandas

---

## Project Structure
webscraper-cantilever/
├── books.csv
├── scraper.py
├── app.py
├── templates/
│ └── index.html
├── static/
└── venv/ (not pushed to GitHub)


---

## How to Run (Step-by-Step)

1. **Open Command Prompt** and navigate to the project folder:
cd path\to\webscraper-cantilever

2. **Create a virtual environment**:
python -m venv venv

3. **Activate the virtual environment**:
venv\Scripts\activate

4. **Install required packages**:
pip install flask pandas requests beautifulsoup4

5. **Run the scraper to collect book data**:
python scraper.py

6. **Start the Flask server**:
python app.py

7. **Open browser and go to**:
http://127.0.0.1:5000/


---

## Notes
- The 'venv' folder is excluded from the repository using '.gitignore'.
- The scraper uses only publicly available test data from books.toscrape.com.



