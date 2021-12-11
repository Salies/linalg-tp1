import numpy as np
from pandas import read_csv

m_names = read_csv("data/movies.csv")['title'].tolist()

# Retorna todos os filmes relacionados com
# o filme, de id "key", requisitado
def get_rel(vector, key):
    res = np.empty(1000)
    a = key - 1
    # Os valores levam em conta o tamanho e organização do vetor
    for n in range(998, 999 - key - 1, -1):
        res[998 - n] = vector[a]
        a += n
    a += 1
    for i in range(999 - key):
        res[key + i] = vector[a + i]
    return res

def get_high_five_indexes(vector, key):
    ind=np.argpartition(vector, -5)[-5:]
    ind=ind[np.argsort(vector[ind])][::-1]
    for i in range(5):
        if ind[i] >= key:
            ind[i] += 1
    return ind

with open('rel.npy', 'rb') as f:
    vals = np.load(f)

print("Dados carregados.")
try:
    while True:
        m_id = int(input("\033[96m\nDigite o id do filme desejado:\033[37m "))
        print("Filme selecionado: \33[31m" + str(m_names[m_id]) + "\033[37m\nCinco filmes mais relacionados:\33[33m")
        for ml_id in get_high_five_indexes(get_rel(vals, m_id), m_id):
            print(m_names[ml_id])
        
except KeyboardInterrupt:
    pass