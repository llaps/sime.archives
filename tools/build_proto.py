#!/usr/bin/env python3
"""Construit le prototype navigable Simé Archives à partir des pages du design system."""
import json, os, re, shutil

S = os.path.dirname(os.path.abspath(__file__))
DS = os.path.join(S, 'ds/project')
C = os.path.join(DS, 'components')
OUT = os.path.join(S, 'proto')
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, 'photos'))

bm = json.load(open(os.path.join(S, 'blobmap.json')))
def fix(s):
    return re.sub(r'/_blob/([0-9a-f]{32})', lambda m: 'photos/' + bm[m.group(1)] + '.jpg' if m.group(1) in bm else m.group(0), s)

for f in os.listdir(os.path.join(S, 'photos')):
    shutil.copy(os.path.join(S, 'photos', f), os.path.join(OUT, 'photos', f))
open(os.path.join(OUT, 'tokens.css'), 'w').write(open(os.path.join(DS, 'tokens.css')).read())
open(os.path.join(OUT, 'bundle.css'), 'w').write(open(os.path.join(C, 'bundle.css')).read())
open(os.path.join(OUT, 'bundle.js'), 'w').write(fix(open(os.path.join(C, 'bundle.js')).read()))
shutil.copy(os.path.join(S, 'proto_nav.js'), os.path.join(OUT, 'proto.js'))

HEAD = '<link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css"><script src="bundle.js"></script>'

def page(src, out, title, patches=(), main=False):
    s = open(os.path.join(C, src, 'preview.html')).read()
    s = re.sub(r'^<!-- @dsCard[^\n]*-->\n', '', s)
    for a, b in patches:
        assert a in s, (src, a[:60])
        s = s.replace(a, b)
    s = re.sub(r'<title>[^<]*</title>', '<title>' + title + '</title>', s)
    s = s.replace('<head>', '<head>' + HEAD, 1)
    s = s.replace('</body>', '<script src="proto.js"></script>\n</body>', 1)
    s = fix(s)
    if main:  # la page principale est enveloppée au moment de la publication
        s = re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>', '', s, flags=re.I)
        s = s.replace('</head>', '').replace('<body class="sa">', '<script>document.body.classList.add("sa")</script>')
        s = re.sub(r'</body>\s*</html>\s*$', '', s)
        t = re.search(r'<title>[^<]*</title>', s).group(0)
        s = t + '\n<meta name="description" content="Prototype navigable du site Simé Archives">\n' + s.replace(t, '', 1)
    open(os.path.join(OUT, out), 'w').write(s)

page('HomePage', 'index.html', 'Simé Archives', main=True)
page('DropPage', 'drop.html', 'Récolte 04 · Simé Archives')
page('ShopPage', 'shop.html', 'Shop · Simé Archives')
page('LocationPageB2', 'location.html', 'Location & RP · Simé Archives')
page('ProductPageB', 'piece.html', 'Pièce · Simé Archives', patches=[
    ('var p = S.find("SA-001");',
     'var p = S.find((location.hash || "").replace("#", "")) || S.find("SA-001");\n'
     'var GILET = p.id === "SA-001";'),
    ("'<p style=\"margin:0\">Un nylon gris qui froisse comme une enveloppe. Col montant zippé, cordon à la taille, emmanchures nettes. <a",
     "'<p style=\"margin:0\">' + (GILET ? 'Un nylon gris qui froisse comme une enveloppe. Col montant zippé, cordon à la taille, emmanchures nettes.' : p.name + '. ' + p.material + ', ' + p.era.toLowerCase() + '.') + ' <a"),
    ("<span>Hauts</span>", "<span>' + p.type + '</span>"),
    ('html:"Gilet sans manches, col montant. Nylon, zip court, cordon de serrage à la taille."', 'html:(GILET ? "Gilet sans manches, col montant. Nylon, zip court, cordon de serrage à la taille." : p.name + ". " + p.material + ", " + p.era.toLowerCase() + ".")'),
])
open(os.path.join(OUT, 'piece.html'), 'a')  # touch

# Journaling : la fiche d'archive retenue, dans le gabarit du site
journal = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Journaling · Simé Archives</title>''' + HEAD + '''
<style>html,body{margin:0;background:var(--paper)} .sa-page{height:100vh;overflow-y:auto;overflow-x:hidden;position:relative}
.jr-sheet{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:4px;padding-top:8px;height:clamp(320px,52vh,480px)}
.jr-sheet figure{margin:0;position:relative;background:var(--packshot,#fff);overflow:hidden}
.jr-sheet img{display:block;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.jr-sheet .is-main{grid-row:span 1}
.jr-sheet figcaption{position:absolute;left:8px;bottom:8px;background:var(--paper);padding:2px 6px;font-size:10px;letter-spacing:.06em;text-transform:uppercase}
@media (max-width:900px){.jr-sheet{grid-template-columns:1fr 1fr;height:auto}.jr-sheet img{aspect-ratio:3/4;height:auto}.jr-sheet .is-main{grid-column:1 / -1}}
</style></head>
<body class="sa"><div class="sa-page" id="r"></div>
<script>
var S = window.SimeArchives, p = S.find("SA-001");
document.getElementById("r").innerHTML = S.announcementBar() + S.header({ active: "location" }) +
  '<div class="sa-wrap"><nav class="sa-crumbs" aria-label="Fil d’Ariane"><a href="#">Accueil</a><span><a href="#">Location & RP</a></span><span>Journaling</span></nav></div>' +
  /* Les visuels de la pièce, en planche contact, avant le texte */
  '<section class="sa-wrap jr-sheet" aria-label="Photos de la pièce">' + [[p.photos[0], "La pièce, gros plan"], [p.photos[1], "Portée"], [S.lookOf(p), "Le look complet"], [S.photos.look3, "Lookbook"]].map(function (v, i) { return '<figure' + (i === 0 ? ' class="is-main"' : '') + '><img src="' + v[0] + '" alt="' + p.name + ', ' + v[1].toLowerCase() + '"><figcaption class="sa-mono">' + String(i + 1).padStart(2, "0") + ' · ' + v[1] + '</figcaption></figure>'; }).join("") + '</section>' +
  '<section class="sa-section sa-wrap" style="display:grid;justify-items:center;padding-top:40px">' + S.archiveChapters(p) + '</section>' +
  '<section class="sa-section sa-wrap">' + S.editoQuote() + '</section>' +
  '<section class="sa-section sa-wrap" style="border-top:1px solid var(--photocopy)">' + S.related(p) + '</section>' +
  S.footer() + S.cartDrawer();
S.init(document);
</script><script src="proto.js"></script></body></html>'''
open(os.path.join(OUT, 'journal.html'), 'w').write(fix(journal))

apropos = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>À propos · Simé Archives</title>''' + HEAD + '''
<style>html,body{margin:0;background:var(--paper)} .sa-page{height:100vh;overflow-y:auto;overflow-x:hidden;position:relative}
.ap-hero{position:relative;height:56vh;min-height:360px;overflow:hidden}.ap-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.ap-txt{display:grid;grid-template-columns:1fr 2fr;gap:var(--space-6);padding-top:96px;padding-bottom:96px}
.ap-txt p{margin:0 0 var(--space-4);font-size:18px;line-height:1.6;max-width:62ch}
.ap-txt h1{margin:0;font-family:var(--font-display,var(--font-sans));font-stretch:112%;font-weight:500;font-size:44px;line-height:1}
.ap-team{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-5);padding-bottom:96px}
.ap-team div{border-top:1px solid var(--ink);padding-top:var(--space-3)}.ap-team b{display:block;font-size:20px;font-weight:500}
.ap-ig{display:inline-block;margin-top:6px;font-family:var(--font-mono);font-size:13px;color:var(--ink);text-decoration:underline;text-underline-offset:3px}.ap-ig:hover{text-decoration-thickness:2px}
@media (max-width:900px){.ap-txt,.ap-team{grid-template-columns:1fr}.ap-txt{padding-top:56px;padding-bottom:56px}}
</style></head>
<body class="sa"><div class="sa-page" id="r"></div>
<script>
var S = window.SimeArchives, P = S.photos;
document.getElementById("r").innerHTML = S.announcementBar() + S.header({ active: "about" }) +
  '<figure class="ap-hero" style="margin:0"><img src="' + P.look5 + '" alt="Lookbook Simé, Paris"></figure>' +
  '<section class="ap-txt sa-wrap"><div><span class="sa-mono sa-muted">À PROPOS</span><h1>L’histoire de Simé</h1></div><div>' +
  '<p>Simé est l’initiative de trois femmes originaires de la Caraïbe, passionnées de mode chacune à sa façon. Laury la regarde à travers l’objectif, Lou-Ann la compose en silhouettes, Vanina la déniche là où personne ne pense à chercher.</p>' +
  '<p>Simé veut dire « semé » en créole. C’est le titre du premier livre photo de Laury, sorti en 2023 avec l’exposition qui a lancé Jardin Créole. Le livre était la graine, Jardin Créole ce qui a poussé. Simé Archives, c’est la récolte : ce qui se garde, se transmet et se porte à nouveau.</p>' +
  '<p>Simé chine des pièces d’archive et les mêle à des pièces contemporaines, choisies parce qu’elles dialoguent avec l’archive. De cette hybridation naissent les looks : technique et fourrure, sport et élégance, tradition et futur. Une récolte par mois, des pièces uniques, et un vestiaire à louer pour les soirées, les shoots et les scènes.</p>' +
  '<p class="sa-muted" style="font-size:14px">Texte de maquette, tiré du cahier des charges, à relire par l’équipe.</p></div></section>' +
  '<section class="ap-team sa-wrap">' + [["DIRECTION ARTISTIQUE, PHOTO", "Laury", "kahlory_"], ["STYLISME", "Lou-Ann", "louannsaliou"], ["SOURCING", "Vanina", "giochinini"]].map(function (m) { return '<div><span class="sa-mono sa-muted">' + m[0] + '</span><b>' + m[1] + '</b><a class="ap-ig" href="https://www.instagram.com/' + m[2] + '/" target="_blank" rel="noopener" aria-label="Instagram de ' + m[1] + ', @' + m[2] + ' (nouvel onglet)">@' + m[2] + ' ↗</a></div>'; }).join("") + '</section>' +
  S.footer() + S.cartDrawer();
S.init(document);
</script><script src="proto.js"></script></body></html>'''
open(os.path.join(OUT, 'apropos.html'), 'w').write(fix(apropos))

aide = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Aide · Simé Archives</title>''' + HEAD + '''
<style>html,body{margin:0;background:var(--paper)} .sa-page{height:100vh;overflow-y:auto;overflow-x:hidden;position:relative}
.ai{display:grid;grid-template-columns:1fr 2fr;gap:var(--space-6);padding-top:72px;padding-bottom:96px}
.ai h1{margin:var(--space-2) 0 0;font-family:var(--font-display,var(--font-sans));font-stretch:112%;font-weight:500;font-size:44px;line-height:1}
.ai nav{display:grid;gap:8px;margin-top:var(--space-5);font-size:14px}.ai nav a{color:var(--ink);text-decoration:underline;text-underline-offset:3px}
.ai section{scroll-margin-top:90px}.ai .sa-acc__inner p{margin:0 0 10px;max-width:62ch}
@media (max-width:900px){.ai{grid-template-columns:1fr;padding-top:40px}}
</style></head>
<body class="sa"><div class="sa-page" id="r"></div>
<script>
var S = window.SimeArchives;
var SECS = [
  ["livraison", "Livraison et retours", "<p>Les pièces achetées partent dans toute la France, Outre-mer compris. La location se fait à Paris uniquement pour l’instant, en retrait à l’atelier ou par coursier. Chaque pièce part sous 48 h, dans du papier de soie, avec un tampon au monogramme et une carte qui renvoie à sa fiche d’archive.</p><p>Vous avez 14 jours pour changer d’avis. La pièce revient dans l’état où elle est partie, étiquette Simé comprise.</p>"],
  ["mesures", "Guide des mesures", "<p>Une pièce vintage ne suit pas les tailles d’aujourd’hui : chaque fiche donne les mesures à plat, en centimètres (aisselles, taille, longueur).</p><p>Pour comparer, posez à plat un vêtement à vous qui tombe bien, et mesurez-le de la même façon. La ligne mannequin vous dit aussi qui porte la pièce et dans quelle taille.</p>"],
  ["location", "Conditions de location", "<p>Simé loue des looks complets, stylés par Lou-Ann. Les pièces à l’unité sont réservées aux pros (stylistes, artistes, marques) avec la formule Shoot pro, sur devis. Une pièce en vente se loue tant qu’elle n’est pas vendue.</p><p>Le prix se calcule en pourcentage de la valeur des pièces : 15 % pour 3 jours, 25 % pour une semaine, 35 % pour deux semaines, 20 % par jour pour un shoot pro, jamais moins de 30 €.</p><p>La caution est une empreinte bancaire du montant de la valeur, sans débit, libérée sous 48 h après le retour. Le nettoyage est inclus. Un rappel part la veille du retour.</p>"],
  ["codes", "Codes promo", "<p>Les codes se saisissent dans le panier, rubrique Code promo, et s’appliquent avant le paiement. Ils arrivent avec la lettre des récoltes et la liste « Amis proches » sur Instagram.</p><p>Un code par commande, non cumulable.</p>"],
  ["contact", "Contact", "<p>Une question sur une pièce, une mesure ou une location : écrivez à Simé en message privé sur Instagram, @sime.archives. Réponse sous 48 h.</p><p>Pour un shoot, un clip ou une campagne, passez par la demande pro de la page Location & RP.</p>"]
];
document.getElementById("r").innerHTML = S.announcementBar() + S.header() +
  '<div class="sa-wrap"><nav class="sa-crumbs" aria-label="Fil d’Ariane"><a href="#">Accueil</a><span>Aide</span></nav></div>' +
  '<div class="ai sa-wrap"><div><span class="sa-mono sa-muted">AIDE</span><h1>Avant, pendant, après</h1><nav aria-label="Sujets">' + SECS.map(function (s) { return '<a href="#' + s[0] + '" data-sec="' + s[0] + '">' + s[1] + '</a>'; }).join("") + '</nav><p class="sa-muted" style="font-size:13px;margin-top:24px">Textes de maquette, à relire par l’équipe.</p></div>' +
  '<div>' + SECS.map(function (s, i) { return '<section id="' + s[0] + '">' + S.accordion([{ title: s[1], open: i === 0, html: s[2] }]) + '</section>'; }).join("") + '</div></div>' +
  S.footer() + S.cartDrawer();
S.init(document);
document.querySelector(".ai nav").addEventListener("click", function (e) {
  var a = e.target.closest("[data-sec]"); if (!a) return; e.preventDefault();
  var s = document.getElementById(a.dataset.sec); s.scrollIntoView({ behavior: "smooth", block: "start" });
  var acc = s.querySelector(".sa-acc"); if (acc && !acc.classList.contains("is-open")) s.querySelector("button").click();
});
</script><script src="proto.js"></script></body></html>'''
open(os.path.join(OUT, 'aide.html'), 'w').write(fix(aide))
print(sorted(os.listdir(OUT)))
