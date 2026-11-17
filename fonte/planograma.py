#!/usr/bin/env python3
# Gera src/s10-gondola.html: planograma por tamanho de loja (P, M, G) com a foto real de cada item repetida por frente,
# em proporção (mesma escala nos três). Medidas de embalagem de referência, conferidas na visita às lojas.
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
E = 3.4            # px por cm
PRAT = 22          # cm entre prateleiras
MOD = 100          # cm por módulo
# nome, arquivo, largura cm, altura cm
P = {
  'feijoada':      ('Feijoada pronta 430 g', 'feijoada.jpg', 7.4, 11),
  'carne-panela':  ('Carne de panela 400 g', 'carne-panela.jpg', 7.4, 11),
  'costela':       ('Costela com mandioca 400 g', 'costela-mandioca.jpg', 7.4, 11),
  'bolonhesa':     ('Bolonhesa 200 g, sachê', 'bolonhesa.jpg', 13, 18),
  'desfiada':      ('Carne desfiada ao molho 200 g, sachê', 'carne-desfiada.jpg', 13, 18),
  'maionese':      ('Maionese de frango com legumes 200 g, sachê', 'maionese-frango.jpg', 13, 18),
  'salsicha':      ('Salsicha', 'salsicha.png', 8, 9.5),
  'salsicha-molho':('Salsicha ao molho', 'salsicha-molho.png', 8, 9.5),
  'aperitivo':     ('Salsicha aperitivo', 'salsicha-aperitivo.png', 8.5, 8),
  'almondegas':    ('Almôndegas ao molho', 'almondegas.png', 7.4, 10.5),
  'carne-bovina':  ('Carne bovina em conserva', 'carne-bovina-conserva.png', 9, 11),
  'carne-conserva':('Carne em conserva', 'carne-conserva.png', 9, 11),
  'fiambre':       ('Fiambre', 'fiambre.png', 10, 9.5),
  'cubos':         ('Carne em cubos', 'carne-cubos.png', 7.4, 10.5),
  'feijoada-cl':   ('Feijoada 310 g', 'feijoada-classica.png', 7.4, 10),
  'carioca':       ('Feijão carioca', 'feijao-carioca.png', 7.4, 10.5),
  'preto':         ('Feijão preto', 'feijao-preto.png', 7.4, 10.5),
}
COR = {'feijoada':'#5E2650','carne-panela':'#E06A00','costela':'#C98A00','bolonhesa':'#B23A1F','desfiada':'#8A3A1E','maionese':'#D9A400','salsicha':'#B04D5B','salsicha-molho':'#50284F','aperitivo':'#359D9B','almondegas':'#81332E','carne-bovina':'#26213F','carne-conserva':'#0050B6','fiambre':'#009ADF','cubos':'#FC4A14','feijoada-cl':'#5E2650','carioca':'#DE271F','preto':'#6B3529'}
PRATS = ['Jantar pronto', 'Lanche e petisco', 'Carne e frios', 'Despensa']
ESC = {'P': 4.5, 'M': 4.5, 'G': 3.4}
LOJAS = {
  'P': (1, 'Vizinhança · 1 módulo', [
      [('feijoada', 4), ('carne-panela', 3), ('costela', 3)],
      [('salsicha', 4), ('salsicha-molho', 3), ('almondegas', 3)],
      [('carne-bovina', 4), ('fiambre', 3)],
      [('feijoada-cl', 4), ('carioca', 3), ('preto', 3)],
  ]),
  'M': (2, 'Supermercado · 2 módulos', [
      [('feijoada', 6), ('carne-panela', 4), ('costela', 4), ('bolonhesa', 2), ('desfiada', 2)],
      [('salsicha', 6), ('salsicha-molho', 5), ('aperitivo', 4), ('almondegas', 5)],
      [('carne-bovina', 6), ('carne-conserva', 4), ('fiambre', 4), ('cubos', 4)],
      [('feijoada-cl', 6), ('carioca', 7), ('preto', 7)],
  ]),
  'G': (3, 'Hiper e atacarejo · 3 módulos', [
      [('feijoada', 8), ('carne-panela', 6), ('costela', 6), ('bolonhesa', 4), ('desfiada', 4), ('maionese', 2)],
      [('salsicha', 10), ('salsicha-molho', 8), ('aperitivo', 6), ('almondegas', 8)],
      [('carne-bovina', 8), ('carne-conserva', 6), ('fiambre', 7), ('cubos', 6)],
      [('feijoada-cl', 10), ('carioca', 12), ('preto', 12)],
  ]),
}

def gondola(mods, prats, E):
    W = mods * MOD * E
    out = [f'<div class="gd" style="width:{W:.0f}px">']
    out.append(f'<div class="gd-test" style="width:{W:.0f}px"><img src="assets/img/logo-bordon.png" alt="Logo Bordon"><span>Ponto Pronto</span></div>')
    for i, linha in enumerate(prats):
        larg = sum(P[k][2] * n for k, n in linha)
        assert larg <= mods * MOD, (mods, i, larg)
        itens = []
        for k, n in linha:
            nome, arq, w, h = P[k]
            for _ in range(n):
                itens.append(f'<img src="assets/latas/{arq}" alt="{nome}" title="{nome}" style="width:{w*E:.1f}px;height:{h*E:.1f}px">')
        out.append(f'<div class="gd-prat" style="height:{PRAT*E:.0f}px"><span class="gd-rot">{PRATS[i]}</span><div class="gd-itens">{"".join(itens)}</div></div>')
        faixa = ''.join('<i style="width:%.1fpx;background:%s"></i>' % (P[k][2] * n * E, COR[k]) for k, n in linha)
        out.append(f'<div class="gd-faixa">{faixa}</div>')
    for m in range(1, mods):
        out.append(f'<i class="gd-div" style="left:{m*MOD*E:.0f}px"></i>')
    out.append('</div>')
    return ''.join(out)

bts = ''.join(f'<button class="aba">Loja {k} · {v[1].split(" · ")[0]}</button>' for k, v in LOJAS.items())
pns = ''
for k, (mods, rot, prats) in LOJAS.items():
    n = sum(len(set(x for x, _ in l)) for l in prats)
    fr = sum(q for l in prats for _, q in l)
    pns += f'<div class="painel"><div class="gd-cab"><b>Loja {k}</b><span>{rot} · {n} itens · {fr} frentes</span></div>{gondola(mods, prats, ESC[k])}</div>'

html = f'''
  <!-- 16 · gôndola -->
  <section class="tela claro gondola" data-parte="4" data-titulo="Gôndola e sortimento" data-capitulo="4 · Como">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-preto.png" alt="Logo 75 LAB"></div></div>
    <div class="miolo gd-g">
      <div class="gd-esq" data-abas>
        <div class="gd-topo"><h2 class="anima">A parede amarela, <em>organizada por ocasião.</em></h2><span class="clique anima d1"><svg><use href="#i-mao"/></svg>Clique no tamanho da loja</span></div>
        <div class="abas-bts anima d1">{bts}</div>
        <div class="anima d2">{pns}</div>
      </div>
      <div class="gd-dir">
      <ol class="gd-regras anima d3">
        <li><b>Olhos para o jantar</b>Pratos prontos na altura dos olhos.</li>
        <li><b>Mãos nos mais vendidos</b>Salsichas e almôndegas ao alcance da mão.</li>
        <li><b>Bloco vertical</b>A marca toda junta, do topo à base.</li>
        <li><b>Faixa com a cor do produto</b>O shopper acha pela cor antes de ler.</li>
        <li><b>Nunca falta</b>Feijoada e salsicha com 4 frentes ou mais.</li>
        <li><b>Preço por pessoa</b>O valor da refeição dividido por quem come.</li>
      </ol>
      <p class="teoria anima d5"><svg class="ico"><use href="#i-livro"/></svg><span><b>Teoria</b> ECR, 1995, gerenciamento por categoria: o varejo dá um papel a cada linha. Conservas são rotina, pratos prontos são conveniência.</span></p>
      </div>
    </div>
    <p class="fonte">Base: gerenciamento por categoria (ECR e The Partnering Group, 1995) e ativos distintivos de marca (Romaniuk, Building Distinctive Brand Assets, OUP, 2018). Gôndola em módulos de 1 m e prateleiras a cada 22 cm, desenhada em escala dentro de cada tamanho de loja; medidas de embalagem de referência, conferidas na visita às lojas.</p>
    <aside class="roteiro" hidden>Este é o planograma, igual ao que vai para a loja: cada lata é a foto real, repetida por frente, em proporção. São três tamanhos. Na loja P, de vizinhança, um módulo com os itens de giro. Na M, dois módulos e a linha quase toda. Na G, hiper e atacarejo, três módulos com a linha completa. A lógica é a mesma: a marca em bloco amarelo, organizada por ocasião. Pratos prontos na altura dos olhos, giro na altura das mãos, carnes e frios embaixo e a despensa na base. A faixa usa a cor de cada produto do manual, para o shopper achar pela cor, e o porta-preço mostra o preço por pessoa.</aside>
  </section>
'''
(R / 'src/s10-gondola.html').write_text(html)
print('gôndola ok')
