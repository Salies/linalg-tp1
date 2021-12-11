import numpy as np
from pandas import read_csv

def get_high_five_indexes(vector, key):
    # Salva em "res" todos os filmes relacionados com
    # o filme, de id "key", requisitado
    res = np.empty(1000)
    a = key - 1
    # Os valores levam em conta o tamanho e organização do vetor
    for n in range(998, 999 - key - 1, -1):
        res[998 - n] = vector[a]
        a += n
    a += 1
    for i in range(999 - key):
        res[key + i] = vector[a + i]
    # Retorna os 5 filmes melhor relacionados com o filme de id "key".
    # Nota-se que aqui "a" é redefinida, apenas para economizar uma variável.
    a = np.argpartition(res, -5)[-5:]
    a = a[np.argsort(res[a])][::-1]
    for i in range(5):
        if a[i] >= key:
            a[i] += 1
    return a

# Carregando os dados
m_names = read_csv("data/movies.csv")['title'].tolist()
with open('rel.npy', 'rb') as f:
    values = np.load(f)
print("Dados carregados.")

# Loop do programa, consulta o usuário
# e imprime os resultados
try:
    while True:
        m_id = int(input("\033[96m\nDigite o id do filme desejado:\033[37m "))
        print("Filme selecionado: \33[31m" + str(m_names[m_id]) + "\033[37m\nCinco filmes mais relacionados:\33[33m")
        for ml_id in get_high_five_indexes(values, m_id):
            print(m_names[ml_id])
except KeyboardInterrupt:
    pass