Software components: 

+ Data manager: 
    - Provides an interaction to the dataset, i.e. query based on users’ input, such as “2017 + rainy + King County” fed to data manager will return crash records that
        * Happens in 2017;
        * Happened in rainy weather condition;
        * Involved young drivers;

+ Analysis manager:
    - recieves data from data manager and is activated by "generate report" button;
    - conducts mostly descriptive analysis for now;
    - fits statistical models to the data and generate factor importance summary;

+ Visualization manager:
    - is the most important task for our projectis;
    - visualizes crashes on maps;
    - with data from the data manager, generates a base map first and then plot the records on the map, with lat/lon information of the records;
    - also allows for plotting of more complex maps with clusters and layers;
    - only shows user's selected data on the map.


A typical interaction is as follows:
    User select “2017” as a criteria for data. Receiving this button click, the data manager queries the dataset in SQL “SELECT * FROM table WHERE year=2017”. The data subset returned is passed to visualization manager, who renders the base map with these records from the subset and displays the plot on the webpage. Lastly, if the user clicks the analysis button, the analysis manager will generate plots on the data and render a PDF file containing the plots.


Preliminary plan (written at tech review):
Finish functional design of app features, develop test cases, develop the interface, and finally put together examples for publish
