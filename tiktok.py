from TikTokApi import TikTokApi
import requests
import os
import glob
from video import edit_videos
from video_database import add_videos_to_used, is_used

def download_trending(results = 10):
    clear_vids()
    vids = get_trending_video_data(results)
    filepaths = []
    for vid in vids:
        filepath = "./vids/"+vid["desc"][:30]+"-"+vid["id"]+".mp4"
        filepaths.append(filepath)
        download(vid["url"], filepath)
    
    return [vids, filepaths]


def get_trending_video_data(results=10):

    api = TikTokApi.get_instance()
    trending = api.by_trending(count=int(results*2)+2, custom_verifyFp="", language="en", region="US")

    new_vids = []
    for tiktok in trending:
        print("tik")
        if(not is_used(tiktok["id"])):
            print("new")
            new_vids.append(tiktok)

    if(results > len(new_vids)):
        print(f"Could not find enough new trending video's, returning {len(new_vids)} new videos")

    vids = []
    for tiktok in new_vids[:min(results,len(new_vids))]:
        data = {}
        data["id"] = tiktok['id']
        data["stats"] = tiktok["stats"]
        data["desc"] = tiktok["desc"]
        data["url"] = tiktok["video"]["downloadAddr"]
        print(data["stats"])
        vids.append(data)
    return vids

def download(url, outputfile):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(outputfile, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return outputfile

def clear_vids():
    files = glob.glob('./vids/*')

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

if __name__ == "__main__":
    [vids, filepaths] = download_trending(3)
    # add_videos_to_used(vids)

    edit_videos(filepaths, endscreen_path="imgs/End screen tiktok highlights.mov")