if __name__ == '__main__':
    from random import *

    print(f'random 함수 {random}')
    print(f'0.0 ~ 1.0 미만의 임의의 값 생성 {random()}')
    print(f'0.0 ~ 10.0 미만의 임의의 값 생성 {random() * 10}')
    print(f'0 ~ 10 미만의 임의의 값 생성 {int(random() * 10)}')
    print(f'1 ~ 10 미만의 임의의 값 생성 {int(random() * 10) + 1}')

    print()
    print(f'randrange 함수 {randrange}')
    print(f'1 ~ 10 미만의 임의의 값 생성 {randrange(1, 10)}')

    print()
    print(f'randint 함수 {randint}')
    print(f'1 ~ 10 미만의 임의의 값 생성 {randint(1, 10)}')
    print()

    resident_registration_number: str = '980125-1234567'
    print('문자열 슬라이싱')
    print(f'성별 : {resident_registration_number[7]}')
    print(f'연 : {resident_registration_number[0:2]}')
    print(f'월 : {resident_registration_number[2:4]}')
    print(f'일 : {resident_registration_number[4:6]}')
    print(f'생년월일 앞 6자리: {resident_registration_number[0:6]}')
    print(f'생년월일 앞 6자리: {resident_registration_number[:6]}')
    print(f'생년월일 뒤 7자리: {resident_registration_number[7:14]}')
    print(f'생년월일 뒤 7자리: {resident_registration_number[7:]}')
    print(f'생년월일 뒤 7자리 (맨 뒤에서부터): {resident_registration_number[-7:]}')
    print()

    print('문자열 처리 함수')
    string: str = 'Hello World!'
    print(string.upper())
    print(string[0].isupper())
    print(string.lower())
    print(string[1].islower())
    print(len(string))
    print(string.replace('Hello', 'Bye'))

    index1: int = string.index('o')
    print(index1)

    index2: int = string.index('o', index1 + 1)
    print(index2)

    print(string.find('Hello'))  # 없는 경우 -1 출력
    print(string.index('Hello'))  # 없는 경우 Error 발생

    print(string.count("o"))

    # str(value) -> "${value}"
    print('문자열 포맷팅')
    number: int = 10
    print("숫자 문자열로 출력 :" + str(number))
    print('old style format으로 출력 : {}'.format(number))
    print('new style format으로 출력 : {number}'.format(number=number))
    print(f'String interpolation으로 출력 f-strings : {number}')

    print('저는 %d살입니다.' % number)
    print('저는 %s살입니다.' % "10")
    print('저는 %d살입니다. 제 동생은 %d살이구요.' % (number, 7))
    print()
