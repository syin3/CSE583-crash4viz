#  import packeage
import pandas as pd
import seaborn as sns
import imblearn
import warnings
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import torch
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
from matplotlib.pyplot import rc
import graphviz

# Create the data frame of Traffic Accidents from 2013 - 2017
merged_data_2013 = pd.read_csv('../data/crash-merged/2013.csv')
merged_data_2014 = pd.read_csv('../data/crash-merged/2014.csv')
merged_data_2015 = pd.read_csv('../data/crash-merged/2015.csv')
merged_data_2016 = pd.read_csv('../data/crash-merged/2016.csv')
merged_data_2017 = pd.read_csv('../data/crash-merged/2017.csv')

# Create the data frame of Trffice Accidents from 2017
df_2017= pd.read_csv("../data/crash-merged/2017.csv")

def year_plot(merged_data_2013, merged_data_2014, merged_data_2015, merged_data_2016, merged_data_2017):

    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    plt.bar([2013, 2014, 2015, 2016, 2017],\
         [merged_data_2013.shape[0],merged_data_2014.shape[0],\
          merged_data_2015.shape[0],merged_data_2016.shape[0],merged_data_2017.shape[0]])
    ax1.set_title("Accidents count by year")
    plt.ylabel('Accidents count')
    plt.xlabel("Year")
    plt.savefig('../outputs/year_plot.png')


def month_plot(df_2017):
    count_by_month = df_2017['MONTH'].value_counts()
    x = []
    y = []
    for i in range(0,12):
        y.append(i+1)
        x.append(count_by_month[i+1])

    # create the plot
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    ind = np.arange(12)
    ax1.set_title("Accidents count by month")
    plt.bar(y , x)
    plt.ylabel('Accidents count')
    plt.xlabel("Month")
    plt.xticks(ind, ('Jan', 'Feb', 'Mar', 'April', 'May', "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"))
    plt.savefig('../outputs/month_plot.png')


def weekday_plot(df_2017):
    count_by_weekday = df_2017['WEEKDAY'].value_counts()
    # print(count_by_weekday)
    x = []
    y = []
    for i in range(0,7):
        y.append(i+1)
        x.append(count_by_weekday[i+1])
    # print(x)
    # print(y)
    # create the plot
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    ind = np.arange(12)
    ax1.set_title("Accidents count by weekdays")
    plt.bar(y , x)
    plt.ylabel('Accidents count')
    plt.xlabel('Weekday')
    plt.savefig('../outputs/weekday_plot.png')


def weather_plot(df_2017):
    count_by_weather = df_2017['weather'].value_counts()
    # print(count_by_weather)

    s = df_2017.groupby(['weather']).median().index.get_level_values('weather').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_weather[s[i]])/47818*100))
    # print(x)
    # print(y)
    # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    labels = ['Unknown', 'Clear or Partly Cloudy', 'Overcast','Raining',
            'Snowing', 'Fog/Smog/Smoke', 'Sleet/Hail/Freezing Rain','Severe Crosswind',
            'Blowing Sand or Dirt or Snow','other']

    for i in range(len(labels)):
        if x[i] <= 2:
            labels[i] = 'other'


    ax1.set_title("Accidents percentage count by weather")
    plt.pie(x, labels=labels, counterclock=True,
            labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True)
    plt.savefig('../outputs/weather_plot.png')


def road_plot(df_2017):
    count_by_road = df_2017['RDSURF'].value_counts()

    s = df_2017.groupby(['RDSURF']).median().index.get_level_values('RDSURF').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_road[s[i]])/47818*100))
    # print(x)
    # print(y)
    # # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    labels = ['Dry', 'Wet', 'Snow/Slush', 'Ice', 'Sand/Mud/Dirt', 'Oil', 'Standing Water', 'Other', 'Unknown']
    for i in range(len(labels)):
        if x[i] < 2:
            labels[i] = 'other'

    ax1.set_title("Accidents percentage count by roadsurface condition")
    plt.pie(x, labels=labels, counterclock=True,
        labeldistance=1.05, autopct='%.0f%%', pctdistance=0.88, shadow=True)
    plt.savefig('../outputs/road_plot.png')

def light_plot(df_2017):
    count_by_LIGHT = df_2017['LIGHT'].value_counts()
    # print(count_by_LIGHT)

    s = df_2017.groupby(['LIGHT']).median().index.get_level_values('LIGHT').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_LIGHT[s[i]])/47818*100))
    # print(x)
    # print(y)
    # # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    # convert the light number to label
    labels = ['Daylight', 'Dawn', 'Dusk', 'Dark, Street Lights On', 'Dark, Street Lights Off', 'No Street Lights', 'Other', 'Unknown']
    ax1.set_title("Accidents percentage count by day light condition")


    plt.pie(x, labels=labels, counterclock=True,
        labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True)
    plt.rcParams['font.size'] = 15
    plt.savefig('../outputs/light_plot.png')

def ml_prediction(df_2017):
    df = df_2017
    columns = ['CASENO',
           'weather',
           'RDSURF',
           'LIGHT',
           'REPORT']

    df_clean = df[columns]

    # cleanning the na data
    df_clean = df_clean.dropna()

    severity_group = df_clean.groupby('REPORT')
    s = df.groupby(['REPORT']).median().index.get_level_values('REPORT').tolist()
    # print(s)
    severity_names = s
    # convert the severity to number
    severity_list= []
    for condition in df_clean['REPORT']:
        severity_list.append(s.index(condition))


    weather_group = df_clean.groupby('weather')
    s = df.groupby(['weather']).median().index.get_level_values('weather').tolist()

    weather_list = []
    for i in df_clean['weather']:
        weather_list.append(s.index(i))


    ROADWAY_SURFACE_CONDITION_group = df_clean.groupby('RDSURF')
    s = df.groupby(['RDSURF']).median().index.get_level_values('RDSURF').tolist()

    road_list = []
    for i in df_clean['RDSURF']:
        road_list.append(s.index(i))


    LIGHTING_CONDITION_group = df_clean.groupby("LIGHT")
    s = df.groupby(["LIGHT"]).median().index.get_level_values("LIGHT").tolist()

    light_list = []
    for i in df_clean['LIGHT']:
        light_list.append(s.index(i))

    weather_list = np.array(weather_list)
    road_list = np.array(road_list)
    light_list = np.array(light_list)
    severity_list = np.array(severity_list)

    # print(weather_list.shape, road_list.shape, light_list.shape, severity_list.shape)
    # print('weather', np.min(weather_list), np.max(weather_list))
    # print('road_list', np.min(road_list), np.max(road_list))
    # print('light_list', np.min(light_list), np.max(light_list))
    # print('severity_list', np.min(severity_list), np.max(severity_list))


    split = [0.8, 0.2]
    num = len(weather_list)
    train_num = int(num * split[0])
    test_num = num - train_num

    inds = np.random.permutation(np.arange(0, len(weather_list)))
    train_inds = inds[:train_num]
    test_inds = inds[train_num:]

    # traim
    weather_train = weather_list[train_inds].reshape(train_num, 1)
    road_train = road_list[train_inds].reshape(train_num, 1)
    light_train = light_list[train_inds].reshape(train_num, 1)

    X_train = np.hstack((weather_train, road_train, light_train))
    y_train = severity_list[train_inds]

    # test
    weather_test = weather_list[test_inds].reshape(test_num, 1)
    road_test = road_list[test_inds].reshape(test_num, 1)
    light_test = light_list[test_inds].reshape(test_num, 1)

    X_test = np.hstack((weather_test, road_test, light_test))
    y_test = severity_list[test_inds]

    # scale the data
    scaler = StandardScaler()
    scaler.fit(X_train)
    train_data = scaler.transform(X_train)

    test_data = scaler.transform(X_test)

    from sklearn.neural_network import MLPClassifier
    # Training Algorithm
    clf = MLPClassifier(hidden_layer_sizes=(32, 32), alpha=1e-3)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_train)
    # print(clf.score(X_train, y_train, sample_weight=None))

    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier()
    clf = clf.fit(X_train, y_train)
    print("The model accuarcy " +  str(clf.score(X_train, y_train)))
    predictions = clf.predict(X_test)

    importances = clf.feature_importances_
    import matplotlib.pyplot as plt
    # plt.style.use('fivethirtyeight')
    feature_list = ['weather', 'road surface condition', 'Daylight']
    x = list(range(len(importances)))

    plt.bar(x, importances, orientation = 'vertical')
    plt.xticks(x, feature_list, rotation='horizontal')
    plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');
    plt.savefig('../outputs/weather_factor_importance.png')


    # more factors
    from sklearn.preprocessing import LabelEncoder
    lblE = LabelEncoder()
    df_2017_clean = df_2017.dropna()
    for i in df_2017_clean:
        if df_2017_clean[i].dtype == 'object':
            df_2017_clean[i] = df_2017_clean[i].astype('str')
            lblE.fit(df_2017_clean[i])
            df_2017_clean[i] = lblE.transform(df_2017_clean[i])

    column_1 = [
               'WEEKDAY',
               'weather',
               'RDSURF',
               'LIGHT',
               'REPORT',
               'rur_urb']
    new_df = df_2017_clean[column_1]
    X_train, X_test, y_train, y_test = train_test_split(new_df.drop('REPORT', axis=1),
                                                        new_df.REPORT, test_size=0.2, random_state=42)

    clf = RandomForestClassifier()
    clf = clf.fit(X_train, y_train)

    print("The model accuarcy with more factors" +  str(clf.score(X_train, y_train)))
    predictions = clf.predict(X_test)

    importances = clf.feature_importances_
    import matplotlib.pyplot as plt
    # plt.style.use('fivethirtyeight')
    feature_list = [
               'WEEKDAY',
               'weather',
               'RDSURF',
               'LIGHT',
               'rur_urb']
    x = list(range(len(importances)))

    plt.bar(x, importances, orientation = 'vertical')
    plt.xticks(x, feature_list, rotation='horizontal')
    plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');

year_plot(merged_data_2013, merged_data_2014, merged_data_2015, merged_data_2016, merged_data_2017)
month_plot(df_2017)
weekday_plot(df_2017)
weather_plot(df_2017)
road_plot(df_2017)
light_plot(df_2017)
ml_prediction(df_2017)
