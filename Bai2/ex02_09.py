# Hàm kiểm tra số nguy tố
def kiem_tra_so_nguyen_to(n):
    # Nếu số nhỏ hơn hoặc bằng 1, không phải số nguyên tố
    if n <= 1:
        return False
    
    # Kiểm tra từ 2 đến căn bậc hai của n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Nhập số từ người dùng và kiểm tra
number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")