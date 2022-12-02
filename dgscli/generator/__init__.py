import pandas as pd
from faker import Faker
from faker.providers import DynamicProvider
from tqdm import tqdm
from faker_vehicle import VehicleProvider

payment_type_provider = DynamicProvider(
    provider_name="payment_type", elements=["instalment", "credit_card", "cash"]
)
fake = Faker()
fake.add_provider(VehicleProvider)
fake.add_provider(payment_type_provider)



def order(num=1, product_no=1, user_no=1):
    order = []
    detail = []
    for i in tqdm(range(1, num)):
        o = {}
        o["product_id"] = fake.random_int(1, product_no)
        o["quantity"] = fake.random_int(1, 3)
        o["created_at"] = fake.date_this_century()
        order.append(o)

        od = {}
        od["order_id"] = i
        od["user_id"] = fake.random_int(1, user_no)
        od["total"] = fake.random_int(100000, 1000000)
        od["payment"] = fake.payment_type()
        detail.append(od)
    dfo = pd.DataFrame(order)
    dfd = pd.DataFrame(detail)
    dfo.to_csv("order.csv", index=False)
    dfd.to_csv("order_detail.csv", index=False)


def product(num=1):
    product = []
    inventory = []
    for i in tqdm(range(1, num)):
        p = fake.vehicle_object()
        p["inventory_id"] = i
        p["created_at"] = fake.date_this_century()
        product.append(p)

        iv = {}
        iv["quantity"] = fake.random_int(0, 500)
        inventory.append(iv)
    dfp = pd.DataFrame(product)
    dfi = pd.DataFrame(inventory)
    dfp.to_csv("product.csv", index=False)
    dfi.to_csv("inventory.csv", index=False)


def user(num=1):
    user = []
    detail = []
    for i in tqdm(range(1, num)):
        u = {}
        u["username"] = fake.user_name()
        u["firstname"] = fake.first_name()
        u["lastname"] = fake.last_name()
        u["email"] = fake.email()
        user.append(u)

        d = {}
        d["user_id"] = i
        d["address"] = fake.address()
        d["city"] = fake.city()
        d["postcode"] = fake.postcode()
        d["country"] = fake.country()
        detail.append(d)
    dfu = pd.DataFrame(user)
    dfd = pd.DataFrame(detail)
    dfu.to_csv("users.csv", index=False)
    dfd.to_csv("user_detail.csv", index=False)
