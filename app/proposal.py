from bs4 import BeautifulSoup
from app.ideascale import get_proposal_html, signin
from scripts.allocated_proposals import load_allocated_proposal_urls


def extract_answer(soup: BeautifulSoup, question: str, answer_type: type = str):

    question_tag = soup.find("dt", string=question)

    if question_tag is None:
        return None

    answer_tag = question_tag.find_next_sibling("dd")

    answer = answer_tag.get_text(strip=True).split(":")[1]  # remove "Answer:" from the text
    if answer_type == str:
        return answer
    elif answer_type == int:
        return int(answer)
    elif answer_type == bool:
        return True if answer == 'Yes' else False


def extract_relevant_links(soup):
    question = "[GENERAL] Website/ GitHub repository, or any other relevant link"
    links_html = soup.find("dt", string=question)

    if links_html is not None:
        links_html = links_html.find_next_sibling("dd")
        links = [link.get('href') for link in links_html.find_all('a')]
        return links
    else:
        return None


def extract_long_answer(soup: BeautifulSoup, question: str):
    question_tag = soup.find("dt", string=question)
    answer_tag = question_tag.find_next_sibling("dd")
    return ' '.join(answer_tag.stripped_strings)


def extract_additional_proposers(soup):
    additional_proposers = extract_answer(soup, question="Additional applicants")

    if additional_proposers.lower() != "none":
        return [app.strip() for app in additional_proposers]


class Proposal:
    def __init__(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # GENERAL
        self.title = soup.find('h1').text
        self.challenge = soup.find('p', class_='idea-campaign').a.text
        self.problem_statement = soup.find('div', class_='ql-editor ql-render').get_text(strip=True)
        self.solution_statement = extract_answer(
            soup, question="[GENERAL] Summarize your solution to the problem (200-character limit including spaces)"
        )

        self.main_proposer = extract_answer(soup, "[GENERAL] Name and surname of main applicant")
        self.additional_proposers = extract_additional_proposers(soup)

        self.requested_funds = extract_answer(soup, question="[GENERAL] Requested funds in ada", answer_type=int)
        self.project_duration = extract_answer(
            soup, answer_type=int,
            question="[GENERAL] Please specify how many months you expect your project to last  (from 2-12 months)"
        )

        self.links = extract_relevant_links(soup)
        self.is_opensource = extract_answer(
            soup, answer_type=bool, question="[GENERAL] Will your project’s output/s be fully open source?"
        )
        self.category = extract_answer(soup, question="[METADATA] Category of proposal")

        self.impact = {
            "proposed_solution": extract_long_answer(
                soup, question="[IMPACT] Please describe your proposed solution."
            ),
            "challenge_and_cardano_benefits": extract_long_answer(
                soup, question="[IMPACT] How does your proposed solution address the challenge "
                               "and what benefits will this bring to the Cardano ecosystem?",
            ),
            "measuring_success": extract_long_answer(
                soup, question="[IMPACT] How do you intend to measure the success of your project?",
            ),
            "output_plans": extract_long_answer(
                soup, question="[IMPACT] Please describe your plans to share the outputs and results of your project?"
            )
        }

        self.capability_feasibility = {
            "capability_to_deliver": extract_long_answer(
                soup, question="[CAPABILITY/ FEASIBILITY] What is your capability to deliver your project "
                               "with high levels of trust and accountability?"
            ),
            "main_goals_and_feasibility": extract_long_answer(
                soup, question="[CAPABILITY/ FEASIBILITY] What are the main goals for the project and "
                               "how will you validate if your approach is feasible?"
            ),
            "detailed_breakdown": extract_long_answer(
                soup, question="[CAPABILITY/ FEASIBILITY] Please provide a detailed breakdown of your "
                               "project’s milestones and each of the main tasks or activities to reach the milestone "
                               "plus the expected timeline for the delivery."
            ),
            "milestone_deliverables": extract_long_answer(
                soup, question="[CAPABILITY/ FEASIBILITY] Please describe the deliverables, outputs and "
                               "intended outcomes of each milestone."
            )
        }

        self.resources_value_for_money = {
            "budget_breakdown": extract_long_answer(
                soup,
                question="[RESOURCES & VALUE FOR MONEY] Please provide a detailed budget breakdown "
                         "of the proposed work and resources."
            ),
            "project_team": extract_long_answer(
                soup, question="[RESOURCES & VALUE FOR MONEY] Who is in the project team and what are their roles?"
            ),
            "value_for_money": extract_long_answer(
                soup,
                question="[RESOURCES & VALUE FOR MONEY] How does the cost of the project represent "
                         "value for money for the Cardano ecosystem?"
            )
        }

    def __repr__(self):
        return f"{self.challenge} - {self.title} - {self.requested_funds} ADA"


if __name__ == "__main__":
    driver = signin()
    allocated_proposal_urls = load_allocated_proposal_urls()
    html = get_proposal_html(driver, proposal_url=allocated_proposal_urls[3])

    proposal = Proposal(html)
    print(proposal)


