import tkinter as tk
#import  mapping
#import testing
#import mapping_funcs
from WAcrashviz import mapping_funcs
from WAcrashviz import mapping
import warnings
warnings.filterwarnings('ignore')

class MainApp(tk.Tk):

    """Structure and main execution of the GUI. The dialogue box drop-down options
    dynamically update based on what feature is selected. The final map gets 
    output based on selections."""
    
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.title('Traffic Feature Mapper')
        self.minsize(800,600)
        self.selection1 = tk.StringVar()
        self.selection1.set('Select group feature to view')
        options1 = [
            'Weather',
            'Surface Condition',
            'Lighting Condition',
            'Junction Relationship',
            'Time', 'Test']
        self.drop1 = tk.OptionMenu(self, self.selection1, *options1)
        self.drop1.grid(row = 0)
        self.drop1.pack()
        
        self.button1 = tk.Button(self,
                            text = 'Save group selection',
                            command = lambda: self.set_options_init(self.drop2, self.selection2)).pack()
        
        self.selection2 = tk.StringVar()
        self.selection2.set('Select subgroup feature to view')
        options2 = 'Select subgroup to view'
        self.drop2 = tk.OptionMenu(self, self.selection2, options2)
        self.drop2.configure(state = 'disabled')
        self.drop2.pack()
        self.button2 = tk.Button(self,
                            text = 'Save subgroup selection',
                            command = lambda: self.set_incidence_options(self.drop3, self.selection3)).pack()

        self.selection3 = tk.StringVar()
        self.selection3.set('Select incident type to view')
        options3 = ['Select incident type to view']
        self.drop3 = tk.OptionMenu(self, self.selection3, *options3)
        self.drop3.configure(state = 'disabled')
        self.drop3.pack()
        self.button3 = tk.Button(self,
                            text = 'Select map type',
                            command = lambda: self.set_map_options(self.drop4, self.selection4)).pack()


        self.selection4 = tk.StringVar()
        self.selection4.set('Select type of map to view')
        options4 = ['Select type of map to view']
        self.drop4 = tk.OptionMenu(self, self.selection4, *options4)
        self.drop4.configure(state = 'disabled')
        self.drop4.pack()
        # show the final map based on selections
        self.button4 = tk.Button(self, text = 'Show map', command = self.show_map).pack()     
        
        
    def set_options_init(self, dropdown, var):

        vars_dict = mapping_funcs.vars_dict
        subgroups_dict = mapping_funcs.subgroups_dict

        if self.selection1.get() in vars_dict.keys():
            dropdown.configure(state='normal') # enable drop-down
            menu = dropdown['menu']
            menu.delete(0, 'end')
            options = subgroups_dict[self.selection1.get()]
            for name in options:
                # Add menu items.
                menu.add_command(label=name, command=lambda name=name: var.set(name))

        return 
    
    def set_incidence_options(self, dropdown, var):

        #vars_dict = mapping_funcs.vars_dict
        #subgroups_dict = mapping_funcs.subgroups_dict
        incident_dict = mapping_funcs.incident_dict

        dropdown.configure(state='normal') #
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = list(incident_dict.keys())
        for name in options:
            menu.add_command(label=name, command=lambda name=name: var.set(name))

        return 
    
    def set_map_options(self, dropdown, var):

        #vars_dict = mapping_funcs.vars_dict
        #subgroups_dict = mapping_funcs.subgroups_dict
        incident_dict = mapping_funcs.incident_dict

        dropdown.configure(state='normal')
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = ['Basic road-map', 
                   'Cluster map', 
                   'Layers by year map', 
                   'Cluster & Layer map']
        for name in options:
            menu.add_command(label=name, command=lambda name=name: var.set(name))

        return
    
    def show_map(self):

        vars_dict = mapping_funcs.vars_dict
        subgroups_dict = mapping_funcs.subgroups_dict
        incident_dict = mapping_funcs.incident_dict

        grp_feature = vars_dict[self.selection1.get()]
        subgrp_feature = self.selection2.get()
        incident_type = incident_dict[self.selection3.get()]
        df = mapping_funcs.clean_dataframe()
        mp = mapping.Maps()

        if self.selection4.get() == 'Basic road-map':
            m = mp.basic_map(
                grp_feature, subgrp_feature, incident_type, df)
            tx = 'Basic map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get()) 
            myLabel = tk.Label(root, text = tx).pack()
            return m

        elif self.selection4.get() == 'Cluster map':
            m = mp.plot_folium_filtered_clusters(
                grp_feature, subgrp_feature, incident_type, df)
            tx = 'Cluster map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get()) 
            myLabel = tk.Label(root, text = tx).pack()

            return m
        elif self.selection4.get() == 'Layers by year map':
            m = mp.plot_folium_filtered_layers(
                grp_feature, subgrp_feature, incident_type, df)
            tx = 'Layer map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get()) 
            myLabel = tk.Label(root, text = tx).pack()

            return m
        elif self.selection4.get() == 'Cluster & Layer map':
            m = mp.plot_folium_filtered_clusters_layers(
                grp_feature, subgrp_feature, incident_type, df)
            tx = 'Cluster & layer map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get()) 
            myLabel = tk.Label(root, text = tx).pack()

            return m


if __name__ == '__main__':
    root = MainApp(None)
    root.mainloop()
