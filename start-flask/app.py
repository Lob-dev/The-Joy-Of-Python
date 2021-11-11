# WSGI Middleware 기반의 Application 을 생성하는 객체를 호출
from uuid import uuid4

from flask import Flask, request

# Static resources 와 template 를 찾는 용도로 쓰이는 값 : __name__
app = Flask(__name__)


# route 정보는 중첩 가능하다.
@app.route('/greeting')
@app.route('/index')
@app.route('/')
def greeting() -> dict[str]:
    return dict(say='greeting')


@app.route('/users/<username>')
def get_user(username: str) -> str:
    return username


@app.route('/posts/<int:post_id>')
def get_post(post_id: int) -> dict[int]:
    return dict(post_id=post_id)


@app.route('/uuid/<uuid:uuid>')
def get_uuid(uuid: uuid4) -> str:
    return str(uuid)


# 여러 메서드가 공통 로직을 사용해야 이용해야 경우 사용하는 방식
@app.route('/greeting/<name>', methods=['GET', 'POST'])
def get_greeting(name: str) -> dict[str]:
    print(f'hello! {name}')
    print('validation name')
    if request.method == 'POST':
        print('POST')
        return dict(say='Hello!' + name)
    else:
        print('GET')
        return dict(say='hello!' + name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)