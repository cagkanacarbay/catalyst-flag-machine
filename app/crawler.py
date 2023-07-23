import requests
from bs4 import BeautifulSoup

# Your login details
payload = {
    'emailAddress': 'chakhan.lk9@gmail.com',  # replace with your email
    'password': 'qxJhA5^buR'  # replace with your password
}

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()
#
# # Go to the website login page
# driver.get("https://cardano.ideascale.com/a/community/login")
#
# # Find the email and password fields and enter your login details
# driver.find_element_by_name('emailAddress').send_keys(payload["emailAddress"])
# driver.find_element_by_name('password').send_keys(payload['password'])
#
# # Find the login button and click it
# driver.find_element_by_name('login-button').click()
#
# # Wait for the next page to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'next-page-element-id')))
#
# # Print the page source
# print(driver.page_source)
#
# # Close the driver
# driver.quit()

def get_proposal_links_from_challenge_page(driver):

    # Find all the links in the 'idea-list' div and visit each one
    idea_list = driver.find_element(By.CLASS_NAME, 'idea-list')
    links = idea_list.find_elements(By.CLASS_NAME, 'classic-link')
    urls = []

    for link in links:
        urls.append(link.get_attribute('href'))

    return urls


def scroll_to_the_bottom(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return driver

# def go_to_proposal_and
#     for link in links:
#         url = link.get_attribute('href')
#         driver.get(url)
#         # Wait for the page to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
#         print(driver.page_source)  # print the page source or do whatever you need with it
#         # Go back to the idea list
#         driver.back()


challenge_pages = ["https://cardano.ideascale.com/c/campaigns/346/stage/stage-finalize9bfa8a/ideas/unspecified"]
driver = webdriver.Firefox()

challenges = {
    "F10: Development & Infrastructure": "https://cardano.ideascale.com/c/campaigns/346/stage/stage-finalize9bfa8a/ideas/unspecified",
    "F10: Products & Integrations": "https://cardano.ideascale.com/c/campaigns/348/stage/stage-finalizef899ed/ideas/unspecified",
    "F10: OSDE: Open Source Dev Ecosystem": "https://cardano.ideascale.com/c/campaigns/349/stage/stage-finalize02260c/ideas/unspecified",
    "F10: DAOs ❤ Cardano": "https://cardano.ideascale.com/c/campaigns/352/about",
    "F10: Developer Ecosystem - The Evolution": "https://cardano.ideascale.com/c/campaigns/351/stage/stage-finalize667cb9/ideas/unspecified",
    "
}

for page in challenge_pages:

    # Go to the website login page
    driver.get(page)

    driver = scroll_to_the_bottom(driver)

    # Find the login button and click it
    # driver.find_element_by_name('login-button').click()

    # Wait for the next page to load
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'next-page-element-id')))

    # Print the page source
    # print(driver.page_source)

    urls = get_proposal_links_from_challenge_page(driver)

    print(urls)
    # Close the driver
    # driver.quit()