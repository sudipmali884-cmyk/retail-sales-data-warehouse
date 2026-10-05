import random
import pandas as pd
from faker import Faker
from datetime import timedelta,date

fake=Faker("en_IN")

random.seed(100)
Faker.seed(100)

sales_df=pd.read_csv("../../csv/sales.csv")

sales_mapping = sales_df[
    [
        "sale_id",
        "sale_date",
        "customer_id",
        "store_id",
        "employee_id",
        "product_id",
        "quantity",
        "unit_price",
        "total_amount"
    ]
]

sales = sales_mapping.values.tolist()

TOTAL_RETURNS = 100000

from utils.mappings import (
    RETURN_STATUS,RETURN_REASONS,REFUND_METHODS
)

# RETURN ID
def generate_return_id(number):
    return f"RET{number:07d}"

# generate returns

rows = []
selected_sales = random.sample(sales,TOTAL_RETURNS)

for i,sale in enumerate(
    selected_sales,start=1
):
    sale_id=sale[0]
    sale_date=pd.to_datetime(sale[1])
    customer_id=sale[2]
    store_id=sale[3]
    employee_id=sale[4]
    product_id=sale[5]
    quantity=sale[6]
    unit_price=sale[7]
    total_amount=sale[8]


    return_quantity=random.randint(
        1,quantity
    )
    return_amount = round(
        return_quantity * unit_price *2
    )
    refund_method=random.choice(REFUND_METHODS)
    return_reason= random.choice(RETURN_REASONS)
    return_status= random.choices(
        RETURN_STATUS,weights=[80,10,10],k=1
    )[0]


    from datetime import date
    today=date.today()


    max_return_date = min(
        sale_date.date() + timedelta(days=30),
        today
    )

    return_date = fake.date_between(
        start_date=sale_date.date(),
        end_date=max_return_date
    )

    created_at = return_date

    updated_at = fake.date_between(
        start_date=created_at,
        end_date=today
    )
    rows.append({

        "return_id": generate_return_id(i),

        "sale_id": sale_id,

        "customer_id": customer_id,

        "store_id": store_id,

        "employee_id": employee_id,

        "product_id": product_id,

        "return_date": return_date,

        "return_reason": return_reason,

        "return_quantity": return_quantity,

        "refund_amount": return_amount,

        "refund_method": refund_method,

        "return_status": return_status,

        "created_at": created_at,

        "updated_at": updated_at

    })
return_df=pd.DataFrame(rows)

print("Return Generated Successfully")
print(f"Total Records: {len(return_df)}")
return_df.to_csv("../../csv/returns.csv",index=False)
