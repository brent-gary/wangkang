import pytest
import yaml
def add_function(a,b):
    return a+b
# def test_add1():
#     assert add_function(1,1) == 2
# def test_add2():
#     assert add_function(1,-1) == 0
#
# def test_add3():
#     assert add_function(-1,-1) == -2
# def test_add4():
#     assert add_function(100000,100000) == 200000
# 参数化加别名参数化加别名
#演示参数文件
'''
@pytest.mark.parametrize("a,b,expected",
                         yaml.safe_load(open("./data.yml"))["datas"],
                         ids=yaml.safe_load(open("./data.yml"))["myid"]
                         )

#读文件可以抽离

'''
def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas,add_ids]
@pytest.mark.parametrize("a,b,expected",
                         get_datas()[0],
                         ids=get_datas()[1]



                         )


def test_add(a,b,expected):
    assert add_function(a,b) == expected

    #参数可以组合
@pytest.mark.parametrize("a",[0,1,20000])
@pytest.mark.parametrize("b",[-2,10000,0.4])

def test_foo(a,b):
    print("测试数据组合：a->%s,b->%s"%(a,b))

