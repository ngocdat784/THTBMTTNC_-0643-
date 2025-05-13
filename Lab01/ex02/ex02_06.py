# Nhập dữ liệu từ người dùng
input_str = input("Nhập X, Y: ")

# Tách chuỗi và chuyển sang số nguyên
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

# Khởi tạo ma trận 2 chiều
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# Gán giá trị theo công thức row * col
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In kết quả
print(multilist)
