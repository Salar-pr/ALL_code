import random#فراخانی کردن کتاب خانه رندوم 


#تعریف تابع برای ساخت جدول
def jadval(row,column,a,b):
    my_list=list(random.randint(a,b)for _ in range(row*column))

#جدا سازی ان به مقدار ستون
    for i in range(0, len(my_list),row):
        print(my_list[i:i+row])

    n = int(input("enter your number:"))


#تعریف تابع برای جست و جو اعدد مشخص
    def search(n):
         
        
        def count_list(my_list,n):
            return my_list.count(n)
                                                     
        print({count_list(my_list,n)})
    search(n)
 
        

row = int(input("enter your row:"))
column = int(input("enter your cole:"))  
a = int(input("enter your start reng random:"))
b = int(input("enter your end rang random:"))
jadval(row,column,a,b)

    




    

      
           


    
