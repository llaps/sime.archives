/* @ds-bundle: {"format":4,"namespace":"SimeArchives","components":[{"name":"Button"},{"name":"AnnouncementBar"},{"name":"Header"},{"name":"ProductCard"},{"name":"ListingToolbar"},{"name":"FilterDrawer"},{"name":"CartDrawer"},{"name":"DropCountdown"},{"name":"InventoryLabel"},{"name":"ArchiveSheet"},{"name":"Accordion"},{"name":"Footer"}]} */
(function () {
  "use strict";

  /* ── Données d'exemple (prototype) ─────────────────────────── */
  /* Photos : groupe d'assets « Photos looks - Lookbook + shop » (shoot Simé, recadré par pièce) */
  var PH = {
    look1: "/_blob/a4ffed76cc4fab9e30ccef1f6f268084", look2: "/_blob/6b93c55bffcc00bca798e8979add6d3e", look3: "/_blob/f62641df0aa554cf926c4b5ca588a0bd",
    look4: "/_blob/11fa8e3702ba635cc23eb5baeca1722e", look5: "/_blob/cd2f27678b6a2a148f4587492fc40f51",
    gilet: "/_blob/f01fb37cb64ce8827d7c1f27c68fb219", giletB: "/_blob/2e3956b8b96ae29f926f07a2c0d01d40",
    voile: "/_blob/b5b24c117f496a2cfea4a5cc9fceba3d", voileB: "/_blob/db0b5c347908f5b753e4cebb100f74bf",
    sac: "/_blob/b6fce6bd5d32faf49cc23cbf51d7fa05", sacB: "/_blob/6cde01ae319422f20ca1ab39093c6533",
    orteils: "/_blob/2ebab65e3d0f3205f075c0177f319fee", orteilsB: "/_blob/83def38e6db4dcb554674493691ac3ff",
    kaki: "/_blob/1e79bf90dbf6e5016ac7f7aa1ec80abf", kakiB: "/_blob/c7ece93d6c9d766c7e4a6c5ab3820cfb",
    tweed: "/_blob/2ea009bb06a6e48112cc50942133245e", tweedB: "/_blob/878490a9d9cec438f78b0cd610ea8b14",
    fourrure: "/_blob/a1fc45c068ec9de82a798871d59243e4", debardeur: "/_blob/52a2af6fc94785d830ee46f31cabf4a8",
    mjNoir: "/_blob/7af5b659b150b6f4eff08919b66930fc",
    look6: "/_blob/ea0911459f51022fb60a73ce1455f217", look7: "/_blob/7021afba37b3bdd214d8e2427bf9d4b4", look8: "/_blob/5e44de2358d34a8dc08efec7b41f48c4",
    chemise: "/_blob/3f258ded0223542438fb57f177650f40", bottes: "/_blob/a96ee4ba574717a64a4238dfa8fb9c82",
    panier: "/_blob/569e77d0a84f1ee9b06b4e87d36b6225", panierB: "/_blob/1a86cc92e62dd9ee77545b6223b40eee"
  };

  /* Données d'exemple : les pièces du shoot. Marques, prix et époques à confirmer par Vanina. */
  /* Mannequin du shoot (exemple à confirmer : prénom et taille réels) */
  var MODEL = { name: "Alima", height: "1,80 m" };

  var products = [
    { id: "SA-001", with: ["SA-002", "SA-013", "SA-003", "SA-004"], brand: "Sans marque", name: "Gilet zippé sans manches, nylon gris", era: "Y2K", eraLabel: "Y2K", type: "Haut", kind: "top", material: "Nylon", size: "S", price: 85, tone: "#8e9091", drop: "Récolte 04", city: "Paris", photos: [PH.gilet, PH.giletB, PH.look1] },
    { id: "SA-002", with: ["SA-013"], brand: "Paloma Wool", name: "Jupe voile blanche", era: "Contemporaine", eraLabel: "Contemporaine", type: "Jupe", kind: "jupe", material: "Voile", size: "36", price: 70, tone: "#e9e4dc", drop: "Récolte 04", city: "Paris", photos: [PH.voile, PH.voileB, PH.look5] },
    { id: "SA-003", brand: "Sans marque", name: "Sac filet tressé anis", era: "Années 90", eraLabel: "Années 90", type: "Accessoire", kind: "sac", material: "Fibre tressée", size: "TU", price: 55, tone: "#b7b23a", drop: "Récolte 04", city: "Marseille", photos: [PH.sac, PH.sacB, PH.look3] },
    { id: "SA-004", brand: "Vibram", name: "Chaussures à orteils séparés FiveFingers V-Aqua, lime", era: "Contemporaine", eraLabel: "Contemporaine", type: "Chaussures", kind: "chaussure", material: "Textile technique, semelle Vibram", size: "41", price: 60, tone: "#d7d36a", drop: "Récolte 04", city: "Lyon", photos: [PH.orteils, PH.orteilsB, PH.look5] },
    { id: "SA-005", brand: "Miu Miu", name: "Mary Jane bout carré, semelle bulle, kaki", era: "Automne-hiver 1999", eraLabel: "Années 90", type: "Chaussures", kind: "chaussure", material: "Daim, mesh technique, bride gros-grain, semelle caoutchouc", size: "38", price: 120, tone: "#6b6a3e", drop: "Récolte 04", tier: "Archive", city: "Anvers", photos: [PH.kaki, PH.kakiB, PH.look2] },
    { id: "SA-006", brand: "Sans marque", name: "Mini-jupe sequins grise", era: "Années 90", eraLabel: "Années 90", type: "Jupe", kind: "jupe", material: "Sequins sur tulle", size: "36", price: 65, tone: "#9b9890", drop: "Récolte 04", city: "Paris", photos: [PH.tweed, PH.tweedB, PH.look4] },
    { id: "SA-007", brand: "Kapital", name: "Gilet peau lainée sans manches", era: "Contemporaine", eraLabel: "Contemporaine", type: "Veste", kind: "veste", material: "Coton et peau lainée", size: "M", price: 140, tone: "#8a8463", drop: "Récolte 04", tier: "Archive", city: "Bordeaux", photos: [PH.fourrure, PH.look4] },
    { id: "SA-010", brand: "NA-KD", name: "Veste plissée vert d'eau", era: "Contemporaine", eraLabel: "Contemporaine", type: "Veste", kind: "veste", material: "Polyester plissé", size: "M", price: 75, tone: "#a9c4b0", drop: "Récolte 03", city: "Paris", photos: [PH.chemise, PH.look6] },
    { id: "SA-011", brand: "Vivienne Westwood", name: "Bottes Pirate à boucles, bout Animal, cuir noir", era: "Contemporaine", eraLabel: "Contemporaine", type: "Chaussures", kind: "chaussure", material: "Cuir", size: "40", price: 350, tone: "#1c1a18", drop: "Récolte 03", tier: "Archive", city: "Paris", photos: [PH.bottes, PH.look6] },
    { id: "SA-012", brand: "Sans marque", name: "Panier paille, anses bois, artisan de Guadeloupe", era: "Années 90", eraLabel: "Années 90", type: "Accessoire", kind: "sac", material: "Paille et bois", size: "TU", price: 68, tone: "#b49a5e", drop: "Récolte 02", city: "Guadeloupe", photos: [PH.panier, PH.panierB, PH.look8] },
    { id: "SA-013", with: ["SA-002"], brand: "Sans marque", name: "Jupe filet bleue", era: "Années 90", eraLabel: "Années 90", type: "Jupe", kind: "jupe", material: "Filet", size: "36", price: 45, tone: "#9fb4c8", drop: "Récolte 04", city: "Paris", photos: [PH.voileB, PH.voile, PH.look5] }
  ];

  /* Les pièces d'archive (tier « Archive », fonds Archives) ne se vendent pas : elles se louent uniquement.
     products = toutes les pièces (location, fiches) ; shopProducts = ce qui s'achète (Shop, récoltes, menus, filtres, recommandations). */
  /* Looks de location (stylés par Lou-Ann). Le grand public loue des looks complets ; les pièces à l'unité sont réservées aux pros. */
  var looks = [
    { id: "L1", name: "Nylon et voile", pieces: ["SA-001", "SA-002", "SA-013", "SA-003", "SA-004"] },
    { id: "L2", name: "Peau lainée et sequins", pieces: ["SA-007", "SA-006"] },
    { id: "L3", name: "Mary Jane kaki", pieces: ["SA-005", "SA-006"] },
    { id: "L4", name: "Plissé vert d'eau", pieces: ["SA-010", "SA-011"] },
    { id: "L5", name: "Panier paille", pieces: ["SA-012"] }
  ];
  var shopProducts = products.filter(function (p) { return p.tier !== "Archive"; });

  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var euro = function (n) { return n.toFixed(2).replace(".", ",") + " €"; };
  var find = function (id) { for (var i = 0; i < products.length; i++) if (products[i].id === id) return products[i]; return products[0]; };

  /* ── Images placeholder : silhouettes SVG, grain photocopie ─── */
  var SHAPES = {
    veste: "M100 92 L132 74 Q150 92 168 74 L200 92 L250 128 L262 250 L232 256 L222 170 L218 338 L82 338 L78 170 L68 256 L38 250 L50 128 Z",
    pull: "M104 92 Q150 112 196 92 L246 126 L262 262 L232 266 L220 172 L220 330 L80 330 L80 172 L68 266 L38 262 L54 126 Z",
    pantalon: "M96 66 L204 66 L222 340 L170 340 L150 150 L130 340 L78 340 Z",
    jupe: "M108 92 L192 92 L240 316 L60 316 Z",
    sac: "M84 168 L216 168 L226 300 L74 300 Z M112 168 Q112 104 150 104 Q188 104 188 168 L176 168 Q176 118 150 118 Q124 118 124 168 Z",
    chaussure: "M62 262 Q60 214 108 206 L150 158 Q182 140 196 170 L236 238 Q252 280 206 284 L88 284 Q62 284 62 262 Z",
    top: "M112 84 L130 84 Q150 112 170 84 L188 84 L196 130 Q214 150 212 200 L216 330 L84 330 L88 200 Q86 150 104 130 Z"
  };
  var GRAIN = "<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .11 0 0 0 0 .1 0 0 0 0 .09 0 0 0 .14 0'/></filter>";
  function madras(id) {
    return "<pattern id='" + id + "' width='24' height='24' patternUnits='userSpaceOnUse'><rect width='24' height='24' fill='#b35a3c'/><rect width='24' height='6' fill='#e3e04a' opacity='.75'/><rect width='5' height='24' fill='#2a49b8' opacity='.55'/><rect y='14' width='24' height='2' fill='#1c1a18' opacity='.4'/><rect x='16' width='2' height='24' fill='#f2ede4' opacity='.5'/></pattern>";
  }
  /* Vue de survol : toujours le look complet porté (dernière photo de la pièce) */
  function lookOf(p) { return p.photos && p.photos.length ? p.photos[p.photos.length - 1] : img(p, "b"); }

  /* Ligne mannequin : « Alima mesure 1,80 m et porte la taille S. » */
  function modelLine(p) {
    var m = p.model || MODEL; if (!m || !p.photos) return "";
    return "<p class='sa-pdp__model'>" + icon("user") + "<span>" + esc(m.name) + " mesure " + esc(m.height) + " et porte la taille " + esc(p.size) + ".</span></p>";
  }

  function img(p, variant) {
    if (p.photos && p.photos.length) {
      var i = variant === "b" ? 1 : variant === "c" ? 2 : 0;
      return p.photos[i] || p.photos[p.photos.length - 1];
    }
    var shape = SHAPES[p.kind] || SHAPES.veste;
    var fill = p.madras ? "url(#m)" : p.tone;
    var defs = "<defs>" + GRAIN + (p.madras ? madras("m") : "") + "</defs>";
    var svg;
    if (variant === "b") {
      /* Détail : gros plan matière + étiquette d'inventaire */
      svg = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 400'>" + defs +
        "<rect width='300' height='400' fill='#e6dfd2'/>" +
        "<g transform='translate(-210 -150) scale(2.6)'><path d='" + shape + "' fill='" + fill + "'/></g>" +
        "<g opacity='.18' stroke='#f2ede4' stroke-width='1'>" + (function () { var l = ""; for (var i = 0; i < 40; i++) l += "<line x1='" + (i * 9) + "' y1='0' x2='" + (i * 9 - 60) + "' y2='400'/>"; return l; })() + "</g>" +
        "<g transform='translate(158 248) rotate(-6)'><rect width='118' height='86' fill='#f2ede4' stroke='#8c877f'/><circle cx='14' cy='43' r='5' fill='#e6dfd2' stroke='#8c877f'/><text x='28' y='30' font-family='IBM Plex Mono, monospace' font-size='15' fill='#1c1a18'>" + p.id + "</text><text x='28' y='50' font-family='IBM Plex Mono, monospace' font-size='8' fill='#5b5650'>" + esc(p.era.toUpperCase()) + "</text><text x='28' y='64' font-family='IBM Plex Mono, monospace' font-size='8' fill='#5b5650'>" + esc(p.material.toUpperCase()) + "</text></g>" +
        "<rect width='300' height='400' filter='url(#g)'/></svg>";
    } else if (variant === "c") {
      /* À plat sur kraft */
      svg = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 400'>" + defs +
        "<rect width='300' height='400' fill='#c9b79f'/><g transform='translate(30 40) scale(.8)'><path d='" + shape + "' fill='" + fill + "'/></g>" +
        "<rect width='300' height='400' filter='url(#g)'/></svg>";
    } else {
      /* Porté / studio : silhouette centrée, ombre portée, fond papier */
      svg = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 400'>" + defs +
        "<rect width='300' height='400' fill='#e6dfd2'/><rect y='300' width='300' height='100' fill='#ddd5c7'/>" +
        "<ellipse cx='150' cy='350' rx='110' ry='10' fill='#1c1a18' opacity='.08'/>" +
        "<path d='" + shape + "' fill='" + fill + "' transform='translate(4 6)' opacity='.12'/>" +
        "<path d='" + shape + "' fill='" + fill + "'/>" +
        "<rect width='300' height='400' filter='url(#g)'/></svg>";
    }
    return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg).replace(/'/g, "%27");
  }

  /* ── Icônes (traits 1.4) ───────────────────────────────────── */
  var ICONS = {
    search: "<circle cx='11' cy='11' r='6.5'/><path d='M16 16l4.5 4.5'/>",
    user: "<circle cx='12' cy='8' r='4'/><path d='M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6'/>",
    heart: "<path d='M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z'/>",
    bag: "<path d='M5 8h14l-1 13H6z'/><path d='M9 8V6a3 3 0 0 1 6 0v2'/>",
    menu: "<path d='M3 7h18M3 12h18M3 17h18'/>",
    close: "<path d='M5 5l14 14M19 5L5 19'/>",
    filter: "<path d='M4 7h10M18 7h2M4 17h2M10 17h10'/><circle cx='16' cy='7' r='2'/><circle cx='8' cy='17' r='2'/>",
    arrow: "<path d='M4 12h16M14 6l6 6-6 6'/>",
    clock: "<circle cx='12' cy='12' r='8'/><path d='M12 8v4l3 2'/>"
  };
  function icon(n, label) {
    return "<svg class='sa-icon' viewBox='0 0 24 24' aria-hidden='" + (label ? "false" : "true") + "'" + (label ? " role='img' aria-label='" + esc(label) + "'" : "") + ">" + ICONS[n] + "</svg>";
  }

  /* ── Composants : renvoient du HTML ────────────────────────── */
  function button(label, opts) {
    opts = opts || {};
    return "<button class='sa-btn sa-btn--" + (opts.variant || "primary") + (opts.block ? " sa-btn--block" : "") + "'" + (opts.disabled ? " disabled" : "") + (opts.action ? " data-action='" + opts.action + "'" : "") + (opts.id ? " data-id='" + opts.id + "'" : "") + ">" + esc(label) + "</button>";
  }

  function announcementBar(msgs) {
    msgs = msgs || ["Récolte 04 · jeudi 19 h (Paris) · accès anticipé 18 h", "Pièces uniques, chinées partout dans le monde", "Envoi dans toute la France et les Outre-mer"];
    return "<div class='sa-announce' data-sa='announce' role='region' aria-label='Annonces'>" + msgs.map(function (m, i) { return "<p class='sa-announce__msg" + (i === 0 ? " is-on" : "") + "'>" + esc(m) + "</p>"; }).join("") + "</div>";
  }

  function logo() {
    return "<a class='sa-logo' href='#' aria-label='Simé Archives, accueil'><span class='sa-logo__word' aria-hidden='true'>SIM<i>E</i> ARCHIVES</span><span class='sa-logo__sub' data-sa='clocks' aria-label='Heure à Paris, en Guadeloupe et en Martinique'>PARIS <span data-tz='Europe/Paris'>--:--:--</span> · <span class='sa-logo__long'>GUADELOUPE / MARTINIQUE</span><span class='sa-logo__short'>GPE / MQ</span> <span data-tz='America/Guadeloupe'>--:--:--</span></span></a>";
  }

  /* Listes du méga-menu, alimentées par les fiches produit comme les filtres */
  function megaList(list, plural) {
    return list.map(function (c) { var t = plural && PLURAL[c[0]] ? PLURAL[c[0]].charAt(0).toUpperCase() + PLURAL[c[0]].slice(1) : c[0]; return "<li><a href='#'>" + esc(t) + "<span class='sa-mega__count'>" + c[1] + "</span></a></li>"; }).join("");
  }
  function megaPanel(key) {
    if (key === "shop") {
      var brands = megaList(counts("brand").filter(function (b) { return b[0] !== "Sans marque"; }));
      return "<div class='sa-mega sa-wrap' data-mega='shop'" + (brands ? "" : " data-nobrand") + ">" +
        "<div><h4 class='sa-label'>Le Shop</h4><ul><li><a href='#'>Récolte 04 en cours<span class='sa-mega__count'>" + shopProducts.filter(function (p) { return p.drop === "Récolte 04" && !p.sold; }).length + "</span></a></li><li><a href='#'>Toutes les pièces<span class='sa-mega__count'>" + shopProducts.filter(function (p) { return !p.sold; }).length + "</span></a></li><li><a href='#'>Récoltes passées<span class='sa-mega__count'>41</span></a></li></ul></div>" +
        (brands ? "<div><h4 class='sa-label'>Par marque</h4><ul>" + brands + "</ul></div>" : "") + /* colonne masquée tant qu'aucune marque n'est renseignée */
        "<div><h4 class='sa-label'>Par époque</h4><ul>" + megaList(counts("eraLabel").sort(function (a, b) { var r = function (e) { return e === "Contemporaine" ? 9999 : e === "Y2K" ? 2000 : parseInt((e.match(/\d+/) || ["0"])[0], 10) + (/^Années \d\d$/.test(e) ? 1900 : 0); }; return r(a[0]) - r(b[0]); })) + "</ul></div>" +
        "<a class='sa-mega__edito' href='#'><img src='" + PH.look3 + "' alt='Récolte 04 : gilet nylon, jupe voile, sac filet'><span><span class='sa-mono sa-muted'>RÉCOLTE 04 · JEUDI 19 H</span><br><span class='sa-serif' style='font-size:22px;line-height:1.15'>Technique et légère</span></span></a>" +
        "</div>";
    }
    if (key === "location") {
      return "<div class='sa-mega sa-wrap' data-mega='location'>" +
        "<div><h4 class='sa-label'>Location & RP</h4><ul><li><a href='#'>Louer</a></li><li><a href='#'>Tarifs et options</a></li><li><a href='#'>Journaling</a></li></ul></div>" +
        "<a class='sa-mega__edito' href='#'><img src='" + PH.giletB + "' alt='Gilet zippé en nylon gris, porté'><span><span class='sa-mono sa-muted'>JOURNAL · SA-001</span><br><span class='sa-serif' style='font-size:22px;line-height:1.15'>Le nylon qui voulait être une fourrure</span></span></a>" +
        "</div>";
    }
    return "";
  }

  function header(opts) {
    opts = opts || {};
    var nav = [["shop", "Shop"], ["location", "Location & RP"], ["about", "À propos"]];
    return "<header class='sa-header' data-sa='header'><div class='sa-header__bar sa-wrap'>" +
      "<nav class='sa-nav' aria-label='Principale'>" + nav.map(function (n) { return "<div class='sa-nav__item" + (opts.active === n[0] ? " is-active" : "") + "' data-menu='" + n[0] + "'><a class='sa-label' href='#'" + (opts.active === n[0] ? " aria-current='page'" : "") + ">" + n[1] + "</a></div>"; }).join("") + "</nav>" +
      "<button class='sa-burger' data-action='open-menu' aria-label='Menu'>" + icon("menu") + "</button>" +
      logo() +
      "<div class='sa-tools'><span class='sa-tools__lang'><b>FR</b> / EN</span>" +
      "<button data-tool='search' aria-label='Rechercher'>" + icon("search") + "</button>" +
      "<button data-tool='account' aria-label='Compte'>" + icon("user") + "</button>" +
      "<button data-tool='wish' aria-label='Favoris'>" + icon("heart") + "</button>" +
      "<button class='sa-bag' data-action='open-cart' aria-label='Panier'>" + icon("bag") + "<span class='sa-bag__count' data-n='0'>0</span></button></div>" +
      "</div>" + megaPanel("shop") + megaPanel("location") + "</header>" + mobileMenu() + "<div class='sa-scrim' data-sa='scrim'></div>";
  }

  /* Menu mobile : les mêmes trois entrées que l'en-tête et le pied de page */
  function mobileMenu() {
    var groups = [["Shop", ["Récolte 04 en cours", "Toutes les pièces", "Par marque", "Récoltes passées"]], ["Location & RP", ["Louer", "Tarifs et options", "Journaling"]], ["À propos", ["Simé Archives", "Jardin Créole", "Contact"]]];
    return "<aside class='sa-drawer sa-drawer--left sa-menu' data-sa='menu' aria-label='Menu'>" +
      "<div class='sa-drawer__head'><span class='sa-label'>Menu</span><button data-action='close' aria-label='Fermer'>" + icon("close") + "</button></div>" +
      "<div class='sa-drawer__body'>" + groups.map(function (g, i) { return "<details class='sa-menu__grp'" + (i === 0 ? " open" : "") + "><summary class='sa-label'>" + g[0] + "<span class='sa-acc__plus' aria-hidden='true'></span></summary><ul>" + g[1].map(function (l) { return "<li><a href='#'>" + l + "</a></li>"; }).join("") + "</ul></details>"; }).join("") + "</div>" +
      "<div class='sa-drawer__foot sa-mono sa-muted'><span><b>FR</b> / EN</span></div></aside>";
  }

  function productCard(p) {
    var sold = !!p.sold;
    /* Badge : l'époque de la pièce (abrégée pour les saisons : AH 1999), précédée de « Archive » pour les pièces de créateur. La taille passe dans la ligne du bas. */
    var era = String(p.era || "").replace(/^Automne-hiver /, "AH ").replace(/^Printemps-été /, "PE ");
    var sz = p.size === "TU" ? "Taille unique" : "Taille " + p.size;
    var badge = sold ? "" : "<span class='sa-card__badge'>" + (p.tier ? esc(p.tier) + " · " : "") + esc(era) + "</span>";
    return "<article class='sa-card" + (sold ? " is-sold" : "") + "' data-type='" + esc(p.type) + "' data-era='" + esc(p.eraLabel) + "' data-brand='" + esc(p.brand) + "' data-mat='" + esc(p.material) + "' data-sold='" + (sold ? 1 : 0) + "' data-price='" + p.price + "'>" +
      "<div class='sa-card__media'>" + badge +
      "<img class='is-a' src='" + img(p, "a") + "' alt='" + esc(p.name) + ", gros plan sur la pièce' loading='lazy'>" +
      "<img class='is-b' src='" + lookOf(p) + "' alt='" + esc(p.name) + ", portée dans le look complet' loading='lazy'>" +
      (sold ? "<span class='sa-stamp' data-date='" + esc(p.sold) + "'>Vendue</span>" : "") +
      (sold ? "" : "<button class='sa-card__wish' aria-pressed='false' aria-label='Ajouter " + esc(p.name) + " aux favoris' data-action='wish'>" + icon("heart") + "</button>") +
      "<span class='sa-card__dots' aria-hidden='true'><span></span><span></span></span>" +
      (sold ? "" : "<div class='sa-card__quick'><div class='sa-card__quick-row'><span class='sa-mono sa-muted'>Pièce unique</span><span class='sa-card__size'>" + esc(p.size) + "</span></div>" + button("Ajouter au panier", { block: true, action: "add", id: p.id }) + "</div>") +
      "</div>" +
      "<a class='sa-card__meta' href='#'><span class='sa-card__top'><span class='sa-label'>" + esc(p.brand) + "</span><span class='sa-mono sa-muted'>" + p.id + "</span></span>" +
      "<span class='sa-card__name'>" + esc(p.name) + "</span>" +
      "<span class='sa-card__top'><span class='sa-price'>" + (sold ? "<span class='sa-muted'>Archive · " + euro(p.price) + "</span>" : euro(p.price)) + "</span><span class='sa-mono sa-muted'>" + esc(sz) + "</span></span></a>" +
      "</article>";
  }

  function listingToolbar(count) {
    var g = function (n) { var r = ""; for (var i = 0; i < n; i++) r += "<rect x='" + (i * (20 / n) + 1) + "' y='3' width='" + (20 / n - 2) + "' height='14'/>"; return "<svg viewBox='0 0 22 20'>" + r + "</svg>"; };
    return "<div class='sa-toolbar sa-wrap' data-sa='toolbar'>" +
      "<div class='sa-toolbar__group'><button class='sa-label' data-action='open-filters'>" + icon("filter") + "Filtrer</button><span class='sa-chips' data-sa='chips'></span></div>" +
      "<div class='sa-toolbar__group'><span class='sa-mono sa-muted sa-toolbar__count' data-sa='count'>" + count + " pièces</span>" +
      "<label class='sa-label' style='display:flex;align-items:center;gap:8px'>Trier<select data-sa='sort' style='font:inherit;border:0;background:transparent;color:inherit;text-transform:uppercase;letter-spacing:.16em'><option value='new'>Nouveautés</option><option value='asc'>Prix croissant</option><option value='desc'>Prix décroissant</option></select></label>" +
      "<span class='sa-cols' role='group' aria-label='Colonnes'>" + [2, 3, 4].map(function (n) { return "<button data-cols='" + n + "' aria-pressed='" + (n === 4) + "' aria-label='" + n + " colonnes'>" + g(n) + "</button>"; }).join("") + "</span></div></div>";
  }

  function accordion(items, opts) {
    opts = opts || {};
    return items.map(function (it, i) {
      var open = it.open || (opts.firstOpen && i === 0);
      return "<div class='sa-acc" + (open ? " is-open" : "") + "'><button class='sa-acc__btn sa-label' aria-expanded='" + !!open + "' data-action='acc'>" + esc(it.title) + "<span class='sa-acc__plus' aria-hidden='true'></span></button><div class='sa-acc__panel'><div><div class='sa-acc__inner'>" + it.html + "</div></div></div></div>";
    }).join("");
  }

  function checks(name, values) {
    return values.map(function (v) { return "<label class='sa-check'><span><input type='checkbox' name='" + name + "' value='" + esc(v[0]) + "'>" + esc(v[0]) + "</span><span class='sa-mono sa-muted'>" + v[1] + "</span></label>"; }).join("");
  }

  function counts(key) {
    var m = {};
    products.forEach(function (p) {
      var v = p[key] || (key === "brand" ? "Sans marque" : "");
      if (p.tier === "Archive") return; /* pièces d'archive : location uniquement, hors filtres et menus du Shop */
      if (!v || (key === "brand" && v === "À identifier")) return; /* jamais affiché côté client */
      m[v] = (m[v] || 0) + 1;
    });
    return Object.keys(m).sort(function (a, b) { return m[b] - m[a] || a.localeCompare(b, "fr"); }).map(function (k) { return [k, m[k]]; });
  }

  function filterDrawer(opts) {
    opts = opts || {};
    var brands = counts("brand");
    var body = accordion([
      { title: "Type de pièce", open: true, html: checks("type", counts("type")) },
      { title: "Marque", open: true, html: (brands.length > 6 ? "<div class='sa-field' style='margin-bottom:8px'><label class='sa-sr' for='brand-q'>Chercher une marque</label><input id='brand-q' data-sa='brand-q' type='search' placeholder='Chercher une marque'></div>" : "") + "<div data-sa='brand-list'>" + checks("brand", brands) + "</div>" },
      { title: "Époque", html: checks("era", counts("eraLabel")) },
      { title: "Matière", html: checks("mat", counts("material")) },
      { title: "Disponibilité", html: "<label class='sa-check'><span><input type='checkbox' name='hidesold' value='1'>Masquer les pièces vendues</span></label>" }
    ]);
    return "<aside class='sa-drawer sa-drawer--left" + (opts.static ? " sa-drawer--static is-open" : "") + "' data-sa='filters' aria-label='Filtres'>" +
      "<div class='sa-drawer__head'><span class='sa-label'>Filtrer</span><button data-action='close' aria-label='Fermer'>" + icon("close") + "</button></div>" +
      "<div class='sa-drawer__body'>" + body + "</div>" +
      "<div class='sa-drawer__foot'>" + button("Voir les pièces", { block: true, action: "close", id: "apply" }) + "<button class='sa-btn sa-btn--link' style='justify-self:center' data-action='reset'>Tout effacer</button></div></aside>";
  }

  function cartDrawer(opts) {
    opts = opts || {};
    return "<aside class='sa-drawer sa-drawer--right" + (opts.static ? " sa-drawer--static is-open" : "") + "' data-sa='cart' aria-label='Panier'>" +
      "<div class='sa-drawer__head'><span class='sa-label'>Panier <span class='sa-mono sa-muted' data-sa='cart-n'>(0)</span></span><button data-action='close' aria-label='Fermer'>" + icon("close") + "</button></div>" +
      "<div class='sa-drawer__body' data-sa='cart-lines'></div>" +
      "<div class='sa-drawer__foot'><div class='sa-hold'>" + icon("clock") + "<span>Pièce unique : Simé vous la garde <b class='sa-mono' data-sa='hold'>15:00</b></span></div>" +
      "<details class='sa-promo' data-sa='promo'><summary class='sa-label'>Code promo<span class='sa-acc__plus' aria-hidden='true'></span></summary>" +
      "<form class='sa-promo__form' data-sa='promo-form' novalidate><div class='sa-field'><label class='sa-sr' for='promo-code'>Code promo</label><input id='promo-code' data-sa='promo-input' type='text' autocomplete='off' autocapitalize='characters' spellcheck='false' placeholder='Votre code'><button class='sa-label' type='submit'>Appliquer</button></div>" +
      "<p class='sa-promo__msg sa-mono' data-sa='promo-msg' role='status' aria-live='polite'></p></form></details>" +
      "<div class='sa-total sa-muted' data-sa='discount-row' hidden><span class='sa-mono' data-sa='discount-label'>Code</span><span class='sa-price' data-sa='discount'>0,00 €</span></div>" +
      "<div class='sa-total'><span class='sa-label'>Sous-total</span><span class='sa-price' data-sa='subtotal'>0,00 €</span></div>" +
      "<span class='sa-muted' style='font-size:13px'>Expédition calculée à l'étape suivante.</span>" +
      button("Passer commande", { block: true, action: "checkout" }) + "</div></aside>";
  }

  /* Bloc coloré d'une ligne : fond accent de la récolte, une info ou une note à mettre en avant (note d'archiviste, contrainte importante). Un seul par vue. */
  function noteLine(label, text, who) {
    return "<p class='sa-noteline'><span class='sa-mono'>" + esc(label) + "</span><span>" + text + "</span>" + (who ? "<span class='sa-mono'>" + esc(who) + "</span>" : "") + "</p>";
  }

  /* Citation éditoriale : réservée aux espaces édito (Journaling, fiches d'archive), jamais sur les pages de vente */
  function editoQuote(text, who) {
    text = text || "Une pièce d’archive n’est pas faite pour dormir au placard. Elle se sort, se mélange, se porte.";
    who = who || "Lou-Ann, stylisme";
    return "<figure class='sa-quote'><blockquote>« " + esc(text) + " »</blockquote><figcaption class='sa-label'>" + esc(who) + "</figcaption></figure>";
  }

  function dropCountdown(opts) {
    opts = opts || {};
    return "<section class='sa-drop' data-sa='drop'>" +
      "<div class='sa-drop__media'><img src='" + PH.look3 + "' alt='Récolte 04 : gilet nylon gris, jupe voile et sac filet anis'></div>" +
      "<div class='sa-drop__panel'><div><span class='sa-mono sa-muted'>RÉCOLTE 04 · " + esc(opts.when || "JEUDI 19 H (PARIS)") + "</span>" +
      "<h1 class='sa-drop__title'>Technique <em>et</em> légère</h1>" +
      "<p style='max-width:380px;margin:16px 0 0'>Des pièces uniques, réactivées en looks par Lou-Ann. Elles se dévoilent sur Instagram, puis ici jeudi à 19 h.</p></div>" +
      "<div class='sa-count' data-sa='count' role='timer' aria-label='Temps avant l&#39;ouverture de la récolte'>" + ["Jours", "Heures", "Min", "Sec"].map(function (u, i) { return "<div class='sa-count__cell'><span class='sa-count__num' data-u='" + i + "'>00</span><span class='sa-count__unit'>" + u + "</span></div>"; }).join("") + "</div>" +
      "<form class='sa-form' data-sa='early'><span class='sa-label'>Accès anticipé · une heure avant</span><div class='sa-field'><label class='sa-sr' for='early-mail'>E-mail</label><input id='early-mail' type='email' placeholder='Votre e-mail' required>" + "<button class='sa-label' type='submit'>Recevoir mon accès</button></div><p class='sa-form-ok'>Mèsi. Votre lien d'accès arrivera jeudi à 18 h.</p></form>" +
      "</div></section>";
  }

  function inventoryLabel(p, opts) {
    p = p || products[0]; opts = opts || {};
    if (opts.compact) {
      /* Version site : une ligne d'inventaire, cliquable pour la provenance */
      return "<p class='sa-tag-line' title='" + esc(p.brand + " · " + p.city) + "'><span>" + p.id + "</span><span>" + esc(p.era) + "</span><span>" + esc(p.material) + "</span><span>" + esc(p.city) + "</span></p>";
    }
    return "<div class='sa-tag'><span class='sa-tag__fund'>" + esc(opts.fund || "Shop") + "</span><span class='sa-tag__no'>" + p.id + "</span>" +
      "<dl><dt>Marque</dt><dd>" + esc(p.brand) + "</dd><dt>Époque</dt><dd>" + esc(p.era) + "</dd><dt>Matière</dt><dd>" + esc(p.material) + "</dd><dt>Provenance</dt><dd>" + esc(p.city) + "</dd><dt>Taille</dt><dd>" + esc(p.size) + "</dd></dl></div>";
  }

  /* Fiche d'archive, version B : tout est visible, en chapitres numérotés, avec un sommaire collant */
  function archiveChapters(p) {
    p = p || products[0];
    var ch = [["piece", "La pièce", "Ce que vous avez entre les mains"], ["histoire", "Son histoire", "La marque, l'époque, le contexte"], ["regard", "La touche Simé", "Comment la porter aujourd'hui"], ["plus", "Pour aller plus loin", "Sources et liens"]];
    var body = {
      piece: "<p class='sa-first'>Le premier détail, c'est le son. Un nylon gris, presque papier, qui froisse comme une enveloppe. Col montant, zip court, emmanchures nettes : un vêtement de pluie qui a perdu ses manches et gagné la ville.</p>" +
        "<dl class='sa-specs'><dt>Type</dt><dd>Gilet sans manches, col montant zippé</dd><dt>Matière</dt><dd>" + esc(p.material) + ", cordon de serrage à la taille</dd><dt>Taille</dt><dd>" + esc(p.size) + " · largeur aisselles 46 cm à plat</dd><dt>État</dt><dd>Très bon. Légère trace sur le zip, photographiée.</dd><dt>Provenance</dt><dd>Trouvé par Vanina, " + esc(p.city) + "</dd></dl>",
      histoire: "<p>Au tournant des années 2000, les vêtements techniques quittent la montagne pour la ville : nylon, zips, cordons. Les maisons italiennes en font un vestiaire urbain, les friperies en héritent vingt ans plus tard.</p>",
      regard: "<p>Technique en haut, voile en bas : Lou-Ann a conçu ce look avec deux jupes superposées, la voile blanche Paloma Wool SA-002 et le filet bleu SA-013, le sac filet SA-003 et les FiveFingers Vibram SA-004. L'hybridation, sans costume.</p><div class='sa-sheet__grid sa-sheet__grid--ig'>" + [["a", "la pièce"], ["b", "portée"], ["c", "le look"]].map(function (v) { return "<a href='https://www.instagram.com/sime.archives/' target='_blank' rel='noopener' aria-label='" + esc(p.name) + ", " + v[1] + " : voir le post sur Instagram (nouvel onglet)'><img src='" + img(p, v[0]) + "' alt=''></a>"; }).join("") + "</div><p class='sa-sheet__src sa-mono sa-muted'>Photos tirées des posts @sime.archives de la pièce. Cliquez pour ouvrir le post.</p>" + (function () {
        /* Le look de Lou-Ann, sous la touche Simé : les autres pièces du look, cliquables, et la location du look */
        var lk = looks.filter(function (l) { return l.pieces.indexOf(p.id) > -1; })[0];
        if (!lk) return "";
        var others = lk.pieces.filter(function (id) { return id !== p.id; }).map(find);
        return "<div class='sa-sheet__look'><span class='sa-label'>Le look de Lou-Ann · " + esc(lk.name) + "</span>" +
          "<div class='sa-sheet__look-grid'>" + others.map(function (q) { return "<a class='sa-sheet__look-item' href='#' data-piece='" + q.id + "'><img src='" + img(q, "a") + "' alt=''><span class='sa-mono sa-muted'>" + q.id + "</span><span>" + esc(q.name) + "</span></a>"; }).join("") + "</div>" +
          "<button class='sa-btn sa-btn--link' data-action='rent' data-look='" + lk.id + "'>Louer le look complet →</button></div>";
      })(),
      plus: "<p><a href='#'>Le défilé</a> · <a href='#'>Le lookbook</a> · <a href='#'>Une interview</a></p><p class='sa-mono sa-muted'>Texte d'exemple, à réécrire et sourcer par l'auteure. Images : photos Simé uniquement.</p>"
    };
    return "<article class='sa-chap' data-sa='chapters'>" +
      "<header class='sa-chap__head'><div class='sa-sheet__kicker sa-label'><span>" + esc(p.brand) + "</span><span>" + esc(p.era) + "</span><span>" + p.id + "</span></div>" +
      "<h2 class='sa-sheet__title'>Le nylon qui voulait être une fourrure</h2><p class='sa-sheet__by'>Par <b>Vanina</b> · Paris, 12 novembre 2026 · <span class='sa-mono'>Lecture 3 min</span></p></header>" +
      "<nav class='sa-chap__toc' aria-label='Sommaire de la fiche'><ol>" + ch.map(function (c, i) { return "<li><a href='#ch-" + c[0] + "' data-chap='" + c[0] + "'" + (i === 0 ? " aria-current='true'" : "") + "><span class='sa-mono'>0" + (i + 1) + "</span><span><b>" + c[1] + "</b><small>" + c[2] + "</small></span></a></li>"; }).join("") + "</ol></nav>" +
      "<div class='sa-chap__body sa-prose'>" + ch.map(function (c, i) { return "<section class='sa-chap__sec' id='ch-" + c[0] + "'><h3><span class='sa-mono sa-muted'>0" + (i + 1) + "</span> " + c[1] + "</h3>" + body[c[0]] + "</section>"; }).join("") + "</div></article>";
  }

  function archiveSheet(p) {
    p = p || products[0];
    return "<article class='sa-sheet' data-sa='sheet'>" +
      "<div class='sa-sheet__kicker sa-label'><span>" + esc(p.brand) + "</span><span>" + esc(p.era) + "</span><span>" + p.id + "</span></div>" +
      "<h2 class='sa-sheet__title'>Le nylon qui voulait être une fourrure</h2>" +
      "<p class='sa-sheet__by'>Par <b>Vanina</b> · Paris, 12 novembre 2026</p>" +
      "<div class='sa-sheet__grid'><img src='" + img(p, "a") + "' alt='" + esc(p.name) + ", la pièce'><img src='" + img(p, "b") + "' alt='" + esc(p.name) + ", portée'><img src='" + img(p, "c") + "' alt='" + esc(p.name) + ", le look'></div>" +
      "<div class='sa-tabs' role='tablist'><button class='sa-label' role='tab' aria-selected='true' data-tab='piece'>La pièce</button><button class='sa-label' role='tab' aria-selected='false' data-tab='archive'>L'archive</button></div>" +
      "<div class='sa-tabpanel' data-panel='piece'><div class='sa-prose'><p class='sa-first'>Le premier détail, c'est le son. Un nylon gris, presque papier, qui froisse comme une enveloppe. Col montant, zip court, emmanchures nettes : un vêtement de pluie qui a perdu ses manches et gagné la ville.</p>" +
      "<dl class='sa-specs'><dt>Type</dt><dd>Gilet sans manches, col montant zippé</dd><dt>Matière</dt><dd>" + esc(p.material) + ", cordon de serrage à la taille</dd><dt>Taille</dt><dd>" + esc(p.size) + " · largeur aisselles 46 cm à plat</dd><dt>État</dt><dd>Très bon. Légère trace sur le zip, photographiée.</dd><dt>Provenance</dt><dd>Trouvé par Vanina, dépôt-vente, " + esc(p.city) + "</dd></dl>" +
      "<h3>La touche Simé</h3><p>Technique en haut, voile en bas : Lou-Ann a conçu ce look avec deux jupes superposées, la voile blanche Paloma Wool SA-002 et le filet bleu SA-013, le sac filet SA-003 et les FiveFingers Vibram SA-004. L'hybridation, sans costume.</p></div></div>" +
      "<div class='sa-tabpanel' data-panel='archive' hidden><div class='sa-prose'><p class='sa-first'>Au tournant des années 2000, les vêtements techniques quittent la montagne pour la ville : nylon, zips, cordons. Les maisons italiennes en font un vestiaire urbain, les friperies en héritent vingt ans plus tard.</p><p>Pour aller plus loin : <a href='#'>le défilé</a>, <a href='#'>le lookbook</a>, <a href='#'>une interview</a>.</p><p class='sa-mono sa-muted'>Texte d'exemple, à réécrire et sourcer par l'auteure. Images : photos Simé uniquement.</p></div></div>" +
      "</article>";
  }

  /* ── Recommandations (à la SSENSE) : le look, la marque, le type de pièce ── */
  var PLURAL = { "Haut": "hauts", "Jupe": "jupes", "Chaussures": "chaussures", "Veste": "vestes", "Accessoire": "accessoires", "Maille": "pièces en maille", "Pantalon": "pantalons" };
  function rail(kicker, title, items, link) {
    if (!items.length) return "";
    return "<section class='sa-rail-block'><div class='sa-section__head'><div><span class='sa-mono sa-muted'>" + esc(kicker) + "</span><h2>" + esc(title) + "</h2></div>" +
      "<div class='sa-rail__nav'><a class='sa-btn sa-btn--link' href='#'>" + esc(link) + "</a><button data-rail='-1' aria-label='Précédent'>" + icon("arrow") + "</button><button data-rail='1' aria-label='Suivant'>" + icon("arrow") + "</button></div></div>" +
      "<div class='sa-rail' tabindex='0' aria-label='" + esc(title) + "'>" + items.map(productCard).join("") + "</div></section>";
  }
  function related(p) {
    /* Deux rangées seulement, comme SSENSE : 1. même type de pièce, 2. même marque. Pièces disponibles uniquement. */
    var pool = shopProducts.filter(function (q) { return q.id !== p.id && !q.sold; });
    var known = p.brand && p.brand !== "Sans marque" && p.brand !== "À identifier";
    var byType = pool.filter(function (q) { return q.type === p.type; });
    var byBrand = known ? pool.filter(function (q) { return q.brand === p.brand; }) : [];
    var label = PLURAL[p.type] || p.type.toLowerCase();
    return rail("MÊME TYPE · " + p.type.toUpperCase(), "D'autres " + label + " disponibles", byType, "Tous les " + label) +
      rail("MÊME MARQUE", "Plus de " + p.brand, byBrand, "Toutes les pièces " + p.brand);
  }

  function footer() {
    return "<footer class='sa-footer sa-wrap'><div class='sa-footer__grid'>" +
      "<div><p class='sa-footer__sign'>Ce qui a été semé revient autrement.</p><p class='sa-footer__gloss sa-mono sa-muted'>Simé : « semé », en créole.</p><form class='sa-form' data-sa='news'><span class='sa-label'>La lettre des récoltes</span><div class='sa-field'><label class='sa-sr' for='news-mail'>E-mail</label><input id='news-mail' type='email' placeholder='Votre e-mail' required><button class='sa-label' type='submit'>OK</button></div><p class='sa-form-ok'>Mèsi. À jeudi, 18 h.</p></form></div>" +
      "<div><h4 class='sa-label'>Shop</h4><ul><li><a href='#'>Récolte en cours</a></li><li><a href='#'>Toutes les pièces</a></li><li><a href='#'>Par marque</a></li><li><a href='#'>Récoltes passées</a></li></ul></div>" +
      "<div><h4 class='sa-label'>Location & RP</h4><ul><li><a href='#'>Louer</a></li><li><a href='#'>Tarifs et options</a></li><li><a href='#'>Journaling</a></li></ul></div>" +
      "<div><h4 class='sa-label'>À propos</h4><ul><li><a href='#'>Simé Archives</a></li><li><a href='#'>Jardin Créole</a></li><li><a href='#'>Instagram @sime.archives</a></li><li><a href='#'>Contact</a></li></ul></div>" +
      "<div><h4 class='sa-label'>Aide</h4><ul><li><a href='#'>Livraison et retours</a></li><li><a href='#'>Conditions de location</a></li><li><a href='#'>Guide des mesures</a></li><li><a href='#'>Codes promo</a></li></ul></div>" +
      "</div><div class='sa-footer__base sa-mono sa-muted'><span>© 2026 Simé Archives · Paris</span><span>CGV · Mentions légales · Confidentialité</span><span>FR / EN</span></div></footer>";
  }

  /* ── Comportements ─────────────────────────────────────────── */
  var cart = [];
  /* Codes de démonstration. En production, les codes se créent dans Shopify (Remises) et se valident au paiement. */
  var PROMOS = { SEME10: { pct: 10, label: "SEME10 · −10 %" }, AMIS15: { pct: 15, label: "AMIS15 · −15 % liste Amis proches" } };
  var promo = null;
  var holdTimer = null;

  function toast(root, msg) {
    var t = root.querySelector(".sa-toast");
    if (!t) { t = document.createElement("div"); t.className = "sa-toast"; t.setAttribute("role", "status"); root.appendChild(t); }
    t.textContent = msg; t.classList.add("is-on");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("is-on"); }, 2200);
  }

  function renderCart(root) {
    var lines = root.querySelector("[data-sa='cart-lines']");
    var total = 0;
    if (lines) {
      lines.innerHTML = cart.length ? cart.map(function (p) {
        total += p.price;
        return "<div class='sa-line'><img src='" + img(p, "a") + "' alt=''><div class='sa-line__info'><span class='sa-label'>" + esc(p.brand) + "</span><span>" + esc(p.name) + "</span><span class='sa-mono sa-muted'>" + p.id + " · Taille " + esc(p.size) + "</span><span class='sa-price'>" + euro(p.price) + "</span><button class='sa-line__remove' data-action='remove' data-id='" + p.id + "'>Retirer</button></div></div>";
      }).join("") : "<p class='sa-empty'>Votre panier est vide.<br><span class='sa-mono'>Le prochaine récolte tombe jeudi à 19 h.</span></p>";
    }
    var set = function (sel, v) { root.querySelectorAll(sel).forEach(function (n) { n.textContent = v; if (n.dataset.n !== undefined) n.dataset.n = v; }); };
    var off = promo && cart.length ? Math.round(total * promo.pct) / 100 : 0;
    root.querySelectorAll("[data-sa='discount-row']").forEach(function (r) { r.hidden = !off; });
    set("[data-sa='discount-label']", promo ? promo.label : "");
    set("[data-sa='discount']", "−" + euro(off));
    set("[data-sa='subtotal']", euro(total - off));
    set("[data-sa='cart-n']", "(" + cart.length + ")");
    root.querySelectorAll(".sa-bag__count").forEach(function (n) { n.textContent = cart.length; n.dataset.n = cart.length; });
  }

  function startHold(root) {
    var end = Date.now() + 15 * 60 * 1000;
    clearInterval(holdTimer);
    holdTimer = setInterval(function () {
      var s = Math.max(0, Math.round((end - Date.now()) / 1000));
      root.querySelectorAll("[data-sa='hold']").forEach(function (n) { n.textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); });
    }, 1000);
  }

  function openDrawer(root, which) {
    var d = root.querySelector("[data-sa='" + which + "']");
    if (!d || d.classList.contains("sa-drawer--static")) return;
    d.classList.add("is-open");
    var s = root.querySelector("[data-sa='scrim']"); if (s) s.classList.add("is-on");
    var f = d.querySelector("button"); if (f) f.focus({ preventScroll: true });
  }
  function closeDrawers(root) {
    root.querySelectorAll(".sa-drawer:not(.sa-drawer--static)").forEach(function (d) { d.classList.remove("is-open"); });
    var s = root.querySelector("[data-sa='scrim']"); if (s) s.classList.remove("is-on");
  }

  function applyFilters(root) {
    var grid = root.querySelector(".sa-grid"); if (!grid) return;
    var pick = function (n) { return Array.prototype.map.call(root.querySelectorAll("input[name='" + n + "']:checked"), function (i) { return i.value; }); };
    var types = pick("type"), eras = pick("era"), brands = pick("brand"), mats = pick("mat"), hide = pick("hidesold").length > 0;
    var n = 0;
    grid.querySelectorAll(".sa-card").forEach(function (c) {
      var ok = (!types.length || types.indexOf(c.dataset.type) > -1) && (!eras.length || eras.indexOf(c.dataset.era) > -1) &&
        (!brands.length || brands.indexOf(c.dataset.brand) > -1) && (!mats.length || mats.indexOf(c.dataset.mat) > -1) && !(hide && c.dataset.sold === "1");
      c.classList.toggle("is-hidden", !ok); if (ok) n++;
    });
    var all = types.concat(brands, eras, mats);
    var ins = grid.querySelector(".sa-insert"); if (ins) ins.classList.toggle("is-hidden", all.length > 0);
    var cnt = root.querySelector("[data-sa='count']"); if (cnt && cnt.classList.contains("sa-toolbar__count")) cnt.textContent = n + " pièces";
    var chips = root.querySelector("[data-sa='chips']");
    if (chips) chips.innerHTML = all.map(function (v) { return "<span class='sa-chip'>" + esc(v) + "</span>"; }).join("") + (hide ? "<span class='sa-chip'>Disponibles</span>" : "");
    var apply = root.querySelector("[data-sa='filters'] [data-id='apply']"); if (apply) apply.textContent = "Voir " + n + " pièces";
  }

  /* Rythme : une récolte par mois, le premier jeudi à 19 h (heure de Paris) */
  function firstThursday19(y, m) { var t = new Date(y, m, 1, 19, 0, 0, 0); t.setDate(1 + (4 - t.getDay() + 7) % 7); return t; }
  function nextThursday19() {
    var now = new Date(), t = firstThursday19(now.getFullYear(), now.getMonth());
    if (now >= t) t = firstThursday19(now.getFullYear(), now.getMonth() + 1);
    return t;
  }

  function init(root) {
    root = root || document;
    var host = root === document ? document.body : root;
    if (host._saInit) return; host._saInit = true;

    /* Barre d'annonce rotative */
    root.querySelectorAll("[data-sa='announce']").forEach(function (bar) {
      var msgs = bar.querySelectorAll(".sa-announce__msg"), i = 0;
      if (msgs.length > 1) setInterval(function () { msgs[i].classList.remove("is-on"); i = (i + 1) % msgs.length; msgs[i].classList.add("is-on"); }, 3600);
    });

    /* Méga-menu au survol (desktop) */
    root.querySelectorAll("[data-sa='header']").forEach(function (h) {
      var timer;
      var close = function () { h.classList.remove("is-mega"); h.querySelectorAll(".sa-mega, .sa-nav__item").forEach(function (m) { m.classList.remove("is-open"); }); };
      h.querySelectorAll(".sa-nav__item").forEach(function (it) {
        var panel = h.querySelector("[data-mega='" + it.dataset.menu + "']");
        it.addEventListener("mouseenter", function () {
          clearTimeout(timer); close();
          if (panel) { h.classList.add("is-mega"); panel.classList.add("is-open"); it.classList.add("is-open"); }
        });
      });
      h.addEventListener("mouseleave", function () { timer = setTimeout(close, 120); });
      h.addEventListener("mouseenter", function () { clearTimeout(timer); });
    });

    /* En-tête : masqué au scroll vers le bas, réaffiché au scroll vers le haut */
    root.querySelectorAll("[data-sa='header']").forEach(function (h) {
      var sc = h.closest(".sa-page"), target = sc || window, wrap = sc || document.body, last = 0, ticking = false, start = h.offsetTop, hh = h.offsetHeight;
      var pos = function () { return sc ? sc.scrollTop : window.pageYOffset; };
      var update = function () {
        var y = pos(), d = y - last;
        if (Math.abs(d) > 6) {
          var hide = d > 0 && y > start + hh + 40 && !h.classList.contains("is-mega");
          h.classList.toggle("is-hidden", hide);
          wrap.classList.toggle("sa-nav-hidden", hide);
          last = y;
        }
        h.classList.toggle("is-scrolled", y > start + 4);
        ticking = false;
      };
      target.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
      h.addEventListener("focusin", function () { h.classList.remove("is-hidden"); wrap.classList.remove("sa-nav-hidden"); });
    });

    /* Deux horloges sous le logo : Paris et la Guadeloupe */
    root.querySelectorAll("[data-sa='clocks']").forEach(function (c) {
      var tick = function () {
        c.querySelectorAll("[data-tz]").forEach(function (n) {
          try { n.textContent = new Date().toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit", second: "2-digit", timeZone: n.dataset.tz }); } catch (e) {}
        });
      };
      tick(); setInterval(tick, 1000);
    });

    /* Compte à rebours de la récolte */
    root.querySelectorAll("[data-sa='count'][role='timer']").forEach(function (c) {
      var target = nextThursday19();
      var tick = function () {
        var s = Math.max(0, Math.floor((target - new Date()) / 1000));
        var v = [Math.floor(s / 86400), Math.floor(s / 3600) % 24, Math.floor(s / 60) % 60, s % 60];
        c.querySelectorAll("[data-u]").forEach(function (n) { n.textContent = String(v[+n.dataset.u]).padStart(2, "0"); });
      };
      tick(); setInterval(tick, 1000);
    });

    /* Formulaires d'inscription */
    root.querySelectorAll(".sa-form").forEach(function (f) { f.addEventListener("submit", function (e) { e.preventDefault(); f.classList.add("is-done"); }); });

    /* Fiche d'archive B : sommaire qui suit la lecture */
    root.querySelectorAll("[data-sa='chapters']").forEach(function (art) {
      var links = art.querySelectorAll("[data-chap]"), secs = art.querySelectorAll(".sa-chap__sec");
      if (!("IntersectionObserver" in window)) return;
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (en.isIntersecting) links.forEach(function (l) { l.setAttribute("aria-current", l.dataset.chap === en.target.id.slice(3)); }); });
      }, { root: art.closest(".sa-page"), rootMargin: "-30% 0px -60% 0px" });
      secs.forEach(function (sc) { io.observe(sc); });
      art.addEventListener("click", function (e) { var l = e.target.closest("[data-chap]"); if (!l) return; e.preventDefault(); art.querySelector("#ch-" + l.dataset.chap).scrollIntoView({ behavior: "smooth", block: "start" }); });
    });

    /* Délégation de clics */
    host.addEventListener("click", function (e) {
      var rb = e.target.closest("[data-rail]");
      if (rb) { var rl = rb.closest(".sa-rail-block").querySelector(".sa-rail"); rl.scrollBy({ left: +rb.dataset.rail * rl.clientWidth * 0.8, behavior: "smooth" }); return; }
      var el = e.target.closest("[data-action], [data-cols], [data-tab], .sa-pdp__gallery figure");
      if (!el) { if (e.target.closest("[data-sa='scrim']")) closeDrawers(root); return; }
      if (el.matches(".sa-pdp__gallery figure")) { el.classList.toggle("is-zoom"); return; }
      if (el.dataset.cols) {
        var grid = root.querySelector(".sa-grid"); if (grid) grid.dataset.cols = el.dataset.cols;
        el.parentNode.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b === el); });
        return;
      }
      if (el.dataset.tab) {
        var sheet = el.closest(".sa-sheet") || root;
        sheet.querySelectorAll("[role='tab']").forEach(function (t) { t.setAttribute("aria-selected", t === el); });
        sheet.querySelectorAll(".sa-tabpanel").forEach(function (p) { p.hidden = p.dataset.panel !== el.dataset.tab; });
        return;
      }
      var a = el.dataset.action;
      if (a === "acc") { var acc = el.closest(".sa-acc"); acc.classList.toggle("is-open"); el.setAttribute("aria-expanded", acc.classList.contains("is-open")); }
      else if (a === "wish") { var on = el.getAttribute("aria-pressed") !== "true"; el.setAttribute("aria-pressed", on); toast(host, on ? "Ajoutée aux favoris" : "Retirée des favoris"); }
      else if (a === "add") {
        e.preventDefault();
        var p = find(el.dataset.id);
        if (cart.some(function (c) { return c.id === p.id; })) { toast(host, p.id + " est déjà dans votre panier"); }
        else { cart.push(p); renderCart(root); startHold(root); }
        if (root.querySelector("[data-sa='cart']:not(.sa-drawer--static)")) openDrawer(root, "cart"); else toast(host, p.id + " ajoutée au panier");
      }
      else if (a === "remove") { cart = cart.filter(function (c) { return c.id !== el.dataset.id; }); renderCart(root); }
      else if (a === "open-cart") openDrawer(root, "cart");
      else if (a === "open-menu") openDrawer(root, "menu");
      else if (a === "open-filters") openDrawer(root, "filters");
      else if (a === "close") { if (el.dataset.id === "apply") applyFilters(root); closeDrawers(root); }
      else if (a === "reset") { root.querySelectorAll("[data-sa='filters'] input").forEach(function (i) { i.checked = false; }); applyFilters(root); }
      else if (a === "checkout") toast(host, "Prototype : le paiement passe par Shopify");
      else if (a === "rent") toast(host, "Ouvre le calendrier de location");
    });
    host.addEventListener("change", function (e) {
      if (e.target.closest("[data-sa='filters']") && e.target.type === "checkbox") applyFilters(root);
      if (e.target.matches("[data-sa='sort']")) {
        var grid = root.querySelector(".sa-grid"); if (!grid) return;
        var cards = Array.prototype.slice.call(grid.querySelectorAll(".sa-card"));
        var v = e.target.value;
        cards.sort(function (x, y) { return v === "asc" ? x.dataset.price - y.dataset.price : v === "desc" ? y.dataset.price - x.dataset.price : 0; });
        cards.forEach(function (c) { grid.appendChild(c); });
      }
    });
    host.addEventListener("submit", function (e) {
      var f = e.target.closest("[data-sa='promo-form']"); if (!f) return;
      e.preventDefault();
      var inp = f.querySelector("[data-sa='promo-input']"), code = inp.value.trim().toUpperCase().replace(/\s+/g, ""), msg = f.querySelector("[data-sa='promo-msg']");
      if (!code) { msg.textContent = "Saisissez un code."; return; }
      if (PROMOS[code]) { promo = PROMOS[code]; msg.textContent = "Code " + code + " appliqué."; f.classList.remove("is-error"); inp.removeAttribute("aria-invalid"); }
      else { promo = null; msg.textContent = "Ce code ne fonctionne pas : il a peut-être expiré."; f.classList.add("is-error"); inp.setAttribute("aria-invalid", "true"); }
      renderCart(root);
    });
    host.addEventListener("input", function (e) {
      if (!e.target.matches("[data-sa='brand-q']")) return;
      var q = e.target.value.trim().toLowerCase();
      root.querySelectorAll("[data-sa='brand-list'] .sa-check").forEach(function (l) { l.style.display = l.textContent.toLowerCase().indexOf(q) > -1 ? "" : "none"; });
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDrawers(root); });
    renderCart(root);
  }

  window.SimeArchives = {
    products: products, shopProducts: shopProducts, looks: looks,
    lookFor: function (id) { return looks.filter(function (l) { return l.pieces.indexOf(id) > -1; })[0] || null; },
    lookPrice: function (l) { var v = l.pieces.reduce(function (s, id) { var q = find(id); return s + (q ? q.price : 0); }, 0); return Math.max(30, Math.round(v * 15) / 100); }, nextRecolte: nextThursday19, photos: PH, img: img, lookOf: lookOf, modelLine: modelLine, related: related, rail: rail, icon: icon, euro: euro, find: find,
    button: button, announcementBar: announcementBar, header: header, logo: logo,
    productCard: productCard, listingToolbar: listingToolbar, filterDrawer: filterDrawer,
    cartDrawer: cartDrawer, dropCountdown: dropCountdown, editoQuote: editoQuote, noteLine: noteLine, inventoryLabel: inventoryLabel,
    archiveSheet: archiveSheet, archiveChapters: archiveChapters, accordion: accordion, footer: footer, init: init
  };
})();
