from source.apps.app2.app2_a import foo


class TestApp2A(object):
    def test_app2a_m(self):
        assert foo() > 1
