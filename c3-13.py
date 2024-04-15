# 사용자 정의 함수부
def make_message() :
    name = input('당신의 이름은? ')
    msg = '반가워요 ' + name    # 두 문자열을 하나로 연결해줌
    print(msg)

# 주 프로그램부
print('시작')
make_message()
print('마침')
