# Метод опорных векторов (SCM - support vector machine) - классификация и регрессия
# Разделяющая классификация
# Выбирается линия с максимальным отступом

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC

iris = sns.load_dataset("iris")
#
# # print(iris.head())
#
# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "seposa") | (data["species"] == "versicolor") ]
#
# X = data_df[["sepal_length", "petal_length"]]
# y = data_df["species"]
#
# data_df_seposa = data_df[data_df["species"] == "seposa"]
# data_df_versicolor = data_df[data_df["species"] == "versicolor"]
#
# plt.scatter(data_df_seposa["sepal_length"], data_df_seposa["petal_length"])
# plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])
#
# model = SVC(kernel="linear", C = 1000)
# model.fit(X, y)
# print(model.support_vectors_)
# plt.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1], s=400, facecolor="none", edgecolors="black")
#
# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)
#
# X1_p, X2_p = np.meshgrid(x1_p, x2_p)
# X_p = pd.DataFrame(np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"])
# y_p = model.predict(X_p)
# X_p["species"] = y_p
#
# X_p_seposa = X_p[X_p["species"] == "seposa"]
# X_p_versicolor = X_p[X_p["species"] == "versicolor"]
#
#
# plt.scatter(X_p_seposa["sepal_length"], X_p_seposa["petal_length"], alpha = 0.4)
# plt.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha = 0.4)
#
# # ДЗ. убрать из данных iris часть точек (на которых обучаемся) и убедиться, что на предсказание влают только опорные вектора
#
# plt.show()
#
# model = SVC(kernel="linear", C=1000)
# model.fit(X, y)
# support_vectors = model.support_vectors_
# support_indices = model.support_  # индексы опорных векторов в X
# support_labels = y.iloc[support_indices]
#
# X_support = X.iloc[support_indices]
# y_support = y.iloc[support_indices]
#
# model_support_only = SVC(kernel="linear", C=1000)
# model_support_only.fit(X_support, y_support)
#
# y_p_support_only = model_support_only.predict(X_p[["sepal_length", "petal_length"]])
# X_p["species_support_only"] = y_p_support_only
#
# plt.figure(figsize=(10, 5))
#
# plt.subplot(1, 2, 1)
# plt.title("Оригинальная модель")
# plt.scatter(X_p_seposa["sepal_length"], X_p_seposa["petal_length"], alpha=0.4, label="seposa")
# plt.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.4, label="Versicolor")
# plt.legend()
# plt.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1], s=400, facecolor="none", edgecolors="black")
#
# plt.subplot(1, 2, 2)
# plt.title("Модель только на опорных векторах")
# X_p_s1 = X_p[X_p["species_support_only"] == "seposa"]
# X_p_s2 = X_p[X_p["species_support_only"] == "versicolor"]
# plt.scatter(X_p_s1["sepal_length"], X_p_s1["petal_length"], alpha=0.4, label="seposa")
# plt.scatter(X_p_s2["sepal_length"], X_p_s2["petal_length"], alpha=0.4, label="Versicolor")
# plt.legend()
# plt.scatter(X_support["sepal_length"], X_support["petal_length"], s=400, facecolor="none", edgecolors="red")
#
# plt.tight_layout()
# plt.show()



# В случае, если данные перекрываются, то идеальной границы не существует. У модели существует гиперпараметр, который определяет "размытие" отступа
data = iris[["sepal_length", "petal_length", "species"]]
data_df = data[(data["species"] == "virginica") | (data["species"] == "versicolor") ]

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

data_df_virginica = data_df[data_df["species"] == "virginica"]
data_df_versicolor = data_df[data_df["species"] == "versicolor"]

c_value = [[10000, 1000, 100, 10], [1, 0.1, 0.01, 0.001]]
fig, ax = plt.subplots(2, 4, sharex="col", sharey="row")

for i in range(2):
    for j in range(4):
        ax[i, j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
        ax[i, j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

        # Если C большое, то отступ задается "жестко". Чем меньше С, тем отступ становится более "размытым"

        model = SVC(kernel="linear", C=c_value[i][j])
        model.fit(X, y)

        # print(model.support_vectors_)
        ax[i, j].scatter(model.support_vectors_[:,0], model.support_vectors_[:,1], s=400, facecolor="none", edgecolors="black")

        x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
        x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

        X1_p, X2_p = np.meshgrid(x1_p, x2_p)
        X_p = pd.DataFrame(np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"])
        y_p = model.predict(X_p)
        X_p["species"] = y_p

        X_p_virginica = X_p[X_p["species"] == "virginica"]
        X_p_versicolor = X_p[X_p["species"] == "versicolor"]


        ax[i, j].scatter(X_p_virginica["sepal_length"], X_p_virginica["petal_length"], alpha = 0.1)
        ax[i, j].scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha = 0.1)


plt.show()

# Достоинства
# - Зависимоть от небольшого числа опорных векторов => компактность модели
# - После обучения предсказания проходят очень быстро
# - На работу метода влияют ТОЛЬКО точки, находящиеся возме отступов, поэтому методы подходят для многомерных данных

# Недостатки
# - При большом количестве обучающих образцов могут быть значительные вычислительные затраты
# - большая зависимость от размытости С. Поиск может привести к большим вычислительным затратам
# - У результатов отсутствует вероятностная интерпретация

