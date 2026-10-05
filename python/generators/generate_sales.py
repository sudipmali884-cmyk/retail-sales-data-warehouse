import random, pandas as pd
from faker import  Faker


fake=Faker("en_IN")

random.seed(100)
Faker.seed(100)

# read customers
customers_df=pd.read_csv("../../csv/customers.csv")
customer_mapping= customers_df[["customer_id"]]

customers=customer_mapping.values.tolist()

# read stores

store_df=pd.read_csv("../../csv/stores.csv")
store_mapping = store_df[["store_id"]]

stores=store_mapping.values.tolist()

# Read Employees
# --------------------------------------------------

employee_df = pd.read_csv("../../csv/employees.csv")

employee_mapping = employee_df[
    [
        "employee_id",
        "store_id"
    ]
]

employees = employee_mapping.values.tolist()

# --------------------------------------------------
# Employee Mapping By Store
# --------------------------------------------------

employee_store_mapping = {}

for employee_id, store_id in employees:

    if store_id not in employee_store_mapping:

        employee_store_mapping[store_id] = []

    employee_store_mapping[store_id].append(employee_id)

# --------------------------------------------------
# Read Products
# --------------------------------------------------

product_df = pd.read_csv("../../csv/products.csv")

product_mapping = product_df[
    [
        "product_id",
        "unit_price",
        "cost_price"
    ]
]
products=product_mapping.values.tolist()

# --------------------------------------------------
# Read Promotions
# --------------------------------------------------

promotion_df = pd.read_csv("../../csv/promotions.csv")

promotion_mapping = promotion_df[
    [
        "product_id",
        "discount_percentage"
    ]
]

promotion_dict = dict(
    promotion_mapping.values
)

# discount = promotion_dict.get(
#
#     product_id,
#
#     0
#
# )
# product_id, unit_price, cost_price = random.choice(products)
#
# discount = promotion_dict.get(
#     product_id,
#     0
# )


# TOTAL SALES

TOTAL_SALES= 600000

from utils.mappings import (
PAYMENT_METHODS,SALES_STATUS
)

# SALES ID

def generate_sale_id(number):
    return f"SALE{number:08d}"

rows= []
for i in range(1,TOTAL_SALES + 1):
    sale_id = generate_sale_id(i)
    customer_id = random.choice(customers)[0]
    store_id = random.choice(stores)[0]
    employee_id = random.choice(employee_store_mapping[store_id])
    product_id , unit_price,cost_price = random.choice(
        products
    )
    quantity=random.randint(1,10)
    discount_percentage = promotion_dict.get(product_id,0)
    gross_amount = quantity * unit_price
    discount_amount= round(
        gross_amount * discount_percentage/100,2
    )
    taxable_amount = gross_amount - discount_amount

    tax_amount = round(
        taxable_amount * 0.18,
        2
    )

    total_amount = round(
        taxable_amount + tax_amount,
        2
    )

    profit = round(
        (unit_price - cost_price) * quantity,
        2
    )

    payment_method = random.choices(

        PAYMENT_METHODS,

        weights=[10, 40, 20, 20, 10],

        k=1

    )[0]

    sales_status = random.choices(

        SALES_STATUS,

        weights=[95, 3, 2],

        k=1

    )[0]

    sale_date = fake.date_between(

        start_date="-5y",

        end_date="today"

    )

    created_at = sale_date

    updated_at = fake.date_between(

        start_date=created_at,

        end_date="today"

    )

    rows.append({

        "sale_id": sale_id,

        "customer_id": customer_id,

        "store_id": store_id,

        "employee_id": employee_id,

        "product_id": product_id,

        "quantity": quantity,

        "unit_price": unit_price,

        "cost_price": cost_price,

        "gross_amount": gross_amount,

        "discount_percentage": discount_percentage,

        "discount_amount": discount_amount,

        "tax_amount": tax_amount,

        "total_amount": total_amount,

        "profit": profit,

        "payment_method": payment_method,

        "sales_status": sales_status,

        "sale_date": sale_date,

        "created_at": created_at,

        "updated_at": updated_at

    })

    # create dataframe

sales_df=pd.DataFrame(rows)



# duplicate rows
duplicate_rows = sales_df.sample(1000,random_state=100)

sales_df=pd.concat([sales_df,duplicate_rows],ignore_index=True)

# ==========================================================
# Duplicate Sale IDs
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

for r in rows:

    sales_df.loc[r, "sale_id"] = "SALE00000001"

#invalid customer ids

rows= random.sample(
    range(len(sales_df)),100
)

for r in rows:
    sales_df.loc[r,"customer_id"]="CUST7777777"

# invalid employee ids

rows=random.sample(range(len(sales_df)),100)
for r in rows:
    sales_df.loc[r,"employee_id"]="EMP90909090"

# Invalid Product IDs
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

for r in rows:

    sales_df.loc[r, "product_id"] = "PROD999999"

#  missing customer ids
rows=random.sample(range(len(sales_df)),200)
for r in rows:
    sales_df.loc[r,"customer_id"]=None


#  missing product id

rows=random.sample(range(len(sales_df)),200)
for r in rows:
    sales_df.loc[r,"product_id"]= None

# # ==========================================================
# # Negative Quantity
# # ==========================================================
#
# rows = random.sample(
#     range(len(sales_df)),
#     100
# )
#
# for r in rows:
#
#     sales_df.loc[r, "quantity"] = -5

# ==========================================================
# Negative Unit Price
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

for r in rows:

    sales_df.loc[r, "unit_price"] = -250

# ==========================================================
# Negative Cost Price
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

for r in rows:

    sales_df.loc[r, "cost_price"] = -150

# ==========================================================
# Selling Price Less Than Cost Price
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

# for r in rows:
#
#     sales_df.loc[r, "cost_price"] = 800
#
#     sales_df.loc[r, "unit_price"] = 500
#
# # =========================================================

# ==========================================================
# Extra Spaces
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
)

for r in rows:

    sales_df.loc[r, "payment_method"] = (

        "   "

        + str(sales_df.loc[r, "payment_method"])

        + "   "

    )

# ==========================================================
# Mixed Case
# ==========================================================

rows = random.sample(
    range(len(sales_df)),
    100
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

        sales_df.loc[r, "payment_method"] = str(
            sales_df.loc[r, "payment_method"]
        ).upper()

    elif style == "lower":

        sales_df.loc[r, "payment_method"] = str(
            sales_df.loc[r, "payment_method"]
        ).lower()

    elif style == "title":

        sales_df.loc[r, "payment_method"] = str(
            sales_df.loc[r, "payment_method"]
        ).title()

    else:

        sales_df.loc[r, "payment_method"] = " ".join(

            word.upper() if random.random() > 0.5 else word.lower()

            for word in str(
                sales_df.loc[r, "payment_method"]
            ).split()

        )

sales_df.to_csv("../../csv/sales.csv", index=False)
print("=*"*15)
print("Records Generated Successfully")
print(f"Total Records : {len(sales_df)}")
print(f"Duplicate rows: {len(duplicate_rows)}")
print("=*"*15)