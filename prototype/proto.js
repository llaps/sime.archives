/* Prototype Simé Archives : relie les maquettes du design system entre elles.
   Les composants du système gardent leurs liens « # » ; ce script les envoie vers la bonne page. */
(function () {
  var MAP = [
    ["drop.html#acces", ["Recevoir l’accès anticipé"]],
    ["drop.html", ["Voir la récolte à venir", "La prochaine récolte →"]],
    ["drop.html?statut=ouvert", ["Récolte 04 en cours", "Récolte en cours", "La récolte en cours", "Voir la récolte", "Voir la Récolte", "Toute la récolte →"]],
    ["shop.html", ["Shop", "Le Shop", "Toutes les pièces", "Tout le Shop", "Entrer →", "Récoltes passées", "Archives de créateurs", "Par marque"]],
    ["location.html", ["Location & RP", "Louer", "Tarifs et options", "Location look", "Location pièces", "Options", "Louer un look", "Les looks à louer", "Réserver →", "Formules et options", "Disponibilités et réservation", "Formules et tarifs", "Option stylisme et photo", "Pros · demande de devis", "Stylistes", "Artistes & musiciens", "Marques · demande de devis"]],
    ["journal.html", ["Journaling", "Tout le Journaling", "Fiches d'archive", "Fiches d’archive", "Lookbooks par shoot", "Archives caribéennes", "Lire la fiche d’archive", "Le défilé", "Le lookbook", "Une interview"]],
    ["apropos.html", ["À propos", "Simé Archives", "L’histoire de Simé", "Jardin Créole"]],
    ["aide.html#livraison", ["Livraison et retours"]],
    ["aide.html#mesures", ["Guide des mesures"]],
    ["aide.html#location", ["Conditions de location"]],
    ["aide.html#codes", ["Codes promo"]],
    ["aide.html#contact", ["Contact"]],
    ["index.html", ["Accueil"]]
  ];
  var MEGA_SHOP = /^(Chaussures|Hauts|Accessoires|Jupes|Vestes|Années \d+)/;
  function clean(t) { return (t || "").replace(/\s+/g, " ").replace(/\d+$/, "").trim(); }
  function target(el) {
    var t = clean(el.textContent);
    for (var i = 0; i < MAP.length; i++) if (MAP[i][1].indexOf(t) > -1) return MAP[i][0];
    if (MEGA_SHOP.test(t)) return "shop.html";
    return null;
  }
  function go(url) { location.href = url; }
  window.__ptTarget = target;
  /* La fiche lit le numéro dans l'ancre : on recharge quand on passe d'une pièce à l'autre */
  window.addEventListener("hashchange", function () { if (/piece\.html$/.test(location.pathname)) location.reload(); });

  document.addEventListener("click", function (e) {
    if (e.defaultPrevented) return;
    var el;
    if (e.target.closest(".pt-plan, .pt-pill")) return;
    if (e.target.closest(".sa-logo")) { e.preventDefault(); return go("index.html"); }
    if ((el = e.target.closest("[data-action='rent-pro']"))) { e.preventDefault(); return go("location.html#pro=" + el.dataset.id); }
    if ((el = e.target.closest("[data-action='rent']"))) { e.preventDefault(); return go("location.html" + (el.dataset.look ? "#look=" + el.dataset.look : el.dataset.id ? "#piece=" + el.dataset.id : "")); }
    if (e.target.closest(".hm-drop__img")) { e.preventDefault(); return go("drop.html?statut=ouvert"); }
    if (e.target.closest(".sa-mega__edito")) { e.preventDefault(); var m = e.target.closest("[data-mega]"); return go(m && m.dataset.mega === "location" ? "journal.html" : "drop.html?statut=ouvert"); }
    if (e.target.closest(".sa-post")) { e.preventDefault(); return go("journal.html"); }
    /* Méga-menu Shop : type, marque, époque → Shop */
    if (e.target.closest("[data-mega='shop'] a")) { e.preventDefault(); return go("shop.html"); }
    /* Portes de l'accueil : la première vers le Shop, la seconde vers la location */
    var door = e.target.closest(".sa-door");
    if (door) { e.preventDefault(); var ds = Array.prototype.indexOf.call(door.parentNode.children, door); return go(ds === 0 ? "shop.html" : "location.html"); }
    /* Rangées de recommandations : « Tous les hauts », « Toutes les pièces X » → Shop */
    if ((el = e.target.closest(".sa-rail-block a[href='#']"))) { e.preventDefault(); return go("shop.html"); }

    /* Vignette produit : clic hors boutons → fiche produit */
    if ((el = e.target.closest("[data-piece]"))) { e.preventDefault(); return go("piece.html#" + el.dataset.piece); }
    var card = e.target.closest(".sa-card");
    if (card && !e.target.closest("button, .sa-btn, input")) {
      var id = (card.textContent.match(/SA-\d{3}/) || [])[0];
      if (id && !card.classList.contains("is-sold")) { e.preventDefault(); return go("piece.html#" + id); }
    }
    el = e.target.closest("a[href='#'], button.sa-btn:not([data-action]), .hm-btn");
    if (el) { var u = target(el); if (u) { e.preventDefault(); go(u); } }
  }, false);

  /* Page récolte ouverte depuis « Recevoir l'accès anticipé » : on amène la cliente au champ e-mail */
  if (/drop\.html$/.test(location.pathname) && location.hash === "#acces") {
    setTimeout(function () { var f = document.getElementById("early-mail"); if (f) { f.scrollIntoView({ block: "center" }); f.focus({ preventScroll: true }); } }, 300);
  }
  /* Page Aide : ouvrir la bonne section */
  if (/aide\.html$/.test(location.pathname) && location.hash) {
    setTimeout(function () { var s = document.getElementById(location.hash.slice(1)); if (s) { s.scrollIntoView({ block: "start" }); s.querySelector("button") && s.querySelector("button").click(); } }, 300);
  }
  /* Fiche produit : changer de pièce sans recharger (lien depuis une recommandation) */
  window.addEventListener("hashchange", function () { if (/piece\.html$/.test(location.pathname)) location.reload(); });

  /* Liens externes : le compte Instagram du pied de page devient un vrai lien */
  document.querySelectorAll("a[href='#']").forEach(function (a) { if (/Instagram/.test(a.textContent)) { a.href = "https://www.instagram.com/sime.archives/"; a.target = "_blank"; a.rel = "noopener"; } });

  /* Plan du prototype */
  var PAGES = [
    ["index.html", "Accueil", "Grande image, en deux mots, la récolte en cours, acheter ou louer"],
    ["drop.html", "Page récolte", "Deux statuts : avant la récolte, récolte ouverte"],
    ["shop.html", "Shop", "Filtres, tri, colonnes, ajout rapide au panier"],
    ["piece.html#SA-001", "Fiche produit", "Photos, mesures, panier, fiche d’archive, recommandations"],
    ["location.html", "Location & RP", "Le tunnel de réservation, de la formule au récapitulatif"],
    ["journal.html", "Journaling", "Une fiche d’archive"],
    ["apropos.html", "À propos", "L’histoire de Simé"],
    ["aide.html", "Aide", "Livraison, mesures, location, codes promo, contact"]
  ];
  var css = document.createElement("style");
  css.textContent =
    ".pt-pill{position:fixed;right:max(12px,env(safe-area-inset-right,0px));bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:60;display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 12px;background:var(--ink);color:var(--on-ink);font:600 10px/1 var(--font-sans);letter-spacing:.14em;text-transform:uppercase;border:0;cursor:pointer}" +
    "body:has(.lb-bar) .pt-pill{bottom:calc(84px + env(safe-area-inset-bottom,0px))}" +
    "@media (max-width:900px){body:has(.lb-bar) .pt-pill{bottom:calc(132px + env(safe-area-inset-bottom,0px))}}" +
    "body:has(.lt-d:not([hidden])) .pt-pill{display:none}" +
    ".pt-pill:focus-visible{outline:2px solid var(--focus);outline-offset:2px}" +
    ".pt-plan{position:fixed;inset:0;z-index:70;background:rgba(28,26,24,.4);display:flex;align-items:flex-end;justify-content:flex-end;padding:max(12px,env(safe-area-inset-left,0px))}" +
    ".pt-plan[hidden]{display:none}" +
    ".pt-plan__box{background:var(--paper);width:min(420px,100%);max-height:80vh;overflow:auto;padding:20px;border:1px solid var(--ink);margin-bottom:calc(72px + env(safe-area-inset-bottom,0px))}" +
    ".pt-plan__box h2{margin:0 0 4px;font:500 22px/1.1 var(--font-display,var(--font-sans));font-stretch:112%}" +
    ".pt-plan__box p{margin:0 0 12px;font-size:13px;color:var(--ink-muted)}" +
    ".pt-plan__box a{display:grid;gap:2px;padding:10px 0;border-top:1px solid var(--photocopy);color:var(--ink);text-decoration:none}" +
    ".pt-plan__box a b{font-weight:500}.pt-plan__box a span{font-size:12px;color:var(--ink-muted)}" +
    ".pt-plan__box a[aria-current='page'] b::after{content:' · vous êtes ici';font-weight:400;color:var(--ink-muted)}";
  document.head.appendChild(css);
  var here = location.pathname.split("/").pop() || "index.html";
  var pill = document.createElement("button");
  pill.className = "pt-pill"; pill.type = "button"; pill.textContent = "Plan du prototype";
  var plan = document.createElement("div");
  plan.className = "pt-plan"; plan.hidden = true; plan.setAttribute("role", "dialog"); plan.setAttribute("aria-label", "Plan du prototype");
  plan.innerHTML = '<div class="pt-plan__box"><h2>Prototype Simé Archives</h2><p>Maquette navigable. Les paiements, réservations et e-mails ne partent pas.</p>' +
    PAGES.map(function (p) { var cur = p[0].split("#")[0] === here || (here === "" && p[0] === "index.html"); return '<a href="' + p[0] + '"' + (cur ? ' aria-current="page"' : '') + '><b>' + p[1] + '</b><span>' + p[2] + '</span></a>'; }).join("") + '</div>';
  pill.addEventListener("click", function () { plan.hidden = !plan.hidden; });
  plan.addEventListener("click", function (e) { if (e.target === plan) plan.hidden = true; });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") plan.hidden = true; });
  document.body.appendChild(pill); document.body.appendChild(plan);
})();
