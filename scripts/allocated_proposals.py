from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import constants
from app.ideascale import signin
import json


def get_allocated_proposal_urls_for_profile(driver: webdriver, profile_url: str):

    driver.get(profile_url)
    time.sleep(3)  # let the page load
    allocations = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/aside/div/div/section[3]/div/article/div/div[1]/ul/li[4]/div/div')
    links = allocations.find_elements(By.TAG_NAME, 'a')
    urls = [link.get_attribute('href') for link in links]

    return urls


if __name__ == "__main__":

    driver = signin(constants['CARDANO_IDEASCALE_EMAIL'], constants["CARDANO_IDEASCALE_PASSWORD"])

    allocated_proposal_urls = get_allocated_proposal_urls_for_profile(driver, "https://cardano.ideascale.com/c/profile/168852/activity")

    with open("allocated_proposals_chakhan.json", "w") as file:
        file.write(json.dumps(allocated_proposal_urls))


def load_allocated_proposal_urls():
    with open("proposals/allocated_proposals_chakhan.json", 'r') as file:
        urls = json.load(file)
    return urls
