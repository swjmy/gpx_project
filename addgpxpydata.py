# coding=utf-8
#创建gpx文件
import gpxpy
import gpxpy.gpx

gpx_file=open('gpxpy1.gpx', "w") #打开文件，进行写操作
gpx1=gpxpy.gpx.GPX()  #变量gpx1为GPX类型
#创建第一个trk
gpx1_track=gpxpy.gpx.GPXTrack() #变量gpx1_track为GPXTrack类型
gpx1.tracks.append(gpx1_track) #在gpx1的tracks中添加gpx1_track即轨迹数据
#第一个trk中第一个segment
gpx1_segment=gpxpy.gpx.GPXTrackSegment() #变量gpx1_segment为GPXTrackSegment类型
gpx1_track.segments.append(gpx1_segment) #在gpx1_track的segments中添加gpx1_segment即轨迹段
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234,5.1234,elevation=1234))#在轨迹段中直接添加点数据，经纬度和高程
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235,5.1235,elevation=1235))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236,5.1236,elevation=1236))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1237,5.1237,elevation=1237))
#第一个trk中第二个segment
gpx1_segment=gpxpy.gpx.GPXTrackSegment()
gpx1_track.segments.append(gpx1_segment)
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1238,5.1238,elevation=1238))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1239,5.1239,elevation=1239))


#创建第二个trk
gpx1_track=gpxpy.gpx.GPXTrack() #变量gpx1_track为GPXTrack类型
gpx1.tracks.append(gpx1_track) #在gpx1的tracks中添加gpx1_track即轨迹数据
#第二个trk中第一个segment
gpx1_segment=gpxpy.gpx.GPXTrackSegment() #变量gpx1_segment为GPXTrackSegment类型
gpx1_track.segments.append(gpx1_segment) #在gpx1_track的segments中添加gpx1_segment即轨迹段
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.12,5.134,elevation=1234))#在轨迹段中直接添加点数据，经纬度和高程
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.35,5.135,elevation=125))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.136,5.126,elevation=126))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.127,5.127,elevation=127))
#第二个trk中第二个segment
gpx1_segment=gpxpy.gpx.GPXTrackSegment()
gpx1_track.segments.append(gpx1_segment)
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.128,5.1238,elevation=138))
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1239,5.139,elevation=1239))


gpxpylist1 = list() #全局
for track in gpx1.tracks:  # 重叠的for循环
     for segment in track.segments:
         for point in segment.points:
              print ('Point at (%f,%f)->%f'%(point.latitude,point.longitude,point.elevation))


print ('Created GPX: to_xml') #转成xml文件，控制台输出
gpx_file.write(gpx1.to_xml()) #写入到文件中







