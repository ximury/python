import numpy

if __name__ == '__main__':
    li = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
    np_list = numpy.array(li)
    print(np_list)
    np_list = numpy.array(li, dtype=numpy.float)
    print(np_list)
    print(np_list.shape)
    print(np_list.ndim)
