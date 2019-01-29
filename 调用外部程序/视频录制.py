# coding = utf8
import os
import time
print(time.localtime())
print(time.strftime('%Y%m%d_%H:%M:%S', time.localtime()))
outputfile = 'd:\\' + time.strftime('%Y%m%d_%H:%M:%S', time.localtime()) + '.mp4'
ffmpeg = 'd:\\data\\ffmpeg.exe'                # 外部应用录屏工具没有下载
setting1 = '-y -rtbufsize 100M -f gdigrab -framerate 10'
setting2 = '-offset_x 1000 -offset_y 0 -video_size 640x480'
setting3 = '-draw_mouse 1 -i desktop -c:v libx264'
setting4 = '-r 20 -present medium -tune zerolatency -crf 35'
setting5 = '-pix_fmt yuv420p -fs 100M -movflags +faststart "%s"' % outputfile

recordingCmdLine = ' '.join([ffmpeg]+[setting1]+[setting2]+[setting3]+[setting4]+[setting5])
print(recordingCmdLine)
os.system(recordingCmdLine)






