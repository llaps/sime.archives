# FilterDrawer

Tiroir de filtres qui glisse depuis la gauche, en accordéons : Type, Marque, Époque, Matière, Disponibilité.

`SimeArchives.filterDrawer({ static })`. `static: true` l'affiche en place (documentation).

Les options et leurs comptes sont calculés à partir des pièces (`SimeArchives.products`) : une nouvelle marque saisie apparaît seule dans le filtre. La section Marque est ouverte par défaut, juste après Type, et affiche un champ de recherche dès qu'il y a plus de 6 marques. Les marques sont triées par nombre de pièces. Tous les filtres (type, marque, époque, matière, pièces vendues) se combinent et filtrent la grille en direct ; les filtres actifs s'affichent en pastilles dans la barre d'outils et le bouton du bas se met à jour (« Voir 3 pièces »). Échap ou le voile ferment le tiroir.
## Mise à jour automatique (Shopify)

Les filtres ne se saisissent jamais à la main : ils se lisent dans les champs de chaque fiche produit. Dès qu'une fiche est enregistrée ou qu'une pièce est vendue, les options et les comptes se mettent à jour, sans autre action.

| Filtre | Champ Shopify de la fiche | Règle de saisie |
| --- | --- | --- |
| Type de pièce | Type de produit | Liste fermée : Veste, Haut, Maille, Pantalon, Jupe, Chaussures, Accessoire |
| Marque | Fournisseur (vendor), relié à une liste « Marques » | Obligatoire. Toujours choisie dans la liste, jamais tapée librement. « Sans marque » si l'étiquette est absente, « À identifier » tant que la recherche est en cours |
| Époque | Métachamp `custom.epoque` (liste) | Années 70, 80, 90, 2000, 2010 |
| Matière | Métachamp `custom.matiere` (liste) | Matière principale de l'étiquette de composition |
| Taille | Option de variante | Taille indiquée, les mesures à plat restent dans la fiche |
| Disponibilité | Stock (1 ou 0) | Passe seul en « Vendue » à la vente |

Les filtres de la boutique se règlent une fois dans l'appli gratuite Shopify Search & Discovery, en choisissant ces champs.

## Identifier les marques

- **Une liste de marques unique** (métaobjet « Marque » : nom, pays, années, lien vers sa fiche d'archive). Elle évite les doublons du type « Girbaud » et « Marithé + François Girbaud », qui couperaient le filtre en deux.
- **Identification à la saisie** : Vanina photographie l'étiquette d'origine. Dans le processus semi-automatisé du cahier des charges, l'assistant IA lit l'étiquette et propose une marque de la liste. L'auteure valide, ou laisse « À identifier ».
- **Contrôle avant publication** : une fiche sans marque, ou avec « À identifier », ne part pas dans une récolte. « À identifier » n'apparaît jamais dans le filtre côté client.
- Une marque ajoutée à la liste apparaît dans le filtre dès sa première pièce publiée, et disparaît quand sa dernière pièce est vendue, si les pièces vendues sont masquées.
