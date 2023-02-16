print(3.14)
print(1000)
print(5+3)
print('풍선')
print("스껄")
print("스껄"*9)

# 이것이 파이썬 주석인가

print(5>10) #false
print(5<10) #True

print(not True) #false
print(not False) #False
print(not(5>10))


print('---------------------------변수------------------------');

#애완동물을 소개해 주세여

# print('우리집 강이지의 이름은 잭슨이에요')
# print('잭슨이는 10살...이고,산책을 아주 좋아해요')
# print('잭슨이는 찰스라는 동생이 있어요 True')

animal = '강아지'
name = '잭슨이'
age = 10
brother = "찰스"
hobby = "산책"
is_old = age >= 8

print('우리집 '+animal+'의 이름은 '+name+'에요')
print(name+'는', age ,'살...이고,'+hobby+'을 아주 좋아해요')
print(animal+'는 '+brother+'라는 동생이 있어요')
print(name + '는 노견일까요?' +str(is_old))

# 변수를 이용하여 다음 문장을 출력하시오

station = "신도림"

print(station+'행 열차가 들어오고 있습니다')

print('---------------------------연산자------------------------');

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 =8
print(5%3) #나머지 구하기 2
print(10%3) #1
print(5//3) #1
print(10//3) #3

print(10 > 3) #True
print(4 >=7 ) #False
print(10 <= 3) #False
print(5 <= 5) #True


print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) #True
print(not(1 != 3)) #False

#and
print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

#or
print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True


print( 5 > 4 > 3 ) #True
print( 5 > 4 > 7 ) #False
