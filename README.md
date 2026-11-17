# Bordon × 75 LAB · Estratégia de trade marketing para os enlatados 2027

Apresentação em HTML da estratégia completa de trade marketing para os enlatados Bordon (JBS/Friboi): plataforma **Ponto Pronto Bordon**.

- Apresentação: https://projetos.75lab.com.br/bordon-enlatados-trade/
- PDF: `bordon-75lab-trade-2027.pdf` (capa com link e QR, uma página por botão)

## Estrutura (v4, 17/11/2026: 15 telas, começo, meio e fim)
Fio no topo: Objetivo → Por quê → A ideia → Como → Execução.
1 Capa · 2 Quem é a 75 LAB · 3 O objetivo · 4 Por que agora · 5 Insight do consumidor · 6 O problema na loja ·
7 A plataforma Ponto Pronto · 8 Mapa da estratégia · 9 Canais · 10 Gôndola · 11 Peças · 12 Ativação ·
13 Calendário 2027 · 14 Execução (cronograma, quem faz, como medimos) · 15 Próximo passo.
A teoria aparece como etiqueta "Teoria" dentro de cada tela, não em tela própria. As telas da v3 (34) estão em `fonte/v3/`.

## Como editar
- Telas em `src/sNN-*.html`, estilos em `src/base.css`, `src/telas.css` e `src/celular.css`, navegação em `src/deck.js`.
- Geradas por script: `fonte/capitulos.py` (capas), `fonte/planograma.py` (gôndola), `fonte/calendario.py` (calendário), `fonte/execucao_v4.py` (tela de execução em abas). `fonte/enxugar.py` guarda a revisão enxuta de 16/11.
- Montar: `python3 fonte/build.py` (gera `index.html`, `assets/deck.*`, `versao.txt` e confere travessão).
- Prévia: `fonte/sincronizar.sh` e servidor local na porta 4783.
- Conferências: `node fonte/sobreposicao.mjs <base> <pasta>` (texto sobre texto ao vivo, aba por aba); `node fonte/miniaturas.mjs <base> <pasta>` (texto sobreposto ou fora da tela), `node fonte/celular.mjs <base> <saida.jpg>` (iPhone), `node fonte/fora.mjs`.
- PDF: `node fonte/gerar-pdf.mjs http://localhost:4783/ bordon-75lab-trade-2027.pdf`.
- Teclas: setas navegam, M abre o sumário, N mostra o roteiro de fala.

## Fontes de material
KV "Mais que bom", logomarca e Manual de Identidade Visual de embalagem enviados pela Friboi (latas recortadas do manual e do KV).
Dados de mercado e teorias com a fonte no pé de cada tela.
