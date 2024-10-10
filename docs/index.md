## Research Question

Le degré d'urbanisation influe t-il beaucoup sur la qualité de logement en terme de pièces par habitant?

## Methodology

To address the research question, we performed a univariate analysis to study the percentage change in the number of rooms per person when moving from a degree 3 urbanization zone to a degree 1 zone in European countries.

First, we retrieved the average number of rooms per person by degree of urbanization from 2003 to 2023 from [https://ec.europa.eu/eurostat/en/](https://example.com/).

Second, we generated three data files from the downloaded dataset. The original file was not directly usable because it contained two parameters per row: the degree of urbanization and the country. We therefore generated three datasets, **deg1**, **deg2**, and **deg3**, corresponding to the average number of rooms per person by urbanization degree from 2003 to 2023 for degree 1, degree 2, and degree 3.

Third, we processed the three datasets in the same way. We cleaned the datasets by removing rows corresponding to groups of countries rather than individual countries. Since there was little fluctuation in the data over time, we calculated the average from 2003 to 2023 for the existing values.

Finally, we generated a new dataset. For each country, we retrieved the average number of rooms per person by urbanization degree for degree 1, degree 2, and degree 3. We then calculated the percentage change in the average number of rooms per person when moving from a degree 3 zone to a degree 1 zone, i.e., from the least urbanized area to the most urbanized area. 


## Visualizations

-Average number of rooms per person from 2003 to 2023 for degree 1 urbanization by country

- Average number of rooms per person from 2003 to 2023 for degree 2 urbanization by country

- Average number of rooms per person from 2003 to 2023 for degree 3 urbanization by country

- Percentage change in the average number of rooms per person when moving from a degree 3 urbanization zone to a degree 1 zone (i.e., from the least urbanized to the most urbanized area)**




## Définitions

 - First-degree urbanization zone refers to highly urbanized areas, typically city centers and large metropolitan zones. These areas are characterized by dense population, intense economic activity, and significant infrastructure development.
For a first-degree urbanization zone, the population density is generally over 5,000 inhabitants per square kilometer, representing the most urbanized spaces with concentrated residential, commercial, and industrial activities.
   
 - Second-degree urbanization zone : refers to areas that are less densely populated than major city centers but still urbanized, such as suburbs or small cities. The population density in these areas is generally lower than in high-density urban centers.
For a second-degree urbanization zone, the population density is typically between 1,000 and 10,000 inhabitants per square kilometer, depending on the specific region.
   
 - Third-degree urbanization zone: refers to areas with lower urban density, often including small towns, peri-urban zones, or semi-rural areas. These zones are less urbanized than city centers and suburban areas, typically serving as transitional spaces between urban and rural areas.
For a third-degree urbanization zone, the population density is generally between 300 and 1,000 inhabitants per square kilometer, depending on the specific region.:
 
## Data

This project uses data from one source:

[https://ec.europa.eu/eurostat/en/](https://example.com/)

## Additional Information

This is the final project for the module Introduction to Data Analytics in Business of the Frankfurt School of Finance & Management. 

### Lecturer:

Prof. Dr. Lucas Böttcher

### Group:

Julie Fasquelle

????

????

