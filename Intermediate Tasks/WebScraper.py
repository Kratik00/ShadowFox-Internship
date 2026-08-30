# Task - 01: WEBSCRAPER (With BeautifulSoup)
#=================================[           WEBSCRAPER           ]=====================================
# Importing Libraries
import requests
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def scrap_book():
    #Defining Url & Headers
    current_url = "https://books.toscrape.com"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/26.5.2 Safari/605.1.15"
    }
    scraped_data = []
    while current_url:
        response = requests.get(current_url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        books_elements = soup.find_all("article", class_="product_pod")
        for book in books_elements:
            #For Title
            title = book.h3.a["title"]
        
            #For Price
            price = book.find('p', class_="price_color").text.strip()
        
            #For checking if the book is still in stock
            availability = book.find("p", class_="instock").get_text(strip=True)
        
            scraped_data.append(
                {
                    'Title': title,
                    'Price': price,
                    'Availability': availability
                }
            )
        next_page = soup.find("li", class_="next")
        if next_page:
            next_url = next_page.find("a")["href"]
            current_url = urljoin(current_url, next_url)
            print(current_url)
        else:
            current_url=None
    file_name = "scraped_bookdata.csv"
    with open(file_name, 'w', encoding="utf-8") as f:
        fieldnames = ['Title', 'Price', 'Availability']
        writer = csv.DictWriter(f, fieldnames)
            
        writer.writeheader()
        writer.writerows(scraped_data)

if __name__ == "__main__":
    scrap_book()