# param = [{'start': 1000, 'end': 1005}, {'start': 1400, 'end': 1600}, {'start': 1601, 'end': 1800}]
param = [{'start': 1000, 'end': 1005}]
# for item in param:
if len(param) <= 1:
    print('no replace')
else:
    for i in range(len(param) - 1):
        for j in range(len(param)):
            if j > i:
                if param[i].get('start') <= param[j].get('end') and \
                        param[j].get('start') <= param[i].get('end'):
                    print('has replace')
                    print(param[i], param[j])
    print('no replace')
