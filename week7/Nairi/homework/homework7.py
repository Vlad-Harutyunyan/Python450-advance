from pymongo import MongoClient
from time import gmtime, strftime
import json
client = MongoClient('mongodb://localhost:27017/')    
db = client['shop_database']

#creating collections
users_collection = db['users']
orders_collection = db['orders']
order_items_collection = db['order_items']
products_collection = db['products']
categories_collection = db['categories']
merchants_collection = db['merchants']
countries_collection = db['countries']

countries_collection.insert_one({'code':'051','name':'Armenia','alpha_2_code':'AR'})
countries_collection.insert_one({'code':'840','name':'United States of America','alpha_2_code':'US'})

users_collection.insert_one(
    {
        'name':'Vlad',
        'surname':'Harutyunyan',
        'age':20,
        'email':'vlad.har.yan@gmail.com',
        'gender':'male',
        'address':countries_collection.find_one({'name':'Armenia'}),
        'created_at':strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
)

orders_collection.insert_one(
    {
        'user': users_collection.find_one({'email':'vlad.har.yan@gmail.com'}),
        'status':True,
        "created_at": strftime("%Y-%m-%d %H:%M:%S", gmtime())
        
    } 
)

merchants_collection.insert_one(
    {
        "admin_id": users_collection.find_one({'email':'vlad.har.yan@gmail.com'}),
        'marchant_name':'Jhon',
        'address':countries_collection.find_one({'alpha_2_code':'US'}) ,
        'created_at': strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
)


categories_collection.insert_one(
    {
        'category_name':'Sweets'
    }
)

products_collection.insert_one(
    {
        'name':'M&M’s',
        'merchant':merchants_collection.find_one({'marchant_name':'Jhon'}) ,
        'price':1200,
        'status':'in stock',
        'created_at': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        'category':categories_collection.find_one({'category_name':'Sweets'}) 
    }
)

order_items_collection.insert_one(
    {
        'order':orders_collection.find_one({'status':True}),
        'product':products_collection.find_one({'name':'M&M’s'}),
        'quantity':11
    }
)
collist = db.list_collection_names()

# print(users_collection.find_one({'email':'vlad.har.yan@gmail.com'}))
# print(orders_collection.find_one({"status":True}))

print(products_collection.find_one({'name':'M&M’s'}))
print(order_items_collection.find_one({'quantity':11}))
