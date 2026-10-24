from pymongo import MongoClient

class AnimalShelter(object):
    
    # initial values for connecting to mongodb
    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COLL = "animals"
        
        # initialize the connection to mongodb
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COLL)]
        

# create function to create a new record in the aac database
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save because the data parameter is empty")
            return False
            
# read function to return records from the aac database
    def retrieve(self, data):
        if data is None:
            return []
        
        try:
            cursor = self.collection.find(data)
            
            return list(cursor)
        
        except Exception as e:
            print(f"Read operation failed: {e}")
            return []
    
# update function to update records from the aac database
    def update(self, query, data):
        if query is None or data is None:
            raise Exception("Data parameter is empty.")
        
        try:
            result = self.collection.update_many(query, data)
            return result.modified_count
        
        except Exception as e:
            print(f"Update failed: {e}")
            return 0

# delete function to delete records from the aac database
    def delete(self, data):
        if data is None:
            raise Exception(f"Data parameter cannot be empty.")
        
        try:
            delete_doc = self.collection.delete_many(data)
            return delete_doc.deleted_count
        
        except Exception as e:
            print(f"Deletion failed: {e}")
            return 0

