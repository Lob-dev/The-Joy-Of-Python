from typing import Optional


def first_item(items: list[str]) -> Optional[str]:
    if len(items) > 0:
        return items[0]
    else:
        return None


if __name__ == '__main__':
    items: list[str] = []
    print('item' in items)
    print('item' not in items)
    print(first_item(items=items))

    items.append('item')
    print('item' in items)
    print('item' not in items)
    print(first_item(items=items))

    for item in items:
        print(item)

    for index in range(len(items)):
        print(f'{index}번째 {items[index]}')

    for index, item in enumerate(items):
        print(f'{index}번째 {item}')

    numbers: list[int] = [2, 4, 6, 8]
    for number in numbers:
        if number % 2 == 1:
            break
        else:
            print('홀수를 포함시켜 주세요.')

    for _ in range(3):
        print(f'{_}')

    index: int = 10
    while index >= 0:
        print(f'{abs(index - 10)}번째 Loop')
        index -= 1

    index: int = 10
    while True:
        if index == 0:
            break
        print(f'{abs(index - 10)}번째 Loop')
        index -= 1


