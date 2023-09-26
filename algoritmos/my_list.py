import time


def external_request():
    time.sleep(0.9)


class MyList:
    def __init__(self, names: [], sort=True):
        if names is not None:
            self.names = list(names)
            if sort:
                self.names.sort()
        else:
            self.names = []

    def get(self, index):
        if index < 0 or index > self.get_last_index():
            return None
        else:
            return self.names[index]

    def get_first(self):
        return self.names[0]

    def get_last(self):
        return self.names[self.get_last_index()]

    def get_last_index(self):
        return self.names.__len__() - 1

    def binary_search(self, name: str):
        # obtem a primeira posicao da lista/array
        low = 0
        # obtem a ulta posicao da lista/array
        high = self.get_last_index()

        while low <= high:
            # obtem a posicao do meio da lista/array
            mid = int((low + high) / 2)
            # o chute sempre sera o elemento do meio
            kick = self.names[mid]
            if kick == name:
                # se porventura o item de pesquisa seja o do meio ja retorna o index
                return mid
            if kick > name:
                # se o chute for maior que item entao elimina os valores maiores
                high = mid - 1
            else:
                # se o chute for menor que item entao elimina os valores menores
                low = mid + 1
        return None

    def binary_search_to_compare(self, name: str):
        init_time = time.time()
        count = 0
        low = 0
        high = self.get_last_index()

        while low <= high:
            external_request()
            count = count + 1
            mid = int((low + high) / 2)
            kick = self.names[mid]
            if kick == name:
                end_time = time.time()
                execution_time = end_time - init_time
                return {"value": kick, "attempts": count, "time": execution_time}
            if kick > name:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def linear_search_to_compare(self, name: str):
        init_time = time.time()
        count = 0

        while count <= self.get_last_index():
            external_request()
            kick = self.names[count]
            if kick == name:
                end_time = time.time()
                execution_time = end_time - init_time
                return {"value": kick, "attempts": count, "time": execution_time}
            count = count + 1
        return None

    def get_name(self, index: int):
        if index >= 0:
            return self.names[index]
        else:
            return None

    def show_names(self, index: int):
        if index < 0 or index > self.get_last_index():
            return
        else:
            dicct = {
                "name": self.names[index],
            }
            print(dicct)
            self.show_names(index+1)


    def __get_minor(self, arr):
        minor = arr[0]
        index_minor = 0
        for i in range(1, arr.__len__()):
            bigger = arr[i]
            if bigger < minor:
                minor = bigger
                index_minor = i
        return index_minor

    def selection_sort(self):
        new_names = []
        arr = self.names.copy()
        for i in range(arr.__len__()):
            minor_index = self.__get_minor(arr)
            minor = arr.pop(minor_index)
            new_names.append(minor)
            new_names.__getitem__()
        self.names = new_names

    def quick_sort(self, arr: [] = None):
        if arr is None:
            arr = self.names

        if arr.__len__() <= 1:
            return arr
        else:
            mid = int(arr.__len__() / 2)
            pivo = arr[mid]
            minors = []
            biggers = []
            for item in arr:
                if item < pivo:
                    minors.append(item)
                if item > pivo:
                    biggers.append(item)
            return self.quick_sort(minors) + [pivo] + self.quick_sort(biggers)
