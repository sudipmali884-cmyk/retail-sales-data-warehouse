import random

import numpy as np
import pandas as pd
from faker import Faker


#  step 2 - fake configuration
fake= Faker("en_IN")
random.seed(100)
np.random.seed(100)
Faker.seed(100)
# This ensures you get the same dataset every time, which makes debugging much easier.

# Step 3 - total data

TOTAL_CUSTOMERS= 300000

# STEP 4- CUSTOMER ID GENERATOR

def generate_customer_id(number):
    return f"CUST{number:06d}"

CUSTOMER_STATUS=[
    "Active","Inactive"
]
# LOYALTY_TIERS = [
#     "Silver",
#     "Gold",
#     "Platinum"
# ]

GENDERS=[
    "Male","Female"
]

from utils.mappings import (
    STATE_CITY_MAPPING
)



CITY_STATE = []
for state, cities in STATE_CITY_MAPPING.items():
    for city in cities:
        CITY_STATE.append((city,state))
# During generation
#
# Just write:
# city, state = random.choice(CITY_STATE)

rows= []
for i in range (1, TOTAL_CUSTOMERS + 1):
    customer_id = generate_customer_id(i)
    gender=random.choice(GENDERS)

    if gender == "Male":
        first_name = fake.first_name_male()
    else:
        first_name= fake.first_name_female()

    last_name = fake.last_name()
    # patient_name = fake.name_male() if gender == "Male" else fake.name_female()
    full_name= f"{first_name} {last_name}"
    dob=fake.date_of_birth(
        minimum_age= 18, maximum_age= 80
    )
    registration_date= fake.date_between(
        start_date= dob,
        end_date="today"
    )
    created_at= registration_date
    updated_at=fake.date_between(
        start_date=created_at,
        end_date= "today"
    )
    phone=str(random.randint(6666666666,9999999999)) #or phone = fake.msisdn()[-10:]
    email=(
        first_name+last_name+"@gmail.com"
    ).lower()

    state=random.choice(list(STATE_CITY_MAPPING.keys()))
    city=random.choice(STATE_CITY_MAPPING[state])
    postal_code = fake.postcode()
    status=random.choices(CUSTOMER_STATUS,weights=[75,25])[0]
    rows.append({
        "customer_id": customer_id,

        "first_name": first_name,

        "last_name": last_name,

        # "full_name": full_name,

        "gender": gender,

        "date_of_birth": dob,

        "phone_number": phone,

        "email": email,

        "city": city,

        "state": state,

        "postal_code": postal_code,

        "registration_date": registration_date,

        "customer_status": status,
        #
        # "loyalty_tier": loyalty,

        "created_at": created_at,

        "updated_at": updated_at
    })

# create dataframe
customer_df=pd.DataFrame(rows)

#  duplicate rows
duplicate_rows = customer_df.sample(500,random_state=100)
customer_df=pd.concat([customer_df,duplicate_rows],ignore_index=True)

# missing values
rows= random.sample(range(len(customer_df)),1000)
for r in rows:
    customer_df.loc[r,"email"]=None


# blank string
rows = random.sample(range(len(customer_df)),500)
for r in rows:
    customer_df.loc[r,"city"]=""

# bad phone
bad_phone = [
    "123456",
   "abcde",
    "99999999999999",
    "",
    "0000000000"
]
rows = random.sample(range(len(customer_df)),250)
for r in rows:
    customer_df.loc[r,"phone_number"] = random.choice(bad_phone)

# Extra spaces

rows=random.sample(range(len(customer_df)),300)
for r in rows:
    customer_df.loc[r,"first_name"]=( "  "+ customer_df.loc[r,"first_name"]+"  "

    )


# wrong postal_code

bad_postal = [
    "ABCDE","123","", None,"XYZ123"
]
rows = random.sample(range(len(customer_df)),500)
for r in rows:
    customer_df.loc[r,"postal_code"]= random.choice(bad_postal)

    # create dataframe
    customer_df = pd.DataFrame(rows)

#  save csv
customer_df.to_csv("../../csv/customers.csv", index=False)

print("Customers Generated Successfully")
print(f"Total Customers : {len(customer_df)}")
print(f"total duplicate rows : {len(duplicate_rows)}")

print("Duplicate Rows:", customer_df.duplicated().sum())
# print(customer_df[
#     customer_df["phone_number"].isin([
#         "123456",
#         "abcde",
#         "99999999999999",
#         "",
#         "0000000000"
#     ])
# ])

print("Blank cities:", (customer_df["city"] == "").sum())

print("NULL emails:", customer_df["email"].isna().sum())
#
# print("Extra spaces:",
#       (customer_df["first_name"] != customer_df["first_name"].str.strip()).sum())
print(customer_df[customer_df["first_name"].str.startswith("  ", na=False)].head())
print("Bad phones:")
print(customer_df["phone_number"].isin([
    "123456",
    "abcde",
    "99999999999999",
    "",
    "0000000000"
]).sum())
