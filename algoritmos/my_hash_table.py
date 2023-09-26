class MyHashTable:
    def __init__(self, size: int = None):
        if size is None or 0:
            size = 20
        self.size = size
        self.capacity = size
        self.hash_table = self.create_bucket()

    def __get_hashed_key(self, key):
        return hash(key) % self.capacity

    def create_bucket(self):
        return [None for _ in range(self.size)]

    def set_value(self, key, value):
        hashed_key = self.__get_hashed_key(key)
        print({key, hashed_key})
        self.hash_table[hashed_key] = (key, value)

    def get_value(self, key):
        hashed_key = self.__get_hashed_key(key)
        found_key = self.hash_table[hashed_key]
        if found_key is None:
            return ()
        return found_key

    def delete_value(self, key):
        hashed_key = self.__get_hashed_key(key)
        found_key = self.hash_table[hashed_key]
        if found_key is None:
            raise Exception("Value not found")
        self.hash_table[hashed_key] = None

    def __str__(self):
        return "".join(str(f'{item} ') for item in self.hash_table)
