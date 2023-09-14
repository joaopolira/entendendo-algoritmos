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

    def test_recursion(self):
        persons = MyList(names, False)
        persons.show_names(0)
        print("recursion succesfull")


if __name__ == '__main__':
    unittest.main()
