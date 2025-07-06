# 主程序: 输出Hello World
from hello_world.main import greet


def test_greet():
    assert greet() == "Hello, World!"
