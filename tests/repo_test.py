import unittest

from domain.entities import Eveniment
from repository.events_repo import FileEventRepo


class TestCaseRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=FileEventRepo('test_repo.txt')

    def test_add_event(self):
        lenght=len(self.__repo.get_events())
        event=Eveniment('23.02.2022','12:45','sport')
        self.__repo.add_event(event)
        self.assertEqual(lenght+1,len(self.__repo.get_events()))