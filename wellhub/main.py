from scraper import load_full_page, extract_main_data, extract_detailed_data
from database import engine, create_tables
import pandas as pd
import time

def main():

    create_tables()
    url = "https://wellhub.com/pt-br/search/sp/franca/"
    page_content = load_full_page(url)
    df_main = extract_main_data(page_content)
    print(df_main)
    df_details = extract_detailed_data(df_main['links'])
    result = pd.concat([df_main, df_details], axis=1)
    result = result[["name","base_plan","address","services","comorbidities"]]
    result.to_sql('gyms_franca_wellhub', engine, if_exists='append', index=False)
    print(result)


if __name__ == "__main__": 
    while True:
        print("Executando tarefa diária...")
        main()
        print("Aguardando para proxima execução")
        time.sleep(86400)
    
    