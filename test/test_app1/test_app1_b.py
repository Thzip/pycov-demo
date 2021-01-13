from pytest import mark
from source.app1.app1_b import App1B


class TestApp1B(object):
    @mark.parametrize('country_name, country_code', [('中国', 'CN'), ('漂亮国', 'US'), ('日本', 'OTHERS')])
    def test_query_country_code(self, country_name, country_code):
        cc = App1B.get_country_code(country_name)
        assert cc == country_code
