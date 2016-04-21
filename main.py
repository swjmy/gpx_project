import gpxpy
import gpxpy.gpx
from tools_Function import get_Eps,get_Density_Core,getCore_Points
from models import CorePoint,ConnectedDensity


gpx_file=open('data\\CAStd_p11_out.gpx','r+')
gpx=gpxpy.parse(gpx_file)
gpx_file.close()



for track in gpx.tracks:
    for segment in track.segments:
        CorePoint.currentSegment=segment
        print('points :%d'%len(segment.points))
        eps = get_Eps(segment)
        print('eps:%f'%eps)
        if eps:
            #如果eps有效，则算出该segment的corepoints
            #core_points是一个deque
            core_points = getCore_Points(eps,segment)
            #根据算出的core_points创建一个ConnectedDensity对象
            density = ConnectedDensity(get_Density_Core(core_points))
            print('length of density:',len(density.density_cores))







