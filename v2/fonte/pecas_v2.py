#!/usr/bin/env python3
# v2: gera uma tela por peça (src/s10zNN-*.html), na ordem da tela de peças, e liga os cards da tela de peças a cada uma.
# Rodar da pasta v2: python3 fonte/pecas_v2.py && python3 fonte/build.py
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent; S = R / 'src'
GR = {'pesada': ('Pesadas', 'atraem e fazem provar'), 'media': ('Médias', 'explicam a ocasião'), 'leve': ('Leves', 'convertem na prateleira')}
P = [  # chave, grupo, nome, resolve, principal, vistas, especificações, texto
 ('ilha', 'pesada', 'Ilha capa pallet', 'Ser vista', 'ilha-giro.webp', ['ilha-v1', 'ilha-v2'],
  [('Medida', '120 x 100 cm · 1,70 m com o logo'), ('Material', 'Capa em polionda, degraus de polionda, painel em PS'), ('Capacidade', '98 latas em 3 degraus'), ('Canal', 'Hiper e atacarejo')],
  'Capa pallet e ilha numa peça só: a saia leva o KV nas quatro faces, os degraus mostram a linha e o painel com o logo chama de longe. O adesivo vermelho no chão marca o território Bordon.'),
 ('lata', 'pesada', 'Display lata gigante', 'Ser lembrada', 'lata-giro.webp', ['lata-v1', 'lata-v2'],
  [('Medida', 'Ø 70 cm · 1,89 m com o logo'), ('Material', 'Polionda com rótulo impresso, base em PS'), ('Capacidade', '64 latas nos nichos + 82 no topo'), ('Canal', 'Supermercado e hiper')],
  'A própria lata de feijoada, em tamanho gigante e sem tampa: o rótulo fica inteiro de frente, as aberturas laterais guardam as prateleiras e o topo vira vitrine com o logo no pirulito.'),
 ('balcao', 'pesada', 'Balcão de degustação', 'Ser provada', 'balcao-v0.webp', ['balcao-v1', 'balcao-v2'],
  [('Medida', '70 x 53 cm · tampo a 95 cm · 2,20 m'), ('Material', 'Frente em PS calandrado, tubos e testeira em faca'), ('Uso', 'Indução, panela, copinhos e latas no tampo'), ('Canal', 'Fim de semana nas lojas grandes')],
  '"Esquentou, provou." A frente curva leva o KV inteiro, a testeira em faca com o logo Bordon fica acima da cabeça do promotor e o tampo comporta a degustação completa.'),
 ('display', 'media', 'Display de balcão gravitacional', 'Ser escolhida', 'display-v0.webp', ['display-v1', 'display-v2', 'display-v3'],
  [('Medida', '26 x 46 x 39 cm'), ('Material', 'Aramado amarelo e PS frontal removível'), ('Capacidade', '20 latas em 2 frentes'), ('Canal', 'Checkout e vizinhança')],
  'As latas descem por gravidade: tirou uma, a próxima já está na frente. O abastecimento é por cima e a comunicação troca sem ferramenta, só levantando o PS.'),
 ('clip', 'media', 'Clip strip de cross', 'Ser lembrada', 'clip-giro.webp', ['clip-v1', 'clip-v2'],
  [('Medida', '27 x 120 cm'), ('Material', 'PS 2 mm com ilhós e bolsos de acrílico'), ('Capacidade', '4 sachês de bolonhesa'), ('Canal', 'Corredor de massas e molhos')],
  'Leva a bolonhesa para perto do macarrão. Os sachês ficam em bolsos de acrílico colados na peça, sem amassar a embalagem, e o clip strip pendura no ilhós.'),
 ('modulo', 'media', 'Testeira e faixas por ocasião', 'Ser vista', 'modulo-v0.webp', ['modulo-v1', 'modulo-v2', 'modulo-v3'],
  [('Medida', 'Testeira 124 x 47 cm · faixas 40 x 4 cm'), ('Material', 'Testeira em PS com faca, faixas em PS 1 mm'), ('Planograma', '5 ocasiões, uma por prateleira'), ('Canal', 'Gôndola de mercearia')],
  'A gôndola vira o cardápio da semana: cada prateleira é uma ocasião, com a sua cor. A testeira assina o bloco e o adesivo no chão puxa o shopper do corredor.'),
 ('stopper', 'leve', 'Stopper', 'Ser escolhida', 'stopper-v0.webp', ['stopper-v1', 'stopper-v2'],
  [('Medida', '18 x 30 cm'), ('Material', 'PS 2 mm, frente e verso'), ('Mensagem', '3 min na panela, 1 min no micro-ondas'), ('Canal', 'Todos')],
  'Sai da gôndola para o corredor e para o carrinho no meio do caminho. Frente e verso impressos: lê dos dois lados.'),
 ('wobbler', 'leve', 'Wobbler com selo', 'Ser escolhida', 'wobbler-v0.webp', ['wobbler-v1', 'wobbler-v2'],
  [('Medida', 'Ø 16 cm'), ('Material', 'PS 1 mm com clipe PET'), ('Mensagem', 'É só esquentar e pronto'), ('Canal', 'Todos')],
  'O selo do benefício balançando na frente da prateleira, sem cobrir a faixa da ocasião.'),
 ('precificador', 'leve', 'Precificador', 'Ser escolhida', 'precificador-v0.webp', ['precificador-v1', 'precificador-v2', 'precificador-v3'],
  [('Medida', '33 x 16 cm'), ('Material', 'PS 1 mm com aba de encaixe'), ('Uso', 'Moldura da etiqueta de preço'), ('Canal', 'Todos')],
  'A aba cortada encaixa na canaleta e a janela emoldura a etiqueta de preço da loja: o preço ganha a marca, sem trocar a etiqueta.'),
 ('faixas', 'leve', 'Faixas por ocasião', 'Ser lembrada', 'faixas-leque.webp', ['faixas-v1', 'faixas-v2'],
  [('Medida', '40 x 4 cm, 3 por prateleira'), ('Material', 'PS 1 mm na canaleta de preço'), ('Ocasiões', 'Dia a dia, jantar a dois, petiscar, família, domingo'), ('Canal', 'Todos')],
  'Cinco cores, cinco momentos de consumo. A faixa diz para quando é a lata antes de o shopper ler o rótulo.'),
]
N0 = 12          # índice da primeira tela de peça (0 = capa)
NV = N0 + len(P) # índice da tela com todas as peças
for f in S.glob('s10z*.html'): f.unlink()
for i, (k, g, nome, res, main, vistas, spec, txt) in enumerate(P):
    gn, gd = GR[g]
    vs = [main] + [v + '.webp' for v in vistas]
    thumbs = ''.join('<button class="p1-th%s" data-src="assets/pecas/%s"><img src="assets/pecas/%s" alt="" loading="lazy"></button>' % (' on' if j == 0 else '', v, v) for j, v in enumerate(vs))
    dl = ''.join('<dt>%s</dt><dd>%s</dd>' % (a, b) for a, b in spec)
    html = f'''
  <!-- peça {i + 1:02d} · {nome} -->
  <section class="tela escuro peca1" data-tela="p-{k}" data-titulo="{i + 1:02d} · {nome}" data-parte="4" data-capitulo="4 · Como">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-lime.png" alt="Logo 75 LAB"></div></div>
    <div class="miolo">
      <div class="p1-midia anima"><img class="p1-main" src="assets/pecas/{main}" alt="{nome} Bordon em 3D"></div>
      <div class="p1-thumbs anima d2">{thumbs}</div>
      <div class="p1-info">
        <div class="pc-gr p1-gr anima">{gn} <span>{gd}</span></div>
        <span class="p1-n anima d1">{i + 1:02d} / {len(P):02d}</span>
        <h2 class="anima d1">{nome}</h2>
        <span class="resolve p1-res anima d2">Resolve: {res.lower()}</span>
        <p class="p1-txt anima d2">{txt}</p>
        <dl class="p1-dl anima d3">{dl}</dl>
        <button class="botao seta p1-todas anima d4" data-ir="{NV}">Ver todas as peças</button>
      </div>
    </div>
    <aside class="roteiro" hidden>{nome}. {txt}</aside>
  </section>
'''
    (S / ('s10z%02d-%s.html' % (i + 1, k))).write_text(html)
# tela de peças: cada card volta para a tela da peça
s = (S / 's11-pecas.html').read_text()
for i, (k, *_ ) in enumerate(P):
    s = re.sub(r'<article class="peca anima (d\d)"( data-ir="\d+")? data-peca="([^"]+)" data-conjunto="(\w+)">\n          <div class="arte a-3d" data-amplia="assets/pecas/%s\.png">' % k,
               lambda m: '<article class="peca anima %s" data-ir="%d" data-peca="%s" data-conjunto="%s">\n          <div class="arte a-3d" data-amplia="assets/pecas/%s.png">' % (m.group(1), N0 + i, m.group(3), m.group(4), k), s)
s = s.replace(' data-amplia="assets/pecas/', ' data-x="assets/pecas/')
s = s.replace('Clique em cada peça para ampliar o 3D', 'Clique em cada peça para ver o detalhe')
(S / 's11-pecas.html').write_text(s)
print('telas de peça', len(P), '· primeira', N0, '· visão geral', NV, '· cards ligados', s.count('data-ir='))
