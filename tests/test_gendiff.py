from pathlib import Path
from gendiff.generate_diff import generate_diff


stylish_path = './tests/fixtures/expectedStylish.txt'
plain_path = './tests/fixtures/expectedPlain.txt'
json_path = './tests/fixtures/expectedJSON.txt'


expectedStylish = Path(stylish_path).read_text().strip()
expectedPlain = Path(plain_path).read_text().strip()
expectedJSON = Path(json_path).read_text().strip()


def test_generate_from_json():
    path1 = './tests/fixtures/before.json'
    path2 = './tests/fixtures/after.json'

    assert generate_diff(path1, path2, 'stylish') == expectedStylish
    assert generate_diff(path1, path2, 'plain') == expectedPlain
    assert generate_diff(path1, path2, 'json') == expectedJSON


def test_generate_from_yaml():
    path1 = './tests/fixtures/before.yml'
    path2 = './tests/fixtures/after.yml'

    assert generate_diff(path1, path2, 'stylish') == expectedStylish
    assert generate_diff(path1, path2, 'plain') == expectedPlain
    assert generate_diff(path1, path2, 'json') == expectedJSON
