from models import GetEps,CorePoint
from collections import deque
from geopy.distance import vincenty
from copy import copy



def getCore_Points(eps,segment):
    #存放core_points
    core_points = deque([])
    i_next = 0
    for i, p in enumerate(segment.points):
        # i_next用于循环的跳转，如果找到core，则需要跳过neighbors
        # 在找到core的时候，设置新值
        if i > i_next:
            neighbors, i_left, i_right = getNeighbrs(i, eps, segment)
            print('i_right', i_right)
            # 判断neighbors是否为空
            if neighbors:
                # 如果是core point,如果是，加入list
                if isCorePoint(neighbors, p):
                    i_next = i + i_right
                    # 新建一个CorePoint对象，将其存储在core_points中
                    core_point = CorePoint(i, (i_left, i_right))
                    core_points.append(core_point)
    return core_points


#求出Density-connected的core_point集合
def get_Density_Core(core_points):
    #这个deque的元素是list，每个list中存着Density-connected的core_points
    density_cores = deque([])
    points=[]
    while core_points:
        pre = core_points.popleft()
        points.append(pre)
        if core_points:
            next = core_points.popleft()
            if next.isNeighbor(pre.index):
                points.append(next)
            else:density_cores.append(copy(points))
    return density_cores


#获取该segment的Eps，
def get_Eps(segment):
    geteps = GetEps(segment)
    return geteps.getEpsFunc()


#获取neighbors:一个point组成的list
def getNeighbrs(i,eps,segment):
    dis = 0
    pre = None
    neighbors = deque([])
    #向前查找
    i_left=0
    for point in segment.points[i::-1]:
        i_left+=1
        if (pre):
            dis += vincenty((pre.latitude, pre.longitude),
                            (point.latitude, point.longitude)).meters
            neighbors.appendleft(point)

            if dis > eps:
                i_left+=-1
                neighbors.popleft()
                break
        pre = point
    #向后查找
    pre = None
    dis=0.0
    i_last=0
    for point in segment.points[i::1]:
        i_last+=1
        if (pre):
            dis += vincenty((pre.latitude,pre.longitude),
                            (point.latitude,point.longitude)).meters
            neighbors.append(point)
            if dis > eps:
                i_last+=-1
                neighbors.pop()
                break
        pre = point
    return (neighbors,i_left,i_last)

#判断是否为core point
def isCorePoint(neighbors,p):
    first = neighbors.popleft()
    if neighbors:
        last = neighbors.pop()
    else:
        last = p
    delta_time = abs((last.time - first.time).total_seconds())
    print('delta_time:', delta_time)
    if delta_time > 13:
        return True
    else:return False
