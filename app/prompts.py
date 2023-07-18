


def analyze_proposal_prompt_v1(proposal_text):

    prompt = """
        I will paste below a proposal to apply for a grant.
        I want you analyze this proposal with a critical eye as an area expert, who is looking to make a suggestion 
        to investors whether or not to invest in this project.        
        Be careful, some of the proposals are outright scams. We want to catch those.
        Analyze the proposal and give me deep insights as to the feasibility, and trustworthiness of the proposal. 
    """ + "\n Proposal: " + proposal_text

    return prompt