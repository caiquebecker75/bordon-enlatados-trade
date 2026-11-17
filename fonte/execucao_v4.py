#!/usr/bin/env python3
# Gera src/s14-execucao.html: execução em três abas (cronograma em Gantt, quem faz em RACI, como medimos).
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
MES = ['dez', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
G = [
 ('Visita às lojas e KV final', '75 LAB', 1, 2, 'a'),
 ('Projeto executivo e produção com QR', '75 LAB', 3, 4, 'b'),
 ('Onda 1: atacarejo e hiper', '75 LAB e trade', 7, 1, 'c'),
 ('Onda 2: super e bairro', '75 LAB e distribuidor', 9, 3, 'c'),
 ('Degustação nos fins de semana', 'Promotoria', 8, 19, 'd'),
 ('Encarte, busca e app', 'Trade e marketing', 7, 20, 'd'),
 ('Leitura mensal e ajuste', '75 LAB', 8, 19, 'e'),
]
MARCOS = [(1, 'Sim da Bordon'), (7, 'Onda 1'), (11, 'Onda 2'), (14, 'São João'), (24, 'Black Friday')]
cab = ''.join(f'<span style="grid-column:{i * 2 + 1}/span 2">{m}<small>{"26" if i == 0 else ("27" if i in (1, 12) else "")}</small></span>' for i, m in enumerate(MES))
linhas = ''.join(f'<div class="gt-l"><div class="gt-r"><b>{n}</b><span>{q}</span></div><div class="gt-t"><i class="gt-b {e}" style="grid-column:{c}/span {k};--k:{i}"></i></div></div>' for i, (n, q, c, k, e) in enumerate(G))
marcos = ''.join(f'<span class="gt-m" style="grid-column:{c}"><i></i><b>{t}</b></span>' for c, t in MARCOS)
PAP = ['Marketing Bordon', 'Trade Bordon', 'Distribuidor', 'Varejista', 'Promotoria', '75 LAB']
A = [
 ('Estratégia, KV e peças', ['A', 'C', 'I', 'I', 'I', 'R']),
 ('Espaço, ponto extra e encarte', ['C', 'R·A', 'C', 'C', 'I', 'C']),
 ('Instalação das peças', ['I', 'A', 'I', 'C', 'C', 'R']),
 ('Pedido e abastecimento', ['I', 'A', 'R', 'C', 'C', 'I']),
 ('Reposição e degustação', ['A', 'A', 'I', 'C', 'R', 'C']),
 ('Leitura mensal e ajuste', ['A', 'C', 'I', 'I', 'I', 'R']),
]
rc = '<div class="rc-a rc-vazio"></div>' + ''.join(f'<div class="rc-p2">{p}</div>' for p in PAP)
for nome, cs in A:
    rc += f'<div class="rc-a">{nome}</div>' + ''.join(f'<div class="rc-c"><span class="l-{c[0]}">{c}</span></div>' for c in cs)
html = f'''
  <!-- 14 · execução: cronograma, quem faz, como medimos -->
  <section class="tela escuro exec4" data-parte="5" data-titulo="Execução" data-capitulo="5 · Execução">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-lime.png" alt="Logo 75 LAB"></div></div>
    <div class="miolo" data-abas>
      <div class="ex4-topo"><h2 class="anima">Do sim à loja em 14 semanas, <em>com prova loja a loja.</em></h2><span class="clique anima d1"><svg><use href="#i-mao"/></svg>Clique em cada aba</span></div>
      <div class="abas-bts anima d1"><button class="aba">Cronograma</button><button class="aba">Quem faz</button><button class="aba">Como medimos</button></div>
      <div class="painel">
        <div class="gt gt4">
          <div class="gt-l gt-cab"><div class="gt-r"></div><div class="gt-t">{cab}</div></div>
          {linhas}
          <div class="gt-l gt-marcos"><div class="gt-r"><b>Marcos</b></div><div class="gt-t">{marcos}</div></div>
        </div>
      </div>
      <div class="painel">
        <div class="rc4-leg"><span><span class="l-R">R</span>faz</span><span><span class="l-A">A</span>aprova</span><span><span class="l-C">C</span>é consultado</span><span><span class="l-I">I</span>é informado</span></div>
        <div class="rc-grade rc4">{rc}</div>
      </div>
      <div class="painel">
        <div class="med4">
          <div class="med4-fluxo"><span><svg class="ico"><use href="#i-caixa"/></svg>Peça com QR</span><i></i><span><svg class="ico"><use href="#i-celular"/></svg>Foto e GPS</span><i></i><span><svg class="ico"><use href="#i-grafico"/></svg>Painel</span><i></i><span class="forte"><svg class="ico"><use href="#i-alvo"/></svg>Decisão</span></div>
          <div class="med4-g">
            <div class="med4-c"><span class="mono">One Shot</span><b>Instalação comprovada</b><p>Quem instala escaneia o QR e fotografa: o painel grava loja, data, hora e GPS.</p></div>
            <div class="med4-c forte"><span class="mono">On Timing</span><b>Ao vivo, toda semana</b><p>Uma tag nas peças grandes avisa se a peça saiu do lugar.</p></div>
            <div class="med4-c"><span class="mono">Loja perfeita</span><b>Nota de 0 a 100</b><p>Mix, falta, bloco amarelo, ponto extra e preço. Meta: 80 em toda loja.</p></div>
          </div>
        </div>
      </div>
      <p class="teoria anima d5"><svg class="ico"><use href="#i-livro"/></svg><span><b>Teoria</b> Gruen, Corsten e Bharadwaj, 2002: quando falta o produto, 31% compram em outra loja. Medir a loja é proteger a venda.</span></p>
    </div>
    <p class="fonte">Considerando aprovação no início de dezembro de 2026. Produção de referência da 75 LAB: peças pesadas em até 30 dias úteis, leves em 10. Matriz de papéis proposta pela 75 LAB, a validar com a Bordon. Reação à falta: Helm e Hegenbart, 2011, a partir de Gruen, Corsten e Bharadwaj, GMA, 2002.</p>
    <aside class="roteiro" hidden>A execução, em três abas. No cronograma, com o sim no início de dezembro, visitamos as lojas, fechamos o key visual e o projeto executivo, produzimos as peças com QR e instalamos a primeira onda no atacarejo e no hiper em março. A segunda onda chega aos supermercados e às lojas de bairro antes do São João. Em quem faz, cada atividade tem quem executa e quem aprova: a 75 LAB cria, produz, instala e mede; o trade da Bordon negocia espaço; o distribuidor abastece; a promotoria repõe e faz a degustação. E em como medimos: QR em toda peça, acompanhamento das peças grandes e uma nota de loja perfeita, lida todo mês.</aside>
  </section>
'''
(R / 'src/s14-execucao.html').write_text(html)
print('ok')
