#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo


def getPolygonBounds(region):
    """
    求外包矩形，即平行于经纬度的最小包容矩形
    :param region: 区域
    :return:外包矩形的四个点坐标集合
    """
    length = len(region)
    top = down = left = right = region[0]
    for i in range(1, length):
        if region[i][1] > top[1]:
            top = region[i]
        elif region[i][1] < down[1]:
            down = region[i]
        else:
            pass
        if region[i][0] > right[0]:
            right = region[i]
        elif region[i][0] < left[0]:
            left = region[i]
    else:
        pass

    point0 = [left[0], top[1]]
    point1 = [right[0], top[1]]
    point2 = [right[0], down[1]]
    point3 = [left[0], down[1]]
    polygonBounds = [point0, point1, point2, point3]
    return polygonBounds


def isPointInRect(point, polygonBounds):
    """
    判断点是否在外包矩形外
    :param point: 需要判断的点坐标
    :param polygonBounds: 外包矩形坐标
    :return:
    """
    if polygonBounds[3][1] <= point[1] <= polygonBounds[0][1] \
            and polygonBounds[3][0] <= point[0] <= polygonBounds[2][0]:
        return True
    else:
        return False


def isPointInPolygon(point, region, way=0):
    """
    采用射线法，计算测试点是否任意一个建筑内
    :param way:方式，0-不含顶点和边，1-含顶点和边，2-含顶点不含边，3-含边不含顶点
    :param point: 点
    :param region: 区域
    :return:
    """
    if way == 0:
        Bound = Vertex = False
    elif way == 1:
        Bound = Vertex = True
    elif way == 2:
        Vertex = True
        Bound = False
    else:
        Vertex = False
        Bound = True
    count = 0
    precision = 2e-10

    # 首先求外包矩形
    polygonBounds = getPolygonBounds(region)

    # 然后判断是否在外包矩形内，如果不在，直接返回false
    if not isPointInRect(point, polygonBounds):
        return False

    length = len(region)
    p = point
    p1 = region[0]

    for i in range(1, length):
        if p[1] == p1[1] and p[0] == p1[0]:
            return Vertex

        p2 = region[i % length]
        if p[1] == p2[1] and p[0] == p2[0]:
            return Vertex

        if p[1] < min(p1[1], p2[1]) or \
                p[1] > max(p1[1], p2[1]) or \
                p[0] > max(p1[0], p2[0]):
            p1 = p2
            continue

        elif min(p1[1], p2[1]) < p[1] < max(p1[1], p2[1]):
            if p1[0] == p2[0]:
                if p[0] == p1[0] and \
                        min(p1[1], p2[1]) < p[1] < max(p1[1], p2[1]):
                    return Bound
                else:
                    count += 1
                    continue

            a = p2[1] - p1[1]
            b = p1[0] - p2[0]
            c = p2[0] * p1[1] - p1[0] * p2[1]
            d = a * p[0] + b * p[1] + c
            if p1[1] < p2[1] and p1[0] > p2[0] or \
                    p1[1] < p2[1] and p1[0] < p2[0]:
                if d < 0:
                    count += 1
                elif d > 0:
                    p1 = p2
                    continue
                elif abs(p[1] - d) < precision:
                    return Bound
            else:
                if d < 0:
                    p1 = p2
                    continue
                elif d > 0:
                    count += 1
                elif abs(p[1] - d) < precision:
                    return Bound
        else:
            if p1[1] == p2[1]:
                if p[1] == p1[1] and \
                        min(p1[0], p2[0]) < p[0] < max(p1[0], p2[0]):
                    return Bound
            else:
                p3 = region[(i + 1) % length]
                if p[1] < min(p1[1], p3[1]) or \
                        p[1] > max(p1[1], p3[1]):
                    count += 2
                else:
                    count += 1
        p1 = p2
    if count % 2 == 0:
        return False
    else:
        return True


def checkPointInRegions(regions, point=None, way=0):
    """
    检查点是否在区域中
    :param point: 被检查的点，当默认不输入时，随机给出一个在区间的经纬点坐标
    :param regions: 区域集合列表
    :param way: 方式，0-不含顶点和边，1-含顶点和边，2-含顶点不含边，3-含边不含顶点
    :return:
    """
    length = len(regions)
    flag = 0
    if point is not None:
        for i in range(len(regions)):
            if isPointInPolygon(point, regions[i], way):
                if length > 1:
                    print("要查询的点在第 %d 个区域内" % (i + 1))
                else:
                    print("要查询的点在区域内")
                return True
            else:
                flag += 1
        if flag == length:
            print("要查询的点不在区域内")
            return False
    else:
        for i in range(len(regions)):
            polygonBounds = getPolygonBounds(regions[i])
            count = 0
            import random
            while True:
                count += 1
                point = [random.uniform(polygonBounds[0][0], polygonBounds[1][0]),
                         random.uniform(polygonBounds[1][1], polygonBounds[2][1])]
                if isPointInPolygon(point, regions[i], way):
                    if length > 1:
                        print("点在第{}个区域内，坐标为：{}".format(i + 1, point))
                    else:
                        print("点在区域内，坐标为：{}".format(point))
                    return point
                if count == 1000:
                    print("1000次都没有随机到一个有效的坐标，你妹，耍我呢")
                    break


"""
regionPointsList = [
    [119.363917, 30.15791],
    [119.400782, 30.143883],
    [119.357995, 30.120351]
]
regions = [regionPointsList]  # 多个区域的集合

# 在内测试点
# point = [119.358995, 30.130351]

# 在顶点测试点
point = [119.357995, 30.120351]
checkPointInRegions(regions, point)

# 返回有效点测试
print(checkPointInRegions(regions))

"""
# region = [[119.959676, 30.159493], [119.960496, 30.124047], [120.016784, 30.125235], [120.051436, 30.118959], [120.05402, 30.116171], [120.050248, 30.107389], [120.050768, 30.09326], [120.05937, 30.09407], [120.081447, 30.080546], [120.087636, 30.079651], [120.100863, 30.081876], [120.113801, 30.098318], [120.128111, 30.107852], [120.149263, 30.108729], [120.171216, 30.103474], [120.181132, 30.111081], [120.127929, 30.154714], [120.128971, 30.192542], [120.13138, 30.194213], [120.132931, 30.195884], [120.137793, 30.204307], [120.148631, 30.21036], [120.144648, 30.226786], [120.141953, 30.231864], [120.136862, 30.241278], [120.150594, 30.243598], [120.147354, 30.255372], [120.147203, 30.257952], [120.157862, 30.261255], [120.156184, 30.266976], [120.155373, 30.26982], [120.155174, 30.270547], [120.154952, 30.271257], [120.154475, 30.272691], [120.154532, 30.272746], [120.154326, 30.274335], [120.154077, 30.275313], [120.153449, 30.276082], [120.15104, 30.278313], [120.150284, 30.279932], [120.149474, 30.281801], [120.148235, 30.283448], [120.14698, 30.28518], [120.146041, 30.286769], [120.145403, 30.288414], [120.144405, 30.290474], [120.143777, 30.291542], [120.143345, 30.291965], [120.142827, 30.292359], [120.141459, 30.293481], [120.140735, 30.294815], [120.136755, 30.292777], [120.124674, 30.294333], [120.106349, 30.293444], [120.111585, 30.2761], [120.100899, 30.275266], [120.101317, 30.27301], [120.101478, 30.27068], [120.090857, 30.269063], [120.090492, 30.271784], [120.089698, 30.274321], [120.085965, 30.280103], [120.064389, 30.280029], [120.059165, 30.279181], [120.053641, 30.278296], [120.05049, 30.278528], [120.052652, 30.282811], [120.054097, 30.28473], [120.055715, 30.286575], [120.048881, 30.286804], [120.051274, 30.29133], [120.053667, 30.295079], [120.048925, 30.295609], [120.037317, 30.295547], [120.025218, 30.300632], [120.01241, 30.298205], [120.012637, 30.300479], [120.005766, 30.310946], [120.005152, 30.325686], [119.97254, 30.324667], [119.970277, 30.331788], [119.946245, 30.311685], [119.936847, 30.302398], [119.935527, 30.29498], [119.93343, 30.292752], [119.930236, 30.290823], [119.921892, 30.268881], [119.916249, 30.26954], [119.911035, 30.268421], [119.905477, 30.254401], [119.902548, 30.250505], [119.902194, 30.245274], [119.914255, 30.23753], [119.91829, 30.234975], [119.948675, 30.227082], [119.965844, 30.191563]]
# regions = []
# regions.append(region)
# checkPointInRegions(regions)
