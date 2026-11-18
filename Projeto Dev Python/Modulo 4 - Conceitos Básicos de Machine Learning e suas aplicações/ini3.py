from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Carregar dados
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# One-hot encoding dos rótulos
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Construção da rede neural
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))  # 3 classes no iris

# Compilação e treinamento
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, verbose=0)

# Avaliação
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Acurácia com TensorFlow/Keras: {accuracy:.2f}")