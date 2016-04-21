#coding=utf-8
import gpxpy
import gpxpy.gpx
import copy
#调用函数计算将经纬度表示的两点间的距离
from geopy.distance import vincenty
gpx_file=open('CAStd_116.gpx','r+')
gpx=gpxpy.parse(gpx_file)

gpxpylist1 = list() #全局，存一条数据中的所有的两点之间的距离
gpxpylist11 = list() #全局，存每段trkseg中的两点距离和，单位数据：一段trkseg中距离总和
gpxpylist12 = list() #全局，存每段trkseg的trkpt的个数，单位数据：一段trkseg中trkpt的个数
gpxpylist13 = list() #全局，存平均值，即每段的距离总和/每段trkpt的个数
gpxpylist14 = list() #全局，存每段segment中不符合临界距离的点的个数
gpxpylist2 = list() #全局，存每条trkseg中不合格数据的下标

#记录量
op={}
num_trk=0
num_seg=0
num_p=0
trknumber=0 #统计轨迹条数
point_list=list()
for track in gpx.tracks:
    trknumber+=1
    trksegnumber=0 #统计每条轨迹的segment数量
    trkptnumber=0
    for segment in track.segments:
        trksegnumber+=1
        pre_point=None
        gpxpylist3 = list()  #局部变量，存每段trkseg的两点间的距离值
        for i, point in enumerate(segment.points):
            #if i < len(segment.points):
            newport_ri = (point.latitude, point.longitude)
                #cleveland_oh = ((segment.points[i + 1]).latitude, (segment.points[i + 1]).longitude)
            trkptnumber+= 1 #trkpt的总和
                #print(vincenty(newport_ri,cleveland_oh).meters)
                #gpxpylist1.append(vincenty(newport_ri, cleveland_oh).meters)
                #gpxpylist3.append(vincenty(newport_ri, cleveland_oh).meters) #每段trkseg
            if pre_point:
                gpxpylist3.append(vincenty(pre_point,newport_ri).meters)
                gpxpylist1.append(vincenty(pre_point,newport_ri).meters)

            pre_point = newport_ri
        pre_point=None

        sum=0 #局部，求局部总合，且下一次for循环时被覆盖
        pointnumber=0 #局部，求每段trkseg中的trkpt的个数，且下一次for循环时被覆盖
        for i1 in gpxpylist3:
            sum += i1
            pointnumber+=1
        avg0=sum/pointnumber  #局部变量，每段trkseg的总和/每段trkseg的个数，得到局部均值，且下一次for循环时被覆盖
        avg=3*avg0
        gpxpyAvg = avg
        #gpxpylist5=list()
        #gpxpylist5.append(avg) #将临界点距离avg数据转成list类型，存入list中，方便之后与距离进行比较。

        gpxpylist11.append(sum)
        gpxpylist12.append(pointnumber)
        gpxpylist13.append(avg)

        print(pointnumber)
        print(sum)
        print(avg)

        print("以下为测试")
        #存储一个seg中的多个断点

        for i1, point1 in enumerate(segment.points):#i1从0开始
            #if (i1 + 1) != len(segment.points):
            newport_ri1 = (point1.latitude, point1.longitude)
            #cleveland_oh1 = ((segment.points[i1 + 1]).latitude, (segment.points[i1 + 1]).longitude)

            gpxpyMeter = 0
            #gpxpylist4 = list()
            if pre_point:
                gpxpyMeter=vincenty(pre_point,newport_ri1).meters
            #    gpxpylist4.append(vincenty(pre_point,newport_ri1).meters)
                #gpxpylist4.append(vincenty(newport_ri1, cleveland_oh1).meters) #将数据存入list中，成为list类型
            pre_point = newport_ri1
            n1=0
            #比较avg与距离的大小
            if gpxpyMeter > gpxpyAvg:
                print ("两点之间的距离值为：")
                print(gpxpyMeter)
                #print(gpxpylist4)
                gpxpylist2.append(i1) #存入数据大的那个值的下标
                print('i1:%d'%i1)
                n1+=1
                print('num_trk:%d,num_seg:%d,num_p:%d'%(num_trk,num_seg,num_p))
                point_list.append(num_p-2)
                gpxpylist14.append(n1) #记录每段segment有几个不符合条件的点
            #else:
            #    break
            num_p+=1
        print('p_list' % point_list)
        if len(point_list)>0:
            op[num_trk] = {num_seg: copy.copy(point_list)}
        point_list=[]
        num_seg+=1
        num_p=0
    num_trk+=1
    num_seg=0
print('list2:',gpxpylist2)
print('list14:',gpxpylist14)
print('op:',op)


gpx_file1=open('CCADST.gpx', "w") #打开文件，进行写操作
gpx1=gpxpy.gpx.GPX()  #变量gpx1为GPX类型
#创建第一个trk
gpx1_track=gpxpy.gpx.GPXTrack() #变量gpx1_track为GPXTrack类型
gpx1.tracks.append(gpx1_track) #在gpx1的tracks中添加gpx1_track即轨迹数据
#第一个trk中第一个segment
gpx1_segment=gpxpy.gpx.GPXTrackSegment() #变量gpx1_segment为GPXTrackSegment类型
gpx1_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234,5.1234,elevation=1234))#在轨迹段中直接添加点数据，经纬度和高程

trk_time=0
seg_time=0
gpx1_new_segments=[]
flag =False
#表示第0个trk的第0个seg怎么分，1:{0:}同理
#for i in range(len(gpxpylist2)):
#    op[i]={0:gpxpylist2[i]}

def splite_seg(start,end,segment):
    new_segment=gpxpy.gpx.GPXTrackSegment()
    gpx1_new_segments.append(gpxpy.gpx.GPXTrackSegment())
    for i in range(start,end):
        print('i=%d' % i)
        gpx1_new_segments[0].points.append(segment.points[i])
    gpx1_track.segments.append(gpx1_new_segments.pop())

for track in gpx.tracks:
    for segment in track.segments:
        #for i,point in segment.points:
        # pt=gpxpy.gpx.GPXTrackPoint(segment.points[i])
        # 在轨迹段中直接添加点数据，经纬度和高程
        #print部分用于测试


        if trk_time in op:
           if seg_time in op[trk_time]:
                 flag = True


        if flag:
            print('trk_time:%d,seg_time:%d' %
                  (trk_time, seg_time))
            j=0
            for i in op[trk_time][seg_time]:
                #分。。。。。。。。。。。。。。。。。。。。。。
                splite_seg(j,i,segment)
                j=i+1
            #分。。。。。。。。。。。。。。。。。。。。。最后一截
            splite_seg(j,len(segment.points),segment)
        flag=False
    seg_time=0
    trk_time+=1


gpx_file1.write(gpx1.to_xml()) #写入gpx1到文件中

