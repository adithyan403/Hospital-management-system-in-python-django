from pymongo import MongoClient as mon


client = mon('mongodb://localhost:27017/')
db=client['hospital']
user_collection=db['users']
def signup(data):
    user_collection.insert_one(data)

    print(data,"data inserted successfully")

def check_email(email):
        data=user_collection.find({})
        for i in data:
            if i["email"]==email:
                return True
        else:
             return False
def login(email,password):
     data=user_collection.find({})
     for i in data:
          if i["email"]==email and i["password"]==password:
               
               return True 
     else:
          return False
def booking(data,user_id):
     booking_collection=db[user_id] 
     booking_collection.insert_one(data)

def booking_details(user_id):
     collection=db[user_id]
     data=collection.find({})
     return data
def cancel_booking(id,user_id):
     collection2=db[user_id]
     collection2.delete_one({"id":int(id)})

def admin_login(email,password):
     collection=db["admins"]
     admins=collection.find({})
     for i in admins:
          if i["email"]==email and i["password"]==int(password):
               return True
     else:
          return False 
user_list=[]     
def booking_admin():
     users=user_collection.find({})
     
     return users
def users_bookings(email):
     collection=db[email]
     data=collection.find({})
     return data 
def id_enter(id):
     id_collection=db["approved_ids"]
     data={"id":id}
     id_collection.insert_one(data)

def approved_ids():
     collection=db["approved_ids"]
     data=collection.find({})
     ids=[int(i["id"]) for i in data]
     return ids  



