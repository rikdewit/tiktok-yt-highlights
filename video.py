from moviepy.editor import *

def edit_videos(vid_paths, outputfile="out.mp4"):

    clips = []
    audios = []
    for vid in vid_paths:
        clip = VideoFileClip(vid).resize((540, 960))
        audio = AudioFileClip(vid)

        clips.append(clip)
        audios.append(audio)

    joined_audio = concatenate_audioclips(audios)
    joined_clips = concatenate_videoclips(clips)
    video = CompositeVideoClip([joined_clips])
    video.set_audio(joined_audio)

    video.write_videofile(outputfile, fps=30, ffmpeg_params=["-nostdin"])

    return outputfile



# txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
# txt_clip = txt_clip.set_pos('center').set_duration(3)
# video = CompositeVideoClip([joined, txt_clip])









