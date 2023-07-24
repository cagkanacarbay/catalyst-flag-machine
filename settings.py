"""
This page is for environment variables,

DO NOT COMMIT THIS FILE TO GIT WHILE THERE ARE LIVE VALUES IN IT.

ONLY UPDATE WITH None values and update gitignore.

"""

constants = {
    "CARDANO_IDEASCALE_EMAIL": None,
    "CARDANO_IDEASCALE_PASSWORD": None,
    "OPENAI_APIKEY": None
}


for constant, value in constants.items():
    if value is None:
        raise ValueError(f"Must enter valid value for {constant}")

