import matplotlib.pyplot as plt

track_map = [(10, 0), (11, 1), (12, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (12, 8), (11, 9), (10, 10),
             (9, 10), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (2, 9), (1, 8), (0, 7), (0, 6), (0, 5),
             (0, 4), (0, 3), (1, 2), (2, 1), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]
# 给定的地图轨迹


def dist_2p(pt1, pt2):
    if abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1]) <= 1:
        return 1
    else:
        return 0
# 判断两点距离是否近


def start(curve1, curve2):
    for m in range(len(curve1)):
        for n in range(len(curve2)):
            if curve1[m] == curve2[n]:
                return m, n
# 找到起始点


def jud(track1, track2):
    (m, n) = start(track1, track2)
    track3 = [track1[m]]
    for a in range(m + 1, len(track1)):
        for b in range(0, len(track2)):
            if dist_2p(track1[a], track2[b]) == 1:
                track3 = track3 + [track1[a]]
                break
    return track3
# 找到用户轨迹中符合地图轨迹的路段


track_ex = [(13, 3), (13, 5), (13, 6), (13.2, 7.2), (12, 8.3), (10, 10.3), (9, 10.4), (8.8, 10.1), (8.6, 9.4),
            (7.4, 9.8)]
# 用户轨迹
ans = jud(track_ex, track_map)
print(ans)

x_track_map, y_track_map = zip(*track_map)
plt.plot(x_track_map, y_track_map, 'b-o')
x_track_ex, y_track_ex = zip(*track_ex)
plt.plot(x_track_ex, y_track_ex, 'r-o')
x_ans, y_ans = zip(*ans)
plt.plot(x_ans, y_ans, 'g-o')
plt.text(x_ans[0], y_ans[0], 'start', color='g')
plt.show()
