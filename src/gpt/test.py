from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
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
        subtitle_y_position = video_height / 4

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips

def main():
    clip1 = VideoFileClip('video_out_subtitled.mp4')
    width, height_final = clip1.size
    ffmpeg_extract_subclip('../videos/sunset.mp4', 0.0, clip1.duration, targetname="passvideo.mp4")
    audio_background = AudioFileClip('music.mp3')
    audio_background = audio_background.volumex(0.3)
    clip2 = VideoFileClip("passvideo.mp4")
    width2, height2 = clip2.size
    clip3 = clip2.resize(width=width)
    final_audio = CompositeAudioClip([clip1.audio, audio_background])
    fc = clip1.set_audio(final_audio)
    fc2 = clip3.without_audio()
    final_clip = clips_array([[fc], [fc2]])
    finalresize = final_clip.resize(height=height_final)
    finalresize.write_videofile('output.mp4')

if __name__ == "__main__":
    main()