import json
from bs4 import BeautifulSoup as BS
import datetime
import undetected_chromedriver as uc
import time


def get_data(url):
    options = uc.ChromeOptions()
    options.user_data_dir = "c:\\temp\\profile"
    options.add_argument('--user-data-dir=c:\\temp\\profile2')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    
    driver = uc.Chrome(options=options)  

    try:
        driver.get(url)
        time.sleep(10)
        html = driver.page_source

    except Exception as ex:
        print(ex)
    finally:
         driver.close()
         driver.quit()

    s = BS(html, "lxml")
    with open("index.html", "w") as file:
        file.write(s.text)
    # card_array = s.findAll("img",class_="story-image__image image-loaded")
    # print(card_array)
    
    # card_dict = []
    # for card in card_array:
    #     card_url = card.find("data-large-image")
    #     print(card_url)
    #     card_discr = card.text
    #     print(card_discr)
    #     card_dict.append(
    #         {
    #             "pictures": card_url,
    #             "discr": card_discr
    #         }
    #     )
    #     print(card_dict)

    # with open("result_dict.json", "w") as file:
    #     json.dump(card_dict, file, indent=4, ensure_ascii=False)

def main():
    get_data("https://pikabu.ru")
    
    
if __name__ == '__main__':
    main()