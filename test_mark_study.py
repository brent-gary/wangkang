import pytest

class Test_Demo3():
    @pytest.mark.demo
    def test_demo(self):
        a=5
        b=-1
        assert a != b
        print("这就是demo")
    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b =-1
        assert  a !=b
        print("这就是dsmoke")

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_three(self):
        b = 2
        assert 0==b
        print("这个是打开的smoke")


