#!/usr/bin/env python3
# Gera src/s13-calendario.html: calendário de trade 2027 com 12 meses clicáveis (abas com temporizador).
# Datas móveis calculadas (Páscoa pelo cômputo gregoriano; Carnaval = Páscoa menos 47 dias; Mães e Pais = 2º domingo).
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
# mês, tema, intensidade (1 a 3), datas, foco de produto, ação de loja, canal em destaque
M = [
 ('Jan', 'Férias: jantar sem fogão quente', 2, 'Férias escolares', 'Salsicha, maionese de frango, carne desfiada', 'Kit cachorro-quente e lanche pronto na padaria', 'Super e vizinhança'),
 ('Fev', 'Carnaval: petisco pronto', 2, 'Carnaval, 09/02', 'Salsicha aperitivo, salsicha ao molho', 'Display de balcão Petisco junto das bebidas', 'Vizinhança e atacarejo'),
 ('Mar', 'Onda 1 no atacarejo e no hiper', 3, 'Consumidor, 15/03 · Páscoa, 28/03', 'Linha completa', 'Capa de palete, ilha Ponto Pronto e lançamento da degustação', 'Atacarejo e hiper'),
 ('Abr', 'Volta à rotina: jantar em 3 minutos', 2, 'Retomada da rotina', 'Carne de panela, bolonhesa, almôndegas', 'Clip strip no corredor de massas e arroz', 'Supermercado'),
 ('Mai', 'Onda 2 e Dia das Mães', 3, 'Dia das Mães, 09/05', 'Pratos prontos', 'Onda 2 em super e vizinhança; combo jantar "folga da cozinha"', 'Super e vizinhança'),
 ('Jun', 'Inverno e São João', 3, 'Namorados, 12/06 · São João, 24/06', 'Feijoada, costela com mandioca, carne desfiada', 'Degustação reforçada e cross com cuscuz no Nordeste', 'Atacarejo e Nordeste'),
 ('Jul', 'Férias de inverno: caldos e feijoada', 2, 'Férias escolares', 'Feijoada, carne em cubos, salsicha', 'Sábado de feijoada no encarte e no app', 'Hiper e digital'),
 ('Ago', 'Dia dos Pais: sábado de feijoada', 2, 'Dia dos Pais, 08/08', 'Feijoada, costela com mandioca', 'Ilha com feijoada e combo com farofa e couve', 'Hiper e super'),
 ('Set', 'Cestas e Dia do Cliente', 2, 'Dia do Cliente, 15/09', 'Carne em conserva, salsicha, feijoada', 'Catálogo para montadoras de cestas; leitura do 1º semestre', 'Cestas e atacarejo'),
 ('Out', 'Dia das Crianças: lanche pronto', 1, 'Dia das Crianças, 12/10', 'Salsicha, maionese de frango', 'Kit cachorro-quente; ajuste das peças pela leitura', 'Super e digital'),
 ('Nov', 'Black Friday: abastecer a despensa', 3, 'Black Friday, 26/11', 'Itens de giro em caixa', 'Leve mais, pague menos e preço por caixa', 'Atacarejo e digital'),
 ('Dez', 'Fim de ano: ceia e dias seguintes', 2, 'Natal, 25/12', 'Fiambre, salsicha aperitivo, feijoada', 'Petisco pronto na ceia e cestas de Natal', 'Todos os canais'),
]
barras = ''.join(f'<button class="aba mes" style="--h:{h}"><i></i><span>{m}</span></button>' for m, _, h, *_ in M)
pns = ''
for m, tema, h, datas, prod, acao, canal in M:
    pns += f'''<div class="painel"><div class="cal-p"><div class="cal-t"><span class="mono">{m} · 2027</span><h3>{tema}</h3><p class="cal-d">{datas}</p></div>
<dl class="cal-dl"><dt>Produtos em foco</dt><dd>{prod}</dd><dt>Na loja</dt><dd>{acao}</dd><dt>Canal em destaque</dt><dd>{canal}</dd></dl></div></div>'''
html = f'''
  <!-- 20 · calendário 2027 -->
  <section class="tela escuro calendario" data-parte="4" data-titulo="Calendário 2027" data-capitulo="4 · Como">
    <div class="marcas"><div class="par"><img class="bd" src="assets/img/logo-bordon.png" alt="Logo Bordon"><span class="x">×</span><img class="lab" src="assets/logos/logo-lime.png" alt="Logo 75 LAB"></div></div>
    <div class="miolo" data-abas>
      <div class="cal-topo"><h2 class="anima">Doze meses, <em>três picos de força.</em></h2><span class="clique anima d1"><svg><use href="#i-mao"/></svg>Clique em cada mês</span></div>
      <div class="cal-leg anima d1"><span><i style="--h:1"></i>manutenção</span><span><i style="--h:2"></i>ativação</span><span><i style="--h:3"></i>pico: ponto extra, degustação e encarte</span></div>
      <div class="abas-bts cal-bar anima d1">{barras}</div>
      <div class="anima d2">{pns}</div>
      <p class="teoria anima d5"><svg class="ico"><use href="#i-livro"/></svg><span><b>Teoria</b> Romaniuk, 2023: cada data forte é um momento de compra. A Bordon aparece onde o shopper já está decidindo o que comer.</span></p>
    </div>
    <p class="fonte">Datas de 2027: Carnaval, Páscoa, Dia das Mães, Dia dos Pais e Black Friday calculados pelas regras de cada data; demais datas fixas. Picos em março (onda 1), maio e junho (onda 2, inverno e São João) e novembro (Black Friday).</p>
    <aside class="roteiro" hidden>O calendário de 2027 tem um tema por mês e três picos de força. Março, com a primeira onda no atacarejo e no hiper. Maio e junho, com a segunda onda, o Dia das Mães, o inverno e o São João, quando a feijoada e a costela com mandioca são protagonistas e o Nordeste ganha cross com cuscuz. E novembro, com a Black Friday, para abastecer a despensa por caixa. Nos outros meses, ativações menores ligadas a momentos: férias, carnaval com petisco, Dia dos Pais com sábado de feijoada e as cestas de fim de ano. Cliquem em cada mês para ver produto, ação e canal.</aside>
  </section>
'''
(R / 'src/s13-calendario.html').write_text(html)
print('calendário ok')
