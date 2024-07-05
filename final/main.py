from tasks import add

if __name__ == '__main__':
    result = add.delay(4, 4)
    print('Task Result:', result.get(timeout=10))

