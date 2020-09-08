import random
import csv
import json
from faker import Faker
from time import time
RECORD_COUNT = 8

fake = Faker()
my_json_file = open("./products/fixtures/products.json", "w")
media_url = "./media"


# def create_csv_file():
#     with open("./test_data/dummy_data.csv", "w", newline="") as csvfile:
#         fieldnames = ["product_name", "price", "color", "size", "image"]
#         product_name = ["Face-mask Pack of 2", "visor"]
#         product_price = [5, 10]
#         product_colors = ["clear", "Black", "Denim", "Dotted", "Multi",
#                           "Flourish", "Gold", "Leopard", "Navy", "White"]
#         all_product = []
#         index = 0
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for item in product_colors:
#             print(item)

#             product = {"product_name": f"{product_name[0]} {item}",
#                        "price": product_price[0],
#                        "color": item,
#                        "size": "ONE SIZE",
#                        "image": f"{media_url}/_{item}",
#                        }
#             writer.writerow(product)


# def get_totals():
#     qty_total = 0
#     amount_total = 0
#     with open("./test_data/dummy_data.csv", "r", newline="") as csvfile:
#         reader = csv.reader(csvfile, delimiter=",")
#         for row in reader:
#             if row[5] != "qty":
#                 qty_total += qty

#                 # size = row[4]
#                 # color = row[3]
#                 price = row[2]
#                 amount_total += price
#                 # product_name = row[0]
#                 # product_id = row[1]
#     return qty_total, amount_total


def write_to_json():
    with my_json_file as json_file:

        fieldnames = ["product_name", "price", "color", "size", "image"]
        # product_name = ["Face-mask Pack of 2", "Visor"]
        # product_price = [5, 10]
        product_colors = ["black", "denim", "dotted", "multi",
                          "gold", "leopard", "navy", "white"]
        all_products = []
        pk_id = 1
        visor = {
            "pk": pk_id,
            "model": "products.product",
            "fields": {
                "product_name": f"Visor",
                "price":  round(random.uniform(5, 10), 2),
                "color": "",
                "has_size": False,
                "image": f"_visor.jpg",
                "image_2": f"_visor_2.jpg",

            }
        }
        all_products.append(visor)
        for item in product_colors:
            print(item)
            pk_id += 1
            product = {
                "pk": pk_id,
                "model": "products.product",
                "fields": {
                    "product_name": f"Face-mask Pack of 2, {item}",
                    "price":  round(random.uniform(5, 10), 2),
                    "color": item,
                    "has_size": False,
                    "image": f"_{item}.jpg",
                    "image_2": f"_{item}_2.jpg",

                }
            }
            all_products.append(product)
        json.dump(all_products, json_file)


if __name__ == "__main__":
    start = time()
    # create_csv_file()
    write_to_json()
    elapsed = time() - start
    print("created csv file - time: {}".format(elapsed))
