def calc_auth_score(biz_level, class_score):
    return 0.2 * (biz_level - 1) + 0.1 + class_score / 10.0

if __name__ == '__main__':
    print(calc_auth_score(3, 0.2164))