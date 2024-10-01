## Research Question

Le degré d'urbanisation influe t-il beaucoup sur la qualité de logement en terme de pièces par habitant?

## Methodology

Pour répondre à la question de recherche, nous avons effectué une analyse univariée, nous etudions la variation en % du nombre de pièces par habitant lorsque l'on passe d'une zone de degré 3 à zone de degré pour les pays europpeens.

Premièrement nous avons récupéré l'average number of rooms per person by degree of urbanization de 2003 à 2023 from [https://ec.europa.eu/eurostat/en/](https://example.com/).

Deusièmement, nous avons généré trois fichiers de données à partir du fichier téléchargé. En effet le fichier initial n'était pas directement exploitable car il y avait deux paramètres par ligne : le degré d'urbanisation et le pays. On a donc généré trois jeux de données deg1, deg2, deg3 correspondant à l'average number of rooms per person of urbanization de 2003 à 2023 par pays pour le degré 1, le degré 2 et le degré 3. 

Troisièmement, on traite de la même manière les trois jeux de données. On nettoie les jeux de données : suppression des lignes correspondant à un groupe de pays et non à un pays.
Il y a peu de fluctuation des données en fonction du temps, on calcule donc la moyenne de 2003 à 2023 sur les valeurs existantes.

Finalement, On génère un nouveau jeux de données. Pour chaque pays on recupère l'average number of rooms per person urbanization pour le degré 1, le degré 2 et le degré 3. On calcul le pourcentage d'évolution de l'average number of rooms per person urbanization lorsque l'on passe d'une zone de degré 3 à une zone de degré 1 c'est à dire d'une zone la moins urbanisée à une zone la plus urbanisée.


## Visualizations

- average number of rooms per person de 2003 à 2023 pour le degré 1 d'urbanisation par pays

- average number of rooms per person de 2003 à 2023 pour le degré 2 d'urbanisation par pays

- average number of rooms per person de 2003 à 2023 pour le degré 3 d'urbanisation par pays

- pourcentage d'évolution de l'average number of rooms per person urbanization lorsque l'on passe d'une zone de degré 3 à une zone de degré 1 c'est à dire d'une zone la moins urbanisée à une zone la plus urbanisée.


## Définitions

 - zone d'urbanisation de degré 1 :
   
 - zone d'urbanisation de degré 2 :
   
 - zone d'urbanisation de degré 3 :
 
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

