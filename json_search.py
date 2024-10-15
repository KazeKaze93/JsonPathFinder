import json

class JSONSearch:
    def __init__(self):
        self.data = None

    def load_json_from_string(self, json_string):
        """Загружает JSON из строки"""
        try:
            self.data = json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False

    def search_in_json(self, search_value, partial=False):
        """Выполняет поиск по JSON с поддержкой частичного совпадения"""
        if not self.data:
            return []

        results = []
        self._search_in_json_recursive(self.data, search_value, '', results, partial)
        return results

    def _search_in_json_recursive(self, data, search_value, current_path, results, partial):
        """Рекурсивный поиск по JSON"""
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f'{current_path}/{key}' if current_path else key
                if not isinstance(value, (dict, list)):
                    if (partial and search_value in str(value)) or (str(value) == search_value):
                        results.append((value, new_path))
                self._search_in_json_recursive(value, search_value, new_path, results, partial)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                new_path = f'{current_path}[{index}]'
                if not isinstance(item, (dict, list)):
                    if (partial and search_value in str(item)) or (str(item) == search_value):
                        results.append((item, new_path))
                self._search_in_json_recursive(item, search_value, new_path, results, partial)
