from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

from DrissionPage.common import By

import time
import string
import random
import json
import os
import logging

from faker import Faker

logging.basicConfig(filename='debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def start(info_message):
    fake = Faker()

    extenstion_path = "extenstion/capsolver"

    options = ChromiumOptions()
    options.add_extension(extenstion_path)
    options.set_argument('--headless=new')
    options.set_argument('--no-sandbox')
    options.headless(True)

    driver = ChromiumPage(options)
    driver.get("https://www.roblox.com")

    driver.set.cookies.clear()
    driver.refresh()
    driver.get("https://www.roblox.com/CreateAccount")
    
    # Elements
    username_loc = By.ID, "signup-username"
    password_loc = By.ID, "signup-password"
    sign_up_loc = By.ID, "signup-button"

    month_dropdown_loc = By.ID, "MonthDropdown"
    birth_dropdown_loc = By.ID, "DayDropdown"
    year_dropdown_loc = By.ID, "YearDropdown"

    month_dropdown_value = By.XPATH, f'//*[@id="MonthDropdown"]/option[3]'
    birth_dropdown_value = By.XPATH, f'//*[@id="DayDropdown"]/option[{random.randint(3, 30)}]'
    year_dropdown_value = By.XPATH, f'//*[@id="YearDropdown"]/option[{random.randint(18, 30)}]'

    # Locate it using driver 
    month_dropdown = driver.ele(month_dropdown_loc)
    birth_dropdown = driver.ele(birth_dropdown_loc)
    year_dropdown = driver.ele(year_dropdown_loc)
    username = driver.ele(username_loc)
    password = driver.ele(password_loc)
    sign_up = driver.ele(sign_up_loc)

    month_value = driver.ele(month_dropdown_value)
    birth_value = driver.ele(birth_dropdown_value)
    year_value = driver.ele(year_dropdown_value)

    # Fill fields 
    month_dropdown.click()
    month_value.click()

    time.sleep(random.randint(3, 4))
    birth_dropdown.click()
    birth_value.click()

    time.sleep(random.randint(3, 4))
    year_dropdown.click()
    year_value.click()

    time.sleep(random.randint(3, 4))
    driver.actions.click(username).input(generate_unique_username(8))
    
    time.sleep(random.randint(3, 4))
    driver.actions.click(password).input(fake.password(8))

    time.sleep(random.randint(3, 4))
    sign_up.click()

    captcha_ele = By.XPATH, '//*[@id="rbx-body"]/div[9]/div[2]/div'
    
    if driver.ele(captcha_ele):
        info_message.configure(text="Captcha detected.. Solving..")
        while driver.ele(captcha_ele):
            time.sleep(1)
        
        logging.info("Captcha detected and solved successfully")
        info_message.configure(text="Captcha solved!")
    else:
        logging.info("No captcha detected")
        print("No captcha found")

    time.sleep(2)
    unique_username = generate_unique_username(5)

    with open(os.getcwd() + f'/accounts/{unique_username}.json', 'w') as file:
        cookies = driver.get_cookies()
        json.dump(cookies, file)

    print("Account was created and saved!")

    time.sleep(0.5)

    driver.close()

    return cookies

def generate_unique_username(len):
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(len))
    return username
