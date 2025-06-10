# 单元测试：验证greet函数
from hello_world.main import greet

def test_greet():
    assert greet() == "Hello, World!"