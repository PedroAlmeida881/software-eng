# ------------------------------------------------------------
# Passo 1: Importar Bibliotecas e Carregar Dados
# ------------------------------------------------------------

# Importar bibliotecas
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar conjunto de dados Iris
iris = load_iris()

# X = características (comprimento e largura das sépalas e pétalas)
# y = classe (0 = setosa, 1 = versicolor, 2 = virginica)
X = iris.data
y = iris.target

# Visualizar uma amostra dos dados em formato de tabela (opcional, ajuda a entender)
df = pd.DataFrame(X, columns=iris.feature_names)
df["especie"] = [iris.target_names[i] for i in y]
print("Primeiras linhas do conjunto de dados:")
print(df.head())
print("\nFormato dos dados:", X.shape)

# ------------------------------------------------------------
# Passo 2: Pré-processamento dos Dados
# ------------------------------------------------------------

# Dividir o conjunto de dados em treinamento (80%) e teste (20%)
# stratify=y mantém a proporção das 3 espécies nos dois conjuntos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Normalizar os dados (média 0 e desvio padrão 1)
# O scaler aprende apenas com os dados de treino (fit) e depois é aplicado (transform) nos dois
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------------------------------------------------
# Passo 3: Construir o Modelo (rede neural simples)
# ------------------------------------------------------------

# Fixar sementes para resultados reproduzíveis
tf.random.set_seed(42)
np.random.seed(42)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),               # 4 características de entrada
    tf.keras.layers.Dense(16, activation="relu"),    # 1ª camada oculta
    tf.keras.layers.Dense(8, activation="relu"),     # 2ª camada oculta
    tf.keras.layers.Dense(3, activation="softmax"),  # saída: probabilidade de cada uma das 3 espécies
])

# Compilar o modelo
# sparse_categorical_crossentropy é usada porque y contém inteiros (0, 1, 2)
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.summary()

# ------------------------------------------------------------
# Passo 4: Treinar o Modelo
# ------------------------------------------------------------

# Treinar com os dados de treinamento
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=8,
    validation_split=0.2,  # separa 20% do treino para acompanhar a validação
    verbose=0,
)

print("\nTreinamento concluído!")
print(f"Acurácia final no treino: {history.history['accuracy'][-1]:.4f}")
print(f"Acurácia final na validação: {history.history['val_accuracy'][-1]:.4f}")

# ------------------------------------------------------------
# Passo 5: Avaliar o Modelo
# ------------------------------------------------------------

# Avaliar a precisão do modelo usando os dados de teste
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nPerda no teste: {test_loss:.4f}")
print(f"Precisão (acurácia) no teste: {test_accuracy:.4f} ({test_accuracy * 100:.2f}%)")

# ------------------------------------------------------------
# Passo 6: Fazer Previsões
# ------------------------------------------------------------

# 6.1) Previsões com os dados de teste
probabilidades = model.predict(X_test, verbose=0)
classes_previstas = np.argmax(probabilidades, axis=1)

print("\nPrimeiras 10 previsões (dados de teste):")
for i in range(10):
    real = iris.target_names[y_test[i]]
    previsto = iris.target_names[classes_previstas[i]]
    print(f"  Amostra {i + 1}: real = {real:<11} | previsto = {previsto:<11}")

# 6.2) Testar com diferentes entradas (novas flores)
# Formato: [comprimento sépala, largura sépala, comprimento pétala, largura pétala] em cm
novas_flores = np.array([
    [5.1, 3.5, 1.4, 0.2],  # parecida com Setosa
    [6.0, 2.9, 4.5, 1.5],  # parecida com Versicolor
    [6.9, 3.1, 5.4, 2.1],  # parecida com Virginica
])

novas_flores_normalizadas = scaler.transform(novas_flores)

prob_novas = model.predict(novas_flores_normalizadas, verbose=0)
classes_novas = np.argmax(prob_novas, axis=1)

print("\nPrevisões para novas flores:")
for i, flor in enumerate(novas_flores):
    especie = iris.target_names[classes_novas[i]]
    confianca = prob_novas[i][classes_novas[i]] * 100
    print(f"  Entrada {flor.tolist()} -> {especie} (confiança: {confianca:.2f}%)")