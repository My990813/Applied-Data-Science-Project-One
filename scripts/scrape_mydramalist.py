from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_drama_info(driver, title):
    try:
        # Construct the search results URL
        search_url = f"https://mydramalist.com/search?q={'%20'.join(title.split(' '))}"
        print('Searching URL:', search_url)
        driver.get(search_url)

        # # Wait for some content to load (adjust the selector based on the page structure)
        # try:
        #     WebDriverWait(driver, timeout=600).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "text-primary title"))
        #     )
        # except:
        #     raise Exception("Timeout waiting for page load")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        print('Page loaded!')

        # Get first search result
        first_result = soup.find(class_='text-primary title').find('a')['href']
        print('Found first result:', first_result)

        # Construct the URL for the drama page on mydramalist
        url = f"https://mydramalist.com{first_result}"
        print('Searching URL:', url)
        driver.get(url)
                
        # # Wait for some content to load (adjust the selector based on the page structure)
        # try:
        #     WebDriverWait(driver, timeout=600).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "inline"))
        #     )
        # except:
        #     raise Exception("Timeout waiting for page load")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        print('Page loaded!')

        # Find the director and screenwriter information
        director_element = soup.find('b', class_='inline', string='Director:')
        if not director_element: 
            director_element = soup.find('b', class_='inline', string='Screenwriter & Director:')
        screenwriter_element = soup.find('b', class_='inline', string='Screenwriter:')
        if not screenwriter_element:
            screenwriter_element = soup.find('b', class_='inline', string='Screenwriter & Director:')
        synopsis_element = soup.find(class_='show-synopsis')
        # native_title_element = soup.find('b', class_='inline', string='Native Title:')
        # also_known_as_element = soup.find('b', class_='inline', string='Also Known As:')
        # genres_element = soup.find('b', class_='inline', string='Genres:')

        director = [a.text.strip() for a in director_element.parent.find_all('a')] if director_element else None
        screenwriter = [a.text.strip() for a in screenwriter_element.parent.find_all('a')] if screenwriter_element else None
        synopsis = synopsis_element.find('span').text.strip() if synopsis_element else None

        print('Director:', director)
        print('Screenwriter:', screenwriter)
        print('Synopsis:', synopsis)

        return director, screenwriter, synopsis

    except Exception as e:
        print(f"Error scraping {title}: {str(e)}")
        return None, None, None
    
    # finally:
    #     driver.quit()
