import datetime
import random


def schedule(current_time):
    # 模拟安排时间
    hours=current_time.hour
    mins=current_time.minute
    hours_left=24-hours-1
    mins_left=60-mins
    if mins_left==60:
        hours_left=hours_left+1
        mins_left=0
    total_left_min=hours_left*60+mins_left
    print('你今晚剩下只有',hours_left,'小时',mins_left,'分钟','(共',total_left_min, '分钟)')
    if hours_left>6*60:
        print("还没到晚上呐，晚上6点后再来吧")
        return 0

    all_char    =  ['战法','男圣骑','女圣骑','漫游','大枪','街霸','鬼泣','风法']
    all_map_min =  [  75  ,  45   ,  45    ,  45 ,  45  ,  45  ,  45 ,  45  ]

    main_char=[0]
    saders=[1,2]
    Sub_C=[3,4]
    Sup_C=[5,6,7]
    schedule=[]
    print('你今晚的安排大概如下：')
    for m in main_char:
        time=total_left_min-all_map_min[m]
        cha=all_char[m]
        tim=all_map_min[m]
        print(cha,tim,'分钟')
    while(time>45):
        rng=random.randint(1,len(all_map_min)-1)        
        time=time-all_map_min[rng]
        cha=all_char[rng]
        tim=all_map_min[rng]
        print(cha,tim,'分钟')
    # print(Sup_C)
    
    print('剩下的',time,'分钟，爱干嘛干嘛~')

def roll(characters):
    # 随机抽取角色
    pass

def selectAllCharacters():
    # 选择你所有的职业
    pass

def midnightCountDown():
    # 倒计时到晚上12点
    pass

def getCurrentTime():
    time=datetime.datetime.now()
    return time
def main():
    # 获取当前时间
    pass
    
    
    # print(time_after_main)


if __name__ == '__main__':
    rc = main()