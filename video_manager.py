# import json

import sqlite3
con = sqlite3.connect("data.bd")
cursor = con.cursor()

cursor.execute('''
    create table IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )                      
''')

# def load_data():
#     try:
#         with open('data.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []

# def save_data_helper(videos):
    # with open('data.txt', 'w') as file:
    #     json.dump(videos, file)
        
def list_all_videos():
    cursor.execute("Select * from videos")
    rows = cursor.fetchall()
    
    print("\n")
    print("*" * 30)
    
    if not rows:
        print("No videos available")
    else:
        for row in rows:
            print(row)
    
    # for row in cursor.fetchall():
    #     print(row)
    print("\n")
    print("*" * 30)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()    
    print(f"Video '{name}' add successfully")
 
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()
    print(f"updated successfully")
    

def delete_video(video_id):
    cursor.execute("DELETE from videos where id = ?", (video_id,))
    con.commit()
    print(f"deleted successfully")


def main():
    # videos = load_data()
    while True:
        print("\n Video Manager with DB | choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit app")
        
        choice = input("Enter your choice: ")
        # print(videos)
        
        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video id to Delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
    
    con.close()
        
        # match choice:
            # case '1':
            #     list_all_videos(videos)
            # case '2':
            #     add_video(videos)
            # case '3':
            #     update_video(videos)
            # case '4':
            #     delete_video(videos)
            # case '5':
            #     break
            # case _:
            #     print("Invalid choice")
        
                
if __name__ == "__main__":
    main()
        