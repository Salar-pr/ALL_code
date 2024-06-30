import random

# تابع برای ساخت جدول اعداد تصادفی
def create_random_table(row, column, a, b):
    # ایجاد لیست اعداد تصادفی
    my_list = [random.randint(a, b) for _ in range(row * column)]
    # چاپ جدول
    for i in range(0, len(my_list), column):
        print(my_list[i:i + column])
    return my_list

# تابع برای یافتن مختصات اعداد تکرار شده
def find_occurrences(my_list, n, row, column):
    occurrences = [(i // column, i % column) for i, x in enumerate(my_list) if x == n]
    return occurrences

# دریافت ورودی‌ها از کاربر
row = int(input("لطفا تعداد ردیف‌ها را وارد کنید: "))
column = int(input("لطفا تعداد ستون‌ها را وارد کنید: "))
a = int(input("لطفا ابتدای محدوده اعداد تصادفی را وارد کنید: "))
b = int(input("لطفا انتهای محدوده اعداد تصادفی را وارد کنید: "))

# ایجاد جدول و یافتن مختصات اعداد تکرار شده
my_list = create_random_table(row, column, a, b)
n = int(input("لطفا عدد مورد نظر برای جستجو را وارد کنید: "))
occurrences = find_occurrences(my_list, n, row, column)

# چاپ مختصات
print(f"مختصات اعداد {n} در جدول:")
for occ in occurrences:
  print(f"ردیف {occ[0] + 1}, ستون {occ[1] + 1}")
  

    




    

      
           


    
