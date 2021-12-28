import argparse
from tiktok import download_trending
from video import edit_videos
from video_database import add_videos_to_used
from youtube import upload_thumbnail, upload_video
from thumbnail import make_thumbnail
import json


def get_episode_number():
    episode = 0
    data = ""
    path = "episode_number.json"
    with open(path, "r+") as f:
        data = json.load(f)
        episode = data["episode_number"]

    return episode

def increment_episode_number():
    episode = 0
    data = ""
    path = "episode_number.json"
    with open(path, "r+") as f:
        data = json.load(f)
        episode = data["episode_number"]
        data["episode_number"] = episode + 1
        
    open(path, "w").close()
    
    with open(path, "r+") as f:
        f.write(json.dumps(data))

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--videos', help='number of videos to download and compile', default='30')
    
    parser.add_argument("--newlogin", help="log in with a new google account", default=False)
    args = vars(parser.parse_args())
    num_vids = int(args["videos"])
    while(num_vids > 100 or num_vids < 4):
        num_vids = int(input("Choose number of videos between 4 and 100: "))
        
    [vids, filepaths] = download_trending(num_vids)
    edited = edit_videos(filepaths, endscreen_path="imgs/End screen tiktok highlights.mov")
    episode_number = get_episode_number()
    title = "Tiktok Trending NL #" + str(get_episode_number())
    description = "Wat is er deze keer weer op tiktok gebeurd? #trending #fyp #tiktok"

    id = upload_video(edited, title=title, privacy_status="public", description=description, newLogin=bool(args["newlogin"]))
    make_thumbnail("thumbnail.png", episode_number )
    upload_thumbnail(id, "thumbnail.png")
    increment_episode_number()
    add_videos_to_used(vids)




