import ast
css,data,fns=ast.literal_eval(open('lc_parts.py').read())
data=data.replace('/* ── Offre (cahier des charges) ── */','/* ── Tarifs (cahier des charges) ── */')
D='ds/project/components/'
common_js = data + fns + r'''
function totals() {
  var v = value(), loc = rental(), extra = st.opts.extra && v ? Math.round(v * 5) / 100 : 0;
  var sty = st.opts.style ? STYLE : 0, pho = st.opts.photo ? PHOTO : 0;
  return { v: v, loc: loc, extra: extra, sty: sty, pho: pho, total: loc + extra + sty + pho };
}
function selLabel() { return st.sel.length ? (st.mode === "look" ? st.sel.length + " look" + (st.sel.length > 1 ? "s" : "") : st.sel.length + " pièce" + (st.sel.length > 1 ? "s" : "")) : "Rien de choisi"; }
function anyBusy() { return st.mode === "look" && st.sel.some(function (id) { return busy(LOOKS.filter(function (x) { return x.id === id; })[0]); }); }
function toast(msg) { var t = document.querySelector(".sa-toast") || document.body.appendChild(Object.assign(document.createElement("div"), { className: "sa-toast", role: "status" })); t.textContent = msg; t.classList.add("is-on"); setTimeout(function () { t.classList.remove("is-on"); }, 2200); }
var FAQ = S.accordion([
  { title: "Peut-on louer une seule pièce ?", html: "Pour l’instant, Simé loue des looks complets, stylés par Lou-Ann. Les pièces à l’unité sont réservées aux pros (stylistes, artistes, marques) avec la formule Shoot pro, sur devis." },
  { title: "Comment est calculé le prix ?", html: "En pourcentage de la valeur estimée des pièces : 15 % pour 3 jours, 25 % pour une semaine, 35 % pour deux semaines, 20 % par jour pour un shoot pro. Jamais moins de 30 € par location." },
  { title: "La caution", html: "Une empreinte bancaire du montant de la valeur, sans débit. Elle est libérée sous 48 h après le contrôle de la pièce." },
  { title: "Nettoyage et petits accrocs", html: "Le nettoyage est inclus. En cas de dommage, un devis de réparation est fait avant toute retenue." },
  { title: "Les photos de la soirée", html: "8 photos retouchées livrées. Simé garde les droits et peut les publier." }
]);
var PRO = '<section class="sa-wrap lc-pro-wrap"><div class="lc-pro-sep"><span class="sa-label">Vous êtes pro ?</span><span class="sa-mono sa-muted">Hors réservation en ligne · demande sur devis</span></div><div class="lc-pro" id="s-pro"><div><span class="sa-mono sa-muted">PROS · STYLISTES, ARTISTES, MARQUES</span><h2>Un shoot, un clip, une campagne ?</h2><p style="margin:0;max-width:420px">Racontez-nous le projet, les dates et les silhouettes qui vous parlent. Réponse sous 48 h.</p></div>' +
  '<form class="lc-form" data-sa="quote"><label>Nom<input required></label><label>E-mail<input type="email" required></label><label>Projet<select><option>Éditorial</option><option>Campagne</option><option>Clip, scène</option><option>Événement de marque</option><option>Autre</option></select></label><label>Dates<input placeholder="ex. 3 et 4 décembre"></label><label class="full">Looks ou pièces souhaités<textarea placeholder="ex. Nylon et voile, SA-007"></textarea></label><div class="full">' + S.button("Envoyer la demande", { variant: "secondary" }) + '</div></form></div></section>';
'''

head = lambda title, sub, extra_css: f'''<!-- @dsCard group="Site" height=900 width=1280 page subtitle="{sub}" -->
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}
{extra_css}
</style>
</head>
<body class="sa">
<div class="sa-page" id="r"></div>
<script>
var S = window.SimeArchives;
var P = S.photos, find = S.find;
'''
tail = '''
document.querySelector("[data-sa='quote']").addEventListener("submit", function (e) { e.preventDefault(); e.target.innerHTML = '<p class="sa-mono full" style="margin:0">Mèsi. Simé revient vers vous sous 48 h.</p>'; });
</script>
</body>
</html>
'''

# ───────── B : pas à pas ─────────
cssB = r'''
  .lb-top { padding-top: var(--space-6); padding-bottom: var(--space-5); display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--space-6); align-items: stretch; }
  .lb-top__txt { display: flex; flex-direction: column; justify-content: space-between; gap: var(--space-5); }
  .lb-top__txt .sa-btn--link { align-self: flex-start; }
  .lb-visual { position: relative; margin: 0; height: 300px; overflow: hidden; background: var(--paper-deep); }
  .lb-visual img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: opacity .45s ease; }
  .lb-visual img.is-out { opacity: 0; }
  .lb-visual figcaption { position: absolute; left: var(--space-3); bottom: var(--space-3); background: var(--paper); padding: 2px 8px; font-family: var(--font-mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; }
  .sa-page { padding-bottom: 72px; box-sizing: border-box; }
  .lb-top h1 { margin: var(--space-2) 0 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 44px; line-height: 1; letter-spacing: -.02em; }
  .lb-top p { margin: var(--space-3) 0 0; max-width: 520px; color: var(--ink-muted); }
  .lb-stepper { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); border-top: 1px solid var(--ink); }
  .lb-stepper button { text-align: left; padding: var(--space-3) var(--space-3) var(--space-3) 0; display: grid; gap: 2px; border-top: 3px solid transparent; margin-top: -2px; color: var(--ink-muted); }
  .lb-stepper button[aria-current="step"] { border-top-color: var(--ink); color: var(--ink); }
  .lb-stepper button.is-done { color: var(--ink); }
  .lb-stepper small { font-family: var(--font-mono); font-size: 11px; color: var(--ink-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .lb-panel { padding-top: var(--space-6); padding-bottom: 140px; min-height: 520px; }
  .lb-panel h2 { margin: 0 0 var(--space-2); font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 30px; line-height: 1.05; }
  .lb-panel > p { margin: 0 0 var(--space-5); color: var(--ink-muted); font-size: 14px; }
  .lb-review { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: var(--space-6); align-items: start; }
  .lb-review .lc-recap { position: static; }
  .lb-bar { position: fixed; left: 0; right: 0; bottom: 0; z-index: 30; background: var(--paper); border-top: 1px solid var(--ink); }
  .lb-bar__in { display: grid; grid-template-columns: 1fr auto auto; gap: var(--space-5); align-items: center; padding-top: var(--space-3); padding-bottom: var(--space-3); }
  .lb-bar__sum { font-size: 13px; color: var(--ink-muted); }
  .lb-bar__sum b { color: var(--ink); font-weight: 500; }
  .lb-bar__tot { font-family: var(--font-mono); font-size: 20px; }
  .lb-bar__btns { display: flex; gap: var(--space-2); }
  .lb-bar__btns .sa-btn { min-width: 150px; }
  @media (max-width: 900px) {
    .lb-top { grid-template-columns: 1fr; } .lb-top h1 { font-size: 34px; } .lb-visual { height: 200px; order: -1; }
    .lb-stepper { grid-template-columns: repeat(5, 1fr); } .lb-stepper small, .lb-stepper .sa-label { display: none; } .lb-stepper .sa-mono { font-size: 13px !important; }
    .lb-review { grid-template-columns: 1fr; }
    .lb-bar__in { grid-template-columns: 1fr auto; } .lb-bar__sum { display: none; } .lb-bar__btns .sa-btn { min-width: 0; }
  }
'''
jsB = common_js + r'''
var st = { pack: "soiree", mode: "look", sel: [], dur: "3j", date: "", opts: { style: true, photo: true, extra: false }, delivery: "atelier" };
var STEPS = ["Formule", "Looks ou pièces", "Dates", "À-côtés", "Récapitulatif"], cur = 0;
/* Un seul visuel, qui change avec l'étape : photos du shoot uniquement */
var VIS = [[P.look4, "Look de location : gilet peau lainée et mini-jupe sequins", "Look 02 · Peau lainée et sequins"], [P.look1, "Look nylon et voile, assis contre une grille", "Look 01 · Nylon et voile"], [P.look7, "Look blazer beige et panier paille", "Lookbook · Paris"], [P.look6, "Look plissé vert d'eau", "Look 04 · Plissé vert d'eau"], [P.look8, "Look panier paille", "Look 05 · Panier paille"]];
function setVisual() {
  var f = document.getElementById("visual"); if (!f) return; var im = f.querySelector("img"), v = VIS[cur];
  if (st.mode === "look" && st.sel.length && cur > 0) { var l = LOOKS.filter(function (x) { return x.id === st.sel[0]; })[0]; if (l) v = [l.photo, "Votre look : " + l.name, "Votre look · " + l.name]; }
  if (im.getAttribute("src") === v[0]) return;
  im.classList.add("is-out"); setTimeout(function () { im.src = v[0]; im.alt = v[1]; im.classList.remove("is-out"); }, 220);
}
function stepSummary(i) {
  var pk = packOf(st.pack), d = durOf(st.dur);
  return [pk.name, st.sel.length ? selLabel() : "À choisir", st.date ? new Date(st.date + "T12:00").toLocaleDateString("fr-FR", { day: "numeric", month: "short" }) + " · " + d.label : "À choisir",
    [st.opts.style ? "Stylisme" : "", st.opts.photo ? "Photo" : "", st.opts.extra ? "+1 jour" : ""].filter(Boolean).join(", ") || "Aucune", ""][i];
}
function canGo(i) { if (i >= 2 && !st.sel.length) return 1; if (i >= 3 && !st.date) return 2; return -1; }
function recapHTML() {
  var pk = packOf(st.pack), t = totals(), d = durOf(st.dur), b = anyBusy();
  var row = function (a, x, m) { return '<div class="lc-recap__row' + (m ? " is-muted" : "") + '"><span>' + a + '</span><span>' + x + '</span></div>'; };
  var thumbs = st.sel.map(function (id) { var l = LOOKS.filter(function (x) { return x.id === id; })[0]; return '<img src="' + (l ? l.photo : S.img(find(id), "a")) + '" alt="">'; }).join("");
  return '<div class="lc-recap__head"><span class="sa-label">Votre location</span><span class="sa-mono sa-muted">' + pk.name + '</span></div><div class="lc-recap__body">' +
    (thumbs ? '<div class="lc-recap__thumbs">' + thumbs + '</div>' : '') + row(selLabel() + " · valeur", S.euro(t.v), true) + row("Location " + d.label.toLowerCase() + " · " + d.pct + " %", S.euro(t.loc)) +
    (t.extra ? row("Journée en plus", S.euro(t.extra)) : "") + (st.opts.style ? row("Stylisme" + (pk.style ? " (inclus)" : ""), S.euro(STYLE)) : "") + (st.opts.photo ? row("Photo de soirée" + (pk.photo ? " (inclus)" : ""), S.euro(PHOTO)) : "") +
    row(st.delivery === "atelier" ? "Retrait à l'atelier" : "Coursier Paris", st.delivery === "atelier" ? "Offert" : "à confirmer", true) +
    row("Dates", st.date ? new Date(st.date + "T12:00").toLocaleDateString("fr-FR", { day: "numeric", month: "long" }) + " · " + d.label : "à choisir", !st.date) + '</div>' +
    '<div class="lc-recap__total">' + row("Total", S.euro(t.total)) + '<p class="lc-recap__warn is-on" style="margin:0">' + (b ? "Un look choisi est pris à ces dates." : "Caution : empreinte bancaire de " + S.euro(t.v) + ", sans débit, libérée sous 48 h après le retour.") + '</p></div>';
}
function panel() {
  var pk = packOf(st.pack);
  if (pk.durs.indexOf(st.dur) < 0) st.dur = pk.durs[0];
  if (cur === 0) return '<h2>Votre formule</h2><p>Du look seul à la soirée accompagnée. Ce qui est inclus sera coché d\'office aux options.</p><div class="lc-packs" role="radiogroup" aria-label="Packs">' + PACKS.map(packCard).join("") + '</div>';
  if (cur === 1) { var items = st.mode === "look" ? LOOKS : PIECES; return '<h2>Ce que vous portez</h2><p>Un look tel que Lou-Ann l\'a stylé pour le shoot, ou des pièces à l\'unité pour composer le vôtre. Prix affiché pour ' + durOf(st.dur).label + '.</p><div class="lc-seg" role="group" aria-label="Type de location"><button data-mode="look" aria-pressed="' + (st.mode === "look") + '">Un look complet</button><button data-mode="piece" aria-pressed="' + (st.mode === "piece") + '">Des pièces à l\'unité</button></div><div class="lc-grid">' + items.map(function (it) { return itemCard(it, st.mode === "look"); }).join("") + '</div>'; }
  if (cur === 2) return '<h2>Vos dates</h2><p>Le jour où vous passez la prendre, et combien de temps vous la gardez.</p><div class="lc-dates"><label class="sa-label">Début de la location<input type="date" id="date" min="2026-11-13" value="' + st.date + '"></label><div class="lc-chips" role="group" aria-label="Durée">' + DUR.map(function (d) { var ok = pk.durs.indexOf(d.id) > -1; return '<button class="lc-chip" data-dur="' + d.id + '" aria-pressed="' + (st.dur === d.id) + '"' + (ok ? "" : " disabled") + '><b>' + d.label + '</b><span>' + d.pct + ' % de la valeur</span></button>'; }).join("") + '</div></div><p class="lc-note">Exemple : le look « Mary Jane kaki » est pris du 20 au 22 novembre.</p>';
  if (cur === 3) return '<h2>Les à-côtés</h2><p>Ce que votre formule inclut est déjà coché.</p><div class="lc-opts">' +
    optRow("style", "Stylisme avec Lou-Ann", "Une séance pour composer et ajuster le look.", "dès " + S.euro(STYLE), { checked: st.opts.style, locked: pk.style }) +
    optRow("photo", "Photo de la soirée par Laury", "2 à 3 h, 8 photos retouchées. Simé garde les droits et peut publier.", "dès " + S.euro(PHOTO), { checked: st.opts.photo, locked: pk.photo }) +
    optRow("extra", "Une journée de plus", "24 h de plus, même calcul.", "+5 % de la valeur", { checked: st.opts.extra }) + '</div><h3 class="sa-label lc-subhead">Retrait ou coursier</h3>' + S.noteLine("Paris uniquement", "Pour l’instant, la location se fait à Paris : retrait à l’atelier ou coursier.") + '<div class="lc-opts">' +
    optRow("atelier", "Retrait à l'atelier, Paris", "Essayage possible sur rendez-vous.", "Offert", { radio: true, name: "deliv", checked: st.delivery === "atelier" }) +
    optRow("coursier", "Coursier dans Paris", "Livraison et reprise le jour choisi.", "à confirmer", { radio: true, name: "deliv", checked: st.delivery === "coursier" }) + '</div>';
  return '<div class="lb-review"><div><h2>Tout est prêt pour une bèl soirée</h2><p>Bèl, « belle » en créole. Relisez votre location : chaque étape se modifie d\'un clic, en haut.</p><div class="sa-prose" style="font-size:14px;line-height:22px;max-width:520px"><p>Le nettoyage est inclus. La caution est une empreinte bancaire, sans débit. Un rappel part la veille du retour.</p></div></div><aside class="lc-recap">' + recapHTML() + '</aside></div>';
}
function render() {
  document.getElementById("stepper").innerHTML = STEPS.map(function (s, i) { return '<button data-step="' + i + '"' + (i === cur ? ' aria-current="step"' : '') + ' class="' + (i < cur ? "is-done" : "") + '"><span class="sa-mono" style="font-size:11px">0' + (i + 1) + '</span><span class="sa-label">' + s + '</span><small>' + (i < 4 ? stepSummary(i) : "") + '</small></button>'; }).join("");
  document.getElementById("panel").innerHTML = panel();
  var t = totals(), last = cur === 4, b = anyBusy();
  document.getElementById("bar").innerHTML = '<div class="lb-bar__in sa-wrap"><span class="lb-bar__sum"><b>' + packOf(st.pack).name + '</b> · ' + selLabel() + ' · ' + durOf(st.dur).label + '</span><span class="lb-bar__tot">' + (st.sel.length ? S.euro(t.total) : '<span class="sa-muted" style="font-size:13px">Total après le choix du look</span>') + '</span><span class="lb-bar__btns">' +
    (cur ? S.button("Retour", { variant: "secondary", action: "prev" }) : "") +
    (last ? (st.pack === "pro" ? S.button("Demander un devis", { action: "quote" }) : S.button("Réserver", { action: "book", disabled: !st.sel.length || !st.date || b })) : S.button("Continuer", { action: "next", disabled: (cur === 1 && !st.sel.length) || (cur === 2 && !st.date) })) + '</span></div>';
  setVisual();
}
function go0(i) { var block = canGo(i); if (block > -1 && i > block) i = block; cur = Math.max(0, Math.min(4, i)); render(); document.getElementById("stepper").scrollIntoView({ block: "nearest" }); }
function go(i) { go0(i); }

document.getElementById("r").innerHTML =
  S.announcementBar() + S.header({ active: "location" }) +
  '<section class="lb-top sa-wrap"><div class="lb-top__txt"><div><span class="sa-mono sa-muted">LOCATION & RP</span><h1>Louer un look Simé</h1><p>Le vestiaire de nos shoots, le temps d\'une soirée. Cinq étapes, et le prix se calcule en direct, selon la valeur des pièces.</p></div><a class="sa-btn sa-btn--link" href="#s-pro">Vous êtes pro ?</a></div>' +
    '<figure class="lb-visual" id="visual"><img src="' + VIS[0][0] + '" alt="' + VIS[0][1] + '"></figure></section>' +
  '<div class="sa-wrap"><nav class="lb-stepper" id="stepper" aria-label="Étapes de la location"></nav><div class="lb-panel" id="panel"></div></div>' +
  '<div class="lb-bar" id="bar"></div>' +
  PRO + '<section class="lc-faq sa-wrap" style="border-top:1px solid var(--photocopy)"><div><span class="sa-mono sa-muted">QUESTIONS</span><h2>Avant de réserver</h2></div><div>' + FAQ + '</div></section>' +
  S.footer() + S.cartDrawer();
S.init(document);
render();
var root = document.getElementById("r");
root.addEventListener("click", function (e) {
  var b;
  if ((b = e.target.closest("[data-step]"))) { go(+b.dataset.step); return; }
  if ((b = e.target.closest("[data-action='next']"))) { if (!b.disabled) go(cur + 1); return; }
  if ((b = e.target.closest("[data-action='prev']"))) { go(cur - 1); return; }
  if ((b = e.target.closest("[data-action='book']"))) { toast("Prototype : la réservation passe par l'app de location Shopify"); return; }
  if ((b = e.target.closest("[data-action='quote']"))) { document.getElementById("s-pro").scrollIntoView({ behavior: "smooth" }); return; }
  if (!e.target.closest("#panel")) return;
  if ((b = e.target.closest("[data-pack]"))) { st.pack = b.dataset.pack; var pk = packOf(st.pack); st.opts.style = pk.style; st.opts.photo = pk.photo; render(); return; }
  if ((b = e.target.closest("[data-mode]"))) { if (st.mode !== b.dataset.mode) { st.mode = b.dataset.mode; st.sel = []; } render(); return; }
  if ((b = e.target.closest("[data-item]"))) { if (b.getAttribute("aria-disabled") === "true") return; var id = b.dataset.item, i = st.sel.indexOf(id); if (i > -1) st.sel.splice(i, 1); else st.sel.push(id); render(); return; }
  if ((b = e.target.closest("[data-dur]"))) { if (!b.disabled) { st.dur = b.dataset.dur; render(); } return; }
});
root.addEventListener("change", function (e) {
  if (e.target.id === "date") { st.date = e.target.value; render(); return; }
  if (["style", "photo", "extra"].indexOf(e.target.dataset.opt) > -1) { st.opts[e.target.dataset.opt] = e.target.checked; render(); return; }
  if (e.target.name === "deliv") { st.delivery = e.target.value; render(); }
});
'''
open(D+'LocationPageB/preview.html','w').write(head("Location & RP · pas à pas","Location & RP, proposition 2 : pas à pas, une étape à la fois, total et bouton Continuer fixés en bas", cssB)+jsB+tail)

# ───────── C : le look d'abord ─────────
cssC = r'''
  .lv-top { padding-top: var(--space-6); padding-bottom: var(--space-5); display: grid; grid-template-columns: 1fr auto; gap: var(--space-5); align-items: end; border-bottom: 1px solid var(--photocopy); }
  .lv-top h1 { margin: var(--space-2) 0 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 44px; line-height: 1; letter-spacing: -.02em; }
  .lv-top p { margin: var(--space-3) 0 0; max-width: 560px; color: var(--ink-muted); }
  .lv-how { display: flex; gap: var(--space-5); font-family: var(--font-mono); font-size: 12px; color: var(--ink-muted); }
  .lv-how b { color: var(--ink); font-weight: 500; }
  .lv-bar { display: flex; justify-content: space-between; align-items: center; gap: var(--space-4); padding-top: var(--space-5); padding-bottom: var(--space-4); }
  .lv-bar .lc-seg { margin: 0; }
  .lv-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-6) var(--space-4); padding-bottom: var(--space-7); }
  .lv-grid.is-pieces { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .lv-card { display: grid; gap: var(--space-2); text-align: left; cursor: pointer; }
  .lv-card__img { position: relative; aspect-ratio: 4/5; overflow: hidden; background: var(--packshot, #fff); }
  .lv-card__img img { width: 100%; height: 100%; object-fit: cover; transition: transform 1s cubic-bezier(.2,.7,.2,1); }
  .lv-card:hover .lv-card__img img { transform: scale(1.03); }
  .lv-card h3 { margin: 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 20px; line-height: 1.15; }
  .lv-card__meta { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 12px; color: var(--ink-muted); }
  .lv-card__meta b { color: var(--ink); font-weight: 500; }
  .lv-card__cta { position: absolute; left: var(--space-3); right: var(--space-3); bottom: var(--space-3); background: var(--paper); text-align: center; padding: 10px; font-size: 11px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; opacity: 0; transform: translateY(6px); transition: opacity .2s, transform .2s; }
  .lv-card:hover .lv-card__cta, .lv-card:focus-visible .lv-card__cta { opacity: 1; transform: none; }
  .lv-services { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-4); padding-top: var(--space-6); padding-bottom: var(--space-7); border-top: 1px solid var(--photocopy); }
  .lv-services h2 { grid-column: 1 / -1; margin: 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 30px; }
  .lv-serv { border-top: 1px solid var(--ink); padding-top: var(--space-3); display: grid; gap: 6px; align-content: start; }
  .lv-serv b { font-weight: 500; font-size: 17px; } .lv-serv span { font-size: 14px; color: var(--ink-muted); }
  /* Tiroir de réservation */
  .lv-drawer { position: fixed; top: 0; right: 0; bottom: 0; width: min(480px, 100%); z-index: 40; background: var(--paper); box-shadow: var(--shadow-drawer); display: flex; flex-direction: column; transform: translateX(105%); visibility: hidden; transition: transform var(--duration-drawer) cubic-bezier(.2,.7,.2,1), visibility 0s var(--duration-drawer); }
  .lv-drawer.is-open { transform: none; visibility: visible; transition: transform var(--duration-drawer) cubic-bezier(.2,.7,.2,1); }
  .lv-scrim { position: fixed; inset: 0; z-index: 39; background: rgba(28,26,24,.28); opacity: 0; pointer-events: none; transition: opacity .3s; }
  .lv-scrim.is-on { opacity: 1; pointer-events: auto; }
  .lv-d__head { display: grid; grid-template-columns: 72px 1fr auto; gap: var(--space-3); align-items: center; padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--photocopy); }
  .lv-d__head img { width: 72px; height: 90px; object-fit: cover; }
  .lv-d__head h2 { margin: 2px 0 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 20px; line-height: 1.15; }
  .lv-d__body { flex: 1; overflow-y: auto; padding: 0 var(--space-5) var(--space-5); }
  .lv-d__sec { padding-top: var(--space-5); display: grid; gap: var(--space-3); }
  .lv-d__sec > .sa-label { display: flex; justify-content: space-between; }
  .lv-d__body .lc-chips { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .lv-d__body .lc-chip { min-width: 0; padding: 10px; }
  .lv-d__body input[type="date"] { font: 15px/24px var(--font-sans); color: var(--ink); background: var(--paper); border: 0; border-bottom: 1px solid var(--ink); padding: 8px 0; border-radius: 0; width: 100%; }
  .lv-d__foot { border-top: 1px solid var(--ink); padding: var(--space-4) var(--space-5); display: grid; gap: var(--space-3); }
  @media (max-width: 900px) { .lv-top { grid-template-columns: 1fr; } .lv-top h1 { font-size: 34px; } .lv-grid, .lv-grid.is-pieces { grid-template-columns: repeat(2, minmax(0, 1fr)); } .lv-services { grid-template-columns: 1fr; } .lv-how { flex-wrap: wrap; } }
'''
jsC = common_js + r'''
var st = { pack: "look", mode: "look", sel: [], dur: "3j", date: "", opts: { style: false, photo: false, extra: false }, delivery: "atelier" };
function card(it, isLook) {
  var price = Math.max(FLOOR, Math.round((isLook ? it.value : it.price) * 15) / 100);
  return '<button class="lv-card" data-open="' + it.id + '"><span class="lv-card__img"><img src="' + (isLook ? it.photo : S.img(it, "a")) + '" alt="' + it.name + '"><span class="lv-card__cta">Louer ' + (isLook ? "ce look" : "cette pièce") + '</span></span>' +
    '<h3>' + it.name + '</h3><span class="lv-card__meta"><span>' + (isLook ? it.pieces.length + (it.pieces.length > 1 ? " pièces" : " pièce") : it.id + " · " + it.size) + '</span><span>dès <b>' + S.euro(price) + '</b> · 3 jours</span></span></button>';
}
function renderGrid() {
  var isLook = st.mode === "look", g = document.getElementById("grid");
  g.className = "lv-grid sa-wrap" + (isLook ? "" : " is-pieces");
  g.innerHTML = (isLook ? LOOKS : PIECES).map(function (it) { return card(it, isLook); }).join("");
  document.getElementById("seg").innerHTML = '<button data-mode="look" aria-pressed="' + isLook + '">Looks complets</button><button data-mode="piece" aria-pressed="' + !isLook + '">Pièces à l\'unité</button>';
}
var PRESETS = [["look", "Le look seul", false, false], ["style", "+ stylisme", true, false], ["soiree", "Soirée complète", true, true]];
function renderDrawer() {
  var id = st.sel[0]; if (!id) return;
  var isLook = st.mode === "look", it = isLook ? LOOKS.filter(function (x) { return x.id === id; })[0] : find(id);
  var t = totals(), d = durOf(st.dur), b = anyBusy();
  var row = function (a, x, m) { return '<div class="lc-recap__row' + (m ? " is-muted" : "") + '"><span>' + a + '</span><span>' + x + '</span></div>'; };
  document.getElementById("drawer").innerHTML =
    '<div class="lv-d__head"><img src="' + (isLook ? it.photo : S.img(it, "a")) + '" alt=""><div><span class="sa-mono sa-muted">' + (isLook ? "LOOK · " + it.pieces.join(", ") : it.id) + '</span><h2>' + it.name + '</h2><span class="sa-mono sa-muted">Valeur ' + S.euro(t.v) + '</span></div><button data-action="dclose" aria-label="Fermer">' + S.icon("close") + '</button></div>' +
    '<div class="lv-d__body">' +
      '<div class="lv-d__sec"><span class="sa-label">1 · Durée</span><div class="lc-chips">' + DUR.filter(function (x) { return x.id !== "pro"; }).map(function (x) { return '<button class="lc-chip" data-dur="' + x.id + '" aria-pressed="' + (st.dur === x.id) + '"><b>' + x.label + '</b><span>' + S.euro(Math.max(FLOOR, Math.round(t.v * x.pct) / 100)) + '</span></button>'; }).join("") + '</div></div>' +
      '<div class="lv-d__sec"><label class="sa-label" for="date">2 · Début</label><input type="date" id="date" min="2026-11-13" value="' + st.date + '">' + (b ? '<p class="lc-recap__warn is-on" style="margin:0">Ce look est pris à ces dates, choisissez-en une autre.</p>' : '') + '</div>' +
      '<div class="lv-d__sec"><span class="sa-label">3 · Avec ou sans nous<span class="sa-mono sa-muted" style="letter-spacing:0;text-transform:none;font-weight:400">facultatif</span></span><div class="lc-chips">' + PRESETS.map(function (p) { var on = st.opts.style === p[2] && st.opts.photo === p[3]; return '<button class="lc-chip" data-preset="' + p[0] + '" aria-pressed="' + on + '"><b>' + p[1] + '</b><span>' + (p[2] || p[3] ? "+" + S.euro((p[2] ? STYLE : 0) + (p[3] ? PHOTO : 0)) : "sans service") + '</span></button>'; }).join("") + '</div><p class="lc-note" style="margin:0">' + (st.opts.photo ? "Stylisme avec Lou-Ann, et Laury photographie votre soirée : 8 photos retouchées." : st.opts.style ? "Une séance avec Lou-Ann pour composer et ajuster le look." : "Vous portez le look à votre façon.") + '</p></div>' +
      '<div class="lv-d__sec"><span class="sa-label">4 · Retrait ou livraison</span><div class="lc-opts">' +
        optRow("atelier", "Retrait à l'atelier, Paris", "Essayage possible sur rendez-vous.", "Offert", { radio: true, name: "deliv", checked: st.delivery === "atelier" }) +
        optRow("coursier", "Coursier dans Paris", "Livraison et reprise le jour choisi.", "à confirmer", { radio: true, name: "deliv", checked: st.delivery === "coursier" }) + '</div></div>' +
    '</div>' +
    '<div class="lv-d__foot">' + row("Location " + d.label.toLowerCase(), S.euro(t.loc), true) + (t.sty ? row("Stylisme", S.euro(t.sty), true) : "") + (t.pho ? row("Photo", S.euro(t.pho), true) : "") +
      '<div class="lc-recap__row" style="font-weight:600"><span>Total</span><span style="font-family:var(--font-mono);font-size:18px">' + S.euro(t.total) + '</span></div>' +
      '<p class="lc-recap__warn" style="margin:0">Caution par empreinte bancaire, sans débit. Nettoyage inclus.</p>' +
      S.button(st.date ? "Réserver" : "Choisissez une date", { block: true, action: "book", disabled: !st.date || b }) + '</div>';
}
function openFor(id) { st.sel = [id]; renderDrawer(); document.getElementById("drawer").classList.add("is-open"); document.getElementById("lvscrim").classList.add("is-on"); var f = document.querySelector("#drawer [data-dur]"); if (f) f.focus({ preventScroll: true }); }
function closeD() { document.getElementById("drawer").classList.remove("is-open"); document.getElementById("lvscrim").classList.remove("is-on"); }

document.getElementById("r").innerHTML =
  S.announcementBar() + S.header({ active: "location" }) +
  '<section class="lv-top sa-wrap"><div><span class="sa-mono sa-muted">LOCATION & RP</span><h1>Louer un look Simé</h1><p>Le vestiaire de nos shoots, le temps d\'une soirée. Choisissez un look ou une pièce, le reste se règle dans un seul panneau.</p></div>' +
    '<div class="lv-how"><span><b>3 jours</b> · 15 %</span><span><b>1 semaine</b> · 25 %</span><span><b>2 semaines</b> · 35 %</span><span>de la valeur, dès 30 €</span></div></section>' +
  '<div class="lv-bar sa-wrap"><div class="lc-seg" id="seg" role="group" aria-label="Looks ou pièces"></div><a class="sa-btn sa-btn--link" href="#s-pro">Shoot pro, devis</a></div>' +
  '<div id="grid"></div>' +
  '<section class="lv-services sa-wrap"><h2>Avec ou sans nous</h2>' +
    '<div class="lv-serv"><span class="sa-mono">01</span><b>Le look seul</b><span>Vous le portez à votre façon. Nettoyage inclus.</span></div>' +
    '<div class="lv-serv"><span class="sa-mono">02</span><b>Avec le stylisme de Lou-Ann</b><span>Une séance pour composer et ajuster le look. Dès ' + S.euro(STYLE) + '.</span></div>' +
    '<div class="lv-serv"><span class="sa-mono">03</span><b>Soirée complète</b><span>Le look, le stylisme, et Laury photographie votre soirée. 8 photos retouchées.</span></div></section>' +
  PRO + '<section class="lc-faq sa-wrap" style="border-top:1px solid var(--photocopy)"><div><span class="sa-mono sa-muted">QUESTIONS</span><h2>Avant de réserver</h2></div><div>' + FAQ + '</div></section>' +
  S.footer() + S.cartDrawer() +
  '<div class="lv-scrim" id="lvscrim" data-action="dclose"></div><aside class="lv-drawer" id="drawer" role="dialog" aria-label="Votre location"></aside>';
S.init(document);
renderGrid();
var root = document.getElementById("r");
root.addEventListener("click", function (e) {
  var b;
  if ((b = e.target.closest("[data-mode]"))) { st.mode = b.dataset.mode; renderGrid(); return; }
  if ((b = e.target.closest("[data-open]"))) { openFor(b.dataset.open); return; }
  if ((b = e.target.closest("[data-action='dclose']"))) { closeD(); return; }
  if ((b = e.target.closest("[data-dur]"))) { st.dur = b.dataset.dur; renderDrawer(); return; }
  if ((b = e.target.closest("[data-preset]"))) { var p = PRESETS.filter(function (x) { return x[0] === b.dataset.preset; })[0]; st.opts.style = p[2]; st.opts.photo = p[3]; renderDrawer(); return; }
  if ((b = e.target.closest("[data-action='book']"))) { if (!b.disabled) toast("Prototype : la réservation passe par l'app de location Shopify"); return; }
});
root.addEventListener("change", function (e) {
  if (e.target.id === "date") { st.date = e.target.value; renderDrawer(); return; }
  if (e.target.dataset.opt === "style" || e.target.dataset.opt === "photo") { st.opts[e.target.dataset.opt] = e.target.checked; renderDrawer(); return; }
  if (e.target.name === "deliv") { st.delivery = e.target.value; renderDrawer(); }
});
document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeD(); });
'''
open(D+'LocationPageC/preview.html','w').write(head("Location & RP · le look d'abord","Location & RP, proposition 3 : le look d'abord, tout se règle dans un panneau latéral", cssC)+jsC+tail)


# ───────── B2 : une seule page, les étapes se déplient sous la précédente ─────────
cssB2 = cssB + r"""
  .lb-hero { position: relative; margin: 0; height: clamp(280px, 52vh, 520px); overflow: hidden; background: var(--paper-deep); }
  .lb-hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
  .lb-top2 { padding-top: var(--space-6); padding-bottom: var(--space-5); display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--space-6); align-items: end; }
  .lb-top2 h1 { margin: var(--space-2) 0 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 56px; line-height: .98; letter-spacing: -.02em; }
  .lb-top2 p { margin: 0 0 var(--space-3); max-width: 480px; color: var(--ink-muted); }
  .lt-sec { border-top: 1px solid var(--ink); padding: var(--space-5) 0 var(--space-7); scroll-margin-top: 72px; }
  .lt-sec__head { display: grid; grid-template-columns: 56px 1fr auto; gap: var(--space-3); align-items: baseline; }
  .lt-sec__no { font-family: var(--font-mono); font-size: 13px; color: var(--ink-muted); }
  .lt-sec__head h2 { margin: 0; font-family: var(--font-display, var(--font-sans)); font-stretch: 112%; font-weight: 500; font-size: 32px; line-height: 1.05; }
  .lt-sec__head p { grid-column: 2 / 3; margin: 6px 0 0; color: var(--ink-muted); font-size: 14px; }
  .lt-sec__state { font-family: var(--font-mono); font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-muted); }
  .lt-sec__body { margin-top: var(--space-5); margin-left: calc(56px + var(--space-3)); }
  .lt-sec.is-locked { padding-bottom: var(--space-5); border-top-color: var(--photocopy); }
  .lt-sec.is-locked h2 { color: var(--ink-muted); }
  .lt-next { margin-top: var(--space-5); display: flex; align-items: center; gap: var(--space-4); flex-wrap: wrap; }
  .lt-next p { margin: 0; font-size: 14px; color: var(--ink-muted); }
  .lt-next p b { color: var(--ink); font-weight: 500; }
  .lt-avail { margin: var(--space-4) 0 0; padding: var(--space-3) var(--space-4); border-left: 2px solid var(--ink); background: var(--paper-deep); font-size: 14px; }
  .lt-avail.is-busy { border-left-color: var(--ink-muted); color: var(--ink-muted); }
  .lc-pack__go { margin-top: var(--space-3); font-size: 11px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; }
  .lc-pack[aria-checked="true"] .lc-pack__go::before { content: "✓ "; }
  #tunnel .lc-item[aria-pressed="true"] .lc-item__img::after { content: "Sélectionné"; position: absolute; left: 0; right: 0; top: 0; height: 32px; padding: 0 10px; display: flex; align-items: center; background: var(--ink); color: var(--on-ink); font-size: 11px; line-height: 1; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; }
  #tunnel .lc-item[aria-pressed="true"] .lc-item__check { z-index: 1; top: 0; right: 4px; height: 32px; width: 28px; border: 0; background: transparent; line-height: 1; }
  .lt-toggle { display: flex; align-items: center; gap: 10px; text-align: left; font: inherit; color: inherit; background: none; border: 0; padding: 6px 0; cursor: pointer; min-width: 0; }
  .lt-toggle > span:nth-child(2) { min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .lt-toggle__lbl { font-size: 11px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--ink); text-decoration: underline; text-underline-offset: 3px; white-space: nowrap; }
  .lt-toggle__ico { flex: none; width: 10px; height: 10px; border-left: 1.5px solid var(--ink); border-top: 1.5px solid var(--ink); transform: rotate(45deg) translate(2px, 2px); transition: transform .2s; }
  .lt-toggle[aria-expanded="true"] .lt-toggle__ico { transform: rotate(225deg) translate(2px, 2px); }
  .lt-toggle:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
  .lt-d { border-bottom: 1px solid var(--photocopy); background: var(--paper); max-height: 60vh; overflow-y: auto; }
  .lt-d__in { display: grid; grid-template-columns: 1.2fr 1fr; gap: var(--space-6); padding-top: var(--space-5); padding-bottom: var(--space-5); }
  .lt-d__col { display: grid; gap: var(--space-3); align-content: start; }
  .lt-d__item { display: grid; grid-template-columns: 48px 1fr auto; gap: var(--space-3); align-items: center; font-size: 14px; }
  .lt-d__item img { width: 48px; height: 64px; object-fit: cover; }
  .lt-d__item small { display: block; color: var(--ink-muted); font-size: 11px; margin-top: 2px; }
  .lt-d__tot { padding-top: var(--space-3); border-top: 1px solid var(--ink); font-weight: 600; }
  .lt-d__tot span:last-child { font-size: 16px; }
  @media (max-width: 900px) { .lt-d__in { grid-template-columns: 1fr; gap: var(--space-4); } .lb-bar .lb-bar__in { grid-template-columns: 1fr auto; gap: var(--space-2) var(--space-3); } .lb-bar .lt-toggle { display: flex; } .lt-toggle > span:nth-child(2) { display: none; } .lb-bar__tot { font-size: 18px; text-align: right; white-space: nowrap; } .lb-bar .lb-bar__btns { grid-column: 1 / -1; } .lb-bar .lb-bar__btns .sa-btn { flex: 1; } }
  .lt-review { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: var(--space-6); align-items: start; }
  .lt-review .lc-recap { position: static; }
  @media (max-width: 900px) { .lb-hero { height: 240px; } .lb-top2 { grid-template-columns: 1fr; gap: var(--space-3); } .lb-top2 h1 { font-size: 36px; } .lt-sec__head { grid-template-columns: 40px 1fr; } .lt-sec__state { grid-column: 2; } .lt-sec__body { margin-left: 0; } .lt-review { grid-template-columns: 1fr; } }
"""
jsB2 = common_js + r"""
var st = { pack: "", mode: "look", sel: [], dur: "3j", date: "", opts: { style: false, photo: false, extra: false }, delivery: "atelier" };
var reached = 0;
var NEXTS = ["Continuer avec cette formule", "Continuer vers les dates", "Continuer vers les à-côtés", "Voir le récapitulatif"];   /* dernière étape dépliée : les suivantes restent fermées tant que la cliente n'a pas validé */
var SECS = [
  ["Votre formule", "Lisez les formules, comparez, choisissez. Rien n'est réservé tant que vous n'avez pas validé."],
  ["Ce que vous portez", "Un look complet, tel que Lou-Ann l'a stylé pour le shoot. Les pièces à l'unité sont réservées aux pros, avec la formule Shoot pro."],
  ["Vos dates", "La durée, puis le jour où vous passez la prendre. Simé vérifie la disponibilité tout de suite."],
  ["Les à-côtés", "Ce que votre formule inclut est déjà coché. Ajoutez ce que vous voulez."],
  ["Votre location", "Relisez : chaque partie au-dessus reste modifiable."]
];
function endDate() { if (!st.date) return null; var n = { "3j": 3, "1s": 7, "2s": 14, "pro": 1 }[st.dur] + (st.opts.extra ? 1 : 0); var d = new Date(st.date + "T12:00"); d.setDate(d.getDate() + n - 1); return d; }
function fmt(d, long) { return d.toLocaleDateString("fr-FR", { day: "numeric", month: long ? "long" : "short" }); }
function done(i) { return [!!st.pack, st.sel.length > 0, !!st.date && !anyBusy(), true, false][i]; }
function stateOf(i) { var pk = packOf(st.pack);
  if (i > reached) return "À compléter";
  if (i === 0) return st.pack ? pk.name : "À choisir";
  if (i === 1) return st.sel.length ? selLabel() : "À choisir";
  if (i === 2) return st.date ? "Du " + fmt(new Date(st.date + "T12:00")) + " au " + fmt(endDate()) : "À choisir";
  if (i === 3) return [st.opts.style ? "Stylisme" : "", st.opts.photo ? "Photo" : "", st.opts.extra ? "+1 jour" : ""].filter(Boolean).join(", ") || "Aucun";
  return ""; }
/* Message de disponibilité : dit ce qui est libre (look ou pièces), pour quelles dates et ce que ça veut dire concrètement */
function availMsg(busyNow) {
  var long = function (d) { return d.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" }); };
  var start = new Date(st.date + "T12:00"), end = endDate(), d = durOf(st.dur), many = st.sel.length > 1, what, pron;
  if (st.mode === "look") {
    var ls = st.sel.map(function (id) { return LOOKS.filter(function (x) { return x.id === id; })[0]; });
    if (busyNow) { var taken = ls.filter(function (l) { return busy(l); }).map(function (l) { return "« " + l.name + " »"; }).join(" et "); return "Le look " + taken + " est déjà loué à ces dates. Choisissez un autre jour de début, ou un autre look à l’étape 02."; }
    what = many ? "Vos " + ls.length + " looks (" + ls.map(function (l) { return "« " + l.name + " »"; }).join(", ") + ") sont libres" : "Le look « " + ls[0].name + " » (" + ls[0].pieces.length + " pièces) est libre";
    pron = many ? "les" : "le";
  } else {
    what = many ? "Vos " + st.sel.length + " pièces sont libres" : "Votre pièce est libre";
    pron = many ? "les" : "la";
  }
  return "<b>" + what + "</b> du " + long(start) + " au " + long(end) + " (" + d.label + "). Vous " + pron + " récupérez le " + fmt(start, true) + " et " + pron + " rendez le " + fmt(end, true) + ".";
}
function nextBtn(i, label, hint) { return '<div class="lt-next">' + S.button(label, { action: "next", id: String(i), disabled: !done(i) }) + '<p>' + hint + '</p></div>'; }
function body(i) {
  var pk = st.pack ? packOf(st.pack) : PACKS[0];
  if (i === 0) return '<div class="lc-packs" role="radiogroup" aria-label="Formules">' + PACKS.map(function (p) { return packCard(p).replace('</button>', '<span class="lc-pack__go">' + (st.pack === p.id ? "Formule sélectionnée" : "Sélectionner") + '</span></button>'); }).join("") + '</div>' +
    (reached === 0 ? nextBtn(0, st.pack ? "Continuer avec « " + pk.name + " »" : "Choisissez une formule", st.pack ? "Les formules restent affichées : vous pouvez changer d'avis à tout moment." : "Cliquez sur une carte pour la sélectionner.") : '');
  if (i === 1) { var items = st.mode === "look" ? LOOKS : PIECES;
    return (st.pack === "pro" ? '<div class="lc-seg" role="group" aria-label="Type de location"><button data-mode="look" aria-pressed="' + (st.mode === "look") + '">Un look complet</button><button data-mode="piece" aria-pressed="' + (st.mode === "piece") + '">Des pièces à l\'unité</button></div>' : '') + '<div class="lc-grid">' + items.map(function (it) { return itemCard(it, st.mode === "look"); }).join("") + '</div>' +
      (reached === 1 ? nextBtn(1, "Continuer vers les dates", st.sel.length ? "<b>" + selLabel() + "</b> sélectionné" + (st.sel.length > 1 ? "s" : "") + ". Prix affichés pour " + durOf(st.dur).label + "." : "Sélectionnez au moins un look ou une pièce.") : ''); }
  if (i === 2) { var b = anyBusy();
    return '<div class="lc-dates"><label class="sa-label">Début de la location<input type="date" id="date" min="2026-11-13" value="' + st.date + '"></label><div class="lc-chips" role="group" aria-label="Durée">' + DUR.map(function (d) { var ok = pk.durs.indexOf(d.id) > -1; return '<button class="lc-chip" data-dur="' + d.id + '" aria-pressed="' + (st.dur === d.id) + '"' + (ok ? "" : " disabled") + '><b>' + d.label + '</b><span>' + d.pct + ' % de la valeur</span></button>'; }).join("") + '</div></div>' +
      (st.date ? '<p class="lt-avail' + (b ? " is-busy" : "") + '">' + availMsg(b) + '</p>' : '<p class="lc-note">Exemple : le look « Mary Jane kaki » est pris du 20 au 22 novembre.</p>') +
      (reached === 2 ? nextBtn(2, "Continuer vers les à-côtés", st.date ? "" : "Choisissez une date de début.") : ''); }
  if (i === 3) return '<div class="lc-opts">' +
      optRow("style", "Stylisme avec Lou-Ann", "Une séance pour composer et ajuster le look.", "dès " + S.euro(STYLE), { checked: st.opts.style, locked: pk.style }) +
      optRow("photo", "Photo de la soirée par Laury", "2 à 3 h, 8 photos retouchées. Simé garde les droits et peut publier.", "dès " + S.euro(PHOTO), { checked: st.opts.photo, locked: pk.photo }) +
      optRow("extra", "Une journée de plus", "24 h de plus, même calcul.", "+5 % de la valeur", { checked: st.opts.extra }) + '</div><h3 class="sa-label lc-subhead">Retrait ou coursier</h3>' + S.noteLine("Paris uniquement", "Pour l’instant, la location se fait à Paris : retrait à l’atelier ou coursier.") + '<div class="lc-opts">' +
      optRow("atelier", "Retrait à l'atelier, Paris", "Essayage possible sur rendez-vous.", "Offert", { radio: true, name: "deliv", checked: st.delivery === "atelier" }) +
      optRow("coursier", "Coursier dans Paris", "Livraison et reprise le jour choisi.", "à confirmer", { radio: true, name: "deliv", checked: st.delivery === "coursier" }) + '</div>' +
      (reached === 3 ? nextBtn(3, "Voir le récapitulatif", "") : '');
  var t = totals(), d = durOf(st.dur);
  var row = function (a, x, m) { return '<div class="lc-recap__row' + (m ? " is-muted" : "") + '"><span>' + a + '</span><span>' + x + '</span></div>'; };
  return '<div class="lt-review"><div><p style="margin:0;max-width:520px">Tout est prêt pour une bèl soirée. <span class="sa-muted">Bèl, « belle » en créole.</span></p><p class="sa-muted" style="font-size:14px;max-width:520px">Le nettoyage est inclus. La caution est une empreinte bancaire, sans débit. Un rappel part la veille du retour.</p></div>' +
    '<aside class="lc-recap"><div class="lc-recap__head"><span class="sa-label">Votre location</span><span class="sa-mono sa-muted">' + pk.name + '</span></div><div class="lc-recap__body">' +
    row(selLabel() + " · valeur", S.euro(t.v), true) + row("Location " + d.label.toLowerCase() + " · " + d.pct + " %", S.euro(t.loc)) + (t.extra ? row("Journée en plus", S.euro(t.extra)) : "") +
    (st.opts.style ? row("Stylisme" + (pk.style ? " (inclus)" : ""), S.euro(STYLE)) : "") + (st.opts.photo ? row("Photo de soirée" + (pk.photo ? " (inclus)" : ""), S.euro(PHOTO)) : "") +
    row("Dates", st.date ? "Du " + fmt(new Date(st.date + "T12:00")) + " au " + fmt(endDate()) : "à choisir", !st.date) + '</div>' +
    '<div class="lc-recap__total">' + row("Total", S.euro(t.total)) + '<p class="lc-recap__warn is-on" style="margin:0">Caution : empreinte bancaire de ' + S.euro(t.v) + ', sans débit, libérée sous 48 h après le retour.</p></div></aside></div>';
}
/* Le rendu garde la position de lecture et le focus : un clic ne doit jamais renvoyer en haut de page */
function render() {
  var sc = document.getElementById("r"), top = sc ? sc.scrollTop : 0, wtop = window.pageYOffset;
  var f = document.activeElement, key = f && f.closest && f.closest("[data-item],[data-pack],[data-dur],[data-mode]");
  var sel = key ? (key.dataset.item ? '[data-item="' + key.dataset.item + '"]' : key.dataset.pack ? '[data-pack="' + key.dataset.pack + '"]' : key.dataset.dur ? '[data-dur="' + key.dataset.dur + '"]' : '[data-mode="' + key.dataset.mode + '"]') : null;
  draw();
  if (sc) sc.scrollTop = top; if (window.pageYOffset !== wtop) window.scrollTo(0, wtop);
  if (sel) { var n = document.querySelector("#tunnel " + sel); if (n) n.focus({ preventScroll: true }); }
}
function draw() {
  if (st.pack) { var pk = packOf(st.pack); if (pk.durs.indexOf(st.dur) < 0) st.dur = pk.durs[0]; }
  document.getElementById("tunnel").innerHTML = SECS.map(function (s, i) {
    var locked = i > reached;
    return '<section class="lt-sec' + (locked ? " is-locked" : "") + '" id="sec-' + i + '"><div class="lt-sec__head"><span class="lt-sec__no">0' + (i + 1) + '</span><h2>' + s[0] + '</h2><span class="lt-sec__state">' + stateOf(i) + '</span>' + (locked ? '' : '<p>' + s[1] + '</p>') + '</div>' +
      (locked ? '' : '<div class="lt-sec__body">' + body(i) + '</div>') + '</section>';
  }).join("");
  drawBar();
}
var barOpen = false;
/* Détail de la sélection, déplié au-dessus de la barre fixe (comme le récap panier mobile de lacoste.fr) */
function barDetail() {
  var pk = st.pack ? packOf(st.pack) : null, t = totals(), d = durOf(st.dur);
  var row = function (a, x, m) { return '<div class="lc-recap__row' + (m ? " is-muted" : "") + '"><span>' + a + '</span><span>' + x + '</span></div>'; };
  var thumbs = st.sel.map(function (id) { var l = LOOKS.filter(function (x) { return x.id === id; })[0]; var it = l || find(id); return '<div class="lt-d__item"><img src="' + (l ? l.photo : S.img(it, "a")) + '" alt=""><span>' + (l ? "Look « " + l.name + " »" : it.name) + '<small class="sa-mono">' + (l ? l.pieces.join(", ") : it.id) + '</small></span><span class="sa-mono">' + S.euro(Math.max(FLOOR, Math.round((l ? l.value : it.price) * d.pct) / 100)) + '</span></div>'; }).join("");
  return '<div class="lt-d" id="bar-detail"' + (barOpen ? '' : ' hidden') + '><div class="sa-wrap lt-d__in">' +
    '<div class="lt-d__col"><span class="sa-label">Votre sélection</span>' + (thumbs || '<p class="sa-muted" style="margin:0;font-size:14px">Aucun look ni pièce pour l’instant.</p>') + '</div>' +
    '<div class="lt-d__col">' + row("Formule", pk ? pk.name : "à choisir", !pk) + row("Dates", st.date ? "Du " + fmt(new Date(st.date + "T12:00")) + " au " + fmt(endDate()) : "à choisir", !st.date) +
      row("Location " + d.label.toLowerCase() + " · " + d.pct + " %", st.sel.length ? S.euro(t.loc) : "–") + (t.extra ? row("Journée en plus", S.euro(t.extra)) : "") +
      (st.opts.style ? row("Stylisme" + (pk && pk.style ? " (inclus)" : ""), S.euro(STYLE)) : "") + (st.opts.photo ? row("Photo de soirée" + (pk && pk.photo ? " (inclus)" : ""), S.euro(PHOTO)) : "") +
      row(st.delivery === "atelier" ? "Retrait à l'atelier" : "Coursier Paris", st.delivery === "atelier" ? "Offert" : "à confirmer", true) +
      '<div class="lc-recap__row lt-d__tot"><span>Total</span><span>' + (st.sel.length ? S.euro(t.total) : "–") + '</span></div>' +
      (st.sel.length ? '<p class="sa-muted" style="margin:0;font-size:12px">Caution par empreinte bancaire de ' + S.euro(t.v) + ', sans débit.</p>' : '') + '</div></div></div>';
}
function drawBar() {
  var t = totals(), last = reached === 4;
  var hasAny = !!st.pack || st.sel.length > 0; if (!hasAny) barOpen = false;
  var sumTxt = '<b>' + (st.pack ? packOf(st.pack).name : "Formule à choisir") + '</b> · ' + selLabel() + (st.date ? ' · du ' + fmt(new Date(st.date + "T12:00")) + ' au ' + fmt(endDate()) : '');
  document.getElementById("bar").innerHTML = (hasAny ? barDetail() : '') + '<div class="lb-bar__in sa-wrap">' + (hasAny ? '<button class="lb-bar__sum lt-toggle" type="button" data-action="bar-toggle" aria-expanded="' + barOpen + '" aria-controls="bar-detail"><span class="lt-toggle__ico" aria-hidden="true"></span><span>' + sumTxt + '</span><span class="lt-toggle__lbl">' + (barOpen ? "Masquer le détail" : "Voir le détail") + '</span></button>' : '<span class="lb-bar__sum">' + sumTxt + '</span>') + '<span class="lb-bar__tot">' + (st.sel.length ? S.euro(t.total) : '<span class="sa-muted" style="font-size:13px">Total après le choix du look</span>') + '</span><span class="lb-bar__btns">' +
    (last ? (st.pack === "pro" ? S.button("Demander un devis", { action: "quote" }) : S.button("Réserver", { action: "book", disabled: !st.sel.length || !st.date || anyBusy() })) : (done(reached) ? S.button(NEXTS[reached], { action: "next", id: String(reached) }) : S.button("Étape " + (reached + 1) + " sur 5", { variant: "secondary", action: "goto" }))) + '</span></div>';
}
function reveal(i) { reached = Math.max(reached, i); render(); var s = document.getElementById("sec-" + i); if (s) s.scrollIntoView({ behavior: "smooth", block: "start" }); }

document.getElementById("r").innerHTML =
  S.announcementBar() + S.header({ active: "location" }) +
  '<figure class="lb-hero"><img src="' + P.look4 + '" alt="Look de location : gilet peau lainée et mini-jupe sequins"></figure>' +
  '<section class="lb-top2 sa-wrap"><div><span class="sa-mono sa-muted">LOCATION & RP</span><h1>Louer un look Simé</h1></div><div><p>Le vestiaire de nos shoots, le temps d\'une soirée. Tout se passe sur cette page : chaque étape s\'ouvre sous la précédente, et le prix se calcule en direct.</p><a class="sa-btn sa-btn--link" href="#s-pro">Vous êtes pro ?</a></div></section>' +
  '<div class="sa-wrap" id="tunnel"></div>' +
  '<div class="lb-bar" id="bar"></div>' +
  PRO + '<section class="lc-faq sa-wrap" style="border-top:1px solid var(--photocopy)"><div><span class="sa-mono sa-muted">QUESTIONS</span><h2>Avant de réserver</h2></div><div>' + FAQ + '</div></section>' +
  S.footer() + S.cartDrawer();
S.init(document);
render();
var root = document.getElementById("r");
root.addEventListener("click", function (e) {
  var b;
  if ((b = e.target.closest("[data-action='next']"))) { if (!b.disabled) reveal(+b.dataset.id + 1); return; }
  if ((b = e.target.closest("[data-action='bar-toggle']"))) { barOpen = !barOpen; drawBar(); var tg = document.querySelector("[data-action='bar-toggle']"); if (tg) tg.focus({ preventScroll: true }); return; }
  if ((b = e.target.closest("[data-action='goto']"))) { var s = document.getElementById("sec-" + reached); if (s) s.scrollIntoView({ behavior: "smooth", block: "start" }); return; }
  if ((b = e.target.closest("[data-action='book']"))) { toast("Prototype : la réservation passera par l'app de location Shopify"); return; }
  if ((b = e.target.closest("[data-action='quote']"))) { document.getElementById("s-pro").scrollIntoView({ behavior: "smooth" }); return; }
  if (!e.target.closest("#tunnel")) return;
  if (e.target.closest("[data-pack],[data-item],[data-mode],[data-dur]")) e.preventDefault();
  if ((b = e.target.closest("[data-pack]"))) { st.pack = b.dataset.pack; var pk = packOf(st.pack); st.opts.style = pk.style; st.opts.photo = pk.photo; if (st.pack !== "pro" && st.mode === "piece") { st.mode = "look"; st.sel = []; } render(); return; }
  if ((b = e.target.closest("[data-mode]"))) { if (st.mode !== b.dataset.mode) { st.mode = b.dataset.mode; st.sel = []; } render(); return; }
  if ((b = e.target.closest("[data-item]"))) { if (b.getAttribute("aria-disabled") === "true") return; var id = b.dataset.item, i = st.sel.indexOf(id); if (i > -1) st.sel.splice(i, 1); else st.sel.push(id); softUpdate(); return; }
  if ((b = e.target.closest("[data-dur]"))) { if (!b.disabled) { st.dur = b.dataset.dur; render(); } return; }
});
/* Mise à jour sur place après un choix de look ou de pièce : la grille n'est pas reconstruite */
function softUpdate() {
  document.querySelectorAll("#tunnel [data-item]").forEach(function (n) { var on = st.sel.indexOf(n.dataset.item) > -1; n.setAttribute("aria-pressed", on); var c = n.querySelector(".lc-item__check"); if (c) c.textContent = on ? "✓" : "+"; });
  document.querySelectorAll("#tunnel .lt-sec").forEach(function (s, i) { var x = s.querySelector(".lt-sec__state"); if (x) x.textContent = stateOf(i); });
  var cur = document.querySelector("#sec-1 .lt-next");
  if (cur) { var tmp = document.createElement("div"); tmp.innerHTML = body(1); var nx = tmp.querySelector(".lt-next"); if (nx) cur.replaceWith(nx); }
  if (reached >= 2) { var b2 = document.querySelector("#sec-2 .lt-sec__body"); if (b2) b2.innerHTML = body(2); }
  if (reached >= 4) { var b4 = document.querySelector("#sec-4 .lt-sec__body"); if (b4) b4.innerHTML = body(4); }
  drawBar();
}
root.addEventListener("change", function (e) {
  if (e.target.id === "date") { st.date = e.target.value; render(); return; }
  if (["style", "photo", "extra"].indexOf(e.target.dataset.opt) > -1) { st.opts[e.target.dataset.opt] = e.target.checked; render(); return; }
  if (e.target.name === "deliv") { st.delivery = e.target.value; render(); }
});
/* Arrivée depuis une fiche produit : #piece=SA-001 ou #look=L1 présélectionne la formule « Le look » et l'élément */
/* La barre de réservation s'efface quand on arrive sur le bloc pro : ce n'est plus le même parcours */
(function () { var pro = document.getElementById("s-pro"); if (!pro || !("IntersectionObserver" in window)) return;
  new IntersectionObserver(function (es) { es.forEach(function (en) { document.body.classList.toggle("is-pro-view", en.isIntersecting); }); }, { threshold: 0.15 }).observe(pro); })();
/* #piece=SA-001 : grand public, on ouvre le look qui contient la pièce ; #pro=SA-001 : formule Shoot pro, pièce à l'unité */
(function () { var m = (location.hash || "").match(/^#(piece|look|pro)=([A-Za-z0-9-]+)$/); if (!m) return;
  if (m[1] === "pro") { st.pack = "pro"; st.mode = "piece"; st.sel = [m[2]]; st.dur = "pro"; }
  else { var id = m[2]; if (m[1] === "piece") { var lk = LOOKS.filter(function (l) { return l.pieces.indexOf(id) > -1; })[0]; id = lk ? lk.id : null; }
    st.pack = "look"; st.mode = "look"; st.sel = id ? [id] : []; }
  reveal(1); })();
"""
import os
os.makedirs(D+'LocationPageB2', exist_ok=True)
open(D+'LocationPageB2/preview.html','w').write(head("Location & RP · tunnel sur une page","Location & RP, tunnel sur une seule page : les formules restent visibles, chaque étape s'ouvre sous la précédente après validation", cssB2)+jsB2+tail)
