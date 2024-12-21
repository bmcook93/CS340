from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in Mongo DB"""
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        # 
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34963
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None and isinstance(data, dict):
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            
            # If successful, return true, else return false
            if insert != 0:
                return True;
            else:
                return False;
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD.
    def read(self, query=None):
        # result in a list if command is successful, else an empty list
        if query is not None:
            data = self.database.animals.find(query, {"_id": False})
            
            #print list
            #for doc in data:
                #print(doc)
                
        else:
            data = self.database.animals.find({},{"_id": False})
            
        return data
    
# Create method to implement the U in CRUD.
    def update(self, old, new):
        # check that parameters have data and is dictionary
        if not old or not isinstance(old, dict) or not new or not isinstance(new, dict):
            raise Exception("Invalid parameters. Must be non-empty dictionary.")
            
        update = self.database.animals.update_many(old, {"$set": new})
        
        # return result as number
        return update.modified_count
    
# Create method to implement the D in CRUD.
    def delete(self, delete):
        # check that parameter has data and is dictionary
        if not delete or not isinstance(delete, dict):
            raise Exception("Nothing to delete, because delete parameter is empty.")
            
        remove = self.database.animals.delete_many(delete)
        
        # return number of deletes
        return remove.deleted_count