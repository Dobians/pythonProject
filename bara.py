sk =input("Введите текущую скорость корабля (км/ч):")
rs =input("Введите расстояние до планеты (в миллионах километров):")
sk =float(sk)
rs =float(rs)
r = rs*1000000
c = r/sk
d = c/24
print(d)