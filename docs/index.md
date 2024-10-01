## Research Question

*Le degré d'urbanisation influe t-il beaucoup sur la qualité de logement en terme de pièces par habiatnt?*

## Methodology

*In order to answer the research question, we performed an interval analysis.
First, we obtained the wages and salaries (US dollars) and the wage and salary employment (number of jobs) from 2010 to 2019 from the Regional Economic Accounts (CAINC4) of the Bureau of Economic Analysis - U.S Department of Commerce.

Second, we extrapolated wages and salaries (US dollars) and wage and salary employment (number of jobs) with data from 2010 to 2019 using linear regression to obtain the 2021 data of those variables. We divided both results and obtained the annual average salary by county before taxes for 2021.

Third, we used the Smart Asset's Federal Paycheck Calculator and assumed that the marital status of the average american is single, gets paid monthly, has a salary and is not exempt from taxes. Then, we developed a script that uses as input the average salary before taxes and extracts the monthly "take home salary" from the calculator.

Finally, we divided the monthly mortgage payment for Q2 2021, obtained from the National Association of Realtors, by the monthly "take home salary" to obtain the monthly mortgage payment as percentage of the monthly average salary after taxes. We visualized the interval analysis in the Tableau Dashboard "Mortgage as a Percentage of Salary".*

## Visualizations

*Average American (by county):*

An average American for this research is an American who receives the mean wage and salary by county, this is obtained by dividing wage and salaries by wage and salary employment (See definitions below).

Wages and Salaries:*

The remuneration receivable by employees (including corporate officers) from employers for the provision of labor services. It includes commissions, tips, and bonuses; employee gains from exercising stock options; and pay-in-kind. Judicial fees paid to jurors and witnesses are classified as wages and salaries. Wages and salaries are measured before deductions, such as social security contributions, union dues, and voluntary employee contributions to defined contribution pension plans (Bureau of Economic Analysis. U.S. Department of Commerce).

Wage and Salary Employment:

Wage and salary employment, also referred to as wage and salary jobs, measures the average annual number of full-time and part-time jobs in each area by place of work. All jobs for which wages and salaries are paid are counted. Although compensation paid to jurors, expert legal witnesses, prisoners, and justices of the peace (for marriage fees), is counted in wages and salaries, these activities are not counted as jobs in wage and salary employment.
Corporate directorships are counted as self-employment. The following description of the sources and methods used in estimating wage and salary employment is divided into two sections: Employment in industries covered by unemployment insurance (UI) programs, and employment in industries not covered by UI (Bureau of Economic Analysis. U.S. Department of Commerce).

House at Current Prices:

Median home price (See definition below).

Median Home Price:

Median home value for the 2nd quarter of 2021 was estimated for each county. Home values represent the value of all homes instead of home sales. Base Price Subject to Population Threshold:
The most recent American Community Survey (ACS) data was used, subject to ACS population thresholds. This means that for counties with population less than 65,000, the 5-year ACS estimates were used for the price calculations. Respectively, for counties which have a population at or exceeding the population threshold of 65,000, the 1-year ACS estimates were used (National Association of Realtors).

Monthly Mortgage Payment:

A 10% down payment was used to calculate the monthly mortgage payment assuming a 30-year fixed-rate fully amortizing mortgage. Mortgage payments in this study include only principal and interest payments; actual payments, which are likely to include escrow payments for insurance and taxes, may be higher (National Association of Realtors).
Data

This project uses data from 2 sources:

1. National Association of Realtors
2. Bureau of Economic Analysis. U.S. Department of Commerce.
## Additional Information

This is the final project for the module Introduction to Data Analytics in Business of the Frankfurt School of Finance & Management.

### Lecturer:

Prof. Dr. Lucas Böttcher

### Group:

Franco Sánchez Torres

Parth Shrivastava

Rahul Singh ESSAIDébuguer



  
Lorsqu'on apprend à programmer, on passe un temps long à débuguer. C'est normal!

Ne négligez jamais le temps de débug, ce temps est un temps important pour apprendre. C'est en cherchant à corriger
ses erreurs que l'on modifie petit à petit sa façon de penser et que l'on acquière ainsi les bons réflexes.
