#!/usr/bin/env python3
# v4: gôndola e calendário com parte do fio, sem rótulo no topo e com etiqueta de teoria.
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
def chip(txt):
    return f'<p class="teoria anima d5"><svg class="ico"><use href="#i-livro"/></svg><span><b>Teoria</b> {txt}</span></p>'
p = R / 'fonte/planograma.py'; s = p.read_text()
s = s.replace('data-titulo="Gôndola e sortimento" data-capitulo="03 · Como"', 'data-parte="4" data-titulo="Gôndola e sortimento" data-capitulo="4 · Como"')
s = re.sub(r'<span class="eyebrow"><b>\(03\)</b> Gôndola</span>', '', s)
if 'class="teoria' not in s:
    s = s.replace('      </ol>\n', '      </ol>\n      ' + chip('ECR, 1995, gerenciamento por categoria: o varejo dá um papel a cada linha. Conservas são rotina, pratos prontos são conveniência.') + '\n', 1)
p.write_text(s)
p = R / 'fonte/calendario.py'; s = p.read_text()
s = s.replace('data-titulo="Calendário 2027" data-capitulo="03 · Como"', 'data-parte="4" data-titulo="Calendário 2027" data-capitulo="4 · Como"')
s = re.sub(r'<span class="eyebrow"><b>\(03\)</b> Calendário</span>', '', s)
if 'class="teoria' not in s:
    s = s.replace("      <div class=\"anima d2\">{pns}</div>\n", "      <div class=\"anima d2\">{pns}</div>\n      " + chip('Romaniuk, 2023: cada data forte é um momento de compra. A Bordon aparece onde o shopper já está decidindo o que comer.') + "\n", 1)
p.write_text(s)
print('ok')
