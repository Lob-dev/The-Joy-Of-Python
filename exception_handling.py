def get_book(index: int, books: list[str]) -> str:
    try:
        return books[index]
    except (IndexError, RuntimeError):
        return f'index({index})가 엘리먼트 범위({len(books) - 1})를 벗어났습니다.'
    except TypeError as exception:
        return f'인자에 잘못된 타입이 들어왔습니다. Message = {exception.args[0]}'


def get_book_raise(index: int, books: list[str]) -> str:
    try:
        if index >= 999:
            print(f'잘못된 index({index}) 범위 값입니다.')
            raise TypeError()
        return books[index]
    except (IndexError, RuntimeError):
        return f'index({index})가 엘리먼트 범위({len(books) - 1})를 벗어났습니다.'
    except TypeError as exception:
        return f'인자에 잘못된 타입이 들어왔습니다. Message = {exception.args[0]}'


def get_book_name(index: int, books: list[str]) -> str:
    try:
        book = books[index]
    except (IndexError, RuntimeError):
        return f'index({index})가 엘리먼트 범위({len(books) - 1})를 벗어났습니다.'
    except TypeError as exception:
        return f'인자에 잘못된 타입이 들어왔습니다. Message = {exception.args[0]}'
    else:  # 예외가 발생하지 않았을 때에만 실행하는 block
        return book.upper()
    finally:  # 예외 여부와 관계없이 실행되는 block. file 리소스를 정리할 때 사용하는 것이 좋다 (file.close())
        print("function ended")


class BizRuntimeError(RuntimeError):
    status: int
    message: str
    pass


class UserNotFoundException(BizRuntimeError):
    pass


if __name__ == '__main__':
    books: list[str] = ['python을 다루는 기술', 'lob을 다루는 기술', '개발자여. 악으로 깡으로 버텨라']
    print(get_book(index=0, books=books))

    print(get_book(index=3, books=books))

    # print(get_book(index="3", books=books))

    print(get_book_name(index=0, books=books))

    try:
        print(get_book_raise(index=999, books=books))
    except IndexError:
        print(f'index가 엘리먼트 범위({len(books) - 1})를 벗어났습니다.')
    except TypeError as exception:
        print(f'인자에 잘못된 타입이 들어왔습니다. Message = {exception.args[0]}')
