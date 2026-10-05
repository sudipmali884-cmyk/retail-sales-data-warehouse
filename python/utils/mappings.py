STATE_CITY_MAPPING = {

    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik",
        "Kolhapur",
        "Solapur",
        "Sangli",
        "Aurangabad",
        "Thane"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Hubli",
        "Belagavi",
        "Mangalore",
        "Shivamogga"
    ],

    "Gujarat": [
        "Ahmedabad",
        "Surat",
        "Vadodara",
        "Rajkot",
        "Bhavnagar"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Salem",
        "Trichy"
    ],

    "Telangana": [
        "Hyderabad",
        "Warangal",
        "Karimnagar",
        "Nizamabad"
    ],

    "Delhi": [
        "New Delhi"
    ],

    "Rajasthan": [
        "Jaipur",
        "Jodhpur",
        "Udaipur",
        "Kota"
    ],

    "West Bengal": [
        "Kolkata",
        "Howrah",
        "Durgapur",
        "Siliguri"
    ],

    "Kerala": [
        "Kochi",
        "Thiruvananthapuram",
        "Kozhikode"
    ],

    "Madhya Pradesh": [
        "Indore",
        "Bhopal",
        "Jabalpur",
        "Gwalior"
    ]
}

STATE_REGION_MAPPING = {

    "Maharashtra": "West",
    "Gujarat": "West",

    "Karnataka": "South",
    "Tamil Nadu": "South",
    "Kerala": "South",
    "Telangana": "South",

    "Delhi": "North",
    "Rajasthan": "North",

    "West Bengal": "East",

    "Madhya Pradesh": "Central"
}

ADDRESS_MAPPING = {
    "Pune": [
        ("FC Road", "411004"),
        ("Kothrud", "411038"),
        ("Hinjewadi", "411057"),
        ("Baner", "411045"),
    ],

    "Mumbai": [
        ("Andheri", "400053"),
        ("Bandra", "400050"),
        ("Dadar", "400014"),
    ],

    "Solapur": [
        ("Jule Solapur", "413004"),
        ("Hotgi Road", "413003"),
        ("Railway Lines", "413001"),
    ]
}

GENDERS=[
    "Male","Female"
]

DESIGNATIONS = {

    "Cashier": "Billing",

    "Sales Associate": "Sales",

    "Inventory Executive": "Inventory",

    "Supervisor": "Operations",

    "Store Manager": "Management"

}

# generate_ products

CATEGORY_MAPPING = {

    "Groceries": [
        "Rice",
        "Wheat Flour",
        "Sugar",
        "Salt",
        "Cooking Oil"
    ],

    "Beverages": [
        "Tea",
        "Coffee",
        "Juice",
        "Soft Drink",
        "Water"
    ],

    "Dairy": [
        "Milk",
        "Curd",
        "Butter",
        "Cheese",
        "Paneer"
    ],

    "Snacks": [
        "Biscuits",
        "Chips",
        "Chocolate",
        "Namkeen",
        "Cookies"
    ],

    "Personal Care": [
        "Soap",
        "Shampoo",
        "Toothpaste",
        "Face Wash",
        "Hair Oil"
    ],

    "Home Care": [
        "Detergent",
        "Floor Cleaner",
        "Dish Wash",
        "Phenyl",
        "Air Freshener"
    ]

}

BRANDS = [

    "Amul",

    "Nestle",

    "Parle",

    "Britannia",

    "Tata",

    "Fortune",

    "Aashirvaad",

    "Surf Excel",

    "Colgate",

    "Dove",

    "Patanjali"

]

SUPPLIERS = [

    "ABC Distributors",

    "National Traders",

    "Fresh Supply Pvt Ltd",

    "Retail Wholesale Ltd",

    "Global Retail Supply"

]

PRODUCT_STATUS = [

    "Active",

    "Discontinued"

]


# -------------------------------------------------- SALES USE
# Payment Methods
# --------------------------------------------------

PAYMENT_METHODS = [

    "Cash",

    "UPI",

    "Credit Card",

    "Debit Card",

    "Net Banking"

]

# --------------------------------------------------
# Sales Status
# --------------------------------------------------

SALES_STATUS = [

    "Completed",

    "Cancelled",

    "Returned"

]

# sales mapping for returns
# --------------------------------------------------
# Return Reasons
# --------------------------------------------------

RETURN_REASONS = [

    "Damaged Product",

    "Wrong Product",

    "Defective Product",

    "Expired Product",

    "Customer Changed Mind"

]

# --------------------------------------------------
# Refund Methods
# --------------------------------------------------

REFUND_METHODS = [

    "Cash",

    "UPI",

    "Bank Transfer",

    "Credit Card"

]

# --------------------------------------------------
# Return Status
# --------------------------------------------------

RETURN_STATUS = [

    "Approved",

    "Pending",

    "Rejected"

]