from url_manager import UrlManager


class Store:

    def __init__(self):
        self.url_store = None
        self.url_manager = UrlManager()

    def _save_record(self, short_id, original_url):
        pass

    def _find_record_by_id(self, id):
        pass

    def _find_record_by_url(self, url):
        pass

    def get_short(self, original_url):
        pass

    def get_original(self, url_id):
        pass

    def increment_hit_count(self, url):
        pass

    def get_url_hit_count(self, url) -> int:
        pass

