# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Simé Archives

Site de vente et de location de pièces d'archive et contemporaines, par récoltes mensuelles. Ce dépôt contient la maquette validée (exportée de Claude Design), à transformer en site (cible : Shopify). Il n'y a ni dépendances, ni étape de build, ni tests : du HTML, du CSS et du JavaScript statiques.

L'utilisatrice est designer et travaille souvent depuis son téléphone : répondre en français, sans jargon, et vérifier soi-même le rendu plutôt que de lui demander de tester.

## Contenu

- `design-system/` : le design system. Lire d'abord `README.md` (posture, ton, lexique, règles visuelles, décisions), puis `workflow.md` (parcours W, L, B et décisions datées) et `benchmark.md`.
  - `tokens.css` / `tokens.json` : couleurs, typo, espacements.
  - `components/bundle.js` + `bundle.css` : tous les composants (`window.SimeArchives`), les données d'exemple (`products`, `looks`) et la logique (compte à rebours, horloges, filtres).
  - `components/<Nom>/preview.html` : une page ou un composant par dossier. Versions retenues : HomePage, DropPage, ShopPage, ProductPageB, ArchiveSheetB, LocationPageB2. Les `README.md` des composants documentent les décisions : les mettre à jour quand on change un comportement.
  - Les sections « generated — do not edit » de `design-system/README.md` renvoient à des fichiers `api/…` propres à Claude Design, absents de ce dépôt.
- `prototype/` : le prototype navigable, publié en ligne. `proto.js` relie les pages.
- `tools/` : scripts qui ont généré le prototype à partir du design system (voir plus bas).

## Architecture

Tout passe par `window.SimeArchives` (`bundle.js`, un seul IIFE) :
- des fonctions qui renvoient des chaînes HTML (`header()`, `productCard(p)`, `footer()`, `cartDrawer()`, `dropCountdown()`…) ;
- `init(root)`, qui branche les comportements sur le HTML injecté via des attributs `data-sa="…"` (horloges `data-sa='clocks'`, compte à rebours, tiroirs, filtres, header masqué au défilement) ;
- les données d'exemple et les helpers (`find("SA-001")`, `shopProducts`, `photos`, `nextRecolte()`).

Chaque page suit le même schéma : `<div class="sa-page" id="r">`, puis un script qui assemble `S.announcementBar() + S.header() + … + S.footer() + S.cartDrawer()` dans `#r`, puis `S.init(document)`. Le `<body>` doit porter la classe `sa`. Les liens des composants restent en `href="#"` ; `prototype/proto.js` les redirige vers la bonne page d'après leur libellé (table `MAP`).

### Deux copies du bundle

`design-system/components/bundle.{js,css}` et `prototype/bundle.{js,css}` ne sont pas identiques : dans la copie du prototype, les URL d'images `/_blob/<hash>` de Claude Design sont remplacées par `photos/<nom>.jpg` (correspondance dans `tools/blobmap.json`). Les aperçus de `design-system/` n'affichent donc pas les photos hors de Claude Design.

**Toute modification d'un composant partagé se fait dans les deux copies** (même remplacement dans chaque fichier), sinon le site en ligne et le design system divergent. Même chose pour `tokens.css`.

### Les scripts de `tools/`

Ils ne tournent pas en l'état : ils attendent l'arborescence d'export de Claude Design (`tools/ds/project/…`) et écrivent dans `tools/proto/`. `gen_lc.py` s'exécute depuis `tools/` (chemins relatifs) et génère les variantes LocationPage à partir de `lc_parts.py`. `recolte.py` remplace « drop » par « récolte » avec les accords. Tant qu'ils ne sont pas adaptés, modifier directement les fichiers de `prototype/` (et reporter dans `design-system/`).

Correspondance des pages : `index.html` ← HomePage, `drop.html` ← DropPage, `shop.html` ← ShopPage, `piece.html` ← ProductPageB (pièce choisie par l'ancre, `piece.html#SA-004`), `location.html` ← LocationPageB2, `archives.html` ← ArchivesPage (vitrine de la location) ; `journal.html` (page d'archive, pièce choisie par l'ancre, `journal.html#SA-005`), `apropos.html` et `aide.html` (Questions fréquentes, ancres `#q-…`) sont écrites dans `build_proto.py` (`journal.html` a depuis été modifiée à la main).

## Commandes

Servir le prototype en local :

```bash
cd prototype && python3 -m http.server 8765
```

Vérifier un changement : charger les pages avec Playwright (préinstallé) et contrôler les erreurs JS (`pageerror`), les réponses 4xx et les images cassées, sur ordinateur et sur mobile (`devices['iPhone 13']`, et 320px de large). Faire une capture du header ou de la zone modifiée.

## Publication

Le dépôt est public. `.github/workflows/pages.yml` publie `prototype/` sur GitHub Pages à chaque push sur `main` : https://llaps.github.io/sime.archives/. À la publication, le workflow ajoute `?v=<commit>` aux liens vers `tokens.css`, `bundle.css`, `bundle.js` et `proto.js` pour contourner le cache des navigateurs ; ne pas versionner ces liens à la main. La session cloud ne peut pas ouvrir `github.io` : vérifier le statut du déploiement via l'API GitHub Actions.

## Règles à respecter

- Français, vouvoiement, phrases courtes, pas de superlatifs ni de tirets cadratins. Simé parle de « Simé », jamais « on » ni « la maison ».
- « Récolte » à la place de « drop » dans tout le texte visible. Une récolte par mois, le premier jeudi à 19 h (Paris), accès anticipé à 18 h.
- Vente : pièces uniques, envoi dans toute la France, Outre-mer compris. Les pièces du fonds Archives (`tier: "Archive"`) ne se vendent pas, elles se louent.
- Location : Paris uniquement (retrait à l'atelier ou coursier). Tout le monde loue des looks complets (15 % de la valeur pour 3 jours, 30 € minimum) et les pièces du fonds Archives à l'unité (20 %, 45 € minimum). Une pièce du Shop se loue seulement dans son look. Un look dont une pièce est vendue sort de la location. Les pros ont la formule Shoot pro, sur devis.
- Numéro d'archive `SA-###`, jamais réutilisé, sert de SKU.
- Filet plein entre sections, filet pointillé pour les séparations internes à un bloc et pour les champs de saisie.
- Les citations et phrases d'intention vont dans le Journaling, pas sur les pages de vente.
- Un seul accent de couleur par vue ; `photocopy` ne porte jamais de texte. Mobile d'abord (trafic Instagram).
