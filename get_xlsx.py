import os


def Get_xlsx(where):
    filelist = []
    for root, dirs, files in os.walk(where, topdown=False):
        for name in files:
            str = os.path.join(root, name)
            if str.split('.')[-1] == 'xlsx':
                filelist.append(str)

    return filelist
