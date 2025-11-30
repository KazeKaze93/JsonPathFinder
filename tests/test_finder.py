import pytest
from json_path_finder.core import find_paths

@pytest.fixture
def complex_json():
    return {
        "store": {
            "book": [
                {"category": "reference", "author": "Nigel", "title": "Sayings", "price": 8.95},
                {"category": "fiction", "author": "Evelyn", "title": "Sword", "price": 12.99}
            ],
            "bicycle": {"color": "red", "price": 19.95}
        },
        "metadata": {"author": "System"}
    }

def test_find_key(complex_json):
    # Ищем ключ 'author' (он есть в двух местах)
    paths = find_paths(complex_json, "author", mode='key')
    assert len(paths) == 3
    assert "$.store.book[0].author" in paths
    assert "$.metadata.author" in paths

def test_find_value(complex_json):
    # Ищем значение 'red'
    paths = find_paths(complex_json, "red", mode='value')
    assert len(paths) == 1
    assert paths[0] == "$.store.bicycle.color"

def test_find_in_list(complex_json):
    paths = find_paths(complex_json, "Sword", mode='value')
    assert "$.store.book[1].title" in paths