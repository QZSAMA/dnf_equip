import pandas as pd
import sys
import os
import datetime

def initialization():
    # 如果没有数据库（假的，只是普通csv）被检测到的话，开一个新的数据库
    path=os.path.dirname(os.path.realpath(__file__))
    db_path=os.path.join(path,'db.csv')
    info_path=os.path.join(path,'info.csv')
    # print(db_path)
    if not os.path.isfile(db_path):
        pass
        # 1.创造新档案
        # db_file= open("db_path","w+",encoding='utf-8')
        # db_file.write("角色,Id,安图恩,卢克,强袭,黎明,魔兽,泰波尔斯")
        # 2.导入文件作为数据库 表头一定为：
        #    0  1   2     3    4    5   6     7
        # "Id,角色,安图恩,卢克,强袭,黎明,魔兽,泰波尔斯"
    else:
        db=pd.read_csv(db_path,index_col='Id')
        # print(db.head())
    # print()
    # Dungeon,Completed,Triger,Each
    if not os.path.isfile(info_path):
        pass
    else:
        info=pd.read_csv(info_path,index_col='Dungeon')
        # print(info.head())
    return db,info

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def trigerParser(value):
    if isInt(value):
        value=int(value)
        return [value]
    string=str(value)
    if ',' in string:
        result=[]
        stringList=string.split(',')
        for eachString in stringList:
            ret=trigerParser(eachString)
            if not ret is None:
                result=result+ret
        return result
    if '-' in string:
        start,end=string.split('-')
        if isInt(start) and isInt(end) :
            return list(range(int(start),int(end)+1))
def isUsed(filePath):
    if os.path.exists(filePath):
        try:
            os.rename(filePath, filePath)
            return False
        except OSError :
            return True
def signed(Id,dungeon):
    path=os.path.dirname(os.path.realpath(__file__))
    db,info=initialization()
    worst=info.loc[dungeon,'Completed']
    own=db.loc[Id,dungeon]
    # print(worst)
    # print(own)
    # print(own+worst)
    
    db.loc[Id,dungeon]=own+worst
    filepath=os.path.join(path,'db.csv')
    while(not isUsed(filepath)):
        db.to_csv(filepath)
        break
    
def isIdExisted(Id):
    db=initialization()[0]
    if Id in db.index:
        return True
    else:
        return False
def isDungeonExisted(Dungeon):
    info=initialization()[1]
    if Dungeon in info.index:
        return True
    else:
        return False
def main():
    # db,info=initialization()
    # # print(db.head())
    # char_list=db.index.tolist()
    # dungeon_list=info.index.tolist()
    # signed('index','安图恩')
    # print(isIdExisted('sb'))
    print(isDungeonExisted('安图恩'))

    # print(db.head())
if __name__ == '__main__':
    rc = main()
