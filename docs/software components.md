Software components: 
    (1) Data manager: 
        Provides an interface to the dataset and further provides application features. Since our product allows users to select conditions of all aspects, the most important task for the data manager is to query the dataset. More specifically, the manager will “select” data based on users’ input, such as “2017 + rainy + young driver” fed to data manager will return crash records that 
            (a) Happens in 2017;
            (b) Happened in rainy weather condition;
            (c) Involved young drivers;

    (2) Analysis manager:
        Our users may also be interested in seeing a report of the crashes. To meet this requirement, an analysis manager is in place. Analysis manager waits for a click on the “analyze and generate report” button by the user. When initiated, based on the data by data manager, the analysis manager will plot defined graphs for the data and render a PDF file that is available for download.

    (3) Visualization manager:
        The most important task for our project is to visualize crashes on maps. With data from the data manager, the visualization manager will generate a base map first and then plot the records on the map, with lat/lon information of the records. Users will only see selected data on the map.


A typical interaction is as follows:
    User select “2017” as a criteria for data. Receiving this button click, the data manager queries the dataset in SQL “SELECT * FROM table WHERE year=2017”. The data subset returned is passed to visualization manager, who renders the base map with these records from the subset and displays the plot on the webpage. Lastly, if the user clicks the analysis button, the analysis manager will generate plots on the data and render a PDF file containing the plots.


Preliminary plan:
Finish functional design of app features, develop test cases, develop the interface, and finally put together examples for publish
