from typing import Union


class App1B(object):
    def __init__(self):
        pass

    def foo(self):
        pass

    @staticmethod
    def get_country_code(country_name: str):
        if country_name == '中国':
            return 'CN'
        elif country_name == '漂亮国':
            return 'US'
        elif country_name == '泡菜省':
            return 'KR'
        else:
            return 'OTHERS'
