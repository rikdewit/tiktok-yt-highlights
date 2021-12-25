from tiktok import download_trending
from video import edit_videos
from youtube import upload_video


if __name__ == "__main__":
    vids = download_trending(10)
    edited = edit_videos(vids)
    upload_video(edited)


