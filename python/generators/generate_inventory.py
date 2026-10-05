import random
import pandas as pd
from faker import Faker



# faker configuration
fake=Faker("en_IN")
random.seed(100)
Faker.seed(100)

# Read Products
product_df=pd.read_csv("../../csv/products.csv")

product_mapping=product_df[["product_id","cost_price","unit_price"]]

products=product_mapping.values.tolist()

# Read stores

store_df = pd.read_csv("../../csv/stores.csv")

store_mapping = store_df[["store_id"]]

stores=store_mapping.values.tolist()

# Inventory Status

INVENTORY_STATUS = [

    "Available",

    "Low Stock",

    "Out Of Stock"

]

# inventory id

def generate_inventory_id(number):
    return f"INV{number:07d}"

# Generate Inventory

rows=[]

inventory_number= 1

for store in stores:
    store_id=store[0]
    selected_products = random.sample(products,700)

    for product in selected_products:
        product_id = product[0]
        cost_price = product[1]
        unit_price= product[2]
        quantity= random.randint(0,500)
        reorder_level = random.randint(20,100)
        if quantity == 0:
            status= "Out Of Stock"
        elif quantity <= reorder_level:
            status="Low Stock"
        else:
            status= "Available"

        last_stock_date= fake.date_between(
            start_date="-90d",
            end_date="today"
        )
        created_at = last_stock_date
        updated_at=fake.date_between(
            start_date=created_at,
            end_date="today"
        )

        inventory_value = quantity * cost_price

        rows.append(
            {
                "inventory_id":generate_inventory_id(inventory_number),
                "store_id":store_id,
                "product_id":product_id,
                "quantity":quantity,
                "reorder_level": reorder_level,
                "inventory_value":inventory_value,
                "status":status,
                "last_stock_date": last_stock_date,
                "created_at":created_at,
                "updated_at":updated_at
            }
        )

        inventory_number += 1

# create dataframe

inventory_df= pd.DataFrame(rows)

print(f"Inventory Generated Successfully")
print(f"Total Records : {len(inventory_df)}")

# this created 500 stores * 700 products = 350000


#  duplicate rows

duplicate_rows = inventory_df.sample(
    2000,random_state=100
)
inventory_df=pd.concat(
    [inventory_df,duplicate_rows],ignore_index=True

)
# Duplicate inventory ids

rows= random.sample(range(len(inventory_df)),300)
for r in rows:
    inventory_df.loc[r,"inventory_id"]= "INV007777"


# invalid  store ids
rows = random.sample(range(len(inventory_df)),2500)
for r in rows:
    inventory_df.loc[r,"store_id"]="STR987463"

# invalid product ids

rows= random.sample(range(len(inventory_df)),2500)
for r in rows:
    inventory_df.loc[r,"product_id"]= "PROD9479328"

# Missing product ids

rows = random.sample(range(len(inventory_df)),2500)

for r in rows:
    inventory_df.loc[r,"product_id"]= None

# same for store ids

# extra spaces
rows=random.sample(range(len(inventory_df)),2500)
for r in rows:
    inventory_df.loc[r,"status"] = (
        "  "+ str(inventory_df.loc[r,"status"]) + "  "
    )

# ==========================================================
# Mixed Case
# ==========================================================

rows = random.sample(
    range(len(inventory_df)),
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

        inventory_df.loc[r, "status"] = str(
            inventory_df.loc[r, "status"]
        ).upper()

    elif style == "lower":

        inventory_df.loc[r, "status"] = str(
            inventory_df.loc[r, "status"]
        ).lower()

    elif style == "title":

        inventory_df.loc[r, "status"] = str(
            inventory_df.loc[r, "status"]
        ).title()

    else:

        inventory_df.loc[r, "status"] = " ".join(

            word.upper() if random.random() > 0.5 else word.lower()

            for word in str(
                inventory_df.loc[r, "status"]
            ).split()

        )

# save csv

inventory_df.to_csv("../../csv/inventory.csv",index=False)

