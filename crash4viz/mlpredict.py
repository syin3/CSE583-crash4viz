import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import numpy as np
from . import mapping_funcs
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

# Create the data frame of Traffic Accidents from 2013 - 2017
merged_data_2013 = pd.read_csv(mapping_funcs.DATA_DIR + '/2013.csv')
merged_data_2014 = pd.read_csv(mapping_funcs.DATA_DIR + '/2014.csv')
merged_data_2015 = pd.read_csv(mapping_funcs.DATA_DIR + '/2015.csv')
merged_data_2016 = pd.read_csv(mapping_funcs.DATA_DIR + '/2016.csv')
merged_data_2017 = pd.read_csv(mapping_funcs.DATA_DIR + '/2017.csv')


def year_plot(merged_data_2013, merged_data_2014,
              merged_data_2015, merged_data_2016,
              merged_data_2017, plot_sink=None):

    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    plt.bar([2013, 2014, 2015, 2016, 2017],
            [merged_data_2013.shape[0], merged_data_2014.shape[0],
            merged_data_2015.shape[0], merged_data_2016.shape[0],
            merged_data_2017.shape[0]])
    ax1.set_title("Accidents count by year")
    plt.ylabel('Accidents count')
    plt.xlabel("Year")

    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/year_plot.png')


def month_plot(dataframe, plot_sink=None):
    count_by_month = dataframe['MONTH'].value_counts()
    x = []
    y = []
    for i in range(0, 12):
        y.append(i + 1)
        x.append(count_by_month[i + 1])

    # create the plot
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    ind = np.arange(12)
    ax1.set_title("Accidents count by month")
    plt.bar(y, x)
    plt.ylabel('Accidents count')
    plt.xlabel("Month")
    plt.xticks(ind, ('Jan', 'Feb', 'Mar', 'April', 'May',
                     "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"))
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/month_plot.png')


def weekday_plot(dataframe, plot_sink=None):
    count_by_weekday = dataframe['WEEKDAY'].value_counts()
    # print(count_by_weekday)
    x = []
    y = []
    for i in range(0, 7):
        y.append(i + 1)
        x.append(count_by_weekday[i + 1])
    # print(x)
    # print(y)
    # create the plot
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    ax1.set_title("Accidents count by weekdays")
    plt.bar(y, x)
    plt.ylabel('Accidents count')
    plt.xlabel('Weekday')
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/weekday_plot.png')


def weather_plot(dataframe, plot_sink=None):
    count_by_weather = dataframe['weather'].value_counts()
    # print(count_by_weather)

    s = dataframe.groupby(['weather']).median().\
        index.get_level_values('weather').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_weather[s[i]]) / 47818 * 100))
    # print(x)
    # print(y)
    # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    labels = ['Unknown', 'Clear or Partly Cloudy', 'Overcast', 'Raining',
              'Snowing', 'Fog/Smog/Smoke', 'Sleet/Hail/Freezing Rain',
              'Severe Crosswind', 'Blowing Sand or Dirt or Snow', 'other']

    for i in range(len(labels)):
        if x[i] <= 2:
            labels[i] = 'other'

    ax1.set_title("Accidents percentage count by weather")
    plt.pie(x, labels=labels, counterclock=True,
            labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True)
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/weather_plot.png')


def road_plot(dataframe, plot_sink=None):
    count_by_road = dataframe['RDSURF'].value_counts()

    s = dataframe.groupby(['RDSURF']).median().\
        index.get_level_values('RDSURF').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_road[s[i]]) / 47818 * 100))
    # print(x)
    # print(y)
    # # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    labels = ['Dry', 'Wet', 'Snow/Slush', 'Ice', 'Sand/Mud/Dirt',
              'Oil', 'Standing Water', 'Other', 'Unknown']
    for i in range(len(labels)):
        if x[i] < 2:
            labels[i] = 'other'

    ax1.set_title("Accidents percentage count by roadsurface condition")
    plt.pie(x, labels=labels, counterclock=True,
            labeldistance=1.05, autopct='%.0f%%',
            pctdistance=0.88, shadow=True)
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/road_plot.png')


def light_plot(dataframe, plot_sink=None):
    count_by_LIGHT = dataframe['LIGHT'].value_counts()
    # print(count_by_LIGHT)

    s = dataframe.groupby(['LIGHT']).median().\
        index.get_level_values('LIGHT').tolist()
    # print(s)
    x = []
    y = []
    for i in range(len(s)):
        y.append(s[i])
        x.append(int(int(count_by_LIGHT[s[i]]) / 47818 * 100))
    # print(x)
    # print(y)
    # # create the plot
    fig, ax1 = plt.subplots(figsize=(10, 15))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')

    # convert the light number to label
    labels = ['Daylight', 'Dawn', 'Dusk', 'Dark, Street Lights On',
              'Dark, Street Lights Off', 'No Street Lights',
              'Other', 'Unknown']
    ax1.set_title("Accidents percentage count by day light condition")

    plt.pie(x, labels=labels, counterclock=True,
            labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True)
    plt.rcParams['font.size'] = 15
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/light_plot.png')


def ml_prediction(dataframe, plot_sink=None):
    df = dataframe
    columns = ['CASENO',
               'weather',
               'RDSURF',
               'LIGHT',
               'REPORT']

    df_clean = df[columns]

    # cleanning the na data
    df_clean = df_clean.dropna()

    s = df.groupby(['REPORT']).median().\
        index.get_level_values('REPORT').tolist()

    # convert the severity to number
    severity_list = []
    for condition in df_clean['REPORT']:
        severity_list.append(s.index(condition))

    s = df.groupby(['weather']).median().\
        index.get_level_values('weather').tolist()

    weather_list = []
    for i in df_clean['weather']:
        weather_list.append(s.index(i))

    s = df.groupby(['RDSURF']).median().\
        index.get_level_values('RDSURF').tolist()

    road_list = []
    for i in df_clean['RDSURF']:
        road_list.append(s.index(i))

    s = df.groupby(["LIGHT"]).median().index.get_level_values("LIGHT").tolist()

    light_list = []
    for i in df_clean['LIGHT']:
        light_list.append(s.index(i))

    weather_list = np.array(weather_list)
    road_list = np.array(road_list)
    light_list = np.array(light_list)
    severity_list = np.array(severity_list)

    # split data
    split = [0.8, 0.2]
    num = len(weather_list)
    train_num = int(num * split[0])
    test_num = num - train_num

    inds = np.random.permutation(np.arange(0, len(weather_list)))
    train_inds = inds[:train_num]
    test_inds = inds[train_num:]

    # train
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

    # training model
    from sklearn.neural_network import MLPClassifier
    # Training Algorithm
    clf = MLPClassifier(hidden_layer_sizes=(32, 32), alpha=1e-3)
    clf.fit(X_train, y_train)

    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier()
    clf = clf.fit(X_train, y_train)
    print("The model accuarcy " + str(clf.score(X_train, y_train)))

    importances = clf.feature_importances_
    # plt.style.use('fivethirtyeight')
    feature_list = ['weather', 'road surface condition', 'Daylight']
    x = list(range(len(importances)))

    plt.figure()
    plt.bar(x, importances, orientation='vertical')
    plt.xticks(x, feature_list, rotation='horizontal')
    plt.ylabel('Importance')
    plt.xlabel('Variable')
    plt.title('Variable Importances')
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/weather_factor_importance.png')

    # more factors
    from sklearn.preprocessing import LabelEncoder
    lblE = LabelEncoder()
    df_clean = dataframe.dropna()
    for i in df_clean:
        if df_clean[i].dtype == 'object':
            df_clean[i] = df_clean[i].astype('str')
            lblE.fit(df_clean[i])
            df_clean[i] = lblE.transform(df_clean[i])

    column_1 = ['WEEKDAY',
                'weather',
                'RDSURF',
                'LIGHT',
                'REPORT',
                'rur_urb']
    new_df = df_clean[column_1]
    X_train, X_test, y_train, y_test = train_test_split(new_df.drop('REPORT',
                                                        axis=1),
                                                        new_df.REPORT,
                                                        test_size=0.2,
                                                        random_state=42)

    clf = RandomForestClassifier()
    clf = clf.fit(X_train, y_train)

    print("The model accuracy with more factors " +
          str(clf.score(X_train, y_train)))

    importances = clf.feature_importances_
    # plt.style.use('fivethirtyeight')
    feature_list = ['WEEKDAY',
                    'weather',
                    'RDSURF',
                    'LIGHT',
                    'rur_urb']
    x = list(range(len(importances)))

    plt.figure()
    plt.bar(x, importances, orientation='vertical')
    plt.xticks(x, feature_list, rotation='horizontal')
    plt.ylabel('Importance')
    plt.xlabel('Variable')
    plt.title('Variable Importances')
    if plot_sink is None:
        plot_sink = mapping_funcs.MAPS_DIR
    plt.savefig(plot_sink + '/factors_importance.png')


