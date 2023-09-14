import unittest

from algoritmos.my_list import MyList

names = [
    "Joao",
    "Paulo",
    "Oliveira",
    "De",
    "Giovana",
    "Endrick",
    "Gustavo",
    "Miriam",
    "Leonardo",
    "Silva",
    "Aline",
    "Joice",
    "Leticia",
    "Meire",
    "Rosicler",
    "Valdenir",
    "Nita",
    "Pablo",
    "Pelego",
    "Megue",
    "Danilo",
    "Marcelo",
    "Dudu",
    "Lidia",
    "Reginaldo",
    "Davi",
    "Bernardinho",
    "Cleitinho"
]


class TestCase(unittest.TestCase):

    def test_selection_sort(self):
        persons = MyList(names, False)
        primary_name = persons.get_first()
        last_name = persons.get_last()
        persons.selection_sort()
        primary_name_to_compare = persons.get_first()
        last_name_to_compare = persons.get_last()
        self.assertNotEqual(primary_name, primary_name_to_compare, "Should be differs")
        self.assertNotEqual(last_name, last_name_to_compare, "Should be differs")


if __name__ == '__main__':
    unittest.main()
