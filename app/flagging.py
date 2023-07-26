from app.proposal import Proposal
from app.openai import ask_jesus

VENTURE_GPT = """"
        You are Venture Capitalist GPT, a seasoned startup investor who knows everything there is to know about 
        startup investing. 
        
        You will use your knowledge to read through entire proposals that ask for funding from the innovation fund of 
        the Cardano blockchain. The proposals must benefit Cardano. 
        
        The currency of Cardano is ADA, which you can take as 1/3rd of USD. eg. 100 ADA is 33 USD
        
        You will be critical and try to find flaws, inadequate thinking, and scams. Lots of people apply for funding to 
        just grab money from this fund, so your aim is to protect the fund and make sure the money goes to well thought 
        out, impactful and feasible proposals that deliver great value. 
        
        Your purpose is to help me flag bad proposals, and find great ones. 
        
        Don't answer with any pre-text or post-text. Just answer the questions, never say anything else.
    """


def problem_and_solution_analysis(proposal: Proposal):
    print(f"The problem the proposal addresses is {proposal.problem_statement}")

    proposal = proposals[1]
    problem_prompt = f"""
        We will start with a high level overview. Here's the proposal in a few words:
        
        Title: {proposal.title}
        Problem statement: {proposal.problem_statement}
        Solution statement: {proposal.solution_statement}
        Requested funds: {proposal.requested_funds} in ADA
    """




def budget_analysis(proposal: Proposal):
    print(f"Requested budget is {proposal.requested_funds}")

    budget_situation_prompt = """
        List all items in the proposal budget, how much each costs, along with any justification on the budget item. 
    """

    result = ask_jesus(prompt=budget_situation_prompt)





if __name__ == "__main__":
    from scripts.pickle_proposals import load_pickled_proposals

    proposals = load_pickled_proposals()
