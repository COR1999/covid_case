import random
import csv
import json
from time import time
RECORD_COUNT = 9

my_json_file = open("./products/fixtures/products.json", "w")


def write_to_json():
    with my_json_file as json_file:

        fieldnames = ["product_name", "price", "color", "size", "image"]
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
                "number_in_stock": round(random.uniform(5, 10), 2),


            }
        }
        all_products.append(visor)
        for item in product_colors:
            # print(item)
            pk_id += 1
            # if image in MEDIA_URL
            #     image = f"_{item}.jpg"
            #     image_2 = f"_{item}.jpg"
            if item == "white":
                image_2 = None
            else:
                image_2 = f"_{item}_2.jpg"
            product = {
                "pk": pk_id,
                "model": "products.product",
                "fields": {
                    "product_name": f"Face-mask Pack of 2",
                    "price":  round(random.uniform(5, 10), 2),
                    "color": item,
                    "has_size": False,
                    "image": f"_{item}.jpg",
                    "image_2": image_2,
                    "number_in_stock": round(random.uniform(5, 10), 2),
                }
            }
            all_products.append(product)
        json.dump(all_products, json_file)


if __name__ == "__main__":
    start = time()
    write_to_json()
    elapsed = time() - start
    print("created json file - time: {}".format(elapsed))
