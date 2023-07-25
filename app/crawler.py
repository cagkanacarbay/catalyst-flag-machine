from selenium import webdriver

from app.ideascale import signin
from settings import constants

#
#
# if __name__ == "__main__":
#
#     driver = webdriver.Firefox()
#     signin(driver, constants['CARDANO_IDEASCALE_EMAIL'], constants["CARDANO_IDEASCALE_PASSWORD"])
#
#     allocated_proposal_urls = get_allocated_proposal_urls_for_profile(driver, "https://cardano.ideascale.com/c/profile/168852/activity")