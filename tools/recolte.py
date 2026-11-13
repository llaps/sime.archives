#!/usr/bin/env python3
"""Remplace « drop » par « récolte » dans les textes visibles, avec les accords (féminin)."""
import re, sys, glob, os

S = os.path.dirname(os.path.abspath(__file__))
files = [os.path.join(S, f) for f in ['proto_nav.js', 'build_proto.py', 'gen_lc.py', 'lc_parts.py']]
files += glob.glob(os.path.join(S, 'ds/project/components/*/preview.html'))
files += glob.glob(os.path.join(S, 'ds/project/components/*/README.md'))
files += [os.path.join(S, 'ds/project/components/bundle.js')]
files += [os.path.join(S, 'ds/project', f) for f in ['README.md', 'workflow.md', 'benchmark.md']]

# Phrases d'abord (déterminants et accords), puis le mot seul.
PHRASES = [
    (r"\bLE DROP\b", "LA RÉCOLTE"), (r"\bDE CE DROP\b", "DE CETTE RÉCOLTE"), (r"\bDU DROP\b", "DE LA RÉCOLTE"),
    (r"\bLe drop\b", "La récolte"), (r"\ble drop\b", "la récolte"),
    (r"\bdu drop\b", "de la récolte"), (r"\bDu drop\b", "De la récolte"),
    (r"\bau drop\b", "à la récolte"), (r"\baux drops\b", "aux récoltes"),
    (r"\bUn drop\b", "Une récolte"), (r"\bun drop\b", "une récolte"),
    (r"\bce drop\b", "cette récolte"), (r"\bCe drop\b", "Cette récolte"),
    (r"\bprochain drop\b", "prochaine récolte"), (r"\bProchain drop\b", "Prochaine récolte"),
    (r"\bdrops précédents\b", "récoltes précédentes"), (r"\bDrops précédents\b", "Récoltes précédentes"),
    (r"\bDrop ouvert\b", "Récolte ouverte"), (r"\bdrop ouvert\b", "récolte ouverte"), (r"\bDROP OUVERT\b", "RÉCOLTE OUVERTE"),
    (r"\ble Drop (\d+)", r"la Récolte \1"), (r"\bLe Drop (\d+)", r"La Récolte \1"), (r"\bdu Drop (\d+)", r"de la Récolte \1"),
    (r"\bau Drop (\d+)", r"à la Récolte \1"), (r"\bun Drop (\d+)", r"une Récolte \1"),
    (r"\bLE DROP (\d+)", r"LA RÉCOLTE \1"), (r"\bDU DROP (\d+)", r"DE LA RÉCOLTE \1"),
]
WORDS = [("drops", "récoltes"), ("Drops", "Récoltes"), ("DROPS", "RÉCOLTES"), ("drop", "récolte"), ("Drop", "Récolte"), ("DROP", "RÉCOLTE")]

def is_ident(s, a, b):
    before = s[a - 1] if a > 0 else " "
    after = s[b] if b < len(s) else " "
    nxt = s[b + 1] if b + 1 < len(s) else " "
    if re.match(r"[\w\-./#$]", before) or re.match(r"[\w\-_(/:=]", after):
        return True
    if after == "." and re.match(r"[A-Za-z]", nxt):
        return True
    w = s[a:b]
    if w == "drop" and before in "'\"" and after in "'\"":   # data-sa='drop'
        return True
    if s[max(0, a - 4):a] == "var " or s[max(0, a - 2):a] == "! ":
        return True
    return False

def sub_safe(s, pat, rep):
    out, last = [], 0
    for m in re.finditer(pat, s):
        # vérifier le mot « drop » lui-même dans la correspondance
        dm = re.search(r"(?i)drops?", m.group(0))
        da, db = m.start() + dm.start(), m.start() + dm.end()
        if is_ident(s, m.start() if m.start() == da else da, db) and m.start() == da:
            continue
        if is_ident(s, da, db) and m.start() == da:
            continue
        out.append(s[last:m.start()]); out.append(m.expand(rep)); last = m.end()
    out.append(s[last:])
    return "".join(out)

total = 0
for f in files:
    s = open(f).read(); o = s
    for p, r in PHRASES:
        s = sub_safe(s, p, r)
    for w, r in WORDS:
        s = sub_safe(s, r"\b" + w + r"\b", r)
    if s != o:
        n = sum(1 for _ in re.finditer(r"(?i)récolte", s)) - sum(1 for _ in re.finditer(r"(?i)récolte", o))
        total += n
        open(f, 'w').write(s)
        print(os.path.relpath(f, S), n)
print("total", total)
