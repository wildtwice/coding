# 주제: 1.연산 // 2. 입력과 자료형 변환

# [연산(1)]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자
'''b = 4
#a = input("숫자를 입력시오:")
a = 4
c = a+b
print(c)
'''


## 숫자산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기
'''
print(7+3)  
print(7-3)  
print(7*3)  
print(7/3)  
print(7//3) 
print(7%3)  
print(7**3) 
'''
'''print(7/2)
print(7//2)
'''

## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어
## 출력해보자
'''a = "#1"
b = "해시태그 2"
c = "#3"
print(a+b+c)
print(a*3)




## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자
print(a*10)
'''

## mission>> 복함할당연산자를 연산을 하고, 그 연산이 무엇을 줄인 식인지 주석으로 적어보자.
'''a = 3
b = 5
a += b#=a=a+b
print(a)'''

# [연산(2)]
## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기
'''
print(5>8)      
print(3<8)      
print(10>=7)    
print(200>=751) 
print(5==11)    
print(5!=5)    
print("3.141592653589793" == "3.141592653589783")           
print("illIIilil|IIIIIilllllIIIlilil" != "illIIilil|IIIIIilllllIIIIlilil")  
'''
# print("박정범"== "하리보 곰젤리")
# print(10.3333333 != 5)

# a = 100
# b = int(input("숫자를 입력하세요: "))
# print("두 값은 같은가요?")
# print(a==b)

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print((4<6) and (10 >= 10))     
print("LoskArk" != "LostArk" or "League of Legend" == "League of Legends")   
print(not 5==5)     
'''
# print(True and True)
# print(False and True)
# print(True or False)
# print(False or True)
# print((100<3)or(40==40))

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 결과를 주석으로 달기

# print("Z" in "The Legend of Zelda")
# print("l" not in "A Dance of Fire and Ice")
#
# print(("신" in "심빛나")and ("전"in "전명주"))


# [입력과 자료형 변환]
## 연습문제>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
# a = input("숫자를 입력하세요>> ")
# b = input("숫자를 입력하세요>> ")
# print(type(a),type(b))
# a += b
# print(a)

## mission>> 출생년도를 입력하고 나이를 출력해보자.
# a = int(input("출생년도를 입력하세요>> "))
# age = 2022 - a + 1
# print("당신의 나이는 %d 살입니다"%age)

money = int(input("지불할 돈을 입력하십시오!"))
drink_money = int(input("음료수의 가격은 이렇게 됩니다:"))

change_money = money - drink_money
print("거스름돈은 %d원입니다."%change_money)

change_1000 = change_money//1000
change_500 = (change_money%1000)//500
change_100 = (change_money%500)//100

print(f"1000원 지폐의 수 => {change_1000}")
print(f"500원 동전의 수 => {change_500}")
print(f"100원 동전의 수=> {change_100}")
