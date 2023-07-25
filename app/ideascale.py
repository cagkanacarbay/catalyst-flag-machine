import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import TimeoutException
from settings import constants


def signin():

    driver = webdriver.Firefox()

    driver.get("https://cardano.ideascale.com/a/community/login")

    driver.find_element(By.CLASS_NAME, 'btn-primary').click()  # accept cookies
    time.sleep(1)

    # enter username and password
    driver.find_element("name", 'emailAddress').send_keys(constants['CARDANO_IDEASCALE_EMAIL'])
    driver.find_element("name", 'password').send_keys(constants["CARDANO_IDEASCALE_PASSWORD"])

    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn-captcha').click()  # login

    time.sleep(5)

    return driver


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


def get_proposal_html(driver: webdriver, proposal_url: str):
    driver.get(proposal_url)
    try:
        WebDriverWait(driver, 10).until(
            ExpectedConditions.presence_of_element_located((By.CLASS_NAME, 'idea-meta'))
        )
        time.sleep(2)
    except TimeoutException:
        print("page timed out i dunno what to do")

    proposal = driver.find_element(By.CLASS_NAME, 'idea-details')
    proposal_html = proposal.get_attribute('outerHTML')

    return proposal_html






