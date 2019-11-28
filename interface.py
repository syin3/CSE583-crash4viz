from tkinter import *
from mapping import *
from testing import *
import mapping_funcs

"""Structure and main execution of the GUI. The dialogue box drop-down options
 dynamically update based on what feature is selected. The final map gets 
 output based on selections."""

root = Tk()
root.title('Traffic Feature Mapper')
root.minsize(800,600)

def set_options_init(dropdown, var):
    
    vars_dict = mapping_funcs.vars_dict
    subgroups_dict = mapping_funcs.subgroups_dict
    
    if selection1.get() in vars_dict.keys():
        dropdown.configure(state='normal') # enable drop-down
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = subgroups_dict[selection1.get()]
        for name in options:
            # Add menu items.
            menu.add_command(label=name, command=lambda name=name: var.set(name))
            
def set_incidence_options(dropdown, var):

    #vars_dict = mapping_funcs.vars_dict
    #subgroups_dict = mapping_funcs.subgroups_dict
    incident_dict = mapping_funcs.incident_dict
    
    dropdown.configure(state='normal') # enable drop-down
    menu = dropdown['menu']
    menu.delete(0, 'end')
    options = list(incident_dict.keys())
    for name in options:
        # Add menu items.
        menu.add_command(label=name, command=lambda name=name: var.set(name))
            

def set_map_options(dropdown, var):

    #vars_dict = mapping_funcs.vars_dict
    #subgroups_dict = mapping_funcs.subgroups_dict
    incident_dict = mapping_funcs.incident_dict
    
    dropdown.configure(state='normal')
    menu = dropdown['menu']
    menu.delete(0, 'end')
    options = ['Basic road-map', 'Cluster map', 'Layers by year map', 'Cluster & Layer map']
    for name in options:
        # Add menu items.
        menu.add_command(label=name, command=lambda name=name: var.set(name))


def show_map():

    vars_dict = mapping_funcs.vars_dict
    subgroups_dict = mapping_funcs.subgroups_dict
    incident_dict = mapping_funcs.incident_dict
    
    grp_feature = vars_dict[selection1.get()]
    subgrp_feature = selection2.get()
    incident_type = incident_dict[selection3.get()]
    df = mapping_funcs.clean_dataframe()
    mp = Maps()
    
    if selection4.get() == 'Basic road-map':
        m = mp.basic_map(
            grp_feature, subgrp_feature, incident_type, df)
        tx = 'Basic map for {}, under {} conditions saved under MyMaps'.format(
            selection3.get(), selection2.get()) 
        myLabel = Label(root, text = tx).pack()
        return m
    
    elif selection4.get() == 'Cluster map':
        m = mp.plot_folium_filtered_clusters(
            grp_feature, subgrp_feature, incident_type, df)
        tx = 'Cluster map for {}, under {} conditions saved under MyMaps'.format(
            selection3.get(), selection2.get()) 
        myLabel = Label(root, text = tx).pack()

        return m
    elif selection4.get() == 'Layers by year map':
        m = mp.plot_folium_filtered_layers(
            grp_feature, subgrp_feature, incident_type, df)
        tx = 'Layer map for {}, under {} conditions saved under MyMaps'.format(
            selection3.get(), selection2.get()) 
        myLabel = Label(root, text = tx).pack()

        return m
    elif selection4.get() == 'Cluster & Layer map':
        m = mp.plot_folium_filtered_clusters_layers(
            grp_feature, subgrp_feature, incident_type, df)
        tx = 'Cluster & layer map for {}, under {} conditions saved under MyMaps'.format(
            selection3.get(), selection2.get()) 
        myLabel = Label(root, text = tx).pack()

        return m
        

# create Tkinter variable for group selection
selection1 = StringVar()
# sets default value of the drop-down list
selection1.set('Select group feature to view')
# set drop-down list for group selection
options1 = [
    'Weather',
    'Surface Condition',
    'Lighting Condition',
    'Junction Relationship',
    'Time', 'Test']
drop1 = OptionMenu(root, selection1, *options1)
drop1.grid(row = 0)
drop1.pack()
# set up button to recognize group selection and initialize subgroup drop-down accordingly
button1 = Button(root,
                 text = 'Save group selection',
                 command = lambda: set_options_init(drop2, selection2)).pack()

# set up subgroup selection variable
selection2 = StringVar()
selection2.set('Select subgroup feature to view')
# set drop-down list for each group's subgroups
options2 = 'Select subgroup to view' # this gets reset when button1 is pressed
drop2 = OptionMenu(root, selection2, options2)
drop2.configure(state = 'disabled')
drop2.pack()
# set up button2 to recognize subgroup selection and initialize incident selection
button2 = Button(root,
                 text = 'Save subgroup selection',
                 command = lambda: set_incidence_options(drop3, selection3)).pack()

# set up incident selection
selection3 = StringVar()
selection3.set('Select incident type to view')
options3 = ['Select incident type to view']
drop3 = OptionMenu(root, selection3, *options3)
drop3.configure(state = 'disabled')
drop3.pack()
# show the final map based on selections
button3 = Button(root,
                 text = 'Select map type',
                 command = lambda: set_map_options(drop4, selection4)).pack()


# another drop-down showing the type of map you want to see?
selection4 = StringVar()
selection4.set('Select type of map to view')
options4 = ['Select type of map to view']
drop4 = OptionMenu(root, selection4, *options4)
drop4.configure(state = 'disabled')
drop4.pack()
# show the final map based on selections
button4 = Button(root, text = 'Show map', command = show_map).pack()


root.mainloop()
