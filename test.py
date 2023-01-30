import mysqlconnecter
print("\nCategory\n")
mysqlconnecter.category_wise_number_of_product()
print("\nProduct < 50\n")
mysqlconnecter.product_less_than_price(50)
print("\nProduct > 1000\n")
mysqlconnecter.product_greater_than_price(1000)
print("\n50 < Product < 100\n")
mysqlconnecter.product_between_price(50,100)