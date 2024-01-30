# _*_coding : utf-8 _*_
# @Author : jerry
# @File : py节奏治疗


# b=input()
# c=b.replace('O','1')
# d=c.replace('X','0')
# sum=int(input())
# for i in range(1,sum+1):
#     g[i-1] = int(input())
# for i in range(1,sum+1):
#     if(g[i-1]==0)

def is_valid_keyboard(heartbeat, doctors):
    # 遍历心跳信号列表
    for i in range(len(heartbeat)):
        # 如果心跳信号为'X'，则检查医生是否有按键
        if heartbeat[i] == 'X':
            # 如果有医生在当前位置按下了按键，返回False
            if any(doctors[j][i] == '1' for j in range(len(doctors))):
                return False
    # 如果没有医生在心跳信号为'X'的位置按下了按键，返回True
    return True

# 输入心跳信号字符串
heartbeat = input().strip()
# 输入医生数量
num_doctors = int(input())
# 初始化医生列表
doctors = []
# 输入每个医生的按键记录
for _ in range(num_doctors):
    doctors.append(input().strip())

# 初始化结果列表
result = []
# 遍历每个医生的按键记录
for doctor in doctors:
    # 如果该医生的按键记录与心跳信号匹配，将"YES"添加到结果列表中
    if is_valid_keyboard(heartbeat, [doctor]):
        result.append("YES")
    # 否则，将"NO"添加到结果列表中
    else:
        result.append("NO")

# 输出结果列表
for res in result:
    print(res)