#coding=utf-8
import gpxpy
import gpxpy.gpx
from geopy.distance import vincenty

gpx_file=open('CAStd_p11.gpx','r+')
gpx=gpxpy.parse(gpx_file)

gpx_file1=open('CAStd_p11_out.gpx', "w") #打开文件，进行写操作
gpx1=gpxpy.gpx.GPX()  #变量gpx1为GPX类型

i_trk=0
i_nt=0
new_trk=gpxpy.gpx.GPXTrack()
for track in gpx.tracks:
    i_trk+=1
    i_seg=0
    for segment in track.segments:
        i_seg+=1
        i_p=0
        new_seg=gpxpy.gpx.GPXTrackSegment()
        for point in segment.points:
            i_p+=1
            if point.time!=None:
                new_seg.points.append(point)
            else:
                i_nt+=1
                break
        if new_seg.points:
            new_trk.segments.append(new_seg)
        else:
            break
    gpx1.tracks.append(new_trk)
print(i_nt)
gpx_file1.write(gpx1.to_xml())

