from pytest import fixture
from source.apps.app1.app1_a import App1A


@fixture(scope='function')
def app1_a():
    return App1A()


class TestApp1A(object):
    def test_app1_a_m1(self, app1_a):
        host_ip = app1_a.app1_a_m1_get_ip()
        print(host_ip)
        assert host_ip != '0.0.0.0'
