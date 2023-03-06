import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

def tfidf(X_train, X_val, X_test):
    
    tfidf= TfidfVectorizer()
    tfidf_train= tfidf.fit_transform(X_train.model)
    tfidf_val= tfidf.transform(X_val.model)
    tfidf_test= tfidf.transform(X_test.model)
    
    return tfidf_train, tfidf_val, tfidf_test

def run_models(y_train, y_val, y_test, tfidf_train, tfidf_val, tfidf_test):  
    y_train= pd.DataFrame(y_train)
    y_val= pd.DataFrame(y_val)
    y_test= pd.DataFrame(y_test)
    
    lm = LogisticRegression().fit(tfidf_train, y_train.language)
    y_train['predict_lm']=  lm.predict(tfidf_train)
    y_val['predict_lm']= lm.predict(tfidf_val)
    y_test['predict_lm']= lm.predict(tfidf_test)

    rf = RandomForestClassifier().fit(tfidf_train, y_train.language)
    y_train['predict_rf']= rf.predict(tfidf_train)
    y_val['predict_rf']= rf.predict(tfidf_val)
    y_test['predict_rf']= rf.predict(tfidf_test)

    knn = KNeighborsClassifier(n_neighbors=3).fit(tfidf_train, y_train.language)
    y_train['predict_knn']= knn.predict(tfidf_train)
    y_val['predict_knn']= knn.predict(tfidf_val)
    y_test['predict_knn']= knn.predict(tfidf_test)

    dt = DecisionTreeClassifier(max_depth=3).fit(tfidf_train, y_train.language)
    y_train['predict_dt']= dt.predict(tfidf_train)
    y_val['predict_dt']= dt.predict(tfidf_val)
    y_test['predict_dt']= dt.predict(tfidf_test)
    
    return y_train, y_val, y_test

def print_confusion_matrix(df,col):
    print('Accuracy: {:.2%}'.format(accuracy_score(df.language, df[col])))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(df[col], df.language))
    print('---')
    print(classification_report(df.language, df[col]))


def print_accuracy(df,col):
    print('Accuracy: {:.2%}'.format(accuracy_score(df.language, df[col])))
    print('---')
    
def accuracy_df(y_train,y_val):
    columns = ['predict_lm', 'predict_rf', 'predict_knn', 'predict_dt']
    name = []
    train = [] 
    val = []
    for c in columns:
        name.append(c)
        train.append(accuracy_score(y_train.language, y_train[c]))
        val.append(accuracy_score(y_val.language, y_val[c]))
    return pd.DataFrame({'model':name,'train':train,'validate':val}).set_index('model')

def viz_models_accuracy(df):
    '''takes in a dataframe and plot a graph to show comparisons models accuracy score on train and valiadate data'''
    df = df.copy()
    df.train = df.train *100
    df.validate = df.validate *100
    ax = df.plot.bar(rot=75)
    ax.spines[['right', 'top']].set_visible(False)
    plt.title('Comparisons of Accuracy')
    plt.xticks(ticks=[0, 1, 2, 3],labels=['Linear Regression', 'Random Forest', 'KNN', 'Decision Tree'])
    plt.ylabel('Accuracy score')
    plt.bar_label(ax.containers[0],fmt='%.0f%%')
    plt.bar_label(ax.containers[1],fmt='%.0f%%')
    plt.show()

def print_baseline(y_train):
    print(round(y_train.value_counts().max()/y_train.value_counts().sum(),2))