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

Navigation : trois entrées, **Shop**, **Location & RP**, **À propos**. Location & RP a deux sous-entrées : **Archives à louer** (la vitrine de la location) et **Tarifs et options** (le tunnel). Décidé le 16 novembre : le Journaling n'a plus d'entrée propre. Décidé le 17 : l'histoire de chaque pièce se lit en bas de sa fiche produit, sans page séparée.

## W · Parcours d'achat

### W-01 · Découverte (Instagram)
- **La cliente** voit un teasing J-7, le carrousel J-3, ou une story « Amis proches ».
- **En place** : barre d'annonce rotative qui reprend le message de la récolte.
- **En place** : section « Nos éditos » sur l'accueil, alimentée automatiquement par les posts Instagram de shoot (app de flux Instagram, filtrée sur un hashtag maison, ex. #simeedito). Chaque photo ouvre son post dans un nouvel onglet.
- **Bonnes pratiques** : produits identifiés dans les posts (Instagram Shopping relié à Shopify), lien en bio vers la récolte en cours et non vers l'accueil, paramètres UTM par post pour savoir ce qui vend.
- **Décidé (17 novembre)** : une page d'arrivée par récolte : la page récolte ouverte est mise à jour chaque mois, pour chaque récolte.
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
- **Décidé (17 novembre)** : rappel par SMS seulement s'il ne coûte rien ; sinon, l'e-mail reste le seul canal (les SMS sont en général facturés à l'envoi).
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
- **Décidé (17 novembre)** : pas de filtre « Ma taille ».
- **Indicateur** : taux de clic vers une fiche produit, usage des filtres.

### W-06 · Vignette produit
- **La cliente** juge la pièce en un regard.
- **En place** : ProductCard. Première vue en gros plan sur la pièce, look complet au survol, ajout rapide, favoris, numéro d'archive et époque.
- **Bonnes pratiques** : deux vues minimum, prix toujours visible, état « Vendue » clair, ajout rapide sans quitter la liste.
- **Décidé (17 novembre)** : l'état de la pièce s'affiche dès la vignette (« État : très bon »). Champ `condition` des données, « Très bon » par défaut, à saisir au back office.
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
- **Décidé (17 novembre)** : pas de livraison offerte ni de réservation au paiement. La livraison est facturée au coût réel : coursier moyen dans Paris, La Poste ailleurs en France et en Outre-mer. Les taxes de l'Outre-mer (octroi de mer) sont dites dans la FAQ.
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
- **Décidé (16 novembre)** : mieux dissocier achat et location, et rendre la location aussi visible que le Shop. Méga-menu et menu mobile : Archives à louer, Tarifs et options.
- **En place** : ArchivesPage (`archives.html`), la vitrine de la location. Onglets Looks (par défaut) et Pièces (fonds Archives, avec leur prix pour 3 jours), « Comment ça marche » en 3 étapes, bloc Pros. La porte Location de l'accueil et « Louer un look » y mènent.
- **Décidé (17 novembre)** : plus de page d'archive séparée. Chaque pièce, en vente ou en location, n'a qu'une page : sa fiche produit, avec la fiche d'archive en chapitres en bas. Les cartes de looks et de pièces de la vitrine y mènent.
- **En place** : LocationPage, une seule page en 4 étapes (pack, looks ou pièces, dates, options) avec récapitulatif fixe à droite (barre en bas sur mobile).
- **Décidé (17 novembre)** : tunnel allégé. Aucun pourcentage sur les formules ni sur les durées : des prix en euros (« À partir de 45 € », prix de la sélection pour 3 jours, une semaine, deux semaines ; « Sur devis » pour le Shoot pro). Les lignes « en option » disparaissent des cartes, les options restent à l'étape « Les à-côtés ». Le calcul en pourcentage n'apparaît qu'au récapitulatif, replié sous « Comment le total est calculé ». Les boutons « Continuer » restent à gauche, sous l'étape (essai à droite annulé le 17 novembre).
- **Décidé (17 novembre)** : LocationPageB2 est la version retenue du tunnel (une page, les étapes s'ouvrent l'une sous l'autre). LocationPage, LocationPageB et LocationPageC restent dans le design system pour mémoire.
- **Indicateur** : visites Location issues d'une fiche produit.

### L-02 · Choisir un look
- **Bonnes pratiques** : looks entiers photographiés portés, pièces du look listées, disponibilité visible dès la liste.
- **Décidé (16 novembre, remplace la règle du 13)** : tout le monde loue les looks complets et les pièces du fonds Archives à l'unité. Seules les pièces classées Archive au back office (jamais en vente) se louent seules ; une pièce du Shop se loue seulement dans son look. Prix d'une pièce seule : 20 % de sa valeur pour 3 jours, 45 € minimum (semaine 30 %, deux semaines 40 %). Les pros gardent la formule Shoot pro, sur devis. Dit dans le tunnel (étape « Ce que vous portez »), dans la FAQ de la page location et dans la page Questions fréquentes.
- **Vigilance** : disponibilités liées. Une pièce louée seule rend son look indisponible à ces dates, et inversement. L'application de location dans Shopify doit gérer ce lien.
- **Décidé (16 novembre)** : semaine 30 % et deux semaines 40 % pour une pièce seule. Une location coûte toujours moins que la valeur des pièces : le minimum (30 € pour un look, 45 € pour une pièce) ne dépasse jamais la moitié de la valeur.
- **Décidé (17 novembre)** : un look coûte au moins 45 € (au lieu de 30 €). Une pièce seule ne coûte jamais plus que le look qui la contient, à durée égale : son prix est plafonné au prix du look.
- **En place** : grille des looks du shoot, sélection, prix pour la durée choisie, tag de récolte ou « Pris à ces dates ». La bascule « Un look complet » / « Des pièces à l'unité » n'apparaît qu'avec la formule Shoot pro. Depuis une fiche produit, « Louer le look » ouvre le tunnel avec le look de la pièce sélectionné ; « Une demande pro ? Louer cette pièce seule » ouvre la formule Shoot pro avec la pièce.
- **Décidé (16 novembre) · retrait automatique** : dès qu'une pièce d'un look est vendue, le look entier sort de la location (vitrine et tunnel) jusqu'à ce que Lou-Ann le recompose. Dans Shopify : stock de la pièce à zéro, looks masqués. Dans le prototype : `archives.html?vendu=SA-012` simule la vente.
- **Décidé (17 novembre)** : quand une pièce d'un look est vendue, tout le look sort de la location (en place).

### L-03 · Dates et formule
- **Bonnes pratiques** : calendrier de disponibilité en direct (The Dress Rental App prévue), prix calculé tout de suite (15 %, 25 %, 35 %, 20 % shoot pro, plancher 30 €), caution et frais de nettoyage annoncés avant la validation.
- **En place** : date de début et durées en boutons (3 jours, 1 semaine, 2 semaines, shoot pro), prix et caution recalculés en direct, plancher 30 €.
- **À faire** : vrai calendrier relié à l'app de location.

### L-04 · Options stylisme et photo
- **Bonnes pratiques** : options en cases à cocher avec prix, exemple de rendu photo, droits d'image dits clairement (Simé garde les droits et peut publier).
- **En place** : 4 packs (Le look, Look + stylisme, Soirée complète, Shoot pro) ; les services inclus sont cochés et verrouillés, les autres en options (stylisme, photo, journée en plus) ; retrait à l'atelier ou coursier dans Paris.
- **À valider** : prix réels du stylisme et de la photo (250 € chacun dans la maquette) et tarif moyen du coursier dans Paris. Ce sont les montants affichés dans le tunnel.

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

**Décidé (17 novembre)** : la liste de contrôle B-05 ne bloque pas la publication. Le back office affiche une alerte sur chaque champ non rempli (marque, mesures, gros plan).

## Règles transverses

**Décidé (17 novembre, remplace les prix précédents)** : prix de location = un forfait de 15 € par location (nettoyage et préparation), compté une fois quel que soit le nombre de pièces, plus 10 % de la valeur pour 3 jours, 20 % pour une semaine, 30 % pour deux semaines. Même calcul pour un look ou des pièces d'archive. Le minimum de 45 € est supprimé. Une location ne dépasse jamais la moitié de la valeur. Restent à décider : réserver le fonds Archives aux pièces d'au moins 150 € de valeur ; déduire la location du prix d'achat d'une pièce du Shop.


### FAQ (16 novembre)
- **Décidé** : la colonne Aide du pied de page devient **FAQ**, avec les quatre questions les plus posées en liens directs. La page Aide devient « Questions fréquentes » (`aide.html`) : 10 thèmes (récoltes, acheter, tailles et mesures, état et authenticité, livraison, retours, location, pros, codes promo, contact), une question par ligne, chacune avec son ancre (`aide.html#q-retard`).
- **Recherche** (marché du vintage et de la location) : les tailles sont la première cause de retour et de question ; viennent ensuite l'état réel des pièces, l'authenticité, la politique de retour et les frais d'envoi. En location : la caution non rendue, les frais de retard, les dommages et l'essayage sont les premiers motifs de plainte, souvent aggravés par un service client lent. Pour les sorties limitées : pièces vendues pendant le paiement, sentiment d'injustice. Sur la seconde main en général (Vinted, études de consommation) : l'hygiène et l'état arrivent en tête des freins, devant la taille, la confiance, les retours et la transparence des prix ; les litiges portent sur les articles non conformes (taille, couleur, odeur, défaut caché) et sur les frais de retour.
- **Décidé (17 novembre)** : réponses de la FAQ validées : moyens de paiement (carte, Apple Pay, Google Pay, PayPal) et paiement en plusieurs fois dès 150 €, 48 h pour signaler une pièce non conforme, retour à la charge de la cliente si elle change d'avis (pris en charge par Simé si la pièce n'est pas conforme), essayage au retrait à l'atelier, frais de retard à 5 % de la valeur par jour, critères de prix, taxes de l'Outre-mer. À vérifier par un juriste : la rétractation sur la location. À confirmer par l'équipe : la méthode de nettoyage décrite dans la FAQ.

- **Accessibilité** : contrastes du système, navigation clavier, textes alternatifs. L'European Accessibility Act s'applique au e-commerce depuis juin 2025. Les micro-entreprises qui vendent des services en sont exemptées, mais on vise le même niveau.
- **Performance** : images compressées, peu d'applis Shopify, chargement visé sous 2,5 s sur mobile.
- **Confiance** : défauts montrés, mesures réelles, retours clairs, mentions légales et CGV de location accessibles depuis chaque étape de paiement.
- **Mesure** : un tableau de bord simple par récolte (visites, inscrits, ventes en 1 h et en 48 h, panier moyen, abandon) pour décider de la prochaine itération.

### Looks et données (17 novembre)
- **Décidé** : la jupe madras portée sous le denim est une pièce à part (SA-027, look Lin et denim). Chaussettes et collants ne se vendent pas, pour une question d'hygiène. La mannequin des looks Mohair et vichy et Lin et denim est Morgane, 1,78 m, qui porte du S. Ces deux looks sont les plus anciens (Récolte 01) : ils passent en dernier sur la vitrine, la page récolte et le Shop. Les autres looks forment la Récolte 02, la récolte en cours ; la prochaine est la Récolte 03. Le classement vente ou location (SA-014 et SA-018 dans le fonds Archives) sera ajusté au back office.
- **À faire** : une photo seule de la jupe filet SA-013 (faite) et de la jupe madras SA-027 ; un texte de fiche d'archive par pièce ; les données réelles (marques, tailles, prix, époques, état) par Vanina.
