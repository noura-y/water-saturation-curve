# Water Saturation Curve

Modélisation de la cloche de saturation de l'eau et étude du diagramme T-s.

## Présentation du projet
Ce projet permet de tracer la courbe de saturation de l'eau (équilibre liquide-vapeur) en fonction de la température et de l'entropie spécifique. Le script met en évidence les points clés de transition de phase de l'eau :
* La courbe de saturation liquide (x = 0)
* La courbe de saturation vapeur (x = 1)
* Le point critique 
* Le point triple (coexistence des phases solide, liquide et gazeuse)

## Technologies
* Python 3
* CoolProp (Accès aux données thermodynamiques de l'eau)
* NumPy (Générations des plages de température)
* Matplotlib (Génération du diagramme T-s)

## Propriétés modélisées
Le script s'appuie sur les tables de données de la bibliothèque CoolProp pour extraire :
* Les entropies spécifiques du liquide et de la vapeur saturée ($kJ/kg/K$)
* Les températures absolues ($K$) converties en degrés Celsius ($°C$)
* Les coordonnées exactes du point critique et du point triple de l'eau
