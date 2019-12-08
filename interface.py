"""Structure and main execution of the GUI. All the functionalities of the
wacrashviz package will be initiated through this interface. The final map
 gets output based on user selections."""

import tkinter as tk
import warnings
from crash4viz import mapping_funcs
from crash4viz import mapping
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

        self.title('Traffic Feature Mapper')
        self.minsize(700, 700)
        self.selection1 = tk.StringVar()
        self.selection1.set('Select group feature to view')
        options1 = [
            'Weather',
            'Surface Condition',
            'Lighting Condition',
            'Junction Relationship',
            'Time', 'Test']
        self.drop1 = tk.OptionMenu(self, self.selection1, *options1)
        self.drop1.grid(row=0)
        self.drop1.pack()

        self.button1 = tk.Button(self,
                                 text='Save group selection',
                                 command=lambda: self.set_options_init(
                                     self.drop2, self.selection2)).pack()

        self.selection2 = tk.StringVar()
        self.selection2.set('Select subgroup feature to view')
        options2 = 'Select subgroup to view'
        self.drop2 = tk.OptionMenu(self, self.selection2, options2)
        self.drop2.configure(state='disabled')
        self.drop2.pack()
        self.button2 = tk.Button(self,
                                 text='Save subgroup selection',
                                 command=lambda: self.set_incidence_options(
                                     self.drop3, self.selection3)).pack()

        self.selection3 = tk.StringVar()
        self.selection3.set('Select incident type to view')
        options3 = ['Select incident type to view']
        self.drop3 = tk.OptionMenu(self, self.selection3, *options3)
        self.drop3.configure(state='disabled')
        self.drop3.pack()
        self.button3 = tk.Button(self,
                                 text='Select map type',
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



    def set_options_init(self, dropdown, var):
        """Change the options in the second drop-down menu based on the user's
        selection in the first drop-down menu."""

        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.SUBGROUPS_DICT

        if self.selection1.get() in vars_dict.keys():
            dropdown.configure(state='normal') # enable drop-down
            menu = dropdown['menu']
            menu.delete(0, 'end')
            options = subgroups_dict[self.selection1.get()]
            for name in options:
                # Add menu items.
                menu.add_command(label=name, command=lambda name=name: var.set(name))

    def set_incidence_options(self, dropdown, var):
        """Change options in the third drop-down menu based on the user's
        selection in the second drop-down menu (whose options depend on the
        first drop-down menu's selection)."""

        #vars_dict = mapping_funcs.VARS_DICT
        #subgroups_dict = mapping_funcs.SUBGROUPS_DICT
        incident_dict = mapping_funcs.INCIDENT_DICT

        dropdown.configure(state='normal') #
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = list(incident_dict.keys())
        for name in options:
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


    def show_map(self):
        """Output the map that was chosen for the features that were selected,
        output text to inidicate where the final interactable html map is saved
        for the user."""

        vars_dict = mapping_funcs.VARS_DICT
        #subgroups_dict = mapping_funcs.SUBGROUPS_DICT
        incident_dict = mapping_funcs.INCIDENT_DICT

        grp_feature = vars_dict[self.selection1.get()]
        subgrp_feature = self.selection2.get()
        incident_type = incident_dict[self.selection3.get()]
        data = mapping_funcs.clean_dataframe()
        my_map = mapping.Maps()

        if self.selection4.get() == 'Basic road-map':
            my_map.basic_map(
                grp_feature, subgrp_feature, incident_type, data)
            my_text = 'Basic map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Cluster map':
            my_map.plot_folium_filtered_clusters(
                grp_feature, subgrp_feature, incident_type, data)
            my_text = 'Cluster map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Layers by year map':
            my_map.plot_folium_filtered_layers(
                grp_feature, subgrp_feature, incident_type, data)
            my_text = 'Layer map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()

        if self.selection4.get() == 'Cluster & Layer map':
            my_map.plot_folium_filtered_clusters_layers(
                grp_feature, subgrp_feature, incident_type, data)
            my_text = 'Cluster & layer map for {}, under {} conditions saved under MyMaps'.format(
                self.selection3.get(), self.selection2.get())
            tk.Label(ROOT, text=my_text).pack()


if __name__ == '__main__':
    ROOT = MainApp(None)
    ROOT.mainloop()
