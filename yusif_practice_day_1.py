
# 1. Adını str tipində, yaşını int tipində, boyunu float tipində bir dəyişəndə saxla.

# 2. Bir list yarat və içərisinə 3 sevdiyin proqramlaşdırma dilini əlavə et.

# name1="Yusif"
# age1=18
# boy1=1.76
# languages=["python","css","js"]
# print(f"ad:{name1},yas:{age1},height:{boy1}")
# print(languages)
# 3. Əgər yaşın (age1) 18-dən böyük və ya bərabərdirsə, ekrana "İcazə verilir" yazsın.

# 4. Əgər languages siyahısının içərisində "python" varsa, əlavə olaraq "Python bilirsən!" yazısını çap etsin. (Bunun üçün if "python" in languages: sintaksisindən istifadə edə bilərsən).

# if age1>=18:
#    print("Icaze verilir")
# else :
#     print("verilmir") 

# if "python" in languages:
#     print("python bilirsen!")
# else :
#     print("Python bilmirsen!")

# 5. Bir for dövrü yaz ki, 1-dən 10-a qədər olan ədədlərin kvadratlarını çap etsin (Məsələn: 1, 4, 9, 16...).

# 6. Bir while dövrü yaz ki, count dəyişəni 5-dən geriyə 0-a qədər saysın (5, 4, 3, 2, 1, 0).

# for i in range(1,11):
#     print(i**2)
    
# count=5
# while count>=0:
#     print(count)
#     count-=1    
# "Ədəd tapma" oyunu: Kompüter bir rəqəm tutsun, sən onu tapmağa çalış (while və if istifadə edərək).

# 7. Sadə kalkulyator: İki rəqəm və bir əməliyyat (+, -, *, /) qəbul edən funksiya yaz.

# 8. İstifadəçi siyahısı: İstifadəçidən adları alıb bir siyahıda saxlayan və onları for ilə çap edən proqram.


# tapilmalieded=int(input("1-10000 arası bir ədəd tutdum, onu tapmağa çalışın:"))

# while True:
    
    
#     texminedileneded=int(input("Təxmin etdiyiniz ədədi daxil edin:"))
    
#     if texminedileneded==tapilmalieded:
#         print("Təbriklər! Düzgün tapdınız.")
#         break
#     elif texminedileneded<tapilmalieded:
#         print("Daha böyük bir ədəd təxmin edin.")
#     else:
#         print("Daha kiçik bir ədəd təxmin edin.")


# a=int(input("Birinci ədədi daxil edin:"))
# b=int(input("İkinci ədədi daxil edin:"))
# operation=input("Əməliyyatı daxil edin (+, -, *, /):")

# if operation=="+":
#     result=a+b
# elif operation=="-":
#     result=a-b
# elif operation=="*":
#     result=a*b  
# elif operation=="/":
#     if b!=0:
#         result=a/b
#     else:
#         result="Sıfıra bölmək olmaz!"
# print(f"Nəticə: {result}")

# users = []
# for _ in range(3):
#     name = input("Adınızı daxil edin: ")
#     users.append(name)

# for user in users:
#     print(user)



# 9. List comprehension: 1-50 arası 3-ə bölünən ədədləri tap
# 10. Student grade proqramını tam işə sal, nəticəni yoxla

# ededler=[i for i in range(1, 51) if i % 3 == 0]

# for eded in ededler:
#     print(eded)


# students = [
#     {"name": "Ali", "grade": 85},
#     {"name": "Fatima", "grade": 90},
#     {"name": "Omer", "grade": 78}
# ]

# for student in students:
#     print(f"Ad: {student['name']}, Qiymət: {student['grade']}")