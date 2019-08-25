import csv

def ReadFile(file: str, encoding: str='utf-8-sig'):
    if str.find(file, ".csv") > -1:
        return open(file=file, mode='r',encoding=encoding)
    elif str.find(file, ".json") > -1:
        pass
    return False

def getWebsiteList(file:str):
    wlist = []
    tmp = []
    file = ReadFile(file=file)
    if file is False:
        return False
    spamreader = csv.reader(file)
    try:
        for i in spamreader:
            tmp.clear()
            tmp.append(i[0])  # website url
            tmp.append(i[1])  # to block
            wlist.append(tmp.copy())
    # the input file format error
    except:
        return False
    return wlist


def WriteFile(file,data: str):
    file.writelines(data+"\n")
    return

def OpenFile(file_path: str,mode: str):
    file = open(file=file_path, mode=mode)
    return file


