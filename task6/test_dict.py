import pytest

from main import DictWithFileLog

PATH = "main.txt"


class TestDict:
    def test_creation(self):
        testDict = DictWithFileLog(PATH, {'dictionary': 1})

        assert testDict == {'dictionary': 1}

        with pytest.raises(ValueError):
            DictWithFileLog(PATH, {'dictionary'})

    def test_get(self):
        testDict = DictWithFileLog(PATH, {'dictionary': 1})

        assert testDict['dictionary'] == 1
        assert 'dictionary' in testDict.log()[-1]

        with pytest.raises(KeyError):
            testDict['dict']

    def test_del(self):
        testDict = DictWithFileLog(PATH, {'dictionary': 1})
        del testDict['dictionary']

        assert 'del' in testDict.log()[-1]

    def test_set(self):
        testDict = DictWithFileLog(PATH)
        testDict['dictionary'] = 1
        assert 'set' in testDict.log()[-1]
