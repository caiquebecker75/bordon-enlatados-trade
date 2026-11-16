#!/usr/bin/env python3
# Gera as 4 capas de capítulo (src/t06, t08, t12, t21). Rodar da raiz: python3 fonte/capitulos.py
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
CAPS = [
    ('t06-cap1.html', '01', 'Para onde vamos', 'A ambição e o que precisa mudar na loja até o fim de 2027.',
     'Começamos pelo destino. Antes de falar de peça, promoção ou calendário, precisamos combinar o que a Bordon tem de conquistar no ponto de venda em 2027 e como vamos saber, loja a loja, que conquistou. Tudo o que vem depois responde a esse destino.'),
    ('t08-cap2.html', '02', 'Por que', 'Mercado, shopper e as barreiras da lata, com dado e com teoria.',
     'Agora o porquê. Nenhuma escolha desta estratégia é opinião: cada uma tem três bases. O que o mercado mostra em números públicos, o que o shopper faz na loja e o que a teoria de marketing e de trade explica. As fontes estão no pé de cada tela.'),
    ('t12-cap3.html', '03', 'Como', 'A plataforma Ponto Pronto, canais, gôndola, peças, ativação e calendário.',
     'Este é o capítulo do como. Primeiro, uma plataforma que organiza todas as ações com uma ideia só. Depois, o manual de execução: o que muda por canal, como fica a gôndola, quais peças entram, como ativamos e o que acontece em cada mês de 2027.'),
    ('t21-cap4.html', '04', 'O que teremos', 'Medição, cronograma, resultados esperados e próximo passo.',
     'Por fim, o que a Bordon terá nas mãos. Execução medida loja a loja, com prova de instalação, um cronograma em ondas até todas as lojas do canal e os ganhos que vamos acompanhar, separando sempre o que é meta do que é resultado real.'),
]
NOMES = [c[2] for c in CAPS]
for arq, n, nome, frase, fala in CAPS:
    trilha = ''.join(f'<li class="{"on" if x == nome else ""}"><b>0{i + 1}</b>{x}</li>' for i, x in enumerate(NOMES))
    html = f'''
  <!-- capítulo {n} -->
  <section class="tela amarelo cap" data-titulo="Capítulo {n} · {nome}" data-capitulo="{n} · {nome}">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-preto.png" alt="Logo 75 LAB"></div><span class="eyebrow"><b>Capítulo</b> {n} de 04</span></div>
    <div class="cap-num anima">{n}</div>
    <div class="cap-txt">
      <h2 class="anima d1">{nome}</h2>
      <p class="lead anima d2">{frase}</p>
    </div>
    <ol class="trilha anima d3">{trilha}</ol>
    <aside class="roteiro" hidden>{fala}</aside>
  </section>
'''
    (R / 'src' / arq).write_text(html)
print('capas ok')
