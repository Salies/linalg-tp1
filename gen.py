from pandas import read_csv
import numpy as np

# Abrindo arquivos de dados para leitura
print("Abrindo arquivos...")
m_scores = read_csv("data/scores.csv")['relevance'].to_numpy().reshape(1000,1128)

# Preparando o array de valores para receber as realções
scores = np.empty(499500)

# Gerando pontuações entre filmes
print("Gerando relações...")
for i in range(1000):
    for j in range(i + 1, 1000):
        # Calculando a pontuação
        dist = np.linalg.norm(m_scores[i] - m_scores[j])
        cos = np.dot(m_scores[i], m_scores[j]) / (np.linalg.norm(m_scores[i]) * np.linalg.norm(m_scores[j]))
        # Associando-a no array
        scores[999*i-(((i-1)*i)//2)+((j-1)-i)] = cos / dist

# Salvando pontuações em um arquivo para consulta posterior,
# já que gerá-las leva um tempo consdirável
with open('rel.npy', 'wb') as f:
    np.save(f, scores)
