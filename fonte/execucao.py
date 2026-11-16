#!/usr/bin/env python3
# Gera src/t23-cronograma.html (Gantt de execução) e src/t23b-papeis.html (papéis e responsabilidades, RACI).
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
MES = ['dez', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# frente, quem faz, coluna inicial (quinzena 1 a 26), duração em quinzenas, estilo
G = [
 ('Aprovação e visita às lojas', '75 LAB e Bordon', 1, 1, 'a'),
 ('KV, desdobramento e executivo', '75 LAB', 2, 2, 'a'),
 ('Produção das peças com QR', '75 LAB', 4, 3, 'b'),
 ('Manual e treino de promotores', '75 LAB e promotoria', 6, 2, 'b'),
 ('Onda 1 instalada: atacarejo e hiper', '75 LAB e trade', 7, 1, 'c'),
 ('Onda 2: super e bairro', '75 LAB e distribuidor', 9, 3, 'c'),
 ('Degustação nos fins de semana', 'Promotoria', 8, 19, 'd'),
 ('Encarte, busca e app nas datas', 'Trade e marketing', 7, 20, 'd'),
 ('Cestas de fim de ano', 'Comercial', 19, 8, 'b'),
 ('Leitura mensal e ajuste trimestral', '75 LAB', 8, 19, 'e'),
]
MARCOS = [(1, 'Sim da Bordon'), (7, 'Onda 1'), (11, 'Onda 2'), (14, 'São João'), (19, 'Leitura do semestre'), (24, 'Black Friday')]
cab = ''.join(f'<span style="grid-column:{i * 2 + 1}/span 2">{m}<small>{"26" if i == 0 else ("27" if i in (1, 12) else "")}</small></span>' for i, m in enumerate(MES))
linhas = ''
for k, (nome, quem, c, n, e) in enumerate(G):
    linhas += f'<div class="gt-l"><div class="gt-r"><b>{nome}</b><span>{quem}</span></div><div class="gt-t"><i class="gt-b {e}" style="grid-column:{c}/span {n};--k:{k}"></i></div></div>'
marcos = ''.join(f'<span class="gt-m" style="grid-column:{c}"><i></i><b>{t}</b></span>' for c, t in MARCOS)
crono = f'''
  <!-- 23 · cronograma de execução -->
  <section class="tela escuro crono" data-titulo="Cronograma de execução" data-capitulo="04 · O que teremos">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-lime.png" alt="Logo 75 LAB"></div><span class="eyebrow"><b>(04)</b> Cronograma de execução</span></div>
    <div class="miolo">
      <div class="cr-topo"><h2 class="anima">Do sim à loja <em>em 14 semanas.</em></h2><p class="lead anima d1">Onda 1 em março, onda 2 antes do São João, leitura todo mês.</p></div>
      <div class="gt anima d2">
        <div class="gt-l gt-cab"><div class="gt-r"></div><div class="gt-t">{cab}</div></div>
        {linhas}
        <div class="gt-l gt-marcos"><div class="gt-r"><b>Marcos</b></div><div class="gt-t">{marcos}</div></div>
        <i class="gt-hoje" style="--c:7"></i>
      </div>
    </div>
    <p class="fonte">Considerando aprovação no início de dezembro de 2026. Produção de referência da 75 LAB: peças pesadas em até 30 dias úteis, leves em 10. Cada coluna é uma quinzena.</p>
    <aside class="roteiro" hidden>O cronograma de execução, do sim à loja. Com aprovação no início de dezembro, visitamos as lojas nas duas primeiras semanas, fechamos o key visual, o desdobramento e o projeto executivo até meados de janeiro, produzimos as peças com QR até o fim de fevereiro e treinamos os promotores. A onda 1 está instalada no atacarejo e no hiper na primeira quinzena de março. A onda 2, em supermercados e lojas de bairro, chega em maio, antes do São João. A degustação, o encarte e a busca rodam o ano todo seguindo o calendário, e lemos os resultados todo mês, com ajuste a cada trimestre.</aside>
  </section>
'''
(R / 'src/t23-cronograma.html').write_text(crono)

PAP = ['Marketing Bordon', 'Trade e comercial Bordon', 'Distribuidor', 'Varejista', 'Promotoria', '75 LAB']
RESUMO = [
 'Aprova estratégia, KV, peças e mídia; dono da leitura mensal.',
 'Negocia espaço, ponto extra e encarte; responde pela loja perfeita.',
 'Abastece os 6 itens que não podem faltar e leva o kit às lojas de bairro.',
 'Libera o espaço, o ponto extra e as datas de encarte e de degustação.',
 'Repõe, mantém o bloco amarelo, faz a degustação e lê o QR.',
 'Cria, faz o executivo, produz, instala, treina e mede de ponta a ponta.',
]
A = [
 ('Estratégia, calendário e KV',      ['A', 'C', 'I', 'I', 'I', 'R']),
 ('Peças: executivo e produção',       ['A', 'C', 'I', 'I', 'I', 'R']),
 ('Espaço, ponto extra e encarte',     ['C', 'R·A', 'C', 'C', 'I', 'C']),
 ('Instalação das peças',              ['I', 'A', 'I', 'C', 'C', 'R']),
 ('Pedido e abastecimento',            ['I', 'A', 'R', 'C', 'C', 'I']),
 ('Reposição e loja perfeita',         ['I', 'A', 'I', 'C', 'R', 'C']),
 ('Degustação',                        ['A', 'C', 'I', 'C', 'R', 'C']),
 ('Busca, encarte e app',              ['A', 'R', 'I', 'C', 'I', 'C']),
 ('Leitura mensal e ajuste',           ['A', 'C', 'I', 'I', 'I', 'R']),
]
bts = ''.join(f'<button class="aba rc-p" style="grid-column:{i + 2}">{p}</button>' for i, p in enumerate(PAP))
lin = ''
for nome, cs in A:
    lin += f'<div class="rc-a">{nome}</div>' + ''.join(f'<div class="rc-c c{i}"><span class="l-{c[0]}">{c}</span></div>' for i, c in enumerate(cs))
pns = ''.join(f'<div class="painel"><p class="rc-res"><b>{p}:</b> {r}</p></div>' for p, r in zip(PAP, RESUMO))
papeis = f'''
  <!-- 23b · papéis e responsabilidades -->
  <section class="tela claro papeis" data-titulo="Papéis e responsabilidades" data-capitulo="04 · O que teremos">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-preto.png" alt="Logo 75 LAB"></div><span class="eyebrow"><b>(04)</b> Papéis e responsabilidades</span></div>
    <div class="miolo" data-abas>
      <div class="rc-topo"><h2 class="anima">Quem faz <em>o quê.</em></h2>
        <div class="rc-leg anima d1"><span><span class="l-R">R</span>faz</span><span><span class="l-A">A</span>aprova</span><span><span class="l-C">C</span>é consultado</span><span><span class="l-I">I</span>é informado</span><span class="clique"><svg><use href="#i-mao"/></svg>Clique em cada papel</span></div></div>
      <div class="rc-grade anima d2"><div class="rc-a rc-vazio"></div>{bts}{lin}</div>
      <div class="anima d3">{pns}</div>
    </div>
    <p class="fonte">Matriz RACI proposta pela 75 LAB, a validar com os times de marketing, trade e comercial da Bordon.</p>
    <aside class="roteiro" hidden>Quem faz o quê, numa matriz simples: R faz, A aprova, C é consultado e I é informado. O marketing da Bordon aprova estratégia, key visual, peças e mídia, e é dono da leitura mensal. O trade e o comercial negociam espaço, ponto extra e encarte e respondem pela loja perfeita. O distribuidor abastece os seis itens que não podem faltar e leva o kit às lojas de bairro. O varejista libera espaço e datas. A promotoria repõe, mantém o bloco amarelo e faz a degustação. E a 75 LAB cria, produz, instala, treina e mede de ponta a ponta. Cliquem em cada papel para ver a coluna.</aside>
  </section>
'''
(R / 'src/t23b-papeis.html').write_text(papeis)
print('cronograma e papéis ok')
