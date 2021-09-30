list = [1, 4, 2, 6, 8]

new_list = []


def get_min(lt):
    a = min(lt)
    lt.remove(a)
    new_list.append(a)
    if len(lt) > 0:
        get_min(lt)
    return new_list


new_list = get_min(list)
print(new_list)
