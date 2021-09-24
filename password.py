def main():
    password = input("print your password longer than 6:")
    while is_valid_password(password):
        print("不满足最小长度，请重新设置")
        break
"""判断密码长度是否合格 合格则输出相应* 不合格则重新输入"""
def is_valid_password(password):
    if len(password) > 6:
        i = 1
        for char in password:
            while i < len(password):
                i += 1
        print("*" * i)
    else:
        return True
main()




