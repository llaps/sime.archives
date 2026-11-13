# ProductCard

Vignette produit du Shop. Première vue : une photo du shoot recadrée en gros plan sur la pièce. Au survol, elle cède la place au look complet porté, et un panneau d'ajout rapide monte du bas de l'image.

`SimeArchives.productCard(product)` avec `{ id, brand, name, era, eraLabel, type, material, size, price, photos, récolte, tier?, sold? }`, où `photos` commence par le gros plan et finit par le look complet.

- Image A : `photos[0]`, le gros plan sur la pièce, issu des assets « Photos looks - Lookbook + shop ». Image B : le look complet, `lookOf(pièce)` (dernière photo de la pièce). Fondu `duration-swap`, léger zoom 1,03.
- Sur mobile (pas de survol) : les deux images défilent en carrousel horizontal, les tirets en bas indiquent la position.
- Badge haut gauche : l'époque de la pièce (« Années 90 », « Y2K », « Contemporaine », « AH 1999 » pour une saison), précédée de « Archive · » pour les pièces de créateur. La récolte n'y figure plus (redondante dans une liste de récolte, décidé le 13 novembre). La taille est dans la ligne du bas, à côté du prix.
- Méta : marque en `label`, numéro d'archive et époque en `archive` (mono), prix en `price`.
- Pièce vendue (`sold: "jj.mm.aa"`) : image en niveaux de gris, tampon « Vendue » daté en `kraft-deep`, prix gardé en `ink-muted`. Elle reste dans les Récoltes passées pour montrer le niveau de curation.
- Ajout rapide : « Pièce unique » + la seule taille + bouton primaire. Pas de choix de taille, une pièce = une taille.
