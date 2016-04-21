import gpxpy
import gpxpy.gpx
import copy
from geopy.distance import vincenty


gpx_file=open('CAStd_2.gpx','r+')
gpx=gpxpy.parse(gpx_file)

gpx_file1=open('CCADST.gpx', "w") #打开文件，进行写操作
out=gpxpy.gpx.GPX()

#平均距离
#avg_dis = 0
avg_dic = {}
i_trk=0
for track in gpx.tracks:
    i_trk+=1
    i_seg=0
    avg_dic[i_trk] = {}
    for segment in track.segments:
        i_seg+=1
        pre_point=None
        i_p=0
        '''if type(segment.points) == list:
            print('points is a list')
        else:print('not a list')
        print('type of seg:',type(segment))
        '''
        # 记录量：总距离
        total_dis = 0
        for point in segment.points:
            i_p+=1
            if pre_point:
                newport_ri = (point.latitude, point.longitude)
                distance = vincenty(pre_point,newport_ri).meters
                total_dis += distance
            pre_point = (point.latitude,point.longitude)
        #记录每个seg的平均值的三倍
        if i_p != 0:
            dic = {i_seg:(total_dis/i_p)*3}
            avg_dic[i_trk].update(dic)
        else:avg_dic[i_trk]={i_seg:-1}
        print()

print(avg_dic)
#分割
'''def splite(trk,seg,avg):
    pre_point =None
    i_p=0
    new_seg=None
    for point in seg.points:
        if pre_point:
            if vincenty(pre_point,pre_point).meters > avg:
                new_seg =splite_seg(index=i_p,seg=seg,trk=trk)
                break

    if new_seg:
        splite(trk,new_seg,avg)
'''
#具体分割细节

'''def splite_seg(index, seg, trk):
    new_segment = gpxpy.gpx.GPXTrackSegment()

    for i in range(index):
        #print('i=%d' % i)
        new_segment.points.append(seg.points[i])

    trk.segments.append(copy.copy(new_segment))
    new_segment.points=[]

    for i in range(index+1,len(seg.points)):
        new_segment.points.append(seg.points[i])
    trk.segments.append(new_segment)

    seg=[]
    return new_segment
'''

def splite_seg(start,end,seg,out_trk):
    new_segment=gpxpy.gpx.GPXTrackSegment()
    for i in range(start,end):
        new_segment.points.append(seg.points[i])
    out_trk.segments.append(new_segment)

#找出所有断点
def find_long_seg(avg,seg):
    p_list=[]
    pre_point =None
    i_p=0
    for point in seg.points:
        i_p+=1
        if pre_point:
            newport_ri = (point.latitude,point.longitude)
            distance = vincenty(pre_point,newport_ri).meters
            if vincenty(distance > avg):
                p_list.append(i_p-1)
        pre_point = (point.latitude,point.longitude)
    return p_list

#传入一个断点数组，根据断点分割
def splite_all(p_list, seg, out_trk):
    start=0
    for i in p_list:
        splite_seg(start=start, end=i, seg=seg, out_trk=out_trk)
        start = i

    splite_seg(start=start, end=len(seg.points), seg=seg, out_trk=out_trk)

'''def splite(out_trk,seg,avg):
    splite_all(find_long_seg(avg=avg,seg=seg),seg=seg,trk=out_trk)
'''
i_trk=0
for track in gpx.tracks:
    out_track = gpxpy.gpx.GPXTrack()
    i_trk+=1
    i_seg=0
    for segment in track.segments:
        i_seg+=1
        avg = avg_dic[i_trk][i_seg]
        if avg>0:
            splite_all(find_long_seg(avg=avg, seg=segment), seg=segment, out_trk=out_track)

    out.tracks.append(out_track)
    print()

gpx_file1.write(out.to_xml())


            #start = 0
            #end = 0
            #if pre_point:
            #   distance = vincenty(pre_point, point).meters
            #    if distance > avg_dic[i_trk][i_seg]:
            #        splite_seg(start=start, end=i_p, seg=segment, trk=track)
            #pre_point=point














