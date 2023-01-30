import mysqlconnecter

new_price_list = []
new_name_list = []
mysqlconnecter.mycursor.execute("select Product_Name,Product_Price from blinkit_scrap_data")
data = mysqlconnecter.mycursor.fetchall()
for i in data:
    new_list = list(i)
    new_name_list.append(new_list[0])
    text = new_list[1]

    if text.__contains__('₹'):
        text = text.replace('₹', '')
        new_price_list.append(text)

for i in range(len(new_price_list)):
    val = (new_price_list[i], new_name_list[i])
    sql = 'UPDATE blinkit_scrap_data SET Product_Price= %s WHERE Product_Name= %s'
    mysqlconnecter.mycursor.execute(sql, val)
    mysqlconnecter.mydb.commit()
#     # print(f"{new_name_list[i]}  {new_price_list[i]}")
