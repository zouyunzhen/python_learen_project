#读取文件，但是需要运用try-except-else关键字规避FileNotFoundError
#在10-8上的改进，对于未找到的文件执行静默失败

def deal(contents):
    try:
        with open(contents,encoding='utf-8') as data:
            data = data.read()
    except FileNotFoundError:
        pass
    else:
        print(data.rstrip())

if __name__ == "__main__":
    deal('The wife')
    deal('cats')