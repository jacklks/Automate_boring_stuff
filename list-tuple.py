# 有序可變動列表 List
grades = [12, 15, 70, 90, 60]
print(grades[0])
grades[0] = 55
print(grades)
print(grades[1:4])
grades[1:4]=[] # 連續刪除列表中從編號  1 到編號 4 (不包括) 的資料
print(grades)
grades = grades + [12, 33]
print(grades)
# 巢狀列表
data = [[3,4,5],[6,7,8]]
print(data[0][1])
data[0][0:3]=[5,5,55,55]
print(data)
# 有序不可變動列表 Tuple
data = (3,4,5)
print(data[0:2])