import pvleopard
import ffmpeg
import os
import pysrt
import moviepy.video.fx.all as vfx

from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from typing import Sequence, Optional
from dotenv import load_dotenv

# Load access jey fir pvleopard
load_dotenv()
access_key = os.getenv("ACCESS_KEY")


def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


def create_subtitle_clips(subtitles, videosize,fontsize=60, font='Novecento Sans', color='white', debug = False):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, stroke_width=1, stroke_color="black", size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height / 3

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips



def second_to_timecode(x: float) -> str:
    hour, x = divmod(x, 3600)
    minute, x = divmod(x, 60)
    second, x = divmod(x, 1)
    millisecond = int(x * 1000.)


    return '%.2d:%.2d:%.2d,%.3d' % (hour, minute, second, millisecond)


def to_srt(
        words: Sequence[pvleopard.Leopard.Word],
        endpoint_sec: float = 1.,
        length_limit: Optional[int] = 1) -> str:
    def _helper(end: int) -> None:
        lines.append("%d" % section)
        lines.append(
            "%s --> %s" %
            (
                second_to_timecode(words[start].start_sec),
                second_to_timecode(words[end].end_sec)
            )
        )
        lines.append(' '.join(x.word for x in words[start:(end + 1)]))
        lines.append('')


    lines = list()
    section = 0
    start = 0
    for k in range(1, len(words)):
        if ((words[k].start_sec - words[k - 1].end_sec) >= endpoint_sec) or \
                (length_limit is not None and (k - start) >= length_limit):
            _helper(k - 1)
            start = k
            section += 1
    _helper(len(words) - 1)


    return '\n'.join(lines)





def main():
    video_path = '../videos/video.mp4'
    audio_path = 'audio.wav'
    mp4filename = "video_out.mp4" 

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    leopard = pvleopard.create(access_key=access_key)
    transcript, words = leopard.process_file('audio.wav')
    with open('sub.srt', 'w') as f:
        f.write(to_srt(words))
    
    video = VideoFileClip('../videos/video.mp4')
    subtitles = pysrt.open('sub.srt')

    begin,end= mp4filename.split(".mp4")
    output_video_file = begin+'_subtitled'+".mp4"

    print ("Output file name: ",output_video_file)

    # Create subtitle clips
    subtitle_clips = create_subtitle_clips(subtitles,video.size)

    # Add subtitles to the video
    final_video = CompositeVideoClip([video] + subtitle_clips)

    # Write output video file
    final_video.write_videofile(output_video_file)
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