# Nhập dữ liệu từ người dùng
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# Khai báo số giờ làm tiêu chuẩn
gio_tieu_chuan = 44

# Tính số giờ làm vượt chuẩn (nếu có)
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập (lương giờ chuẩn + lương tăng ca 1.5x)
thuc_linh = (gio_tieu_chuan * luong_gio) + (gio_vuot_chuan * luong_gio * 1.5)

# In kết quả
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")
