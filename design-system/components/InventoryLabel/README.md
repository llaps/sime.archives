# InventoryLabel

Étiquette d'inventaire, comme celle attachée à chaque pièce : œillet, numéro d'archive, marque, époque, matière, provenance, taille.

`SimeArchives.inventoryLabel(product, { fund })` avec `fund` = `Shop` (à vendre) ou `Archives` (location uniquement).

Deux tailles, selon le support :

- **Site : `inventoryLabel(pièce, { compact: true })`.** Une seule ligne mono en haut de la fiche produit : `SA-001 · ANNÉES 2000 · NYLON · PARIS`. Le numéro en `ink`, le reste en `ink-muted`. C'est la référence que la cliente cite en DM ou au SAV, et le marqueur visuel « archive » de la marque, sans prendre de place.
- **Imprimés : l'étiquette complète.** Tout en mono, bordure `rule-strong`, `radius-tag`, œillet. Pour l'étiquette physique attachée à chaque pièce, les visuels Instagram (carrousel d'archive), les cartes de remerciement et l'inventaire de l'équipe (fonds Shop ou Archives).

Ne jamais afficher les deux sur la même vue : sur le site, la ligne suffit.
