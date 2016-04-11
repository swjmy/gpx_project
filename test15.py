import gpxpy
import gpxpy.gpx
from geopy.distance import vincenty


gpx_file=open('CAStd_116.gpx','r+')
gpx=gpxpy.parse(gpx_file)

gpx_file1=open('CCADST.gpx', "w") #打开文件，进行写操作
out=gpxpy.gpx.GPX()



#分割
def splite(start,avg,seg,new_trk):
    i_p=0
    pre_point=None
    new_seg=gpxpy.gpx.GPXTrackSegment()

    for point in seg.points[start:]:
        i_p+=1
        if pre_point:
            newport_ri=(point.latitude,point.longitude)
            distance=vincenty(pre_point,newport_ri).meters
            if distance>avg:
                #递归
                splite(start=start+i_p,avg=avg,seg=seg,new_trk=new_trk)
                break
            else:new_seg.points.append(seg.points[i_p+start-1])
        else:new_seg.points.append(seg.points[i_p+start-1])
        pre_point=(point.latitude,point.longitude)
    new_trk.segments.append(new_seg)


#计算平均值的三倍
avg_list = []
i_trk=0
for track in gpx.tracks:
    i_trk+=1
    i_seg=0
    new_trk=gpxpy.gpx.GPXTrack()

    for segment in track.segments:
        i_seg+=1
        pre_point=None
        i_p=0
        # 记录量：总距离
        total_dis = 0
        #第一次循环计算出avg*3
        for point in segment.points:
            i_p+=1
            if pre_point:
                newport_ri = (point.latitude, point.longitude)
                distance = vincenty(pre_point,newport_ri).meters
                total_dis += distance
            pre_point = (point.latitude,point.longitude)

        if i_p!=0:
            avg = (total_dis/i_p)*3
        else:avg = float('inf')
        #分割
        splite(start=0,avg=avg,seg=segment,new_trk=new_trk)
    out.tracks.append(new_trk)


gpx_file1.write(out.to_xml())
#print(avg_list)