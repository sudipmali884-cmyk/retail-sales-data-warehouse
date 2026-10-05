import  random, pandas as pd
from faker import  Faker



fake=Faker("en_IN")
random.seed(100)
Faker.seed(100)

products_df=pd.read_csv("../../csv/products.csv")

product_mapping=products_df[["product_id","unit_price","category","brand"]]

products= product_mapping.values.tolist()


TOTAL_PROMOTIONS = 500
PROMOTIONS_TYPES= [
    "Flat Discount",

    "Percentage Discount",

    "Buy One Get One",

    "Festival Offer",

    "Clearance Sale"
]

PROMOTION_STATUS =["Active","Expired","Scheduled"]


def generate_promotion_id(number):
    return f"PROMP{number:05d}"


rows= []
selected_products = random.sample(products,TOTAL_PROMOTIONS)

for i, product in enumerate(selected_products,start=1):
    product_id=product[0]
    unit_price= [1]
    category=product[2]
    brand=product[3]
    promotion_type = random.choice(PROMOTIONS_TYPES)
    promotion_name=(
        f"{brand}  {promotion_type}"
    )
    discount_percentage= random.choice(
        [5,10,15,20,25,30,40,50]
    )

    start_date = fake.date_between(
        start_date ="-1y",
        end_date= "today"
    )
    end_date = fake.date_between(

        start_date=start_date,

        end_date="+60d"

    )
    today=pd.Timestamp.today().date()
    if end_date < today:
        status= "Expired"
    elif start_date > today:
        status = "Scheduled"

    else :
        status = "Active"
    created_at = start_date
    updated_at = fake.date_between(
        start_date=created_at,
        end_date="today"

    )
    rows.append({
        "promotion_id": generate_promotion_id(i),
        "product_id": product_id,
        "promotion_name": promotion_name,

        "promotion_type": promotion_type,

        "category": category,

        "brand": brand,

        "discount_percentage": discount_percentage,

        "start_date": start_date,

        "end_date": end_date,

        "status": status,

        "created_at": created_at,

        "updated_at": updated_at
    })

promotion_df=pd.DataFrame(rows)
print("=*"*15)
print("Promotions Generated Successfully")


# duplicate rows

duplicate_rows = promotion_df.sample(20,random_state=100)
promotion_df = pd.concat([promotion_df,duplicate_rows],ignore_index=True)

# duplicate ids
rows=random.sample(range(len(promotion_df)),20)
for r in rows:
    promotion_df.loc[r,"promotion_id"]= None

# blank

rows=random.sample(range(len(promotion_df)),5)
for r in rows:
    promotion_df.loc[r,"promotion_name"]= ""


# invalid status

bad_status= [ "Running","Completed","Offer", None]

rows=random.sample(range(len(promotion_df)),10)
for r in rows:
    promotion_df.loc[r,"status"]= random.choice(bad_status)

#  mixed case

rows=random.sample(range(len(promotion_df)),20)
for r in rows:
    style=random.choice(
        [
            "upper",
            "lower",
            "title",
            "mixed"
        ]
    )
    if style=="upper":
        promotion_df.loc[r,"promotion_name"]=str(promotion_df.loc[r,"promotion_name"]).upper()
    elif style=="lower":
        promotion_df.loc[r,"promotion_name"]=str(
            promotion_df.loc[r,"promotion_name"]
        ).lower()
    elif style=="title":
        promotion_df.loc[r,"promotion_name"]=str(
            promotion_df.loc[r,"promotion_name"]
        ).title()
    else:
        promotion_df.loc[r, "promotion_name"] = " ".join(

            word.upper() if random.random() > 0.5 else word.lower()

            for word in str(
                promotion_df.loc[r, "promotion_name"]
            ).split()

        )

# save csv
promotion_df.to_csv("../../csv/promotions.csv",index=False)
print("total records ",len(promotion_df))
print("duplicate records",len(duplicate_rows))
print("=*"*15)