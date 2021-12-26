from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os
from pathlib import Path
from moviepy.editor import *
import glob


def clear_old():
    files = glob.glob('./thumbs/*')

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def get_thumbnails():
    clear_old()
    path = "./vids/"
    vid_paths = sorted(Path(path).iterdir(), key=os.path.getmtime)

    first = str(vid_paths[0])
    second = str(vid_paths[len(vid_paths)//2])
    third = str(vid_paths[-1])

    for i, path in enumerate((first, second, third)):
        clip = VideoFileClip(path)
        image = clip.save_frame(f"./thumbs/{str(i+1)}.png", clip.duration/2)

def resize(im):
    resized = im.resize((1280//3, 720), resample=Image.BICUBIC)
    return resized

def add_episode_number(img, number):
    base = img.convert("RGBA")
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (0,0,0,0))

    # get a font
    fnt = ImageFont.truetype("./fonts/Montserrat-BoldItalic.ttf", 110)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((845, 240), f"#{number}", font=fnt, fill=(29,240,235,255))


    d.text((853, 240), f"#{number}", font=fnt, fill=(10,10,10,255))


    out = Image.alpha_composite(base, txt)

    return out


def make_thumbnail(path="thumbnail.png", episode_number = 10):
    get_thumbnails()

    im1 = resize(Image.open('./thumbs/1.png'))
    im2 = resize(Image.open('./thumbs/2.png'))
    im3 = resize(Image.open('./thumbs/3.png'))

    overlay = Image.open("./imgs/Tiktok thumbnail.png")

    final = Image.new('RGB', (1280, 720))
    final.paste(im1, (0,0))
    final.paste(im2, (im1.width, 0))
    final.paste(im3, (im1.width+im2.width , 0))
    final = final.filter(ImageFilter.GaussianBlur(2))
    final.paste(overlay, (100, 0), overlay)
    final = add_episode_number(final, episode_number)
    final.save(path)
    return final



if __name__ == "__main__":
    make_thumbnail().show()
    


