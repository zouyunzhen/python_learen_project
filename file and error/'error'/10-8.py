#读取文件，但是需要运用try-except-else关键字规避FileNotFoundError

def deal(contents):
    try:
        with open(contents,encoding='utf-8') as data:
            data = data.read()
    except FileNotFoundError:
        print('文件未找到')
    else:
        print(data.rstrip())

if __name__ == "__main__":
    deal('The wife')
    deal('cats')