from bs4 import BeautifulSoup
from app.ideascale import get_proposal_html, signin
from scripts.allocated_proposals import load_allocated_proposal_urls


def extract_answer(soup: BeautifulSoup, question: str, answer_type: type = str):

    question_tag = soup.find("dt", string=question)
    answer_tag = question_tag.find_next_sibling("dd")

    # remove this from the text "Answer:
    answer = answer_tag.get_text(strip=True).split(":")[1]
    if answer_type == str:
        return answer
    elif answer_type == int:
        return int(answer)
    elif answer_type == bool:
        return True if answer == 'Yes' else False

def extract_relevant_links(soup):
    question = "[GENERAL] Website/ GitHub repository, or any other relevant link"
    links_html = soup.find("dt", string=question).find_next_sibling("dd")
    links = [link.get('href') for link in links_html.find_all('a')]
    return links


# title = soup.find('h1').text
# challenge = soup.find('p', class_='idea-campaign').a.text
# problem_statement_div = soup.find('div', class_='ql-editor ql-render').get_text(strip=True)
#
# proposers = soup.find("dt", string="[GENERAL] Name and surname of main applicant").find_next_sibling("dd").get_text(strip=True).split(':')[1]
# additional_applicants = soup.find("dt", string="Additional applicants").find_next_sibling("dd").get_text(strip=True).split(':')[1]
#
# if additional_applicants.lower() != "none":
#     proposers += [app.strip() for app in additional_applicants.split(",")]
#
# requested_funds = extract_answer(soup, question="[GENERAL] Requested funds in ada", answer_type=int)
# project_duration = extract_answer(
#     soup, answer_type=int,
#     question="[GENERAL] Please specify how many months you expect your project to last  (from 2-12 months)"
# )
# solution_statement = extract_answer(
#     soup, question="[GENERAL] Summarize your solution to the problem (200-character limit including spaces)"
# )
#
# links = extract_relevant_links(soup)
#
# is_opensource = extract_answer(soup, question="[GENERAL] Will your project’s output/s be fully open source?",
#                                answer_type=bool)
#
# category = extract_answer(soup, question="[METADATA] Category of proposal")


def extract_long_answer(soup: BeautifulSoup, question: str):
    question_tag = soup.find("dt", string=question)
    answer_tag = question_tag.find_next_sibling("dd")
    return ' '.join(answer_tag.stripped_strings)


impact_questions = [
    "[IMPACT] Please describe your proposed solution.",
    "[IMPACT] How does your proposed solution address the challenge and what benefits will this bring to the Cardano ecosystem?",
    "[IMPACT] How do you intend to measure the success of your project?",
    "[IMPACT] Please describe your plans to share the outputs and results of your project?"
]

capability_feasibility_questions = [
    "[CAPABILITY/ FEASIBILITY] What is your capability to deliver your project with high levels of trust and accountability?",
    "[CAPABILITY/ FEASIBILITY] What are the main goals for the project and how will you validate if your approach is feasible?",
    "[CAPABILITY/ FEASIBILITY] Please provide a detailed breakdown of your project’s milestones and each of the main tasks or activities to reach the milestone plus the expected timeline for the delivery.",
    "[CAPABILITY/ FEASIBILITY] Please describe the deliverables, outputs and intended outcomes of each milestone."
]

resources_value_questions = [
    "[RESOURCES & VALUE FOR MONEY] Please provide a detailed budget breakdown of the proposed work and resources.",
    "[RESOURCES & VALUE FOR MONEY] Who is in the project team and what are their roles?",
    "[RESOURCES & VALUE FOR MONEY] How does the cost of the project represent value for money for the Cardano ecosystem?"
]


impact_answers = {}
capability_feasibility_answers = {}
resources_value_answers = {}

# Extract answers for each question
for question in impact_questions:
    impact_answers[question] = extract_long_answer(soup, question)

for question in capability_feasibility_questions:
    capability_feasibility_answers[question] = extract_long_answer(soup, question)

for question in resources_value_questions:
    resources_value_answers[question] = extract_long_answer(soup, question)


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
        self.additional_proposers = self.extract_additional_proposers(soup)

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

        self.capability = {

        }


    def __repr__(self):
        return f"{self.challenge} - {self.title} - {self.requested_funds} ADA"

    @staticmethod
    def extract_additional_proposers(soup):
        additional_proposers = extract_answer(soup, question="Additional applicants")

        if additional_proposers.lower() != "none":
            return [app.strip() for app in additional_proposers]





if __name__ == "__main__":
    driver = signin()
    allocated_proposal_urls = load_allocated_proposal_urls()
    html = get_proposal_html(driver, proposal_url=allocated_proposal_urls[3])

    proposal = Proposal(html)
    print(proposal)


