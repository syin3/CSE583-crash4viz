from tkinter import *
from mapping import *
from testing import *

root = Tk()
root.title('Traffic Feature Mapper')
root.state('zoomed')

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
    
selected = StringVar() # creates Tkinter variable
# sets default value of the drop-down list
selected.set('Select crash and road features to view on map')

# set up the drop-down list
options = ['Weather', 'Surface Condition', 'Lighting Condition', 'Junction Relationship', 'Time', 'Test']
drop = OptionMenu(root, selected, *options)
drop.pack()

# reveal the map
button = Button(root, text = 'Show Map', command = selected_features).pack()

root.mainloop()