#coding=utf-8
#第三步处理数据，算出trk中每段segment的Eps值，存入数组。
import gpxpy
import gpxpy.gpx
import math
from geopy.distance import vincenty

#gpx_file=open('data\\CAStd_p13.gpx', "r+") #打开文件，进行写操作
#gpx=gpxpy.parse(gpx_file)
class GetEps():
    def __init__(self,segment):
        self.segment=segment
        self.funCMemo = []  # 将算出的sum一一存入
        self.funCMemoFlag = []  # 判断是否值是否为1，是则取funCMemo[k]的值使用
        self.count = 0  # 计数器

    def funC(self,k):  # 求Ck
        if k != 0:
            sum = 0
            if self.funCMemoFlag[k] == 1:  # 嵌套中，值为1则直接读取之前算出来的数
                return self.funCMemo[k]
            #global count  # 全局变量
            #count = count + 1
            for i in range(k):
                sum += (self.funC(i) * self.funC(k - 1 - i)) / ((i + 1) * (2 * i + 1))
            self.funCMemoFlag[k] = 1
            self.funCMemo[k] = sum  # 将funC(k)的值一一存入
            return sum
        else:
            return 1.0

    def funE(self,n, k):  # 求erf的反函数，其中调用funC(k)函数
        sum = 0.0
        for i in range(k):
            sum += self.funC(i) * (math.pow((math.sqrt(math.pi) * n / 2), (2 * i + 1))) / (2 * i + 1)
        return sum

    def getEpsFunc(self):
        pre_point = None
        i_p = 0  # 点的量
        i_dis = -1  # distance的量
        total_dis = 0  # 记录量：总距离
        dis_list = list()  # 放入distance
        # 第一次循环计算出avg
        for point in self.segment.points:
            i_p += 1
            i_dis += 1
            if pre_point:
                newport_ri = (point.latitude, point.longitude)
                distance = vincenty(pre_point, newport_ri).meters  # 所有的距离包括0都记录下来了
                dis_list.append(distance)
                total_dis += distance
            pre_point = (point.latitude, point.longitude)

        if i_p > 2:  # segment中点的数量大于1个
            avg_value = total_dis / i_dis
            print(total_dis, i_dis, avg_value)
            variance = 0.0  # 方差
            for i1 in dis_list:
                variance += math.pow(abs(avg_value - i1), 2)  # 方差
            st_de_value = math.sqrt(variance)  # 标准差
            # print ("方差和标准差是：{0}，{1}").format(variance,st_de_value)
            # 调用功能函数
            erf = 0
            for i in range(128):
                self.funCMemo.append(0)
                self.funCMemoFlag.append(0)
            p_value = 0.6  # p值
            k_value = 100  # k值
            n_num = float(p_value) * 2 - 1  # 求2p-1
            erf = self.funE(n_num, int(k_value))
            Eps = float(avg_value) + math.sqrt(2) * float(st_de_value) * erf  # 求Eps
        else:
            Eps = 0
        return Eps


'''
#计算平均值和标准差
avg_list = list()
eps_list=list()
i_trk=0
i_segpt=0 #只有一个点的segment个数
for track in gpx.tracks:
    i_trk+=1
    i_seg=0
    for segment in track.segments:
        i_seg+=1
        pre_point=None
        i_p=0  #点的量
        i_dis=-1  #distance的量
        total_dis = 0  #记录量：总距离
        dis_list=list() #放入distance
        #第一次循环计算出avg
        for point in segment.points:
            i_p+=1
            i_dis+=1
            if pre_point:
                newport_ri = (point.latitude, point.longitude)
                distance = vincenty(pre_point,newport_ri).meters #所有的距离包括0都记录下来了
                dis_list.append(distance)
                total_dis += distance
            pre_point = (point.latitude,point.longitude)
        if i_p==1: #segment中点的数量是1个
             i_segpt+=1
        elif i_p>1: #segment中点的数量大于1个
            avg_value = total_dis/i_dis
            print(total_dis,i_dis,avg_value)
            variance=0.0 #方差
            for i1 in dis_list:
                variance+=math.pow(abs(avg_value-i1),2) #方差
            st_de_value=math.sqrt(variance) #标准差
            #print ("方差和标准差是：{0}，{1}").format(variance,st_de_value)
            #调用功能函数
            erf=0
            for i in range(128):
                funCMemo.append(0)
                funCMemoFlag.append(0)
            p_value=0.6 #p值
            k_value=100 #k值
            n_num=float(p_value)*2-1  #求2p-1
            erf=funE(n_num,int(k_value))
            Eps=float(avg_value)+math.sqrt(2)*float(st_de_value)*erf #求Eps
            eps_list.append(Eps) #将每个segment的Eps存入该list中

        i2=0
        print("distance的个数为：")
        print(i_dis)
        print ("distance为：")
        for i2,distance in enumerate(dis_list):
            print(i2,distance)
            #print(dis_list[i2])
            if dis_list[i2]!=0:
                if dis_list[i2]>=Eps:
                    print("第i2个点后一段距离就已经满足大于Eps的条件")
                #elif (dis_list[i2]+dis_list[i2+1])>=Eps:
                 #    print("第i2个点后两段距离就已经满足大于Eps的条件")
                else:
                    continue
            else:
                continue



print (i_segpt)
'''




























