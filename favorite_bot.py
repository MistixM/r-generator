import json
import os
import time
import logging

from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from DrissionPage.common import By

logging.basicConfig(filename='debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def favorite(cloth_id, cloth_acc, info_message, button, request_delay):

    favs = 0

    try:
        account_count = int(cloth_acc)
    except Exception as e:
        info_message.configure(text="Invalid limit value!")
        button.configure(state='normal')
        return
    
    files = os.listdir("accounts/")
    

    for account in files:
        if favs == account_count:
            break

        with open(f"accounts/{account}", 'r') as file:
            try:
                cookies = json.load(file)

                options = ChromiumOptions()
                # options.set_argument('--headless=new')
                # options.set_argument('--no-sandbox')
                # options.headless(True)

                driver = ChromiumPage(options)
                driver.get(f"https://www.roblox.com/catalog/{cloth_id}")

                print("Cookie as about to set")
                for cookie in cookies:
                    print("cookie set")
                    driver.set.cookies(cookie)
                
                print("set cookies, continue")

                driver.refresh()

                time.sleep(2)
                
                driver.get(f"https://www.roblox.com/catalog/{cloth_id}")
                
                time.sleep(1)

                # Elements
                fav_button_el = By.ID, "toggle-favorite"

                # Fav cloth
                driver.ele(fav_button_el).click()
                favs += 1
                info_message.configure(text=f"Liked: {favs}/{account_count}")

                time.sleep(request_delay) # Default: 4 sec

            except Exception as e:
                logging.warn(f"An error occurred: {e}")
                info_message.configure(text="Something went wrong.. Please try again later")
                driver.quit()
                button.configure(state='normal')
                return
            
    button.configure(state='normal')
    info_message.configure(text=f"You're all set!")
    driver.quit()