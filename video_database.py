from tinydb import TinyDB, Query

def add_videos_to_used(videos):
    db = TinyDB("used_videos.json")
    for video in videos:
        db.insert({"video_id":video["id"]})

def is_used(video_id):
    db = TinyDB("used_videos.json")
    query = Query()
    
    return db.contains(query.video_id == video_id)
        

if __name__ == "__main__":
    # db = TinyDB("used_videos.json")
    # query = Query()
    print(not is_used("7016303498082012421"))