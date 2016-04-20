import gpxpy
import gpxpy.gpx
from geopy.distance import vincenty
from getEps import GetEps

gpx_file=open('data\\CAStd_p11_out.gpx','r+')
gpx=gpxpy.parse(gpx_file)
gpx_file.close()

#获取该segment的Eps，
def get_Eps(segment):
    geteps = GetEps(segment)
    return geteps.getEpsFunc()


#获取neighbors:一个point组成的list
def getNeighbrs(i,eps,segment):
    dis = 0
    pre = None
    neighbors = []
    #向前查找
    for point in segment.points[i::-1]:
        if (pre):
            dis += vincenty((pre.latitude, pre.longitude),
                            (point.latitude, point.longitude)).meters
            if dis > eps:
                neighbors.append(pre)
                break
            neighbors.append(pre)
        pre = point
    #向后查找
    pre = None
    dis=0.0
    for point in segment.points[i::1]:
        if (pre):
            dis += vincenty((pre.latitude,pre.longitude),
                            (point.latitude,point.longitude)).meters
            if dis > eps:
                neighbors.append(pre)
                break
            neighbors.append(pre)
        pre = point
    return neighbors




for track in gpx.tracks:
    for segment in track.segments:
        print('points :%d'%len(segment.points))
        eps = get_Eps(segment)
        print('eps:%f'%eps)
        for i,p in enumerate(segment.points):
            neighbors = getNeighbrs(i,eps,segment)
            if neighbors:
                print('neighors %d: %d' % (i, len(neighbors)))
                first = neighbors[0]
                last = neighbors[len(neighbors)-1]
                max_dis = vincenty((first.latitude, first.longitude),
                                   (last.latitude, last.longitude)).meters
                print('max dis:%f'%max_dis)



