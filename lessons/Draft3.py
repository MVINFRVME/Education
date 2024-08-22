print(3)

def bold(func):
    def wrapper():
        val = func()
        # Вставка HTML кода до и после 'val'
        return '<b>' + val + '</b>'
    return wrapper


def italic(func):
    def wrapper():
        val = func()
        # Вставка HTML кода до и после 'val'
        return '<i>' + val + '</i>'
    return wrapper


@bold
@italic
def say():
    return "hello"


print(say())
# <b><i>hello</i></b>
