# Button

Bouton rectangulaire en capitales espacées, à angles vifs (`radius-none`), hauteur 48px.

`SimeArchives.button(label, { variant, block, disabled, action, id })`

- `primary` : fond `ink`, texte `on-ink`. Une seule action primaire par vue (Ajouter au panier, Commander).
- `secondary` : bordure `rule-strong`, pour l'action parallèle (Louer ce look).
- `link` : souligné, pour « Toutes les pièces », « Lire la fiche ».
- `disabled` : pièce vendue ou indisponible.

À éviter : coins arrondis, icône seule sans libellé, couleur d'accent sur un bouton.
