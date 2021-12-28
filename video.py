from moviepy.editor import *

def edit_videos(vid_paths, outputfile="out.mp4", endscreen_path=None):

    clips = []
    audios = []
    for vid in vid_paths:
        clip = VideoFileClip(vid).resize((540, 960))
        audio = AudioFileClip(vid)

        clips.append(clip)
        audios.append(audio)

    if(endscreen_path):
        endscreen = VideoFileClip(endscreen_path).resize((540,960))
        endscreen_audio = AudioFileClip(endscreen_path)
        clips.append(endscreen)
        audios.append(endscreen_audio)

    joined_audio = concatenate_audioclips(audios)
    joined_clips = concatenate_videoclips(clips)
    video = CompositeVideoClip([joined_clips])
    video.set_audio(joined_audio)

    video.write_videofile(outputfile, fps=30, ffmpeg_params=["-nostdin"])

    return outputfile
