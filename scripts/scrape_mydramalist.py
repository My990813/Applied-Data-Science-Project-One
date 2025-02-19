from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_drama_info(title):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Add a random user agent
    UAS = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"]
    chrome_options.add_argument(f'user-agent={random.choice(UAS)}')

    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)

        # Construct the search results URL
        search_url = f"https://mydramalist.com/search?q={'%20'.join(title.split(' '))}"
        driver.get(search_url)

        # Wait for some content to load (adjust the selector based on the page structure)
        try:
            WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text-primary title"))
            )
        except:
            raise Exception("Timeout waiting for page load")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Get first search result
        first_result = soup.find(class_='text-primary title').find('a')['href']

        # Construct the URL for the drama page on mydramalist
        url = f"https://mydramalist.com{first_result}"
        driver.get(url)

        # Wait for some content to load (adjust the selector based on the page structure)
        try:
            WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inline"))
            )
        except:
            raise Exception("Timeout waiting for page load")
        
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the director and screenwriter information
        director_element = soup.find('b', class_='inline', string='Director:')
        if not director_element: 
            director_element = soup.find('b', class_='inline', string='Screenwriter & Director:')
        screenwriter_element = soup.find('b', class_='inline', string='Screenwriter:')
        synopsis_element = soup.find(class_='show-synopsis')
        # native_title_element = soup.find('b', class_='inline', string='Native Title:')
        # also_known_as_element = soup.find('b', class_='inline', string='Also Known As:')
        # genres_element = soup.find('b', class_='inline', string='Genres:')

        director = director_element.parent.find('a').text.strip() if director_element else None
        screenwriter = screenwriter_element.parent.find('a').text.strip() if screenwriter_element else None
        synopsis = synopsis_element.find('span').text.strip() if synopsis_element else None

        return director, screenwriter, synopsis

    except Exception as e:
        print(f"Error scraping {title}: {str(e)}")
        return None, None, None
    
    finally:
        driver.quit()
