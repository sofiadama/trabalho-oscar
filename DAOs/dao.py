import pickle
import os
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        self.__load()

    def __dump(self):
        try:
            # Cria o diretório se não existir
            directory = os.path.dirname(self.__datasource)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(self.__datasource, 'wb') as file:
                pickle.dump(self.__cache, file)
        except Exception as e:
            print(f"Erro ao salvar arquivo {self.__datasource}: {e}")

    def __load(self):
        try:
            if os.path.exists(self.__datasource):
                with open(self.__datasource, 'rb') as file:
                    self.__cache = pickle.load(file)
                print(f"Dados carregados de {self.__datasource}")
            else:
                print(f"Arquivo {self.__datasource} não encontrado. Criando novo...")
                self.__cache = {}
                self.__dump()  # Cria o arquivo vazio
        except EOFError:
            print(f"Arquivo {self.__datasource} está vazio. Inicializando...")
            self.__cache = {}
            self.__dump()
        except pickle.UnpicklingError:
            print(f"Erro ao deserializar {self.__datasource}. Inicializando...")
            self.__cache = {}
            self.__dump()
        except Exception as e:
            print(f"Erro inesperado ao carregar {self.__datasource}: {e}")
            self.__cache = {}
            self.__dump()
        
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        if key in self.__cache:
            self.__cache[key] = obj 
            self.__dump()
        else:
            print(f"Chave {key} não encontrada para atualização.")

    def get(self, key):
        return self.__cache.get(key, None)

    def remove(self, key):
        if key in self.__cache:
            removed = self.__cache.pop(key)
            self.__dump()
            return removed
        else:
            print(f"Chave {key} não encontrada para remoção.")
            return None

    def get_all(self):
        return list(self.__cache.values())
    
    def exists(self, key):
        return key in self.__cache
    
    def clear(self):
        self.__cache = {}
        self.__dump()
    
    def size(self):
        return len(self.__cache)
