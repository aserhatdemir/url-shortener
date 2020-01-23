import string


class UrlManager:
    def __init__(self):
        self.base_url = 'http://devsec.systems:8081/url/'
        self.base_converter = BaseConverter()

    def convert_to_short(self, store_id) -> tuple:
        short_id = self.base_converter.encode(store_id)
        short_url = self.append_base_url(short_id)
        return short_url, short_id

    def append_base_url(self, short_id):
        return f'{self.base_url}{short_id}'

    def convert_to_original(self, short_url) -> str:
        original_url = 'original'
        return original_url

    def is_valid(self, url):
        return True


class BaseConverter:
    def __init__(self):
        self.base_alph = f'{string.ascii_letters}{string.digits}'
        self.base_dict = dict((c, v) for v, c in enumerate(self.base_alph))
        self.base_len = len(self.base_alph)

    def decode(self, string):
        num = 0
        for char in string:
            num = num * self.base_len + self.base_dict[char]
        return num

    def encode(self, num):
        if not num:
            return self.base_alph[52]  # -> '0'
        encoding = ""
        while num:
            num, rem = divmod(num, self.base_len)
            encoding = self.base_alph[rem] + encoding
        return encoding

