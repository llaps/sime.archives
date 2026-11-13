# CartDrawer

Mini-panier qui glisse depuis la droite à chaque ajout, sans quitter la page.

`SimeArchives.cartDrawer({ static })`.

- Chaque ligne : vignette 88px, marque, nom, numéro d'archive et taille, prix, Retirer.
- Bandeau de réservation : 15 minutes, en mono, sur `paper-deep`. Il porte l'urgence de la récolte sans couleur d'alerte.
- Une pièce déjà dans le panier ne s'ajoute pas deux fois.
- Code promo : replié par défaut sous les lignes (« Code promo + »), pour ne pas pousser à chercher un code. Un champ souligné en mono majuscules et un bouton texte « Appliquer ». Code valide : ligne de remise au-dessus du sous-total (« SEME10 · −10 % ») et message « Code SEME10 appliqué. ». Code invalide : « Ce code n'est pas valide ou a expiré. », champ souligné en `ink`, sans rouge, annoncé aux lecteurs d'écran.
- Codes de démonstration : SEME10 (−10 %) et AMIS15 (−15 %, liste « Amis proches »). En production, les codes se créent dans Shopify (Remises) et se valident au paiement : le mini-panier ne fait que les transmettre.
