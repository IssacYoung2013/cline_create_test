def login(username, password):
    # 简单的硬编码验证
    if username == 'admin' and password == '123456':
        return True
    return False

if __name__ == '__main__':
    # 测试登录
    user = input('Username: ')
    pwd = input('Password: ')
    if login(user, pwd):
        print('Login successful!')
    else:
        print('Invalid credentials!')