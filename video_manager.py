import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"))

db = client["video_manager_db"]
video_collection = db["videos"]

def list_all_videos():
    videos = video_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Video Manager | choose an option ")
        print("1. List All videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit from application")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to be update: ")
            name = input("Enter the video name to be update: ")
            time = input("Enter the video time to be update: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to be deleted: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
