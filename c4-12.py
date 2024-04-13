# 사용자 정의 함수부
def show_division(dividend, divisor) :
    # quotient = 나눗셈 연산의 몫을 구함
    quotient = dividend // divisor

    # remainder = 나눗셈 연산의 나머지를 구함
    remainder = dividend % divisor

    # 나눗셈 연산의 몫(quotient)과 나머지(remainder)를 출력
    print('몫 =', quotient)
    print('나머지 =', remainder)

# 주 프로그램부
# n1 = 사용자로부터 나뉘는 값(피젯수)을 입력받음
n1 = int(input('피젯수를 정수로 입력하세요: '))

# n2 = 사용자로부터 나누는 값(젯수)를 입력받음
n2 = int(input('젯수를 정수로 입력하세요: '))

# 나눗셈 연산의 몫과 나머지를 구해 출력
show_division(n1, n2)
