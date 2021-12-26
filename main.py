import argparse
from tiktok import download_trending
from video import edit_videos
from youtube import upload_video

import json


def get_episode_number():
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

    return episode

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--videos', help='number of videos to download and compile', default='30')
    args = vars(parser.parse_args())
    num_vids = int(args["videos"])
    vids = download_trending(num_vids)
    edited = edit_videos(vids)

    title = "Tiktok Trending NL #" + str(get_episode_number())
    description = "Wat is er deze week op tiktok gebeurd?"

    upload_video(edited, title=title, privacy_status="public", description=description)


