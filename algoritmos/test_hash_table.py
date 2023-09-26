import unittest

from algoritmos.my_hash_table import MyHashTable


class TestCase(unittest.TestCase):

    def test_hash_table(self):
        my_hash_table = MyHashTable()
        my_hash_table.set_value("Giovana", 19988331765)
        my_hash_table.set_value("Rosicler", 19988331764)
        my_hash_table.set_value("Aline", 19988331763)
        my_hash_table.set_value("Joice", 19988331762)
        giovana = my_hash_table.get_value("Giovana")
        self.assertEqual(giovana[1], 19988331765, "Should be equals")
        my_hash_table.delete_value("Joice")
        print(my_hash_table)
        joice = my_hash_table.get_value("Joice")
        self.assertEqual(joice, (), "Should be equals")
        with self.assertRaises(Exception):
            my_hash_table.delete_value("Joice")


if __name__ == '__main__':
    unittest.main()
