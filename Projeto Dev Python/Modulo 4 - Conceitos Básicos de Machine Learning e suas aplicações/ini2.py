from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Gerar dados de regressão
X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)

# Treinar modelo
reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.predict(X)

# Visualizar
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, y_pred, color='red', label='Regressão Linear')
plt.title("Regressão com Scikit-learn")
plt.legend()
plt.show()