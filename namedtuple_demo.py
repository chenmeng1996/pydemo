from collections import namedtuple

# 定义一个namedtuple类型User,并包含name,sex和age属性
User = namedtuple('User', ['name', 'sex', 'age'])

# 创建一个User对象
user = User(name='quincy', sex='male', age=24)

# 通过一个list来创建User对象，需使用“_make”方法
user = User._make(['quincy', 'male', 24])

# 输出
print(user)
print(user.name, user.age, user.sex)

# 修改对象属性
user = user._replace(age=23)
print(user)

# 将对象转为字典

print(user._asdict())