import random,pandas as pd
from faker import Faker

# faker configuration

fake= Faker("en_IN")

random.seed(100)
Faker.seed(100)

# total products

TOTAL_PRODUCTS = 2000

# PRODUCT ID GENERATOR
def generate_product_id(number):
    return f"PRO{number:06d}"

# product categories

from  utils.mappings import (
    CATEGORY_MAPPING,BRANDS,SUPPLIERS,PRODUCT_STATUS
)

product=[]

for i in range(1, TOTAL_PRODUCTS + 1):
    product_id = generate_product_id(i)

    category= random.choice(list(CATEGORY_MAPPING.keys()))
    sub_category= random.choice(CATEGORY_MAPPING[category])
    brand = random.choice(BRANDS)
    product_name= f"{brand} {sub_category}"
    supplier= random.choice(SUPPLIERS)
    cost_price=random.randint(20,1000)
    margin=random.randint(10,500)
    unit_price= cost_price + margin #selling price
    barcode= str(
        random.randint(
            100000000000,999999999999
        )
    )
    weight = round(random.uniform(0.10,10.00))
    launch_date = fake.date_between(
        start_date="-10y",
        end_date="today"
    )

    created_at=launch_date

    updated_at=fake.date_between(
        start_date=created_at,
        end_date="today"
    )
    status= random.choices(PRODUCT_STATUS,weights=[95,5],k=1)[0]

    product.append({
    "product_id": product_id,

        "product_name": product_name,

        "category": category,

        "sub_category": sub_category,

        "brand": brand,

        "supplier": supplier,

        "cost_price": cost_price,

        "margin":margin,

        "unit_price": unit_price,

        "barcode": barcode,

        "weight": weight,

        "launch_date": launch_date,

        "status": status,

        "created_at": created_at,

        "updated_at": updated_at
    })

    # create dataframe

product_df=pd.DataFrame(product)
print("Products Generated successfully")
print(f"Total Records : {len(product_df)}")

# duplicate rows

duplicate_rows = product_df.sample(
    100,random_state=100
)

product_df = pd.concat(
    [product_df,duplicate_rows], ignore_index=True
)

# missing product name

rows= random.sample(range(len(product_df)),100)

for r in rows:
    product_df.loc[r,"product_name"]= None

# blank category

rows=random.sample(range(len(product_df)), 50)
for r in rows:
    product_df.loc[r,"category"]= ""

# Invali Category
bad_category = [

    "Electronics",

    "Mobiles",

    "Furniture",

    "",

    None

]

rows = random.sample(
    range(len(product_df)),
    20
)

for r in rows:

    product_df.loc[r, "category"] = random.choice(
        bad_category
    )

# ==========================================================
# Invalid Brand
# ==========================================================

bad_brand = [

    "XYZ",

    "ABC",

    "123",

    "",

    None

]

rows = random.sample(
    range(len(product_df)),
    20
)

for r in rows:

    product_df.loc[r, "brand"] = random.choice(
        bad_brand
    )

# negative cost price

rows= random.sample(range(len(product_df)),50)
for r in rows:
    product_df.loc[r,"cost_price"]= -7777

# Future Launch Date
# ==========================================================

rows = random.sample(
    range(len(product_df)),
    20
)

for r in rows:

    product_df.loc[r, "launch_date"] = "2035-01-01"

# Mixed Case
# ==========================================================

rows = random.sample(
    range(len(product_df)),
    30
)

for r in rows:

    style = random.choice(
        [
            "upper",
            "lower",
            "title",
            "mixed"
        ]
    )

    if style == "upper":

        product_df.loc[r, "product_name"] = str(
            product_df.loc[r, "product_name"]
        ).upper()

    elif style == "lower":

        product_df.loc[r, "product_name"] = str(
            product_df.loc[r, "product_name"]
        ).lower()

    elif style == "title":

        product_df.loc[r, "product_name"] = str(
            product_df.loc[r, "product_name"]
        ).title()

    else:

        product_df.loc[r, "product_name"] = " ".join(

            word.upper() if random.random() > 0.5 else word.lower()

            for word in str(
                product_df.loc[r, "product_name"]
            ).split()

        )

# save cssv

product_df.to_csv("../../csv/products.csv",index=False)