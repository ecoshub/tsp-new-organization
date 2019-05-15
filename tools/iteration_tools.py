from itertools import islice


def line_iterator(points, ignore_list=[]):
    lenp = len(points)
    for i in range(lenp):
        for j in range(lenp):
            if i != j:
                if i not in ignore_list:
                    if j not in ignore_list:
                        yield i, j


def uniq_line_iterator(points, ignore_list=[]):
    lenp = len(points)
    for i in range(lenp):
        for j in range(i + 1, lenp):
            if i != j:
                if i not in ignore_list:
                    if j not in ignore_list:
                        yield i, j


def point_iterator(points, ignore_list=[]):
    lenp = len(points)
    for i in range(lenp):
        if i not in ignore_list:
            yield i


def slice_iteration(iterator, total_iteration, number_of_slice):
    iterators_list = []
    batch_size = int(total_iteration / number_of_slice + 0.5)
    for i in range(0, total_iteration, batch_size):
        start = i
        end = i + batch_size
        if end > total_iteration:
            end = total_iteration
        it = islice(iterator, start, end)
        iterators_list.append(it)
    return iterators_list
