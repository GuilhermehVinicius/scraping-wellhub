from scraper import load_full_page, extract_main_data, extract_detailed_data, extract_plans_values
#from database import engine, create_tables
import pandas as pd
from datetime import datetime
import time

def main():

    #create_tables()
    url = "https://wellhub.com/pt-br/search/sp/franca/"
    page_content = load_full_page(url)
    df_main = extract_main_data(page_content)
    print(df_main)
    df_details = extract_detailed_data(df_main['links'])
    
    
    url_plans = "https://wellhub.com/pt-br/plans-pricing/"
    plans_values = extract_plans_values(url_plans)

    result = pd.concat([df_main, df_details], axis=1)

    result = pd.merge(result, plans_values, on='base_plan', how='left')

    result = result[["name","base_plan","address","services","comorbidities","values"]]
    print(result)
    #result.to_sql('gyms_franca_wellhub', engine, if_exists='append', index=False)
    result['date'] = datetime.now().date()
    result.to_csv('gyms_franca_wellhub.csv',index=False)
    


if __name__ == "__main__": 
    while True:
        print("Executando tarefa diária...")
        main()
        print("Aguardando para proxima execução")
        time.sleep(86400)
    
    