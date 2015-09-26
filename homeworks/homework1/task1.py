#Task 1
obj = input()
num = int(input())
if obj == 'утюг':
    sclon = ['утюг', 'утюга', 'утюгов']
else:
    sclon = ['ложка', 'ложки', 'ложек']
if num % 10 == 1 and num % 100 != 11:
    print(num, sclon[0])
elif 2 <= num % 10 <= 4 and (12 > num % 100 or num % 100 > 14):
    print(num, sclon[1])
else:
    print(num, sclon[2])
