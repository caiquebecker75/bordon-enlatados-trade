#!/usr/bin/env python3
# v4 (17/11/2026): deck de 15 telas em src/sNN-*.html, fio da história no topo e ícone de livro para as etiquetas de teoria.
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
b = R / 'fonte/build.py'; s = b.read_text(); b.write_text(s.replace("S.glob('t*.html')", "S.glob('s[0-9]*.html')"))
for f, old, new in [('fonte/planograma.py', 'src/t16-gondola.html', 'src/s10-gondola.html'), ('fonte/calendario.py', 'src/t20-calendario.html', 'src/s13-calendario.html')]:
    p = R / f; t = p.read_text()
    if old in t: p.write_text(t.replace(old, new))
sh = R / 'src/shell.html'; t = sh.read_text()
liv = '<symbol id="i-livro" viewBox="0 0 24 24"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5M4 19a2 2 0 0 1 2-2h13M8 7h7M8 10h5"/></symbol>'
if 'i-livro' not in t: t = t.replace('<symbol id="i-seta"', liv + '\n<symbol id="i-seta"', 1)
if 'id="fio"' not in t:
    t = t.replace('  <div id="topoBt">', '  <ol id="fio" aria-label="Fio da história"><li data-p="1">Objetivo</li><li data-p="2">Por quê</li><li data-p="3">A ideia</li><li data-p="4">Como</li><li data-p="5">Execução</li></ol>\n  <div id="topoBt">', 1)
sh.write_text(t)
d = R / 'src/deck.js'; j = d.read_text()
if 'marcaFio' not in j:
    a = '  function entra(t){'
    add = "  function marcaFio(t){const p=+(t.dataset.parte||0);$$('#fio li').forEach(li=>{const k=+li.dataset.p;li.classList.toggle('on',k===p);li.classList.toggle('feito',k<p);});$('#fio').classList.toggle('some',!p);}\n"
    assert a in j; j = j.replace(a, add + a, 1)
    b2 = "    history.replaceState(null,'','#'+(n+1));mostrarFala();\n  }"
    assert b2 in j; j = j.replace(b2, "    history.replaceState(null,'','#'+(n+1));mostrarFala();marcaFio(t);\n  }", 1)
d.write_text(j)
print('ok')
