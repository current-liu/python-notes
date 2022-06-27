from functools import wraps


def log_decorator(func):
    @wraps(func)  # Update a wrapper function to look like the wrapped function
    def wrapper(arg):
        print(f'log before exec func')
        func(arg)
        print('log after exec func')

    return wrapper


def log_it(file=''):
    def log_deco(func):
        @wraps(func)
        def wrapper(arg):
            print(f'{file}:log before exec func')
            func(arg)
            print('log after exec func')
        return wrapper
    return log_deco


@log_it('log_file')
def hi(x):
    print('hi' + x)


@log_decorator
def hi(x):
    print('hi' + x)


class LogIt:
    def __init__(self, prefix='Log'):
        self.prefix = prefix

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.prefix)
            func(*args, **kwargs)

        return wrapper


@LogIt()
def hello():
    print('hello')


def make_notebook():
    text = []

    def notebook(input_text):
        text.append(input_text)
        return ' '.join(text)
    return notebook


if __name__ == '__main__':
    hi('123')
    print(hi.__name__)
    hello()
