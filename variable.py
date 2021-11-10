if __name__ == '__main__':
    print('값 연산')
    print('빼기', 7 - 6, '더하기', 5 + 3,'곱하기', 2 * 8, '나누기', 2 / 6, '나머지', 5 % 3)
    print('나누기 연산 후 소수점 이하 수 버리기', 5 // 3)
    print('절댓값', abs(-2))
    print('제곱1', 2 ** 3, '제곱2', pow(2, 3))
    print('우선순위', 3 * (3 + 1))
    print('max 값', max(5, 12), 'min 값', min(5, 12))
    print('반올림', round(3.141))

    from math import *

    print('내림', floor(4.99))
    print('올림', ceil(3.14))
    print('제곱근', sqrt(16))
    print()
    print('숫자 변수')
    number: int = 10
    print(number)
    print()

    print('문자 변수')
    string: str = 'hello world!'
    print(string)
    print('Multiple String')
    print('''
         문자
         여러줄
         .
    ''')
    print()

    print('참 거짓')
    condition: bool = 5 > 10
    print(condition)
    print()

    # not -> !
    not_condition: bool = not condition
    print(not_condition)
    print()
