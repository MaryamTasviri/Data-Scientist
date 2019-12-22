from app import app
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition, datasets
import csv
import numpy


@app.route('/')
def home():
    data = pd.read_csv('1-python-basic.csv')
    return data.head().to_html()

@app.route('/maryam')
def home2():
    data = pd.read_csv('1-python-basic.csv')
    fig , ax = plt.subplots()
    data.groupby('Sex')['Survived'].aggregate(lambda x: x.sum() / len(x)).plot(kind='bar')
    fig.savefig('my_plott.png')
    image = "<img src='file:///home/maryamtasviri/Desktop/DataScience/Docker/FlaskDockerWithoutPython/my_plott.png'>"
    return image



@app.route('/pca')
def home3():
    data = pd.read_csv('1-python-basic.csv')
    y = data[['Survived']]
    q = data['Survived']
    data = data.drop('Sex', 1)
    data = data.drop('Name', 1)
    data = data.drop('Cabin', 1)
    data = data.drop('Embarked', 1)
    data = data.drop('Ticket', 1)
    data = data.drop('Survived', 1)
    data["Age"].fillna(data["Age"].median(), inplace=True)
    pca = decomposition.PCA(n_components=2)
    
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents, columns = ['principal component1','principal component2'] )
    finalDf = pd.concat([principalDf,y] , axis =1)
    mindf = finalDf.head()

    X = finalDf.drop('principal component1',1)
    Z = finalDf.drop('principal component2',1)
    fig , ax = plt.subplots()

    plt.scatter(X, Z)
    fig.savefig('scatter_titanic.png')
    return finalDf.to_html()


@app.route('/scatter')
def home4():
    N = 50
    x = numpy.random.rand(N)
    y = numpy.random.rand(N)
    colors = numpy.random.rand(N)
    area = (30 * numpy.random.rand(N))**2  # 0 to 15 point radii

    fig , ax = plt.subplots()
    
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    
    fig.savefig('my_scatter.png')



    a = numpy.array([[ 1, 2, 3, 4, 5, 6, 7, 8 ],
              [ 1, 4, 8, 14, 12, 7, 3, 2 ]])

    categories = numpy.array([0, 2, 1, 1, 1, 2, 0, 0])

    colormap = numpy.array(['r', 'g', 'b'])

    plt.scatter(a[0], a[1], s=100, c=colormap[categories])

    plt.savefig('ScatterClassPlot.png')
    
    return "scatter"