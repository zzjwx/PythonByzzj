# 1
# x = 1
# def getPentagonalNumber(n):
#    jiaojiao = n * (3 * n - 1) / 2
#    return jiaojiao
# M = getPentagonalNumber(x)
# print('有多少个五角数:>>')
# count = 0
# for i in range(100):
#    jiaojiao = getPentagonalNumber(x)
#    x += 1
#    i += 1
#    print(jiaojiao,end='   ')
#    count += 1
#    if(count%10==0):
#        print(end='\n')



# 2
# def sumDigits(n):
#     n1 = n % 10
#     n2 = (n // 10) % 10
#     n3 = n // 100
#     print('n1+n2+n3=',(n1+n2+n3))
# sumDigits(789)



# 3
# def displaySortedNumbers(num1,num2,num3):
#     i = 0
#     while i<4:
#        if num1 > num2:
#            x = num2
#            num2 = num1 
#            num1 = x
#        elif num2 > num3:
#            x = num3
#            num3 = num2
#            num2 = x
#        i += 1
#     print(num1,num2,num3)
# displaySortedNumbers(5,7,9)




# 5
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=" ")
#         if i% 10 == 0:
#             print("\n")
# printChars()



# 6
# def numberOfDaysInAYear(year):
#     for count in range(year,year+11):
#         if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
#             print("{}年有366天".format(count))
#         else:
#             print("{}年有365天".format(count))
# numberOfDaysInAYear(2010)



# 7
# def distance(x1,x2,y1,y2):
#     dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     print("这两个点的距离是：%f"%dis)
# distance(1,4,4,2)






# 9
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("本地时间为 :", localtime)
#     print(time.time())
# main()




# 10
# import random


# def shaizi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# shaizi()
