from tkinter import *
from mapping import *
from testing import *
import mapping_funcs

root = Tk()
root.title('Traffic Feature Mapper')
root.minsize(800,600)

# functions enabled by the dropdown
def selected_features():
    
    if selected.get() == 'Test':
        feature = 'WEATHER'
        mp = Tests()
        m = mp.plot_folium_test(feature)
    
    if selected.get() == 'Weather':
        feature = 'WEATHER'
        mp = Maps()
        m = mp.plot_folium(feature)
        #display(m)
        
    if selected.get() == 'Surface Condition':
        feature = 'ROADWAY SURFACE CONDITION'
        mp = Maps()
        m = mp.plot_folium(feature)
        #display(m)
    
    

def set_options_init(dropdown, var):
    
    vars_dict = mapping_funcs.vars_dict
    subgroups_dict = mapping_funcs.subgroups_dict
    
    if selection1.get() in vars_dict.values():
        dropdown.configure(state='normal') # enable drop-down
        menu = dropdown['menu']
        menu.delete(0, 'end')
        options = subgroups_dict[selection1.get()]
        for name in options:
            # Add menu items.
            menu.add_command(label=name, command=lambda name=name: var.set(name))
    

    
# create Tkinter variable for group selection
selection1 = StringVar()
# sets default value of the drop-down list
selection1.set('Select group feature to view')

# set drop-down list for group selection
options1 = ['Weather', 'Surface Condition', 'Lighting Condition', 'Junction Relationship', 'Time', 'Test']
drop1 = OptionMenu(root, selection1, *options1)
drop1.grid(row = 0)
drop1.pack()

# set up button to recognize group selection and initialize subgroup drop-down accordingly
button1 = Button(root, text = 'Save group selection', command = lambda: set_options_init(drop2, selection2))
#button1.grid(row = 1)
button1.pack()

# set up subgroup selection variable
selection2 = StringVar()
selection2.set('Select subgroup feature to view')

# set drop-down list for each group's subgroups
options2 = 'Select subgroup to view' # this gets reset when button1 is pressed
drop2 = OptionMenu(root, selection2, options2)
drop2.configure(state = 'disabled')
drop2.pack()

# set up button2 to recognize subgroup selection and initialize incident selection
button2 = Button(root, text = 'Save subgroup selection', command = lambda: set_options_init(drop3, selection3)).pack()

# set up incident selection
selection3 = StringVar()
selection3.set('Select incident type to view')

#option3 = ['Select incident type to view']
#drop3 = OptionMenu(root, selection3, *options3)
#drop3.configure(state = 'disabled')
#drop3.pack()

# show the final map based on selections
#button3 = Button(root, text = 'Show map', command = show_map).pack()


root.mainloop()