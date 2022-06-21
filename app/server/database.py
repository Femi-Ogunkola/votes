import datetime

import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("users_collection")

poll_collection = database.get_collection("polls_collection")

# helpers 


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "password": user["password"],
        "createdDate": user["createdDate"],
        "updatedDate": user["updatedDate"],
    }

def poll_helper(poll) -> dict:
    return {
        "id": str(poll["_id"]),
        "title": poll["title"],
        "description": poll["description"],
        "createdDate": poll["createdDate"],
        "updatedDate": poll["updatedDate"],
        "type": poll["type"],
    }



async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

async def retrieve_polls():
    polls = []
    async for poll in poll_collection.find():
        polls.append(poll_helper(poll))
    return polls


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def add_poll(poll_data: dict) -> dict:
    createdDate = datetime.datetime.now()
    poll_data['createdDate'] = createdDate
    poll_data['updatedDate'] = createdDate
    poll = await poll_collection.insert_one(poll_data)
    new_poll = await poll_collection.find_one({"_id": poll.inserted_id})
    return poll_helper(new_poll)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

async def retrieve_poll(id: str) -> dict:
    poll = await poll_collection.find_one({"_id": ObjectId(id)})
    if poll:
        return poll_helper(poll)

# Update a user with a matching ID
async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        data['updatedDate'] = datetime.datetime.now()
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

async def update_poll(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    poll = await poll_collection.find_one({"_id": ObjectId(id)})
    print(poll)
    if poll:
        data['updatedDate'] = datetime.datetime.now()
        print(data)
        updated_poll = await poll_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_poll:
            return True
        return False
    
async def vote_poll(id: str, data: dict):
    poll = await poll_collection.find_one({"_id": ObjectId(id)})
    if poll:
        #data['updatedDate'] = datetime.datetime.now()
        print(f"${data['vote']}")
        updated_poll = await poll_collection.update_one(
            {"_id": ObjectId(id)}, {"$inc": {f"option.{data['vote']}":1}}
        )
        if updated_poll:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

async def delete_poll(id: str):
    poll = await poll_collection.find_one({"_id": ObjectId(id)})
    if poll:
        await poll_collection.delete_one({"_id": ObjectId(id)})
        return True