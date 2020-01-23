import threading

from stores.store import Store


class VolatileStore(Store):

    def __init__(self):
        super().__init__()
        self.url_store = {}
        self.id = 0
        self.lock = threading.Lock()

    def _save_record(self, short_id, original_url):
        self.url_store[short_id] = original_url

    def _find_record_by_id(self, id):
        if id in self.url_store.keys():
            return self.url_store[id]
        return None

    def _find_record_by_url(self, url):
        if url in self.url_store.values():
            for key, value in self.url_store.items():
                if value == url:
                    return key
        return None

    def get_short(self, original_url):
        if not self.url_manager.is_valid(original_url):  # -> is url valid
            return None
        short_id = self._find_record_by_url(original_url)
        if short_id:  # -> does id exist for url in the store
            short_url = self.url_manager.append_base_url(short_id)
            return short_url
        id = self.__get_unique_id()
        short_url, short_id = self.url_manager.convert_to_short(id)
        self._save_record(short_id, original_url)
        print(self.url_store)
        return short_url

    def get_original(self, url_id):
        original_url = self._find_record_by_id(url_id)
        if original_url:
            return original_url
        return None

    def increment_hit_count(self, url):
        pass

    def get_url_hit_count(self, url):
        pass

    def __get_unique_id(self):
        with self.lock:
            self.id += 1
            return self.id




