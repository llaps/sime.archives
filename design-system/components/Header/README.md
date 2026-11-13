# Header

En-tête collant : trois entrées seulement (Shop, Location & RP, À propos) à gauche, logotype au centre, outils à droite (langue, recherche, compte, favoris, panier).

`SimeArchives.header({ active })` où `active` vaut `shop`, `location` ou `about`. Fournir aussi `cartDrawer()` dans la page pour que l'icône panier ouvre le tiroir.

- Survol de **Shop** ou **Location & RP** : méga-menu pleine largeur avec une vignette éditoriale, voile `ink` à 28 % sur la page. Shop : trois colonnes seulement, Le Shop, Par marque, Par époque (le type se filtre dans la page Shop) ; les listes et leurs compteurs viennent des fiches produit, comme les filtres (« Sans marque » et « À identifier » n'apparaissent pas). La colonne Par marque reste masquée tant qu'aucune marque n'est renseignée.
- Location & RP : une seule liste de trois entrées, Louer (le tunnel, où l'on choisit look ou pièces), Tarifs et options, Journaling (décidé le 13 novembre). Pas de rubrique Pros : les pros passent par le formulaire de la page location. Le Journaling n'a pas d'entrée propre dans la barre.
- Shop et Location & RP restent deux entrées séparées, comme dans le cahier des charges.
- Au défilement vers le bas, la barre se masque (glisse vers le haut) dès qu'elle est sortie de l'écran ; au moindre défilement vers le haut, elle revient, en version compacte (56px, sans la ligne des horloges). Comme la barre de menus masquée sur Mac. Elle ne se masque jamais quand le méga-menu est ouvert ou qu'un élément du header a le focus clavier. La barre d'outils du Shop remonte avec elle.
- Sous 900px : burger, logotype réduit, seuls recherche et panier restent. Le burger ouvre un tiroir à gauche avec les trois mêmes entrées dépliables (Shop, Location & RP avec le Journaling, À propos) ; Échap ou la croix le ferment.
- L'en-tête, le menu mobile et le pied de page partagent les mêmes entrées : une modification sur l'un se reporte sur les deux autres.
- Le compteur du panier est le seul élément rond du système (`radius-round`).
- Sous le logotype : deux horloges en direct, « PARIS 14:47:12 · GUADELOUPE / MARTINIQUE 09:47:12 » (fuseaux Europe/Paris et America/Guadeloupe, même heure qu'en Martinique, secondes qui défilent, chiffres à chasse fixe pour que la ligne ne bouge pas), à la place de « PARIS · EST. 2026 ». Masquées en version compacte et sous 900px.
