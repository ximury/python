try:
    file = open('test.txt')
    line = file.readline()
except IOError:
    print('except IOError:')
else:
    print(line)
    file.close()

try:
    file = open('word.txt')
    line = file.readlines()
    print(line)
    file.close()
except IOError:
    print('except IOError:')
else:
    print(file.closed)
finally:
    print(file.closed)
