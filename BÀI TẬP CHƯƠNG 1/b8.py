class Date:
    def __init__(self, day=29, month=1, year=2005):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date

    def display(self):
        return f"Tên: {self.name}, Ngày sinh: {self.birth_date.display()}, Ngày vào công ty: {self.join_date.display()}"

class QuanLyNhanVien:
    def __init__(self):
        self.employees = []

    def them_nhan_vien(self, employee):
        self.employees.append(employee)

    def hien_thi_tat_ca(self):
        for i, emp in enumerate(self.employees, 1):
            print(f"Nhân viên {i}: {emp.display()}")

qlnv = QuanLyNhanVien()

qlnv.them_nhan_vien(Employee("HA HUY H", Date(), Date(14, 4, 2023)))
qlnv.them_nhan_vien(Employee("NGUYEN THAI B", Date(23, 5, 2005), Date(15, 6, 2024)))

print("Danh sách tất cả nhân viên:")
qlnv.hien_thi_tat_ca()