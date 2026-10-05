import random
def generate_store_id(number: int) -> str:
    return f"STR{number:06d}"

def random_state(mapping):
    return random.choice(list(mapping.keys()))

def random_city(state,mapping):
    return random.choice(mapping[state])

def company_email(city,company):
    city=city.lower().replace(" ","")
    company=company.lower().replace(" ", "")
    number = random.randint(1,999)

    return f"{city}{number}@{company}.com"
def company_phone():

    return "9" + "".join(
        random.choices("0123456789", k=9)
    )

def store_name(company, city):

    suffixes = [

        "Central",
        "Market",
        "Mall",
        "Express",
        "Premium",
        "Plaza",
        "Bazaar",
        "Retail Park",
        "Mega Store",
        "Shopping Centre"

    ]

    return f"{company} {city} {random.choice(suffixes)}"