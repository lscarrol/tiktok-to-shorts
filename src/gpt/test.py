from moviepy.editor import *
import moviepy.video.fx.all as vfx
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import ffmpeg
import pvleopard
from typing import Sequence, Optional
import pysrt

def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000

def create_subtitle_clips(subtitles, videosize,fontsize=60, font='AvantGarde-Demi', color='white', debug = False):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(subtitle.text.upper(), fontsize=fontsize, font=font, color=color, stroke_width=1, stroke_color="black", size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height * 4 / 5

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips

def main():
    clip1 = VideoFileClip('video_out_subtitled.mp4')
    width, height_final = clip1.size
    ffmpeg_extract_subclip('../videos/sunset.mp4', 0.0, clip1.duration, targetname="passvideo.mp4")
    audio_background = AudioFileClip('music.mp3')
    clip1 = clip1.fx(vfx.crop, x1=0, y1=0, x2=1080, y2=1080)
    #crop(clip1, x1=0, y1=0, x2=1080, y2=1080)
    audio_background = audio_background.volumex(0.3)
    clip2 = VideoFileClip("passvideo.mp4")
    width2, height2 = clip2.size
    # clip3 = clip2.resize(width=width)
    #crop(clip3, x1=0, y1=0, x2=1080, y2=1080)
    clip2 = clip2.fx(vfx.crop, x1=0, y1=0, x2=1080, y2=840)
    final_audio = CompositeAudioClip([clip1.audio, audio_background])
    fc = clip1.set_audio(final_audio)
    fc2 = clip2.without_audio()
    
    
    final_clip = clips_array([[fc], [fc2]])
    #finalresize = final_clip.resize(height=height_final)
    print(final_clip.size)
    final_clip.write_videofile('output.mp4')

if __name__ == "__main__":
    main()