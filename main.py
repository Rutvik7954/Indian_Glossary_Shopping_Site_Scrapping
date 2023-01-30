import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
# import csv

from selenium.webdriver.common.keys import Keys
url = ['https://blinkit.com/cn/fresh-vegetables/cid/1487/1489', 'https://blinkit.com/cn/dairy-breakfast/milk/cid/14/922', 'https://blinkit.com/cn/munchies/chips-crisps/cid/1237/940', 'https://blinkit.com/cn/cold-drinks-juices/soft-drinks/cid/332/1102', 'https://blinkit.com/cn/instant-frozen-food/noodles/cid/15/962', 'https://blinkit.com/cn/tea-coffee-health-drinks/tea/cid/12/957', 'https://blinkit.com/cn/bakery-biscuits/cookies/cid/888/28', 'https://blinkit.com/cn/sweet-tooth/indian-sweets/cid/9/943', 'https://blinkit.com/cn/atta-rice-dal/atta/cid/16/1165', 'https://blinkit.com/cn/dry-fruits-masala-oil/dry-fruits/cid/1557/1160', 'https://blinkit.com/cn/sauces-spreads/tomato-chilli-ketchups/cid/972/1131', 'https://blinkit.com/cn/chicken-meat-fish/chicken/cid/4/1362', 'https://blinkit.com/cn/organic-premium/oil-ghee/cid/175/799', 'https://blinkit.com/cn/baby-care/diapers-wipes-more/cid/7/1000', 'https://blinkit.com/cn/pharma-wellness/cough-cold/cid/287/75', 'https://blinkit.com/cn/cleaning-essentials/detergent-powder-bars/cid/18/983', 'https://blinkit.com/cn/home-office/fresheners/cid/1379/1085', 'https://blinkit.com/cn/personal-care/oral-care/cid/163/722', 'https://blinkit.com/cn/pet-care/dog-food/cid/5/133']
ctgry = []
pname = []
pprice = []
qty = []
csv_data = []

driver = webdriver.Chrome(r"C:\Users\BAPS\Downloads\chromedriver.exe")
# Optional argument, if not specified will search path.
for i in url:
    driver.get(i)

    time.sleep(2)
    # Let the user actually see something!

    driver.maximize_window()
    time.sleep(5)

    sub_catagories = driver.find_elements(by=By.CLASS_NAME, value='CategoryListItem__Text-sc-ve8uzt-4.fYRgqC')

    for sub_catagory in sub_catagories:

        cat = sub_catagory.text

        sub_catagory.click()

        time.sleep(5)
        Product_name = driver.find_elements(by=By.CLASS_NAME, value='Product__ProductName-sc-11dk8zk-6.fxBwnM')
        Price = driver.find_elements(by=By.CLASS_NAME, value='ProductPrice__Price-sc-14194u2-1.eJcLXJ')
        Quantity = driver.find_elements(by=By.CLASS_NAME, value='variant_text_only.plp-product__quantity--box')

        for j in Product_name:
            pn = j.text
            pname.append(pn)
            ctgry.append(cat)
            # print(pn)

        for j in Price:
            pp = j.text
            pprice.append(pp)
            # print(pp)

        for j in Quantity:
            qy = j.text
            qty.append(qy)
            # print(qy)


# for i in range(len(qty)-1):
#
#     # print("%s %s %s %s" % (ctgry[i], pname[i], pprice[i], qty[i]))
#
#     data = [ctgry[i], pname[i], pprice[i], qty[i]]  # the data
#     print(data)
#     csv_data.append(data)


# with open('D:\Data.csv', 'w', encoding="utf-8") as f:
#     writer = csv.writer(f)  # this is the writer object
#     column_name = ['Product_Catagoty', 'Product_Name', 'Product_Price', 'Product_Quantity']
#     writer.writerow(column_name)
#     for i in csv_data:
#         writer.writerow(i)  # this is the data
#     f.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database"
)

mycursor = mydb.cursor()
sql = "INSERT INTO blinkit_scrap_data (Product_Category,Product_Name,Product_Price,Product_Quantity) VALUES (%s, %s, %s, %s)"

for i in range(len(qty)-1):
    val = (ctgry[i], pname[i], pprice[i], qty[i])
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


time.sleep(5)
# Let the user actually see something!

driver.quit()
