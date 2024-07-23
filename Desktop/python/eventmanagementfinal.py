 
!pip install pymongo

from pymongo import MongoClient
#from bson import ObjectId
client=MongoClient('mongodb+srv://kiruthikavenu:G1TnaugyWwu6pH6k@cluster0.biotw1y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db=client['db1']
collection=db['EventManagement']

# Sample event data
sample_event = {
    "name": "Python Seminar",
    "date": "2024-06-01",
    "location": "New York",
    "description": "An in-depth Python workshop."
}
# Function to create events
def create_event(sample_event):
    result = collection.insert_one(sample_event)
    return result.inserted_id

# Function to get all events
def get_all_events():
    events = list(collection.find())
    return events

# Function to update an event by ID
def update_event(event_id, updated_event):
    result = collection.update_one({"_id": ObjectId(event_id)}, {"$set": updated_event})
    return result.modified_count


# Function to delete an event by ID
def delete_event(event_id):
    result = collection.delete_one({"_id": ObjectId(event_id)})
    return result.deleted_count

# Create an event
event_id = create_event(sample_event)
print(f"Event created with ID: {event_id}")


# Get all events
events = get_all_events()
print("All events:")
for event in events:
    print(event)


# Update an event
updated_event = {
    "name": "Advanced Python Workshop",
    "location": "San Francisco"
}
update_count = update_event(event_id, updated_event)
print(f"Number of events updated: {update_count}")

# Delete an event
delete_count = delete_event(event_id)
print(f"Number of events deleted: {delete_count}")



client.close()