A broad variety of factors (environmental, physical, etc) contribute to a road’s overall safety and thus it is important to visualize and further to understand how crashes happen. Moreover, both professional and non-professional users need user-friendly interfaces to efficiently query and analyze data. To create such a tool, that integrates sources of data, visualize intermediate results and analyze in deep, is our goal of the project.

There are 3 groups of users of this platform:
    (1) average driver of WA, commoners who drive on WA highways. They do not know how to code and anticipate clear visualizations from the website;
    (2) professional users: city and state planners and police officers. These users understand concepts and phenomena of traffic accidents. However, they are neither programmers and generally want to have easy-to-use analysis reports;
    (3) rofessional developers: knowledgeable transportation engineers. This group of users not only master the knowledge, but they also know how to code. Some developable features should be present and be accessible for developing professional tools.

Data are provided by Highway Safety Information System (HSIS), whose data request page is here. Several aspects of data are available: crashes, roads, grades, vehicles involved. They are organized in separate CSV files that share attributes, which can later serve as KEYS in joining the tables.

Use cases include:
    (1) general visualization: before hitting the road for a trip, average drivers would like to understand risks. They can select time, path, weather, driver age and various other features on the platform and thus visualize what crashes in past years in fact meet their criteria. Through this, drivers will have a good picture how likely it is for an accident to occur in selected conditions. If they are planning in such conditions, they will be more careful.
    (2) professional analysis: planners and police officers are interested in obtaining reports of past crashes. They will select conditions as general users do, and then click “analyze and generate report” button, which will produce standard report figures and allow for download. In the report, there will be plots and statistical analysis of which factors contributed the most to crashes selected.
