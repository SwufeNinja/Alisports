import matplotlib.pyplot as plt


x = 0
y = 0
curve_a = [(10, 0), (11, 1), (12, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (12, 8), (11, 9), (10, 10),
           (9, 10), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (2, 9), (1, 8), (0, 7), (0, 6), (0, 5),
           (0, 4), (0, 3), (1, 2), (2, 1), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]

x_curve_a, y_curve_a = zip(*curve_a)
plt.plot(x_curve_a, y_curve_a, 'b-o')
length = len(curve_a)
curve_b = [(0, 0)] * length
for i in range(length):
    curve_b[i] = curve_a[length - 1 - i]


def inn(pt1, pt2):
    if abs(pt1[0] - pt2[0]) == 0 and abs(pt1[1] - pt2[1]) == 0:
        return 1
    else:
        return 0


def start(curve1, curve2):
    for m in range(len(curve1)):
        for n in range(len(curve2)):
            if curve1[m] == curve2[n]:
                return m, n


def lu(curve1, curve2):
    sum = -1
    (m, n) = start(curve1, curve2)
    for a in range(m, len(curve1)):
        if a == len(curve1) - 1:
            if inn(curve1[a], curve2[n]) == 0:
                return sum
            else:
                print(curve1[a])
                sum += 1
                return sum
        elif inn(curve1[a], curve2[n]) == 0:
            return sum
        else:
            n += 1
            sum += 1
            print(curve1[a])


curve_ex = [(4, 10), (3, 10), (2, 9), (1, 8), (0, 7), (0, 6), (0, 5),
           (0, 4), (0, 3), (1, 2), (2, 1), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]
x_curve_ex, y_curve_ex = zip(*curve_ex)
plt.plot(x_curve_ex, y_curve_ex, 'r-o')
example1 = lu(curve_ex, curve_a)
example2 = lu(curve_ex, curve_b)
print('总路程1：' + str(example1))
print('总路程2：' + str(example2))
plt.text(x_curve_ex[0], y_curve_ex[0], 'start', color='g')
plt.show()