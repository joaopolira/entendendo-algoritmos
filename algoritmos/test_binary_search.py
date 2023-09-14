# A pesquisa binaria e uma busca em lista/array no qual considera que todos seus elementos estejam ordenados, comecando a busca pelo
# o meio e caso encontro o elemento, retorna sua posicao ou quando nao retorna None.
# A diferenca da pequisa binaria para pesquisa sequencial e a quantidade de tentativas, pois a cada tentativa na pesquisa binaria e eliminado mais da
# metade dos elementos e na pesquisa sequencial e eliminado somente 1.
# Se a busca for realiazada em uma lista no qual ha 240mil elemento na pior das hipoteses de cada pesquisa a binaria levaria 18 tentativas e
# na sequencial 240mil. Isso acontece porque a pesquisa binaria e feita na base de logaritmos.
# Neste caso, log 2 de (tamanho da lista). Por exemplo: uma lista com 100 elementos teriamos log 2 de 100, e fazemos a
# multiplicacão de quantas vezes e necesssario multiplicar o 2 para chegar ate 100 e essa seria a nossa quantidade de
# tentativas que resulta em 7.

from algoritmos.my_list import MyList
import unittest

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

    def test_binary_search(self):
        persons = MyList(names)
        # ================================================================================================================
        name_to_search1 = "Joao"
        index = persons.binary_search(name_to_search1)
        name_to_compare1 = persons.get_name(index)
        self.assertEqual(name_to_search1, name_to_compare1, "Should be Joao")
        # ================================================================================================================
        name_to_search2 = "Dudu"
        index = persons.binary_search(name_to_search2)
        name_to_compare2 = persons.get_name(index)
        self.assertEqual(name_to_search2, name_to_compare2, "Should be Dudu")
        # ================================================================================================================
        name_to_search3 = "Davizito"
        name_to_compare3 = persons.binary_search(name_to_search3)
        self.assertEqual(None, name_to_compare3, "Should be None")

    def test_binary_search_and_linear_search(self):
        persons = MyList(names)
        result_binary = persons.binary_search_to_compare("Valdenir")
        result_linear = persons.linear_search_to_compare("Valdenir")
        print(f'binary search result {result_binary}')
        print(f'linear search result {result_linear}')


if __name__ == '__main__':
    unittest.main()
