import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database"
)

mycursor = mydb.cursor()


def category_wise_number_of_product():
    print("Category and Number of Products")
    mycursor.execute('select Product_Category,count(Product_Name) from blinkit_scrap_data group by Product_Category')
    data = mycursor.fetchall()
    print(data)


def insert_data(data):
    sql = "INSERT INTO blinkit_scrap_data (Product_Category,Product_Name,Product_Price,Product_Quantity) VALUES (%s, %s, %s, %s)"
    val = data
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def product_between_price(val1, val2):
    val = (val1, val2)
    sql = "select * from blinkit_scrap_data where Product_Price BETWEEN %s AND %s"
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    print(data)


def product_greater_than_price(val1):
    sql = "select * from blinkit_scrap_data where Product_Price > {v1} ".format(v1=val1)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print(data)


def product_less_than_price(val1):
    sql = "select * from blinkit_scrap_data where Product_Price < {v1} ".format(v1=val1)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print(data)


def product_greater_or_equal_to_price(val1):
    val = val1
    sql = "select * from blinkit_scrap_data where Product_Price >= {v1} ".format(v1=val1)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print(data)


def product_less_or_equal_to_price(val1):
    val = val1
    sql = "select * from blinkit_scrap_data where Product_Price <= {v1} ".format(v1=val1)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print(data)


mydb.commit()
