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

print(2 + 2 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4 #14
print(number)

number = number + 2 #16
print(number)

number += 2
print(number) #18

number *= 2
print(number) #36

number /= 2
print(number) #18

number -= 2
print(number) #16


print('---------------------------숫자열 함수------------------------');

print(abs(-5)) #5
print(pow(4,2)) # 4의 2승 16
print(max(2,3,4)) #4
print(min(3,8,1,5)) #1

print(round(3.14)) #반올림 3
print(round(4.14)) #반올림 4


from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의 값 생성
print(random() * 10) # 0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 "미만"의 임의의 값 생성
print(int(random() * 10) + 1 ) #1 ~ 10"이하"의 임의의 값 생성


print(randrange(1,46)) # 1 ~ 46 미만의 임의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성



print('---------------------------퀴즈------------------------');

from random import *

date = randint(4, 28)

print("오프라인 스터디 모임은 매월 " + str(date) + "일로 선정되었습닌다")


print('--------------------------문자열------------------------');

sentence = '나는 소년입니다'
print(sentence)

sentence2 = '파이썬 뚝딱이입니다'
print(sentence2)

sentence3 = """ 
나는 소년이고,
파이썬 뚝딱입니다
"""
print(sentence3)



print('--------------------------슬라이싱------------------------');

jumin = '990120-1234567'

print('성별 : '+ jumin[7]) #인덱스 7번째 위치 출력 성별 : 1
print('연 : ' + jumin[0:2]) #인덱스 번호 0번째부터 2번째까지 출력 연 : 99
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print('생년월일: ' + jumin[:6]) #콜론으로 시작하면 처음부터 인덱스 번호 6까지 가져옴
print('뒤 7자리: ' + jumin[7:]) #콜론으로 끝나면 인덱스 번호 끝까지 가져옴
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:]) #맨뒤에서 7번째부터 끝까지



print('--------------------------문자열 처리 함수------------------------');

python = "python is Amazing"

print(python.lower()) #문자열 소문자로 출력 값: python is amazing
print(python.upper()) #문자열 대문자로 출력 값: PYTHON IS AMAZING
print(python[0].isupper()) #인덱스 번호 0번의 값이 대문자인자 확인함 False

print(len(python)) #문자 수 출력 17

print(python.replace('python','java')) #replace('문장안에 있던 기존 값','기존 값 위치에 새롭게 넣는 값'))
#값: java is Amazing

index = python.index('n') #n의 인덱스 번호 출력
print(index) #5
index = python.index('n', index + 1)
print(index) #"python is Amazing" 문장에서 두번째 n을 찾음

print(python.find('n')) #인덱스 번호 출력
print(python.find('java')) #없는 데이터이므로 -1 출력

print(python.count('n')) # n이라는 문자가 얼만큼 나오는지 출력 값: 2



print('--------------------------문자열 포맷------------------------');

#방법 1

print('나는 %d살입니다' % 20) # %뒤에 있는 20을 앞에 있는 %뒤에 d위치에 넣겠다는 뜻 d는 정수를 의미
print('나는 %s을 좋아해요' % "파이썬") # s는 string 값 문자열을 의미
print('apple은 %c로 시작해요.' %"a" ) #c는 하나의 문자를 의미

print('나는 %s색과 %s색을 좋아해요.' % ("파란","빨간")) #괄호안에 넣어서 하나 이상의 값 넣기



#방법 2

print("나는 {}살입니다." .format(20)) #format을 사용해서 중괄호 안에 20을 넣음
print('나는 {}색과 {}색을 좋아해요'.format('파란','빨간')) #괄호안에 하나 이상의 값을 넣어서 출력하기
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간')) #인덱스번호를 중괄호 안에 넣어서 값 설정하기


#방법 3

print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 2 , color = "빨간")) #중괄호 안에서 변수선언


#방법 4
age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요.") # 밖에서 변수를 선언하는 방식



print('------------------------탈출문자--------------------------');

print('백문이 불여일견 \n 백견이 불여일타') # \n 줄바꿈

print('사실 저는 "프론트엔드 개발자"입니다') #큰따옴표 출력하는 법
print('사실 저는 \'프론트엔드 개발자\'입니다') #작은따옴표 출력하는 법


# \\ : 문장 내에서 \ 출력하기
print(" c:\\Users\\coding\\Desktop> ") 

# \r : 커서를 맨 앞으로 이동
print('Red Apple \r pine') #값 pineApple

# \b : 백스페이스 (한 글자 삭제)
print('redd\b Apple') #값 red Apple

#\t : 탭
print('red\tApple') #값 red     Apple



print('-----------------------퀴즈-------------------------');

site = "http://naver.com"
my_str = site.replace("http://", "") #규칙1
my_str = my_str[:my_str.index('.')] #규칙2

# print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"

print('{0}의 비밀번호는 {1} 입니다'.format(site, password))


print('-----------------------리스트-------------------------');

#지하철 칸별로 10명 20명 30명이 있다고 가정

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?

print(subway.index('조세호'))


# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄

subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


# 같은 이름의 사람이 몇명 있는 지 확인하기

subway.append("유재석") #같은 이름이 없으니 유재석 한번 더 추가
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count('유재석')) # 2


# 정렬도 가능

num_list = [5,2,4,3,1]
num_list.sort()

print(num_list)

# 순서 뒤집기

num_list.reverse()
print(num_list)

# 모두 지우기

num_list.clear()
print(num_list)


# 다양한 자료형을 함께 사용

num_list = [5,2,4,3,1]
mix_list = ["조세호",20,True]

# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)



print('-----------------------사전-------------------------');

cabinet = {3:'유재석',100:'김태호'}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))


print(3 in cabinet) #True
print(5 in cabinet) #False


cabinet2 = {'a-3':'유재석','a-100':'김태호'}
print(cabinet2['a-3'])
print(cabinet2['a-100'])



# 새 캐비넷 주인
print(cabinet2)
cabinet2["c-20"] = '조세호'

print(cabinet2['c-20'])


# 주인 빠진 캐비넷

del cabinet2['a-3']
print(cabinet2)


# key들만 출력

print(cabinet2.keys())

# value들만 출력

print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 캐비넷 폐점

cabinet2.clear()
print(cabinet2)

print('-----------------------튜플-------------------------');

menu = ('돈까스','치즈까스')

print(menu[0])
print(menu[1])

#튜플은 고정된 값에서 사용하는 것, 

# name = "김종국"
# age="99"
# hobby="코딩"
# print(name,age,hobby)

#=>
(name , age , hobby) = ('김종국','99','코딩')
print(name,age,hobby)

print('-----------------------세트-------------------------');
# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,4,5,5}
print(my_set) # 1,2,3,4,5

java = {'유재석','김태호','양세형'}
python = set(['유재석','박명수'])
# 교집합 (java와 python을 모두 할 수 있는 개발자) 출력

print(java & python)
print(java.intersection(python)) #유재석 출력

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자) 출력
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자) 출력
print(java - python)
print(java.difference(python))


# 파이썬을 할 줄 아는 개발자가 생김
python.add("김태호")
print(python)

# 자바를 잊어서 자바개발자에서 제외됨
java.remove('김태호')
print(java)

print('-----------------------자료구조의 변경-------------------------');
#커피숍
menu = {'커피','우유','주스'}
print(menu, type(menu)) #{'커피', '주스', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) #['우유', '주스', '커피'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) #('커피', '우유', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #{'커피', '우유', '주스'} <class 'set'>


print('-----------------------퀴즈-------------------------');

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(list)
# shuffle(list)
# print(list)

from random import *
user = range(1,21) #1부터 20까지 숫자생성
# print(type(user))
user = list(user)
# print(type(user))

print(user)
shuffle(user)
print(user)

winners = sample(user, 4)
print('치킨 당첨자: {0}'.format(winners[0]))
print('커피 당첨자: {0}'.format(winners[1:]))



print('-----------------------if문-------------------------');

# weather = input('오늘 날씨는 어때요?')
# # if 조건:
# #     실행 명령문

# if weather == "비":
#     print('우산을 챙기세요')
# elif weather == "미세먼지":
#     print('마스크를 챙기세요')
# else:
#     print('준비물 필요없어요.')


# temp = int(input('기온은 어때요?'))
# if 30 <= temp:
#     print('너무 더워요. 나가지 마세요')
# elif 10 <= temp and temp < 30:
#     print('괜찮은 날씨에요')
# elif 0 <= temp and temp < 10:
#     print('외투를 챙기세요')
# else:
#     print('너무 추워요. 나가지 마세요')


print('-----------------------for문-------------------------');

# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')

for waiting_no in [0,1,2,3,4]:
    print('대기번호: {0}'.format(waiting_no))

# randrange()
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print('대기번호: {0}'.format(waiting_no))


starbucks = ['아이언맨','토르','아이엠 그루트']
for customer in starbucks:
    print("{0},커피가 준비되었습니다".format(customer))


print('-----------------------while문-------------------------');

# customer = '토르'
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print('커피는 폐기처분되었습니다')


# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer, index))
#     index += 1
 #무한루프 코드 컨트롤 c 누르면 종료

customer = "토르"
person = "UnKnown"

while person != customer :
    print("{0},커피가 준비 되었습니다.".format(customer))
    person = input('이름이 어떻게 되세요?')