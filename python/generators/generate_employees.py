import random,pandas as pd

from faker import Faker
fake=Faker("en_IN")
random.seed(100)
Faker.seed(100)

TOTAL_EMPLOYEES= 50000

# READ STORES
store_df=pd.read_csv("../../csv/stores.csv")
store_df["opening_date"]=pd.to_datetime(
    store_df["opening_date"],
    errors="coerce"
)

store_mapping=store_df[["store_id","opening_date","city","state"]]# this will get data from generate_store

stores=store_mapping.values.tolist()

#
EMPLOYEE_STATUS=["Active","Resigned","On Leave" ]

from utils.mappings import (
    GENDERS, DESIGNATIONS
)

def generate_employee_id(number):
    return  f"EMP{number:06d}"


# generate employee

employee=[]

for i in range(1, TOTAL_EMPLOYEES +1):
    employee_id = generate_employee_id(i)
    gender= random.choice(GENDERS)
    if gender =='Male' :
        employee_name = fake.name_male()
    else:
        employee_name= fake.name_female()

    designation=random.choices(
        list(DESIGNATIONS.keys()),
        weights=[40,30,15,10,5],
        k=1
    )[0]
    department= DESIGNATIONS[designation]
    store_id,opening_date,city,state = random.choice(stores)
    hire_date=fake.date_between(
        start_date=opening_date.date(),
        end_date="today"
    )
    created_at=hire_date
    updated_at=fake.date_between(
        start_date=created_at,
        end_date="today"
    )
    if designation == "Cashier":
        salary = random.randint(18000,25000)
    elif designation == "Sales Associate":
        salary = random.randint(20000,30000)
    elif designation =="Inventory Executive":
        salary= random.randint(25000,35000)

    elif designation == "Supervisor":

        salary = random.randint(35000,50000)

    else:

        salary = random.randint(50000,80000)

    phone = str(

        random.randint(

            6666666666,

            9999999999

        )

    )
    email=(
        employee_name.replace(" ","").lower()+"@gmail.com"
    )

    status= random.choices(
        EMPLOYEE_STATUS,
        weights=[85,10,5],
        k=1
    )[0]
    employee.append({
        "employee_id": employee_id,

        "employee_name": employee_name,

        "gender": gender,

        "designation": designation,

        "department": department,

        "store_id": store_id,

        "city":city,
        "state":state,

        "phone": phone,

        "email": email,

        "salary": salary,

        "hire_date": hire_date,

        "status": status,

        "created_at": created_at,

        "updated_at": updated_at
    })
employee_df=pd.DataFrame(employee)

# duplicate rows

duplicate_rows=employee_df.sample(
    100,random_state=100
)
employee_df=pd.concat(
    [employee_df,duplicate_rows],ignore_index=True
)

# duplicate ids

rows= random.sample(range(len(employee_df)),50)

for r in rows:
    employee_df.loc[r,"employee_id"]="EMP000007"

# missing employee email
rows = random.sample(range(len(employee_df)),100)
for r in rows:
    employee_df.loc[r,"email"]=None

# Blank Department

rows=random.sample(range(len(employee_df)),100)
for r in rows:
    employee_df.loc[r,"department"]=""

# extra spaces
rows=random.sample(range(len(employee_df)),100)
for r in rows:
    employee_df.loc[r,"employee_name"]=(
        " "+ str(employee_df.loc[r,"employee_name"]) + " "
    )

# ==========================================================
# Future Hire Dates
# ==========================================================

rows = random.sample(
    range(len(employee_df)),
    30
)

for r in rows:

    employee_df.loc[r, "hire_date"] = "2035-01-01"

# Invalid Store IDs
# ==========================================================

rows = random.sample(
    range(len(employee_df)),
    25
)

for r in rows:

    employee_df.loc[r, "store_id"] = "STORE9999"

employee_df.to_csv("../../csv/employees.csv",index=False)

print("Employee Generated Successfully")

print(f"Total Records : {len(employee_df)}")

print(f"Duplicate Records: {len(duplicate_rows)}")

