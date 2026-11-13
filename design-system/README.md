Utilise exclusivement la palette neutre (Écru #F2EDE4, Gris photocopie #B9B6AF) pour l'interface et réserve les couleurs d'accent (Lavande, Vert sauge) à un seul élément par vue, pour préserver l'aspect 'herbier papier'.

## Posture

Simé Archives se lit comme un fonds d'archives, pas comme une boutique. Chaque pièce a un numéro, une époque, une provenance et un texte d'auteure. L'interface est celle d'un magazine de mode (SSENSE, Vogue Runway) posée sur un parcours e-commerce éprouvé (lacoste.fr) : annonce rotative, méga-menu, grille filtrable, vignette qui change d'image au survol, ajout rapide, mini-panier en tiroir, fiche produit à panneau collant.

L'essence est l'hybridation : technique et fourrure, sport et élégance, tradition et futur, archive et présent. Simé mélange des pièces d'archive et des pièces contemporaines dans un même look : une jupe Paloma Wool sur un filet des années 90, des FiveFingers Vibram avec un gilet nylon des années 2000. Une pièce récente entre dans le fonds si elle dialogue avec l'archive ; sa fiche porte alors l'époque « Contemporaine ». Le système la porte par le mélange de trois voix typographiques (grotesque élargie pour les titres, sans neutre pour le texte, mono d'inventaire), jamais par un décor « exotique ».

## Contenu et ton

- Français d'abord, anglais en miroir (FR / EN dans l'en-tête), touches de créole assumées (« Simé » = semé).
- Vouvoiement. Phrases courtes, concrètes, sans superlatif : « Un nylon serré qui froisse comme une enveloppe. »
- Les textes d'auteure sont signés et datés : « Par Vanina · Paris, 12 novembre 2026 ».
- Les défauts sont dits et photographiés : « Légère brillance au genou gauche, visible en photo 03. »
- Pas d'emoji. Pas de point d'exclamation. Pas de « luxe », « exclusif », « must-have ».
- Signature : *Ce qui a été semé revient autrement.* / *What was sown, worn again.*
- Vocabulaire maison : récolte (le nom des mises en vente, choisi le 13 novembre à la place de « drop » ; une récolte par mois pour commencer, le premier jeudi à 19 h, heure de Paris, dans la continuité de Simé, « semé » ; « drop » reste possible sur Instagram en anglais), pièce (jamais « article »), fonds Shop et fonds Archives, fiche d'archive, récoltes passées, Location & RP.

### Le lexique

**Positionnement** : un site vintage pointu, moderne, jeune, audacieux et premium. Pas une maison de luxe : Simé parle comme une bande qui s'y connaît, pas comme une institution. Simé parle d'elle-même par son nom : « Simé chine », « Simé vous la garde ». Ni « on », trop familier, ni « la maison », trop luxe ; « nous » seulement quand les trois fondatrices signent ensemble. Premium dans le soin (photos, mesures, emballage), jamais dans la distance.

La voix de Simé est celle d'une archiviste de mode : elle connaît le jargon du vintage et des maisons, elle l'emploie juste, sans le réciter. Com sans prise de tête, comme chez Nhogirl. Précision du regard, comme sur SSENSE et chez L'Étiquette.

- **Vintage et archive** : chiner, dénicher, pièce d'archive, archives de créateurs, saison (« Automne-Hiver 2003 »), griffe et étiquette, deadstock (jamais portée, étiquette encore là), mesures à plat, tombé, main (le toucher d'une matière), patine, provenance.
- **État, toujours dans cet ordre** : Neuve avec étiquette, Excellent état, Très bon état, Bon état. Le défaut est nommé et photographié, jamais caché.
- **Stylisme** : silhouette, look, vestiaire, superposer, casser une pièce (la porter à contre-emploi), l'hybridation.
- **Ce qu'on n'écrit pas** : « luxe », « la maison » (pour parler de Simé), « savoir-faire d'exception », « exclusif », « must-have », « offre », « le plus demandé », « article », « collection capsule », point d'exclamation, emoji.

### Le créole, par petites touches

Le cahier des charges le dit : un mot de créole quand il a du sens. Règle maison : un seul mot par vue, sur un moment chaleureux (merci, une confirmation, un souhait), et toujours compréhensible dans son contexte ou glosé juste à côté. Jamais sur un bouton d'action, un prix ou une information légale. Jamais en décor.

| Mot | Sens | Où on l'emploie |
| --- | --- | --- |
| Simé | semé | le nom, glosé sous la signature du pied de page |
| Mèsi | merci | confirmations : inscription à l'accès anticipé, lettre des récoltes, demande pro |
| Bèl | belle, beau | « Tout est prêt pour une bèl soirée », récapitulatif de location |
| An nou alé | allons-y | le jour de la récolte, sur Instagram et dans l'e-mail d'ouverture |
| Lakou | la cour commune, le collectif | les événements et la communauté Jardin Créole |
| Grenn | graine | les textes de marque sur l'origine de Simé |

Graphie : celle du créole guadeloupéen et martiniquais (accents graves ouverts : « Mèsi », « Bèl »). En cas de doute, on fait relire par quelqu'un qui le parle au quotidien.

## Couleur

- `paper` est le fond de tout. `paper-deep` sert de fond aux images et aux encarts d'inventaire.
- Texte en `ink`, secondaire en `ink-muted`. `photocopy` ne porte jamais de texte : filets et séparateurs seulement. Les champs et contrôles prennent `rule-strong` pour tenir 3:1.
- Un seul accent par vue, posé sur une seule surface (badge de récolte, encart de citation, compte à rebours). Texte `ink` sur tous les accents, `on-ink` sur `cobalt`.
- `accent` pointe vers l'accent de la récolte en cours (aujourd'hui `lavande`). À chaque récolte ou saison, on change cet alias, comme un fil de madras qui tourne.
- `cobalt` est réservé aux liens du Journaling et à l'anneau de focus (`focus`, 2px plein, décalé de 2px).
- `kraft` pour les aplats et le packaging ; `kraft-deep` quand il devient texte (tampon « Vendue »). Les signatures des auteures passent en `lavande-deep` (#545A9C, version texte de la lavande, 5,4:1 sur `paper`), décidé le 13 novembre.
- Le madras complet n'apparaît qu'en motif ponctuel (papier de soie, doublure), jamais en fond d'interface.

## Typographie

- `display` (Archivo élargi, `font-stretch: 112%`, approche serrée) : titres de récolte (`display`, graisse 600), titres de fiche (`title`), sections (`heading`), chapô italique (`lead`), lettrine (`dropcap`). Même famille que le texte, poussée en largeur : moderne, cohérente avec les pistes de logo, sans serif classique.
- `sans` (Archivo) : texte courant (`body`, `body-sm`), noms de pièces (`product-name`), navigation et boutons (`label`, toujours en capitales espacées 0,16em).
- `mono` (IBM Plex Mono) : tout ce qui relève de l'inventaire. Numéros d'archive, époques, matières, mesures, prix (`archive`, `price`, `countdown`).
- Règle des trois voix : une vignette produit montre toujours la marque en `label`, le nom en `product-name`, le numéro et le prix en mono.
- Une seule famille Google Fonts gratuite (Archivo variable : largeur 62 à 125 %, graisse 100 à 900, italique) plus IBM Plex Mono, chargées par `components/bundle.css`.

## Espace, grille, formes

- Marges latérales `space-6` (40px) sur desktop, `space-4` (16px) sur mobile.
- Grille produit : 4 colonnes par défaut, 2 ou 3 au choix, 2 fixes sous 900px. Gouttières `space-5` / `space-3`.
- Images au ratio 3:4, collées (4px) dans les galeries et les grilles éditoriales, comme une planche contact.
- Angles vifs partout (`radius-none`). `radius-tag` pour l'étiquette d'inventaire, `radius-round` pour le compteur du panier seulement.
- Une seule ombre (`shadow-drawer`) pour les tiroirs. Le reste se sépare par des filets `photocopy`.
- Bloc coloré d'une ligne (`SimeArchives.noteLine(libellé, texte, auteure)`) : fond `accent` de la récolte, libellé mono, texte court. Pour mettre en avant une note ou une contrainte qui compte (note d'archiviste en tête de liste, « Paris uniquement » dans la location). Un seul par vue, jamais deux à la suite, jamais pour de la promotion.
- Fonds Archives (pièces de créateur, `tier: "Archive"`) : ces pièces ne se vendent pas, elles se louent. Elles n'apparaissent ni dans le Shop, ni sur les pages récolte, ni dans les menus, filtres et recommandations ; seulement dans la location. Leur fiche affiche « Fonds Archives · Location uniquement » et un seul bouton, « Louer cette pièce » (décidé le 13 novembre). Dans le code : `SimeArchives.shopProducts` pour la vente, `SimeArchives.products` pour tout le fonds.
- Location (décidé le 13 novembre) : le grand public loue des looks complets, stylés par Lou-Ann ; les pièces à l'unité sont réservées aux pros, formule Shoot pro, sur devis. Une pièce en vente se loue (dans son look) tant qu'elle n'est pas vendue. Sur la fiche produit : « Louer le look · dès X € » (15 % de la valeur du look pour 3 jours, 30 € minimum) et le lien « Une demande pro ? Louer cette pièce seule ». La règle est dite au client dans le tunnel, la FAQ location et l'Aide.
- Époques : « Années 90 », « Y2K » (jamais « Années 2000 »), « Contemporaine », ou la saison pour une pièce de défilé (« Automne-hiver 1999 », abrégé « AH 1999 » sur les vignettes). Même libellé partout : vignettes, fiche, menu, filtres.
- Deux filets, deux rôles. Filet plein `photocopy` : limite entre deux sections ou structure d'un composant (en-tête, tiroir, onglets). Filet pointillé `1px dashed rule-strong` : séparation interne entre deux contenus d'un même bloc (récolte en cours / récolte à suivre, lignes d'accordéon, prix d'un pack, bas du footer). Jamais de pointillé entre deux sections. Les champs de saisie (lettre des récoltes, accès anticipé, formulaires) sont soulignés en pointillé ; le trait redevient plein au focus.

## Images

- Source unique : le groupe d'assets « Photos looks - Lookbook + shop » (le shoot de Laury). Toutes les images produit et éditoriales en viennent, recadrées par pièce (`SimeArchives.photos`).
- Première vue, toujours : une photo issue de ces assets, recadrée en gros plan sur la pièce à vendre (zoom), pour qu'on voie d'abord la pièce, sa matière, sa couleur. C'est l'image par défaut de la vignette et la première de la fiche produit.
- Au survol d'une vignette : la vue portée du look complet (`SimeArchives.lookOf(pièce)`), en fondu `duration-swap`. Sur mobile, les deux vues défilent en carrousel.
- Ordre des vues dans la fiche produit : gros plan sur la pièce, look complet, autres vues portées, puis packshot, dos et défauts.
- Packshots : pièce seule sur fond blanc pur (`packshot`, #FFFFFF), jamais sur papier ou kraft. Ils complètent la fiche produit, ils ne remplacent pas la première vue.
- Les silhouettes SVG de `bundle.js` ne servent que de secours quand une pièce n'a pas encore de photo.
- Jamais de photo de défilé ou de magazine copiée : liens et intégrations officielles seulement.

## Iconographie

Icônes au trait 1,4px, 20px, dessinées dans `components/bundle.js` (`SimeArchives.icon(nom)`) : search, user, heart, bag, menu, close, filter, arrow, clock. Pas d'icône remplie, sauf le cœur actif. Pas d'emoji.

## Logo

Le logotype de l'en-tête est provisoire. Les pistes V2 (page LogoPistes) suivent le board : grotesque grasse et encrée, pochoir étendu, index entre barres, lame Y2K, double trait, semis de lettres. Choix et validation visés le 22 novembre.

## Parcours

- **Navigation** : trois entrées, Shop, Location & RP, À propos. Le Journaling se consulte dans Location & RP. Le détail de chaque étape, avec les bonnes pratiques et ce qu'il reste à itérer, est dans la section Workflow.
- **Accueil (HomePage)** : droit au but, sans décor aspirationnel. Ouverture courte (signature, une phrase sur ce que fait Simé, deux accès), la récolte en cours avec ses quatre premières pièces et le lien vers toute la récolte, une section Récolte à venir (compte à rebours, date, aperçu Instagram, accès anticipé), Acheter ou louer, Nos éditos (Instagram), pied de page. Pas de manifeste, de citation ni de Journaling sur l'accueil : le Journaling reste dans Location & RP.
- **Phrases d'intention et citations** (« Une pièce d'archive n'est pas faite pour dormir au placard… ») : uniquement dans les espaces édito, Journaling et fiches d'archive, via `SimeArchives.editoQuote(texte, auteure)`. Les pages de vente (accueil, Shop, récolte, fiche produit, location) restent factuelles.
- **Page récolte (DropPage)**, deux statuts. 1. Avant la récolte : compte à rebours, accès anticipé, puis « Encore disponibles », les pièces des récoltes précédentes toujours en vente, avec un encart qui précise clairement qu'elles ne font pas partie de la récolte à venir (ou un message si tout est parti). 2. Récolte ouverte : uniquement les pièces de la récolte en cours, avec le nombre de pièces encore disponibles et la note d'archiviste. Le statut bascule tout seul à l'ouverture (publication de la collection de la récolte dans Shopify).
- **Shop** : fil d'Ariane, titre de la récolte, barre d'outils collante, grille avec un encart éditorial en `accent` inséré en 7e position, tiroir de filtres.
- **Fiche produit (ProductPageB, retenue)** : grande photo à gauche avec miniatures cliquables, flèches, compteur et zoom ; panneau à droite (ligne d'inventaire, marque, titre, prix, taille et mesures, ligne mannequin, « Pièce unique », Ajouter au panier, Louer ce look, accordéons) ; puis la fiche d'archive en chapitres (ArchiveSheetB, sans onglets) et deux rangées de recommandations (même type, même marque).
- Le panier s'ouvre en tiroir à chaque ajout, avec une réservation de 15 minutes.

## Accessibilité

Mobile d'abord (trafic Instagram). Textes 4,5:1 minimum, contrôles 3:1, anneau de focus `cobalt` visible, texte alternatif sur chaque image (« Gilet zippé sans manches, nylon gris, portée »), Échap ferme les tiroirs, compte à rebours en `role="timer"`.


---

## Consuming this system (generated — do not edit)

Every path named below is under `project/` in this design system: read `project/api/tokens.md`, not `api/tokens.md`.

`components/bundle.js` defines `window.SimeArchives` (13 components); `components/bundle.css` is its stylesheet; `tokens.css` is every token as a CSS variable plus `@font-face` for the fonts. `components/bundle.css` reads its variables from `tokens.css`. Build any UI by mounting these components; never hand-build a control or draw an icon the system provides.

- **Standalone page:** inline `tokens.css` and `components/bundle.css` in a `<style>`, then `components/bundle.js` as a classic script (a file containing `</style`, `</script` or `<!--` breaks an inline element: write the sequence `<\/style`, `<\/script` or `\x3C!--` in your copy, or load that file by URL).
- **Design canvas:** bring `tokens.css`, `components/bundle.css` and `components/bundle.js` onto the canvas in full, as the canvas type’s design-system components reference says (a server-side copy first where it offers one); in each artboard that uses this system, right after the `support.js` line, load `tokens.css` first, then the stylesheet, then the script; mount with `<x-import component-from-global-scope="SimeArchives.<Comp>" …>`.
- **Slides deck, or any surface that cannot run the bundle:** tokens only — the values are on `api/tokens.md`; the deck takes `tokens.json` by file path for its colour pickers.

**Read, per thing:** a component’s props, parts and examples: `api/components/<Comp>.md`; token values: `api/tokens.md`; stored assets and their paths: `api/assets/<Group>.md`. After this README, fetch the cards and fonts you need in ONE message as parallel calls — none depends on another.

**Two rules.** Before you use a thing — a component, a token group, an icon, an asset — read its card from the index below; a value you did not read from a card is a guess. `tokens.json`, `manifest.json` and `design-system.json` are sources for tools: hand them over. `components/<Comp>/README.md` is the long-form second read a card links to; `SKILL.md` and `artifact-type/` beside them are authoring guidance, not needed to consume the system.

## Index (generated — do not edit)

**Tokens**

- `api/tokens.md` — Every token: surface, text, fill, palette, type, spacing, radius, shadow, duration. (9.6k)

**Icons and assets**

- `api/assets/Other.md` — 1 file, by asset id. (0.7k)
- `api/assets/logo-inspi.md` — 3 files, by asset id. (1.0k)
- `api/assets/Photos-looks-Lookbook-shop.md` — 8 files, by asset id. (1.7k)
- `api/assets/Photos-produits.md` — 27 files, by asset id. (2.9k)

**Components** (`api/components/<Comp>.md`, 25; 12 of them showcase pages)

- **Actions**: `Button` — Bouton rectangulaire en capitales espacées, à angles vifs (radius-none), hauteur 48px
- **Navigation**: `AnnouncementBar` — Barre noire au-dessus de l'en-tête, messages qui défilent toutes les 3,6 s, comme sur lacoste.fr · `Header` — En-tête collant : trois entrées seulement (Shop, Location & RP, À propos) à gauche, logotype au centre, outils à droite (langue, recherche, compte, favoris, pa… · `Footer` — Pied de page : signature de marque en Archivo élargi italique, inscription aux récoltes et à l'accès anticipé par e-mail, puis les mêmes trois entrées que l'en-tê…
- **Shop**: `ProductCard` — Vignette produit du Shop · `ListingToolbar` — Barre collante sous l'en-tête des pages de liste : Filtrer, filtres actifs en pastilles, nombre de pièces, Tri, choix 2 / 3 / 4 colonnes · `FilterDrawer` — Tiroir de filtres qui glisse depuis la gauche, en accordéons : Type, Marque, Époque, Matière, Disponibilité · `CartDrawer` — Mini-panier qui glisse depuis la droite à chaque ajout, sans quitter la page · `Accordion` — Sections repliables de la fiche produit et du tiroir de filtres, séparées par un filet photocopy
- **Éditorial**: `DropCountdown` — Ouverture de l'accueil : la pièce phare à gauche, la récolte à droite avec compte à rebours et inscription à l'accès anticipé · `InventoryLabel` — Étiquette d'inventaire, comme celle attachée à chaque pièce : œillet, numéro d'archive, marque, époque, matière, provenance, taille · `ArchiveSheet` — Version à onglets, écartée : la fiche produit utilise ArchiveSheetB (chapitres visibles à la suite) · `ArchiveSheetB` — Fiche d'archive, proposition 2 : au lieu de deux onglets, quatre chapitres numérotés tous visibles l'un sous l'autre, et un sommaire collant à gauche qui suit…
- **Workflow**: `BenchmarkReview` (showcase page) — BenchmarkReview · `Userflows` (showcase page) — Userflows
- **Site**: `DropPage` (showcase page) — DropPage · `HomePage` (showcase page) — HomePage · `LocationPage` (showcase page) — archive cette propal · `LocationPageB` (showcase page) — LocationPageB · `LocationPageB2` (showcase page) — LocationPageB2 · `LocationPageC` (showcase page) — LocationPageC · `ProductPage` (showcase page) — ProductPage · `ProductPageB` (showcase page) — ProductPageB · `ShopPage` (showcase page) — ShopPage
- **Identité**: `LogoPistes` (showcase page) — LogoPistes
