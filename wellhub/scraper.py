from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import pandas as pd
from utils import configure_driver

def load_full_page(url):
    driver = configure_driver()
    driver.get(url)
    time.sleep(10)


    while True:
        try:
            button_more = driver.find_element(By.CSS_SELECTOR, "button.sc-4c820cc2-9.gdPfkB.sc-4c820cc2-129.gBIdEb.sc-4c820cc2-129.gBIdEb")
            button_more.send_keys(Keys.RETURN)
            time.sleep(5)
            
        except (NoSuchElementException, ElementNotInteractableException):
            print("Todos os parceiros foram carregados ou o botão não está mais disponível.")
            break
    
    page_content = driver.page_source

    print(page_content)

    driver.quit()
    return page_content

def extract_main_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    
    card_selector = 'body > div.sc-81390cec-0.cgVNna > div:nth-child(4) > div > div > div > div > div > div > div > div > div > div > div.sc-4c820cc2-8.jpWCYa > div > div'
    name_selector = f'{card_selector} > a > div.sc-4c820cc2-8.ha-dQxy > div.sc-4c820cc2-8.fvaiuu > p'
    plan_selector = f'{card_selector} > a > div.sc-4c820cc2-8.ha-dQxy > div.sc-4c820cc2-90.geoXDo > span'
    link_selector = f'{card_selector} > a'

    names, plans, links = [], [], []
    cards = soup.select(card_selector)
    for card in cards:
        name = card.select_one(name_selector)
        plan = card.select_one(plan_selector)
        link = card.select_one(link_selector)
        names.append(name.text if name else "N/A")
        plans.append(" ".join(plan.text.split()[4:]) if plan else "N/A")
        links.append(link.get('href') if link else "N/A")
    return pd.DataFrame({'name': names, 'base_plan': plans, 'links': links})

def extract_detailed_data(links):
    names, addresses, services, comorbidities = [], [], [], []
    for link in links:
        driver = configure_driver()
        driver.get(f"https://wellhub.com/{link}")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        address = soup.select_one('body > div.sc-81390cec-0.cgVNna > div.sc-3e899c21-0.bjuvVE > div.sc-4c820cc2-55.sc-c531bbc2-0.hTZZoP.rDsOg > div > div > div > div.sc-4c820cc2-8.hVCHVl > div:nth-child(1) > div.sc-cdf5f068-1.fFzbcC > p')
        service_elements = soup.select('span.sc-4c820cc2-92.bwULEV')
        comorbidity_elements = soup.select('p.sc-4c820cc2-74.sc-178740bd-5.TDbSS.gbrHZH')

        addresses.append(address.text if address else "N/A")
        services.append(",".join([s.text for s in service_elements]))
        comorbidities.append(",".join([c.text for c in comorbidity_elements]))
    return pd.DataFrame({'address': addresses, 'services': services, 'comorbidities': comorbidities})

def extract_plans_values(url_plans):
    plans, plans_values = [], []
    driver = configure_driver()
    driver.get(url_plans)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    plans_elements = soup.select('h3.sc-4c820cc2-71.cXCAJT, h2.sc-4c820cc2-71.cXCAJT')
    plans_values_elements = soup.select('p.sc-4c820cc2-67.jrOKC')
    
    plans.append([v.text for v in plans_elements])
    plans_values.append([v.text for v in plans_values_elements])


    plans = [valor.replace(' ', '') for valor in plans[0]]
    plans_values = [float(valor.replace(',', '.')) for valor in plans_values[0]]
    print(plans)
    print(plans_values)

    return pd.DataFrame({'base_plan': plans, 'values': plans_values})
    
