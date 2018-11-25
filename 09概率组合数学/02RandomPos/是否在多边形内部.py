#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
计算方法是射线法，计算交点个数:
1.poly[i],poly[j]表示多边形的边；
2.if ((poly[i]["lat"] <= pt["lat"]and pt["lat"] < poly[j]["lat"])or
(poly[j]["lat"] <=pt["lat"]and pt["lat"] < poly[i]["lat"]))
: 找到横坐标（lat）范围包括待测试点的的边（可以形象理解为：
画一条以待测试点横坐标为基点的竖线，找到跟多边形相交的边）
3.if (pt["lng"] < (poly[j]["lng"]- poly[i]["lng"])* (pt["lat"]- poly[i]["lat"])/ (poly[j]["lat"]-poly[i]["lat"])+ poly[i]["lng"]):
计算待测试点在步骤2中的边下方的个数（可以形象理解为：从上到下画一条竖线，找到穿过多边形边的次数）
最后，初始设置在多边形外（c=False)，每穿过一条边则变化一次标志(c=not c)。
总之，想象自己是一个小偷，多边形是围墙，开始你在外面，沿直线穿越围墙向目标出发，第一次穿墙进入围墙内，
第二次穿墙就到围墙外了，第三次进入围墙内... ...当到达目标时候，根据穿墙次数就能判断目标是否在多边形内。
'''
def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        print(i, poly[i], j, poly[j])
        if ((poly[i]["lat"] <= pt["lat"] and pt["lat"] < poly[j]["lat"]) or (
                poly[j]["lat"] <= pt["lat"] and pt["lat"] < poly[i]["lat"])):
            if (pt["lng"] < (poly[j]["lng"] - poly[i]["lng"]) * (pt["lat"] - poly[i]["lat"]) / (
                    poly[j]["lat"] - poly[i]["lat"]) + poly[i]["lng"]):
                c = not c
        j = i
    return c


if __name__ == '__main__':
    abc = [{'lat': 1, 'lng': 1}, {'lat': 1, 'lng': 4}, {'lat': 3, 'lng': 7}, {'lat': 4, 'lng': 4}, {'lat': 4, 'lng': 1}]
    print(isInsidePolygon({'lat': 2, 'lng': 5}, abc))
