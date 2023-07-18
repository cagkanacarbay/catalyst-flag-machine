from dataclasses import dataclass
from app.pdf_utils import read_pdf, clean_proposal_text
import pprint


@dataclass
class Proposal:
    title: str
    solution: str
    problem: str
    proposers: list[str]
    requested_funds: int
    challenge: str
    project_length_in_months: int
    problem_perception: str
    approach_reason: str
    project_engagement: str
    impact_proof: str
    challenge_address: str
    success_metrics: str
    output_sharing: str
    previous_funding: str
    project_goals: str
    feasibility_validation: str
    timeline_milestones: str
    deliverables: str
    budget: str
    team_members: str
    value_for_money: str
    agreement_acceptance: str
    main_proposer: str
    additional_proposers: str
    open_source: str

    @classmethod
    def instantiate_from_text(cls, text: str):

        lines = text.split("\n")

        proposal = {
            "challenge": lines[0].split("Campaign: ")[1].split("Project")[0],
            "idea": lines[4].split(': ')[1],

        }



        answers = text.split("Answer:\n")[1:]
        values = [answer.strip().split('\n')[0] for answer in answers]


        print(1)
        # return cls(*values)
        return cls(*values)


def replace_newlines_with_spaces(text: str):
    return text.replace("\n", " ")

def extract_problem_statement(full_proposal_text: str):
    return full_proposal_text.split("Idea Details: Notes:")[1].split("Custom")[0]

def extract_solution_and_links(proposal_answers: [str]):
    cleaned = replace_newlines_with_spaces(proposal_answers[3])
    split_text = cleaned.split("Link")
    return {
        "solution": split_text[0],
        "links": split_text[1:]
    }


# def read_proposal_pdf(file_path: str):

file_path = r"D:\Projects\flag-machine\proposals\Ideas-2023-07-18-06-35-55.pdf"
text = read_pdf(file_path)

def extract_header_info(proposal_text: str):
    proposal_text = text
    lines = proposal_text.split("\n")[:5]

    return {
        "challenge": lines[0].split("Campaign: ")[1].split("Project")[0],
        "idea": lines[4].split(': ')[1],
        "main_applicant": lines[2].split(": ")[1],
        "date_of_submission": lines[3].split(": ")[1],
    }




# x = Proposal.instantiate_from_text(pdf)

proposal = extract_header_info(text)


proposal_text, lines = clean_proposal_text(text)


answers = proposal_text.split("Answer:\n")[1:]
#
answers = [answer.replace("\n", " ") for answer in answers]

proposal = {
    **proposal,
    "requested_funds": int(answers[1]),
    "timeline": int(answers[2]),
    "problem": extract_problem_statement(answers[3])

    # ""
}

# proposal = {**proposal, **extract_solution_and_links(answers)}

pprint.pprint(proposal)





