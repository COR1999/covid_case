import csv
from faker import Faker
from time import time
RECORD_COUNT = 9


fake = Faker()


def create_csv_file():
    with open("./test_data/dummy_data.csv", "w", newline="") as csvfile:
        fieldnames = ["product_name", "price", "color", "size", "qty", "image"]
        product_name = ["Face-mask Pack of 2", "visor"]
        product_price = [5, 10]
        product_colors = ["clear", "Black", "Denim", "Dotted", "Multi",
                          "Flourish", "Gold", "Leopard", "Navy", "White"]
        all_product = []
        index = 0
        for item in product_colors:
            print(item)

            product = {"product_name": f"{product_name[0]} + {item}",
                       "price": product_price[0],
                       "color": item,
                       "size": "ONE SIZE",
                       "qty": fake.random_int(min=0, max=5),
                       "image": f"./media/_{item}",
                       }
            all_product.append(product)

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # product_price = product_price[0]
        print(all_product)
        # if product_colors[0]:
        #     product_price = product_price[1]
        #     product_name = product_name[1]
        # else:
        #     product_price = product_price[0]
        #     product_name = product_name[0]

        for i in range(RECORD_COUNT):
            writer.writerow(all_product)


def get_totals():
    qty_total = 0
    amount_total = 0
    with open("./test_data/dummy_data.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[5] != "qty":
                qty_total += qty

                # size = row[4]
                # color = row[3]
                price = row[2]
                amount_total += price
                # product_name = row[0]
                # product_id = row[1]
    return qty_total, amount_total


if __name__ == "__main__":
    start = time()
    create_csv_file()
    elapsed = time() - start
    print("created csv file - time: {}".format(elapsed))
