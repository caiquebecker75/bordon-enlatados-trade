#!/usr/bin/env python3
# Monta as telas 7 a 13 da v4 a partir da v3 (fonte/v3): parte do fio, sem rótulo no topo, sem "Em outras palavras", com etiqueta de teoria.
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
V = R / 'fonte/v3'
def chip(txt, extra=''):
    return f'<p class="teoria{extra} anima d5"><svg class="ico"><use href="#i-livro"/></svg><span><b>Teoria</b> {txt}</span></p>'
def limpa(s, parte, cap):
    s = re.sub(r'data-capitulo="[^"]*"', f'data-parte="{parte}" data-capitulo="{cap}"', s, count=1)
    s = re.sub(r'<span class="eyebrow"><b>\([0-9]+\)</b>[^<]*</span>', '', s)
    s = re.sub(r'\s*<p class="explica anima d5">.*?</p>', '', s, flags=re.S)
    return s

# 07 · a ideia
s = limpa((V / 't13-plataforma.html').read_text(), 3, '3 · A ideia')
s = s.replace('<p class="pl-desdobra anima d3">Os dois selos da lata assinam todas as peças.</p>',
              chip('Romaniuk, 2018, ativos distintivos: o amarelo, a coroa e os dois selos da lata, repetidos em toda peça, fazem o shopper reconhecer a Bordon sem ler.'))
(R / 'src/s07-ideia.html').write_text(s)

# 08 · o mapa
s = limpa((V / 't12a-mapa.html').read_text(), 3, '3 · A ideia')
s = s.replace('A estratégia inteira <em>em um mapa.</em>', 'Do objetivo ao indicador, <em>em um mapa.</em>')
(R / 'src/s08-mapa.html').write_text(s)

# 09 · canais
s = limpa((V / 't15-canais.html').read_text(), 4, '4 · Como')
s = s.replace('\n    </div>\n    <p class="fonte">', '\n      ' + chip('Kantar, 2024, missões de compra: abastecer, repor, resolver uma urgência ou comprar perto de casa. Cada missão pede uma loja diferente.') + '\n    </div>\n    <p class="fonte">', 1)
(R / 'src/s09-canais.html').write_text(s)

# 11 · peças
s = limpa((V / 't18-pecas.html').read_text(), 4, '4 · Como')
s = s.replace('\n    </div>\n    <p class="fonte">', '\n      ' + chip('POPAI, 2014: display na loja aumentou a venda em 19% no canal alimentar. Pesadas atraem, médias explicam, leves convertem.') + '\n    </div>\n    <p class="fonte">', 1)
(R / 'src/s11-pecas.html').write_text(s)

# 12 · ativação: uma etiqueta de teoria por aba
s = limpa((V / 't19-ativacao.html').read_text(), 4, '4 · Como')
abas = [
 ('<dd>Traz gente nova e o efeito dura semanas.</dd></dl>', 'Chandukala, Dotson e Liu, 2017: a degustação traz compradores novos para a categoria e o efeito dura semanas.'),
 ('<p>No máximo 1 oferta a cada 4 itens.</p></div>\n        </div>', 'Tversky e Kahneman, 1974: o primeiro preço vira a régua. Anderson e Simester, 2001, com atum enlatado: oferta em mais de um quarto dos itens dilui o efeito.'),
]
for a, t in abas:
    assert a in s, a
    s = s.replace(a, a + chip(t, ' na-aba'), 1)
# aba "ao lado de" e "encarte": etiqueta depois do bloco
s = s.replace('<p><b>Pães e torradas</b>lanche pronto na padaria</p></div>\n        </div>', '<p><b>Pães e torradas</b>lanche pronto na padaria</p></div>\n        </div>' + chip('Bezawada et al., 2009: produtos que se completam, frente a frente no mesmo corredor, venderam 9% mais.', ' na-aba'), 1)
s = s.replace('<p>Anúncio no celular de quem está perto da degustação.</p></div>\n        </div>', '<p>Anúncio no celular de quem está perto da degustação.</p></div>\n        </div>' + chip('Sharp, 2010, disponibilidade mental: a marca precisa vir à cabeça antes da loja. 45,4% dos lares já compram online.', ' na-aba'), 1)
(R / 'src/s12-ativacao.html').write_text(s)
print('ok', s.count('class="teoria'))
