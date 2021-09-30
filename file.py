import os

file_path = 'D://PycharmProjects//TestCode//assert1.py'
print(os.path.exists(file_path))
if not os.path.exists(file_path):
    os.mknod(file_path)

def get_FileSize(filePath):
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    # fsize = fsize / float(1024 * 1024)
    # return '%.2f MB' % (round(fsize, 2))
    return '%.2f B' % (round(fsize, 2))


# print((get_FileSize('D://VSCodeProjects//0419//monitor-view//public//static//video//test.mp4')))


# print((get_FileSize('D://VSCodeProjects//0419//monitor-view//public//static//video//test2.flv')))
