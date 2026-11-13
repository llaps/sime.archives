# Simé Archives

Site de vente et de location de pièces d'archive et contemporaines, par récoltes mensuelles. Ce dossier contient la maquette validée, à transformer en site (cible : Shopify).

## Contenu

- `design-system/` : le design system. Lire d'abord `README.md` (posture, ton, lexique, règles visuelles, décisions), puis `workflow.md` (parcours W, L, B et décisions datées) et `benchmark.md`.
  - `tokens.css` / `tokens.json` : couleurs, typo, espacements.
  - `components/bundle.js` + `bundle.css` : tous les composants (`window.SimeArchives`), les données d'exemple (`products`, `looks`) et la logique (compte à rebours, horloges, filtres).
  - `components/<Nom>/preview.html` : une page ou un composant par dossier. Versions retenues : HomePage, DropPage, ShopPage, ProductPageB, ArchiveSheetB, LocationPageB2.
- `prototype/` : le prototype navigable (ouvrir `index.html` via un petit serveur local, par exemple `python3 -m http.server`). `proto.js` relie les pages.
- `tools/` : scripts qui génèrent le prototype à partir du design system (`build_proto.py`, `gen_lc.py` + `lc_parts.py` pour la page location, `proto_nav.js`). Les chemins des scripts sont à adapter à ce dossier.

## Règles à respecter

- Français, vouvoiement, phrases courtes, pas de superlatifs ni de tirets cadratins. Simé parle de « Simé », jamais « on » ni « la maison ».
- « Récolte » à la place de « drop » dans tout le texte visible. Une récolte par mois, le premier jeudi à 19 h (Paris), accès anticipé à 18 h.
- Vente : pièces uniques, envoi dans toute la France, Outre-mer compris. Les pièces du fonds Archives (`tier: "Archive"`) ne se vendent pas, elles se louent.
- Location : Paris uniquement (retrait à l'atelier ou coursier). Le grand public loue des looks complets ; les pièces à l'unité sont réservées aux pros (formule Shoot pro, sur devis).
- Numéro d'archive `SA-###`, jamais réutilisé, sert de SKU.
- Filet plein entre sections, filet pointillé pour les séparations internes à un bloc et pour les champs de saisie.
- Les citations et phrases d'intention vont dans le Journaling, pas sur les pages de vente.
