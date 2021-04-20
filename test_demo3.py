import pytest
import yaml
#理解pytest的框架结构
#类外面的测试
#python 中一个模块就是一个文件，setup_module可实现整个模块中自执行一次
def setup_module():
    print("\nsetup module:整个模块只执行一次￥$$$")

def teardown_module():
    print("\n**$$teradown module:整个模块只执行一次￥$$$")
def setup_function():
    print("\nsetup function: 每个类中的用例开始前会执行")
def teardown_function():
    print("\nteardown _function:每个不在类中的用例结束后会执行")

def test_one():
    print("\n正在执行测试模块：test one")

def test_two():
    print("\n正在执行测试模块：test two")

class TestCase():
    def stup_class(self):
        print("\n**setup class:class类里面说有用例前执行")
    def teardown_class(self):
        print("\n***theardoen class:class类里面所有用例后执行")
    def Setup(self):
        print("\nSteup：每个开始前都会执行")
    def teardown(self):
        print("\nteardown:结束后执行")
    def test_three(self):
        print("\n正在自行测试模块三: test three")
    def test_four(self):
        print("\n正在自行测试模块三: test four")



