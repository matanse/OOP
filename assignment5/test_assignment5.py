from assignment5 import WritePickleDictToFile
import os
import pickle
import pytest

file_name = './test_dict.txt'
bad_file_path = './noneExistentPath/no_file.txt'
test_dict_file = './test_dict_file.txt'


class TestWritePickleDictToFile:

    def teardown_class(self):
        os.remove(file_name)

    def test_object(self):
        pickle_dict = WritePickleDictToFile(file_name)
        assert isinstance(
            pickle_dict, WritePickleDictToFile), 'did not succeed to create an instense of WritePickleDictToFile.'
        assert isinstance(pickle_dict._file_content,
                          dict), 'did not succeed to create a dict instense.'

    def test_exiting_filename(self):
        pickle_dict = WritePickleDictToFile(file_name)
        assert os.path.isfile(file_name), 'file does not exist.'

    def test_bad_file_path(self):
        with pytest.raises(FileNotFoundError):
            WritePickleDictToFile(bad_file_path), 'file path does not work.'

    def test_read_dict(self):
        assert WritePickleDictToFile(test_dict_file)._file_content == {
            'a': 'yyy', 'b': 'ttt', 'c': 'uuu'}, 'reading file did not work right'

    def test_file_maneger(self):
        test_write_to_file = WritePickleDictToFile(file_name)
        test_write_to_file['a'] = 'yyy'
        test_read_file = WritePickleDictToFile(file_name)
        assert test_read_file._file_content == {
            'a': 'yyy'}, 'writing to file and reading comparing did not work.'

    def test_get_method(self):
        assert WritePickleDictToFile(
            test_dict_file)._file_content['a'] == 'yyy', 'get method is failing.'

    def test_get_method_key_not_exist(self):
        with pytest.raises(Exception):
            WritePickleDictToFile(test_dict_file)._file_content['d']
