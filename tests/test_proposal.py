import pytest
from app.ideascale import signin, get_proposal_html
import json

@pytest.fixture
def driver():
    driver = signin()
    return driver

@pytest.fixture
def allocated_proposal_urls():
    with open("proposals/allocated_proposals_chakhan.json", 'r') as file:
        urls = json.load(file)
    return urls

def test_proposal_page_loads(driver, urls):
    get_proposal_html(driver, proposal_url=urls[1])

    assert