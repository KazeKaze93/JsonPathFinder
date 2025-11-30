from typing import Any, Generator, Union, List

class PathFinder:
    def __init__(self, data: Union[dict, list]):
        self.data = data

    def find(self, target: Any, search_mode: str = 'key') -> List[str]:
        """
        Главный метод поиска.
        :param target: Что ищем (имя ключа или значение)
        :param search_mode: 'key' (по ключам) или 'value' (по значениям)
        :return: Список найденных путей
        """
        return list(self._recursive_search(self.data, target, search_mode, "$"))

    def _recursive_search(
        self, 
        current_data: Any, 
        target: Any, 
        mode: str, 
        path: str
    ) -> Generator[str, None, None]:
        
        # Если текущий элемент - словарь
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                # Формируем путь (для ключей с пробелами используем ['key'], иначе .key)
                new_path = f"{path}['{key}']" if not key.isalnum() else f"{path}.{key}"

                # Логика поиска
                if mode == 'key' and key == target:
                    yield new_path
                elif mode == 'value' and value == target:
                    yield new_path
                
                # Ныряем глубже
                if isinstance(value, (dict, list)):
                    yield from self._recursive_search(value, target, mode, new_path)

        # Если текущий элемент - список
        elif isinstance(current_data, list):
            for index, item in enumerate(current_data):
                new_path = f"{path}[{index}]"
                
                if mode == 'value' and item == target:
                    yield new_path
                
                if isinstance(item, (dict, list)):
                    yield from self._recursive_search(item, target, mode, new_path)

# Удобный алиас для импорта
def find_paths(json_data: Union[dict, list], target: Any, mode: str = 'key') -> List[str]:
    return PathFinder(json_data).find(target, mode)