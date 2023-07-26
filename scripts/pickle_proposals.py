from app.proposal import Proposal
from bs4 import BeautifulSoup
from app.ideascale import get_proposal_html, signin
from scripts.allocated_proposals import load_allocated_proposal_urls
import pickle


def pickle_proposals(proposals: list[Proposal], file_path: str, append_to_the_end: bool = False):
    if append_to_the_end is True:
        older_proposals = load_pickled_proposals()
        proposals = older_proposals + proposals

    with open(file_path, "ab") as file:
        pickle.dump(proposals, file, protocol=pickle.HIGHEST_PROTOCOL)


def load_pickled_proposals():
    with open("proposals/allocated_proposals.pickle", 'rb') as file:
        proposals = pickle.load(file)
    return proposals


if __name__ == "__main__":

    driver = signin()
    # allocated_proposal_urls = load_allocated_proposal_urls()
    #
    # proposals, errors = [], []
    # for url in allocated_proposal_urls:
    #     try:
    #         html = get_proposal_html(driver, proposal_url=url)
    #         proposals.append(Proposal(html))
    #     except Exception as e:
    #         errors.append(url)

    errors = ['https://cardano.ideascale.com/a/dtd/105123-163', 'https://cardano.ideascale.com/a/dtd/106594-163', 'https://cardano.ideascale.com/a/dtd/106891-163', 'https://cardano.ideascale.com/a/dtd/106302-163', 'https://cardano.ideascale.com/a/dtd/100821-163', 'https://cardano.ideascale.com/a/dtd/100134-163', 'https://cardano.ideascale.com/a/dtd/103671-163', 'https://cardano.ideascale.com/a/dtd/105901-163', 'https://cardano.ideascale.com/a/dtd/102358-163', 'https://cardano.ideascale.com/a/dtd/104677-163', 'https://cardano.ideascale.com/a/dtd/101190-163', 'https://cardano.ideascale.com/a/dtd/104920-163', 'https://cardano.ideascale.com/a/dtd/107409-163', 'https://cardano.ideascale.com/a/dtd/100669-163', 'https://cardano.ideascale.com/a/dtd/102846-163', 'https://cardano.ideascale.com/a/dtd/105214-163', 'https://cardano.ideascale.com/a/dtd/106563-163', 'https://cardano.ideascale.com/a/dtd/107116-163', 'https://cardano.ideascale.com/a/dtd/105731-163', 'https://cardano.ideascale.com/a/dtd/107570-163', 'https://cardano.ideascale.com/a/dtd/106824-163', 'https://cardano.ideascale.com/a/dtd/100117-163', 'https://cardano.ideascale.com/a/dtd/106212-163', 'https://cardano.ideascale.com/a/dtd/106457-163']
    file_path = "proposals/allocated_proposals.pickle"

    proposals = []
    for url in errors[]:
        html = get_proposal_html(driver, url)
        proposal = Proposal(html)
        proposals.append(proposal)

    pickle_proposals(proposals, file_path, append_to_the_end=True)
    # driver.quit()

