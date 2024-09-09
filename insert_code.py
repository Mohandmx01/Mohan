from pymongo import MongoClientt
cluster=MongoClient("mongodb://localhost:27017")


print(cluster.list_database_names())

# #create database ecommerce
db=cluster["ecommerce"]
# #list collections
customers = db["customers"]
#inserting values
#data= {"first_name":"Jane", "last_name":"Doe", "email":"jane.doe@example.com"}
#customers.insert_one(data)

# data= [{'first_name':'John','last_name':'Doe','email':'john.doe@example.com'}, 
#        {'first_name':'Bruce', 'last_name': 'Wayne', 'email':'bruce.wayne@example.com'} ]
# customers.insert_many(data)

customers.delete_one({"first_name":"Bruce","last_name":"Wayne"})
# customers.delete_many({})



# customers.update_one({"first_name":"Jane"},{"$set":{"Address":{"street":"downing street1","code":6000,"country":"UK"}}})
# customers.update_one({"first_name":"John"},{"$set":{"Address":{"street":"downing street2","code":6001,"country":"USA"}}})
# customers.update_one({"first_name":"Peter"},{"$set":{"Address":{"street":"downing street3","code":6002,"country":"India"}}})
# customers.update_one({"first_name":"Mary"},{"$set":{"Address":{"street":"downing street4","code":6003,"country":"India"}}})
# customers.update_one({"first_name":"Bruce"},{"$set":{"Address":{"street":"downing street5","code":6004,"country":"USA"}}})

#products collection
# data={"name":'iPhone 14 Pro Max', "description":'Latest iPhone.', "price":1099.00, "category":'Electronics'}
# products=db['products']
# # products.insert_one(data)



customers.delete_one({"first_name":"Bruce","last_name":"Wayne"})
products_list = [('iPhone 14 Pro Max', 'Latest iPhone.', 1099.00, 'Electronics'),
 ('Galaxy S22 Ultra', 'Best Android phone.', 1199.00, 'Electronics'),
  ('MacBook Air M2', 'Popular Apple laptop.', 999.00, 'Electronics'),
  ('iPad Pro 2023', 'Best tablet for power users.', 799.00, 'Electronics'),
  ('Sony WH-1000XM5', 'Best noise-cancelling headphones.', 399.00, 'Electronics'),
  ('Air Jordan 1', 'Popular sneaker.', 175.00, 'Clothing'),
  ('Yeezy Boost 350 v2', 'Another popular sneaker.', 220.00, 'Clothing'),
  ('Instant Pot Duo Plus', 'Multi-cooker.', 129.00, 'Home & Garden'),
  ('Ninja Air Fryer Max', 'Air fryer.', 99.00, 'Home & Garden'),
  ('Vitamix 5200 Blender', 'Powerful blender.', 499.00, 'Home & Garden'),
  ('iRobot Roomba j7+', 'Self-emptying robot vacuum.', 799.00, 'Home & Garden'),
  ('Google Nest Hub Max', 'Smart display.', 229.00, 'Home & Garden')]

# products_data = [{"name":product[0],"description":product[1],"price":product[2], "category":product[3]} for product in products_list]
# print(products_data)
# products.insert_many(products_data)
