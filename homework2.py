# 1
# a = float(input('a='))
# b = float(input('b='))
# c = float(input('c='))
# d = b**2-4*a*c
# r1 = (-b+d**0.5)/(2*a)
# r2 = (-b-d**0.5)/(2*a)
# if d > 0:
#     print('r1=%f,r2=%f'%(r1,r2))
# elif d == 0:
#     print('r1=r2=%f'%r1)
# elif d<1:
#     print('没有实根')



# 2
# import numpy as np 
# res = np.random.choice(101)
# res1 = np.random.choice(101)
# print(res,res1)
# number = float(input('用户输入的数：'))
# if number == (res +res1):
#     print('则为真')
# else:
#     print('则为假')





# 3
# today = int(input('今天星期？(请输入数字1，2，3……)：'))
# jg = int(input('几天后？：'))
# weilai = today + jg
# if weilai > 7:
#     print('未来某天是星期',weilai % 7)
# else:
#     print('未来某天是星期',weilai)



# 4
# x = int(input('x='))
# y = int(input('y='))
# z = int(input('z='))
# if x > y:
#     x, y = y, x
# if x > z:
#     x, z = z, x
# if y > z:
#     y, z = z, y 
# print(x, y, z)






# 5
# weight1,price1= eval(input("Enter weight  and price for package 1 :"))
# weight2,price2= eval(input("Enter weight  and price for package 2 :"))
# permj1 = price1 / weight1
# permj2 = price2 / weight2
# if permj1 > permj2:
#     print("package 2  has the better price ")
# else:
#     print("package 1  has the better price ")






# 6
# month,year = eval(input("Enter month an year (5,2004):"))
# leapyear =  year % 4
# if month == 1 or  month == 3 or month == 5 or month == 7 or month == 8  or month == 10 or  month == 12:
#     month1 = 31
# elif month ==4 or  month == 6 or  month == 8  or  month ==9 or month ==11 :
#     month1 =30
# elif leapyear == 0 and   month == 2:
#     month1 = 29
# else:
#     month = 28
# print(year,"年",month,"月","有",month1,"天")




# 7
# import numpy as np 
# res = np.random.choice(['正面','反面'])
# print(res)
# user = input('请输入(正面，反面)：')
# if res == user:
#     print('这个猜测值是正确的')
# else:
#     print('这个猜测值是错误的')



# 8
# import numpy as np 
# res = np.random.choice(['0','1','2'])
# print(res)
# user = input('请输入(0,1,2)：')
# if res == user:
#     print('平局')
# elif res =='1' and user =='0':
#     print('你输了')
# elif res =='0' and user =='2':
#     print('你输了')
# elif res =='2' and user =='1':
#     print('你输了')
# else:
#     print('你赢了')




# 9
# year = int(input('请输入年份：'))
# m = int(input('请输入月份：'))
# q = int(input('请输入天数：'))
# j = (year/100)//1
# k = year%100
# h = (q+((26*(m+1))/10)+k+(k/4)+(j/4)+5*j)%7
# print ('%d'%h)



# 10
# import numpy as np 
# res = np.random.choice(['梅花','红桃','方块','黑桃']) 
# res1 = np.random.choice(13)
# print('%s%s'%(res,res1))




# 11
# number = (input('请输入一个数：'))
# number1 = (number[::-1])
# if number == number1:
# print('是回文数')
# else:
# print('不是回文数')



# 12
# lenght1,lenght2,lenght3, =eval(input("输入三边的长度:"))
# perimeter = lenght1 + lenght2 + lenght3
# if   lenght1 + lenght2 > lenght3 and   lenght1 + lenght3 > lenght2 and lenght2 + lenght3 > lenght1:
#     print("周长是：",perimeter)
# else:
#     print("非法的")



# 13








# 14











# 15









# 16
# i = 0
# for i in range(100,1000):
#     if i%5==0 and i%6==0:
#         print(i,'\t',end='')



# 17
 
       





# 18










# 19










# 20
# res = 0
# for i in range(1,98,2):
#     res += i/(i+2)
# print(res)



# 21
# res = 0
# for i in range(1,100000):
#     res += 4*((-1)**(i+1)/(2*i-1))
# print(res)





# 22
# for i in range(1,10000):
#     res = 0
#     for j in range(1,i):
#         if i%j ==0:
#             res += j
#     if i == res:
#         print(i)




# 23
# a = 0
# for i in range(1,8,2):
#     for j in range(2,8):
#         if i !=j:
#             print(i,j)
#             a+=1


        

        


