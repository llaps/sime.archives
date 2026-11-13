# Workflow

Chaque étape clé du parcours, de la découverte sur Instagram au retour de location, avec un identifiant pour en parler (`W-03`, `L-04`, `B-02`). Pour chaque étape : ce que fait la cliente, ce qui existe déjà dans le système, les bonnes pratiques e-commerce actuelles retenues pour Simé, ce qu'il reste à trancher, et l'indicateur à suivre. On itère étape par étape : une décision prise ici se reporte dans le composant concerné et dans ce fichier.

**Userflows** : les 8 parcours sont dessinés et modifiables dans le composant « Userflows » (groupe Workflow) : achat pendant une récolte, chercher et filtrer, fiche produit, panier et paiement, Location & RP, retour de location, Journaling, coulisses. Chaque étape porte la référence de ce fichier (W-07, L-03…), on peut la déplacer, la renommer, ajouter une note, relier ou supprimer des étapes, puis exporter le parcours pour le partager.

Statuts : **En place** (prototypé dans le système), **À valider** (proposé, à décider à trois), **À faire** (pas encore conçu).

**Pour tester et trancher** : chaque élément En place, À valider ou À faire de ce fichier est repris dans le composant **BenchmarkReview** (groupe Workflow, tableau 02). Pour chaque ligne : le composant où le tester, une case « Testé », une décision Valider ou À revoir, une note. Le bouton « Valider mes retours » produit un récapitulatif à m'envoyer ; les statuts de ce fichier sont mis à jour à partir de lui.

## Vue d'ensemble

| Parcours | Étapes | Objectif principal |
| --- | --- | --- |
| W · Achat d'une pièce | W-01 à W-10 | Vendre une récolte de 6 à 10 pièces en moins de 48 h |
| L · Location & RP | L-01 à L-07 | Transformer une envie de look en réservation confirmée |
| B · Coulisses (équipe) | B-01 à B-08 | Publier une récolte en 2 à 3 h de travail par personne |

Navigation : trois entrées, **Shop**, **Location & RP**, **À propos**. Le Journaling (lookbooks, fiches d'archive, archives caribéennes) vit dans Location & RP.

## W · Parcours d'achat

### W-01 · Découverte (Instagram)
- **La cliente** voit un teasing J-7, le carrousel J-3, ou une story « Amis proches ».
- **En place** : barre d'annonce rotative qui reprend le message de la récolte.
- **En place** : section « Nos éditos » sur l'accueil, alimentée automatiquement par les posts Instagram de shoot (app de flux Instagram, filtrée sur un hashtag maison, ex. #simeedito). Chaque photo ouvre son post dans un nouvel onglet.
- **Bonnes pratiques** : produits identifiés dans les posts (Instagram Shopping relié à Shopify), lien en bio vers la récolte en cours et non vers l'accueil, paramètres UTM par post pour savoir ce qui vend.
- **À valider** : une page d'atterrissage dédiée par récolte, plutôt que l'accueil.
- **Indicateur** : taux de clic Instagram vers le site, ventes attribuées à Instagram.

### W-02 · Arrivée sur l'accueil
- **La cliente** comprend en 3 secondes ce qu'est Simé et quand tombe le prochaine récolte.
- **En place** : accueil immersif (HomePage) séparé de la page récolte (DropPage). L'accueil installe l'univers : grande image, manifeste, la récolte en cours par sa date d'ouverture, portes Shop et Location & RP. Le compte à rebours, l'accès anticipé et les pièces vivent sur la page récolte.
- **Bonnes pratiques** : mobile d'abord (la majorité du trafic viendra d'Instagram), image principale optimisée et chargée en priorité, aucune pop-up à l'arrivée, chargement visé sous 2,5 s sur mobile.
- **Décidé** : aucune pièce à venir n'est montrée sur le site, ni floutée ni sans prix. Le teasing se fait uniquement sur Instagram. L'accueil ne montre que les pièces déjà en vente (« Les pièces disponibles »).
- **Indicateur** : taux de rebond mobile, part des visites qui atteignent le Shop.

### W-03 · Inscription à l'accès anticipé
- **La cliente** laisse son e-mail pour accéder à la récolte une heure avant.
- **En place** : champ unique dans DropCountdown, confirmation en mono.
- **Bonnes pratiques** : un seul champ, consentement explicite (RGPD), e-mail de confirmation immédiat, rappel automatique la veille et à H-1, lien d'accès personnel plutôt qu'un mot de passe partagé.
- **À valider** : ajouter le numéro de téléphone en option pour un rappel SMS.
- **Indicateur** : inscrits par récolte, taux d'ouverture du rappel H-1.

### W-04 · Ouverture de la récolte
- **La cliente** arrive à 18 h (accès anticipé) ou 19 h.
- **Décidé (13 novembre)** : pour commencer, une récolte par mois, le premier jeudi à 19 h (heure de Paris), accès anticipé à 18 h. Le compte à rebours et la date de l'accueil se calent sur ce rythme.
- **En place** : DropPage, la page de la récolte, que visent le lien en bio et les e-mails. Deux statuts : **avant la récolte** (compte à rebours, accès anticipé, pièces encore disponibles des récoltes précédentes, signalées comme telles) et **récolte ouverte** (uniquement les pièces de la récolte en cours, compteur « X pièces sur Y »). Le passage de l'un à l'autre suit la publication programmée de la collection dans Shopify.
- **En place** : collection programmée (cahier des charges), pièces à stock 1.
- **Bonnes pratiques** : pages préchargées et tenues en cache pour encaisser le pic, compteur « X pièces restantes » honnête et mis à jour, pas de faux stock ni de faux compte à rebours.
- **À faire** : état de la page pendant la récolte (pièces qui passent en « Vendue » en direct, sans recharger).
- **Indicateur** : pièces vendues dans la première heure, temps jusqu'au sold out.

### W-05 · Liste des pièces (Shop)
- **La cliente** parcourt, filtre, compare.
- **En place** : ShopPage, ListingToolbar (filtrer, trier, 2 / 3 / 4 colonnes), FilterDrawer (type, marque, époque, matière, disponibilité), encart éditorial.
- **Bonnes pratiques** : filtres alimentés par les fiches produit (voir FilterDrawer), filtres actifs visibles et retirables un par un, nombre de résultats affiché, tri « Nouveautés » par défaut pendant une récolte, taille indiquée sur la vignette (une pièce = une taille).
- **À valider** : un filtre « Ma taille » mémorisé, puisque chaque pièce est unique.
- **Indicateur** : taux de clic vers une fiche produit, usage des filtres.

### W-06 · Vignette produit
- **La cliente** juge la pièce en un regard.
- **En place** : ProductCard. Première vue en gros plan sur la pièce, look complet au survol, ajout rapide, favoris, numéro d'archive et époque.
- **Bonnes pratiques** : deux vues minimum, prix toujours visible, état « Vendue » clair, ajout rapide sans quitter la liste.
- **À valider** : afficher l'état de la pièce (Très bon, Bon) dès la vignette.
- **Indicateur** : ajouts au panier depuis la liste.

### W-07 · Fiche produit
- **La cliente** vérifie l'état, les mesures, et se projette.
- **En place** : ProductPageB, validée le 12 novembre (grande photo, miniatures cliquables, flèches, zoom, iso Lacoste). ProductPage (galerie 2 colonnes) est écartée. Mesures à plat, ligne mannequin sous la taille (« Alima mesure 1,80 m et porte la taille S. »), état, « Comment le porter », étiquette d'inventaire, fiche d'archive, « Louer ce look ».
- **Bonnes pratiques** : mesures à plat comparées à un vêtement de la cliente (guide de mesure illustré), défauts photographiés et nommés, livraison et retours visibles avant l'ajout, bouton d'ajout fixé en bas d'écran sur mobile, zoom.
- **Recommandations (à la SSENSE)** : deux rangées seulement sous la fiche, qui défilent à l'horizontale. 1. « D'autres [type] disponibles » : les pièces du même type (un haut propose d'autres hauts). 2. « Plus de [marque] » : les autres pièces de la même marque. Pièces disponibles uniquement ; une rangée vide n'est pas affichée, et « Sans marque » ou « À identifier » ne compte pas comme une marque.
- **Fiche d'archive** : ArchiveSheetB, validée le 12 novembre, sous la fiche produit : les 4 chapitres visibles à la suite avec un sommaire collant. La version à onglets (ArchiveSheet) est archivée.
- **À valider** : ajouter le bouton fixe sur mobile, alerte « pièces similaires » quand une pièce est vendue.
- **Indicateur** : taux d'ajout au panier par fiche vue.

### W-08 · Panier
- **La cliente** confirme, applique un code, passe au paiement.
- **En place** : CartDrawer en tiroir, réservation 15 min, code promo replié.
- **Bonnes pratiques** : coût de livraison estimé avant le paiement (c'est la première cause d'abandon), seuil de livraison offerte affiché, suggestion « Complète le look » limitée à 2 ou 3 pièces, réservation réelle côté stock et pas seulement affichée.
- **Décidé (13 novembre)** : les pièces achetées s'expédient dans toute la France, Outre-mer compris. La location reste à Paris (retrait à l'atelier ou coursier) pour commencer.
- **À valider** : montant du seuil de livraison offerte, durée de réservation.
- **Indicateur** : taux d'abandon panier, panier moyen.

### W-09 · Paiement (Shopify Checkout)
- **La cliente** paie en moins d'une minute.
- **Bonnes pratiques** : commande sans création de compte, paiement express (Shop Pay, Apple Pay, Google Pay, PayPal), paiement en plusieurs fois pour les pièces Archive (à partir de 150 €), adresse en autocomplétion, mondial relay et point retrait proposés, mention « TVA sur marge » cohérente avec la fiche.
- **À faire** : personnaliser le checkout aux couleurs du système (logo, typographies, `paper`, `ink`).
- **Indicateur** : taux de conversion du checkout, part des paiements express.

### W-10 · Après l'achat
- **La cliente** reçoit, déballe, partage, revient.
- **Bonnes pratiques** : e-mail de confirmation à l'image de la marque (numéro d'archive, photo), suivi de colis, carte avec QR code vers la fiche d'archive (cahier des charges), invitation à partager en story, relance panier abandonné à 1 h et 24 h, accès anticipé à la récolte suivante pour les acheteuses.
- **À faire** : séquence d'e-mails post-achat, politique de retour lisible (14 jours de rétractation).
- **Indicateur** : taux de réachat à 60 jours, partages Instagram.

## L · Parcours Location & RP

### L-01 · Entrée Location & RP
- **La cliente** arrive par le menu, la porte de l'accueil ou « Louer ce look » sur une fiche.
- **En place** : méga-menu (Louer, Pros, Journaling).
- **En place** : LocationPage, une seule page en 4 étapes (pack, looks ou pièces, dates, options) avec récapitulatif fixe à droite (barre en bas sur mobile).
- **À valider** : trois versions de la page, avec une préférence de Laury pour LocationPageB (12 novembre). LocationPage (tout sur une page, archivée le 12 novembre dans le groupe Archives), LocationPageB (pas à pas, une étape à la fois, total et bouton Continuer fixés en bas), LocationPageC (le look d'abord : grille des looks, puis durée, date, stylisme ou photo et retrait dans un panneau latéral).
- **Indicateur** : visites Location issues d'une fiche produit.

### L-02 · Choisir un look
- **Bonnes pratiques** : looks entiers photographiés portés, pièces du look listées, disponibilité visible dès la liste.
- **Décidé (13 novembre)** : le grand public loue des looks complets, stylés par Lou-Ann. Les pièces à l'unité sont réservées aux pros, avec la formule Shoot pro, sur devis. Dit dans le tunnel (étape « Ce que vous portez »), dans la FAQ de la page location et dans l'Aide.
- **En place** : grille des looks du shoot, sélection, prix pour la durée choisie, tag de récolte ou « Pris à ces dates ». La bascule « Un look complet » / « Des pièces à l'unité » n'apparaît qu'avec la formule Shoot pro. Depuis une fiche produit, « Louer le look » ouvre le tunnel avec le look de la pièce sélectionné ; « Une demande pro ? Louer cette pièce seule » ouvre la formule Shoot pro avec la pièce.
- **Vigilance** : un look qui contient une pièce en vente perd cette pièce le jour de la vente. Composer les looks surtout avec le fonds Archives, ou les recomposer.

### L-03 · Dates et formule
- **Bonnes pratiques** : calendrier de disponibilité en direct (The Dress Rental App prévue), prix calculé tout de suite (15 %, 25 %, 35 %, 20 % shoot pro, plancher 30 €), caution et frais de nettoyage annoncés avant la validation.
- **En place** : date de début et durées en boutons (3 jours, 1 semaine, 2 semaines, shoot pro), prix et caution recalculés en direct, plancher 30 €.
- **À faire** : vrai calendrier relié à l'app de location.

### L-04 · Options stylisme et photo
- **Bonnes pratiques** : options en cases à cocher avec prix, exemple de rendu photo, droits d'image dits clairement (Simé garde les droits et peut publier).
- **En place** : 4 packs (Le look, Look + stylisme, Soirée complète, Shoot pro) ; les services inclus sont cochés et verrouillés, les autres en options (stylisme, photo, journée en plus) ; retrait à l'atelier ou coursier dans Paris.
- **À valider** : prix réels du stylisme et de la photo (250 € en exemple), tarif du coursier dans Paris.

### L-05 · Demande pro (stylistes, artistes, marques)
- **Bonnes pratiques** : formulaire court (projet, dates, looks, budget), réponse promise sous 48 h, crédit « RP : @sime.archives » rappelé.
- **En place** : bloc Pros avec formulaire court sur la LocationPage, le pack Shoot pro y renvoie.

### L-06 · Réservation et caution
- **Bonnes pratiques** : empreinte bancaire pour la caution plutôt qu'un débit, conditions de location à cocher, confirmation avec dates et adresse de retrait ou d'envoi.
- **En place** : récapitulatif avec caution par empreinte ; bouton Réserver actif seulement avec une sélection, une date et des looks disponibles.
- **À faire** : écran de confirmation après réservation.

### L-07 · Retour et nettoyage
- **Bonnes pratiques** : rappel J-1 avant le retour, caution libérée sous 48 h après contrôle.
- **Décidé (13 novembre)** : pas d'envoi postal des locations au lancement. Retrait à l'atelier ou coursier dans Paris uniquement. L'envoi France et Antilles-Guyane pourra revenir plus tard.
- **Indicateur** : délai de libération de caution, taux de retours en retard.

## B · Coulisses de l'équipe

| Étape | Qui | Ce qui se passe | Outil |
| --- | --- | --- | --- |
| B-01 Sourcing | Vanina | Achat, classement immédiat en fonds Shop ou Archives | Tableau partagé |
| B-02 Saisie | Vanina | Ligne de fiche : marque (liste), époque, matière, mesures, photo d'étiquette, mannequin du shoot (prénom, taille) | Base partagée, puis Shopify |
| B-03 Shoot | Laury, Lou-Ann | Looks, gros plans par pièce, packshots fond blanc, défauts | Shoot mensuel de 5 h |
| B-04 Rédaction | Autrice du mois | Fiche d'archive, touche Simé, sources vérifiées | Assistant IA puis relecture |
| B-05 Contrôle | Laury | Marque renseignée, prix, photos dans l'ordre (gros plan, look), alt text | Liste de contrôle |
| B-06 Programmation | Laury | Collection de la récolte programmée, accès anticipé, e-mails et posts | Shopify |
| B-07 Expédition | Laury | Emballage, tampon, carte QR, envoi sous 48 h | Boxtal ou Sendcloud |
| B-08 Archivage | Laury | Pièce vendue passe dans les Récoltes passées | Automatique |

**À tester** : saisie assistée par IA à l'étape B-02. Vanina prend 3 photos (pièce, étiquette, détail), une app Shopify ou un assistant pré-remplit un brouillon (titre, type, matière, couleur, marque lue sur l'étiquette, description), puis elle corrige. Rien n'est publié sans relecture. Pistes : RE:Catalog, VintageFlow AI, Thriftify (apps récentes, sans avis), ou un assistant IA relié à Shopify via son API.

**Décidé (13 novembre) · numéro d'archive, pour le back office** : format `SA-###` (SA pour Simé Archives, puis 3 chiffres). Le numéro est attribué à la saisie B-02, dans l'ordre d'entrée à l'inventaire. Il ne change jamais et n'est jamais réutilisé, même après la vente ou la suppression d'une pièce (SA-008 et SA-009, retirées le 13 novembre, restent vacants). Il ne dépend pas de la récolte. Il sert de référence (SKU) dans Shopify et figure sur l'étiquette d'inventaire, la vignette, la fiche, la fiche d'archive et la carte QR du colis. L'année d'entrée et le fonds (Shop ou Archives) sont des champs de la fiche, pas des parties du numéro.

**À valider** : la liste de contrôle B-05 bloque-t-elle la publication (aucune pièce sans marque, sans mesures ou sans gros plan) ?

## Règles transverses

- **Accessibilité** : contrastes du système, navigation clavier, textes alternatifs. L'European Accessibility Act s'applique au e-commerce depuis juin 2025. Les micro-entreprises qui vendent des services en sont exemptées, mais on vise le même niveau.
- **Performance** : images compressées, peu d'applis Shopify, chargement visé sous 2,5 s sur mobile.
- **Confiance** : défauts montrés, mesures réelles, retours clairs, mentions légales et CGV de location accessibles depuis chaque étape de paiement.
- **Mesure** : un tableau de bord simple par récolte (visites, inscrits, ventes en 1 h et en 48 h, panier moyen, abandon) pour décider de la prochaine itération.
