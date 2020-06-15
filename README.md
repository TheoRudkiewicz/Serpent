# Serpent
Dénombrement de chaînes hamiltoniennes dans un graphe rectangulaire

Python 3.7 avec numba

Le pdf présente le problème et résous le cas de graphe rectangle 2xn et 3xn. Les formules sont seulement en partie démontrées. Le code formules_3xn_clean.py permet d'exploiter ces formules. Le codematrice_parcour_sans_try_numba.py et  	matrice_parcour_sans_try_numba_bord.py permettent de calculer pour une taille quelconque mais ont une complexité exponentielle. Dans matrice_parcour_sans_try_numba_bord.py on élague quelques branche en vérifiant si le graphe n'est pas coupé en deux de façon évidente. brut_test.py est un fichier de test pour matrice_parcour_numba.py.
