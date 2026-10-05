# import random
# from datetime import datetime, timedelta
#
# import pandas as pd
# from faker import Faker
# Faker.seed(100)
# random.seed(100)
# from utils.constants import (
#     TOTAL_STORES,
#     RANDOM_SEED,
#     FAKER_LOCALE,
#     COMPANY_NAMES,
#     STORE_TYPES,
#     STORE_STATUS
# )
#
# from utils.mappings import (
#     STATE_CITY_MAPPING,
#     STATE_REGION_MAPPING
# )
#
# from utils.helpers import (
#     generate_store_id,
#     random_state,
#     random_city,
#     company_email,
#     company_phone,
#     store_name
# )
#
# fake = Faker(FAKER_LOCALE)
#
# random.seed(RANDOM_SEED)
# Faker.seed(RANDOM_SEED)
#
#
#
# stores = []
#
# for i in range(1, TOTAL_STORES + 1):
#
#     state = random_state(STATE_CITY_MAPPING)
#
#     city = random_city(state, STATE_CITY_MAPPING)
#
#     company = random.choice(COMPANY_NAMES)
#
#     email = company_email(city, company)
#
#     region = STATE_REGION_MAPPING[state]
#
#     opening_date = fake.date_between(
#         start_date="-15y",
#         end_date="today"
#     )
#
#     created_at = fake.date_time_between(
#         start_date=opening_date,
#         end_date="now"
#     )
#
#     row = {
#
#         "store_id": generate_store_id(i),
#
#         "brand_name": company,
#         "store_name": store_name(
#             company,
#             city
#         ),
#
#
#
#         "store_type": random.choice(STORE_TYPES),
#
#         "city": city,
#
#         "state": state,
#
#         "region": region,
#
#         "phone": company_phone(),
#
#         "email": company_email(city,company),
#
#         "manager_name": fake.name(),
#
#         "opening_date": opening_date,
#
#         "status": random.choice(STORE_STATUS),
#
#         "created_at": created_at
#
#     }
#
#     stores.append(row)
# df=pd.DataFrame(stores)
# df.to_csv("../../csv/stores.csv",index=False)
# print("Stores Generated Successfully")
# print(f"TOTAL RECORDS : {len(df)}")


import random
import pandas as pd

from faker import Faker

from utils.helpers import generate_store_id

# faker configuration
fake=Faker("en_IN")

random.seed(100)
Faker.seed(100)

TOTAL_STORES= 500

STORE_TYPES=[
    "Supermarket",
    "Hypermarket",
    "Express",
    "Wholesale",
    "Bazaar",
    "Mart"
]

STORE_STATUS=[
    "Active","Closed","Renovation"
]


from utils.mappings import (
    STATE_CITY_MAPPING

)

from utils.constants import (
    COMPANY_NAMES
)

CITY_STATE = []
for state , cities in STATE_CITY_MAPPING.items():
    for city in cities:
        CITY_STATE.append((city,state))

# store id generator

rows= []

for i in range(1, TOTAL_STORES + 1):
    store_id = generate_store_id(i)

    city,state= random.choice(CITY_STATE)
    store_type=random.choice(STORE_TYPES)
    store_name=random.choice(COMPANY_NAMES)
    manager_name=fake.name()
    phone=str(random.randint(6666666666,9999999999))
    email=(city.replace(" ","").lower()+ "@retailmart.com")
    # area,postal_code=random.choice(ADDRESS_MAPPING[city])
    address=fake.street_address()
    postal_code=fake.postcode()
    opening_date=fake.date_between(
        start_date="-50y",
        end_date="-1y"
    )
    created_at=opening_date
    updated_at=fake.date_between(
        start_date=created_at,
        end_date="today"
    )
    status=random.choices(
        STORE_STATUS,
        weights=[90,5,5],
        k=1
    )[0]

    rows.append({
        "store_id": store_id,
        "store_name":store_name,
        "store_type":store_type,
        "manager_name": manager_name,
        "phone": phone,
        "email": email,
        "address": address,
        "city": city,
        "state": state,
        "postal_code": postal_code,
        "opening_date": opening_date,
        "status": status,
        "created_at": created_at,

        "updated_at": updated_at
    })

store_df=pd.DataFrame(rows)

# duplicate data
duplicate_rows = store_df.sample(
    10,random_state=100
)
store_df=pd.concat(
    [store_df,duplicate_rows],
    ignore_index=True
)


#  duplicate store ids
rows= random.sample(range(len(store_df)),10)
for r in rows:
    store_df.loc[r,"store_id"]="STR0001"

#  Missing emails
rows= random.sample(range(len(store_df)),5)
for r in rows:
    store_df.loc[r,"email"] = None

# Blank Address

rows= random.sample(
    range(len(store_df)),10
)
for r in rows:
    store_df.loc[r,"address"]= ""

# invalid email
bad_email = [
"abcgmail.com",

    "store@",

    "@gmail.com",

    "",

    None
]

rows = random.sample(
    range(len(store_df)),10)
for r in rows:
    store_df.loc[r,"email"]= random.choice(bad_email)

# extra spaces
rows=random.sample(range(len(store_df)),10)
for r in rows:
    store_df.loc[r,"store_name"]=(
        " "+ store_df.loc[r,"store_name"]
        +"  "
    )

#  save csv
store_df.to_csv("../../csv/stores.csv", index=False)

print("=*"*10)
print("Total Records: ",len(store_df))
print(f"Duplicate Records : {len(duplicate_rows)}")
print((store_df["address"] == "").sum())
print(store_df[store_df["address"] == ""])
print("=*"*10)