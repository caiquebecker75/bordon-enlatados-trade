#!/usr/bin/env python3
# A etiqueta de teoria da gôndola fica na coluna das regras (antes caía numa linha nova da grade, fora da tela).
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
p = R / 'fonte/planograma.py'; s = p.read_text()
if 'class="gd-dir"' not in s:
    s = s.replace('      <ol class="gd-regras anima d3">', '      <div class="gd-dir">\n      <ol class="gd-regras anima d3">', 1)
    s = re.sub(r'(<p class="teoria anima d5">.*?</p>\n)', r'\1      </div>\n', s, count=1, flags=re.S)
p.write_text(s)
print('ok', 'gd-dir' in s)
