import random
import pandas as pd
import math
import numpy as np

random.seed(42)
np.random.seed(42)

def read_data():
    file_path = 'game.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')
    ret = []
    for index, row in df.iterrows():
        name = row['index']  
        number = row['weight'] 
        ret.append([name, number])
    return ret

def read_users():
    file_path = 'users.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')
    ret = {}
    for index, row in df.iterrows():
        user_index = int(row['index'])
        name = row['name'] 
        ret[user_index] = name
    return ret


if __name__ == '__main__':
    weight_data = read_data()
    user_map = read_users()
    users = [int(weight_data[i][0]) for i in range(len(weight_data))]
    weights = [weight_data[i][1] for i in range(len(weight_data))]
    # 没发言的人也有概率中奖
    weights = [1 if math.isnan(x) else x + 1 for x in weights]
    weights_sum = sum(weights)
    probs = [x / weights_sum for x in weights ]
    print("*********** 中奖概率 ***********")
    for i in range(len(probs)):
        if i % 5 == 0:
            print()
        tmp = probs[i]*100
        print(users[i], f"{tmp:.2f}%",end='   ')
    print()
    selected_users = []
    total_times = 15
    # selected = random.choices(users, probs, k=total_times)
    selected_indices = np.random.choice(len(users), size=total_times, replace=False, p=probs)
    selected_users = [users[i] for i in selected_indices]
    dolls = []
    for i in range(5): 
        dolls.extend(["猛虎","坐福","短鹅"])
    random.shuffle(dolls)
    # print(selected_users)
    # print(dolls)
    print("*********** 中奖名单 ***********")
    for i in range(len(selected_users)):
        output = "{:<{}} {:<{}}".format(user_map[selected_users[i]], 22, dolls[i], 10)
        print(output)

