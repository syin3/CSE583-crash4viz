"""Structure and main execution of the GUI. All the functionalities of the
wacrashviz package will be initiated through this interface. The final map
 gets output based on user selections."""

import tkinter as tk
import warnings
from crash4viz import mapping_funcs
from crash4viz import mapping
from crash4viz import mlpredict
import pandas as pd
warnings.filterwarnings('ignore')

class MainApp(tk.Tk):

    """
    The drop-down options described in this class dynamically update based
    on user selections.
    """

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        """Initiate the interface with certain features that will update based
        on user selections."""

        self.title('WA Crash Feature Mapper')
        self.minsize(700, 700)

        self.selection0 = tk.StringVar()
        self.selection0.set('Select year to view')
        options0 = ['2013', '2014', '2015', '2016', '2017']
        self.drop0 = tk.OptionMenu(self, self.selection0, *options0)
        self.drop0.pack()
        self.button0 = tk.Button(self,
                                 text='Save year selection',
                                 command=lambda: self.enable_next_dropdown(self.drop1)).pack()

        self.selection1 = tk.StringVar()
        self.selection1.set('Select county to view')
        options1 = ['Adams',
                    'Asotin',
                    'Benton',
                    'Chelan',
                    'Clallam',
                    'Clark',
                    'Columbia',
                    'Cowlitz',
                    'Douglas',
                    'Ferry',
                    'Franklin',
                    'Garfield',
                    'Grant',
                    'Grays Harbor',
                    'Island',
                    'Jefferson',
                    'King',
                    'Kitsap',
                    'Kittitas',
                    'Klickitat',
                    'Lewis',
                    'Lincoln',
                    'Mason',
                    'Okanogan',
                    'Pacific',
                    'Pend Oreille',
                    'Pierce',
                    'San Juan',
                    'Skagit',
                    'Skamania',
                    'Snohomish',
                    'Spokane',
                    'Stevens',
                    'Thurston',
                    'Wahkiakum',
                    'Walla Walla',
                    'Whatcom',
                    'Whitman',
                    'Yakima']
        self.drop1 = tk.OptionMenu(self, self.selection1, *options1)
        self.drop1.configure(state='disabled')
        self.drop1.pack()
        self.button1 = tk.Button(self,
                                 text='Save county selection',
                                 command=lambda: self.enable_next_dropdown(
                                     self.drop2)).pack()

        self.selection2 = tk.StringVar()
        self.selection2.set('Select group feature to view')
        options2 = [
            'Weather',
            'Surface Condition',
            'Lighting Condition',
            'Day of the week']
        self.drop2 = tk.OptionMenu(self, self.selection2, *options2)
        self.drop2.configure(state='disabled')
        self.drop2.pack()

        self.button2 = tk.Button(self,
                                 text='Save group selection',
                                 command=lambda: self.set_options_init(
                                     self.drop3, self.selection3)).pack()

        self.selection3 = tk.StringVar()
        self.selection3.set('Select subgroup feature to view')
        options3 = 'Select subgroup to view'
        self.drop3 = tk.OptionMenu(self, self.selection3, options3)
        self.drop3.configure(state='disabled')
        self.drop3.pack()
        self.button3 = tk.Button(self,
                                 text='Save subgroup selection',
                                 command=lambda: self.set_map_options(
                                     self.drop4, self.selection4)).pack()

        self.selection4 = tk.StringVar()
        self.selection4.set('Select type of map to view')
        options4 = ['Select type of map to view']
        self.drop4 = tk.OptionMenu(self, self.selection4, *options4)
        self.drop4.configure(state='disabled')
        self.drop4.pack()
        # show the final map based on selections
        self.button4 = tk.Button(self, text='Show map',
                                 command=self.show_map).pack()

        self.button5 = tk.Button(self, text='Generate ML reports',
                                 command=lambda: self.generate_ml(self.selection0.get())).pack()

    def enable_next_dropdown(self, dropdown):
        dropdown.configure(state='normal') # enable drop-down
        
    def set_options_init(self, dropdown, var):
        """Change the options in the third drop-down menu based on the user's
        selection in the second drop-down menu."""

        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.SUBGROUPS_DICT

        if self.selection2.get() in vars_dict.keys():
            dropdown.configure(state='normal') # enable drop-down
            menu = dropdown['menu']
            menu.delete(0, 'end')
            options = subgroups_dict[self.selection2.get()].values()
            for name in options:
                # Add menu items.
                menu.add_command(label=name, command=lambda name=name: var.set(name))

    def set_map_options(self, dropdown, var):
        """Set the different options for types of maps that the user can see
        based on their selections in the previous drop-down menus."""

        dropdown.configure(state='normal')
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = ['Basic road-map',
                   'Cluster map',
                   'Layers by year map',
                   'Cluster & Layer map']
        for name in options:
            menu.add_command(label=name, command=lambda name=name: var.set(name))


    def generate_ml(self, year):
        
        merged_data = pd.read_csv(mapping_funcs.DATA_DIR + f'/{year}.csv')
        month = mlpredict.month_plot(merged_data)
        weekday = mlpredict.weekday_plot(merged_data)
        weather = mlpredict.weather_plot(merged_data)
        road = mlpredict.road_plot(merged_data)
        light = mlpredict.light_plot(merged_data)
        ml_prediction = mlpredict.ml_prediction(merged_data)

        merged_data_2013 = pd.read_csv(mapping_funcs.DATA_DIR + '/2013.csv')
        merged_data_2014 = pd.read_csv(mapping_funcs.DATA_DIR + '/2014.csv')
        merged_data_2015 = pd.read_csv(mapping_funcs.DATA_DIR + '/2015.csv')
        merged_data_2016 = pd.read_csv(mapping_funcs.DATA_DIR + '/2016.csv')
        merged_data_2017 = pd.read_csv(mapping_funcs.DATA_DIR + '/2017.csv')
        years = mlpredict.year_plot(merged_data_2013, merged_data_2014,
                                    merged_data_2015, merged_data_2016, merged_data_2017)
        
    def show_map(self):
        """Output the map that was chosen for the features that were selected,
        output text to inidicate where the final interactable html map is saved
        for the user."""

        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.R_SUBGROUPS_DICT
        incident_dict = mapping_funcs.R_INCIDENT_DICT
        county_dict = mapping_funcs.R_COUNTY_DICT

        year = self.selection0.get()
        county = county_dict[self.selection1.get()]
        county_name = mapping_funcs.COUNTY_DICT[county]
        grp_feature = vars_dict[self.selection2.get()]
        subgrp_feature = subgroups_dict[self.selection2.get()][self.selection3.get()]
        my_map = mapping.Maps() 

        data = mapping_funcs.read_dataframe(year)
        dataframe = data[data.COUNTY == county]
        group_df = dataframe.groupby(grp_feature)
        subgrp_df = group_df.apply(lambda g: g[g['weather'] == subgrp_feature])
        grp_dict = mapping_funcs.GRP_DICT
        group = grp_dict[grp_feature]
            
        if self.selection4.get() == 'Basic road-map':
            
            my_map.basic_map(county_name, county, group, dataframe, subgrp_df)
            if subgrp_df.shape[0] == 0:
                my_text = f'No data for the provided {group} selection, an empty map was generated into the "outputs" folder'
            else:
                my_text = 'Basic map for {}, under {} conditions saved in "outputs" folder'.format(
                    self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Cluster map':
            my_map.plot_folium_filtered_clusters(county_name, county, group, dataframe, subgrp_df)
            if subgrp_df.shape[0] == 0:
                my_text = f'No data for the provided {group} selection, an empty map was generated into the "outputs" folder'
            else:
                my_text = 'Cluster map for {}, under {} conditions saved in "outputs" folder'.format(
                    self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Layers by year map':
            my_map.plot_folium_filtered_layers(group, county_name, county, grp_feature, subgrp_feature)
            my_text = 'Layer map for {}, under {} conditions saved in "outputs" folder'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Cluster & Layer map':
            my_map.plot_folium_filtered_clusters_layers(county_name, county, group, grp_feature, subgrp_feature)
            my_text = 'Cluster & layer map for {}, under {} conditions saved in "outputs" folder'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()


if __name__ == '__main__':
    ROOT = MainApp(None)
    ROOT.mainloop()
