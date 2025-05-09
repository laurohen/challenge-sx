from lru_cache import LRUCache

def main():
    cache = LRUCache(2)
    cache.put(1, 1)  # cache = {1: 1}
    cache.put(2, 2)  # cache = {1: 1, 2: 2}
    print(cache.get(1))  # retorna 1
    cache.put(3, 3)  # remove chave 2, cache = {1: 1, 3: 3}
    print(cache.get(2))  # retorna -1 (não encontrado)
    cache.put(4, 4)  # remove chave 1, cache = {3: 3, 4: 4}
    print(cache.get(1))  # retorna -1 (não encontrado)
    print(cache.get(3))  # retorna 3
    print(cache.get(4))  # retorna 4

if __name__ == "__main__":
    main()