# Bordon × 75 LAB · Estratégia de trade marketing para os enlatados 2027

Apresentação em HTML da estratégia completa de trade marketing para os enlatados Bordon (JBS/Friboi): plataforma **Ponto Pronto Bordon**.

- Apresentação: https://projetos.75lab.com.br/bordon-enlatados-trade/
- PDF: `bordon-75lab-trade-2027.pdf` (capa com link e QR, uma página por botão)

## Estrutura (31 telas, 4 capítulos)
Abertura (dado, capa, 75 LAB, diferencial, resumo, oito recomendações) · 01 Para onde vamos · 02 Por que (mercado, pesquisa de compra, insight do consumidor, shopper, barreiras) ·
03 Como (mapa da estratégia, plataforma e KV, pilares, canais, gôndola P/M/G, sistema de peças, 10 peças, ativação, calendário 2027, execução) ·
04 O que teremos (medição One Shot e On Timing, cronograma de execução em Gantt, papéis RACI, resultados esperados, próximo passo).
Transição de cinema entre telas (cortina amarela, faixas e zoom), ícones e infográficos animados.

## Como editar
- Telas em `src/tNN-*.html`, estilos em `src/base.css`, `src/telas.css` e `src/celular.css`, navegação em `src/deck.js`.
- Geradas por script: `fonte/capitulos.py` (capas), `fonte/planograma.py` (gôndola), `fonte/calendario.py` (calendário), `fonte/execucao.py` (Gantt e RACI). `fonte/enxugar.py` guarda a revisão enxuta de 16/11.
- Montar: `python3 fonte/build.py` (gera `index.html`, `assets/deck.*`, `versao.txt` e confere travessão).
- Prévia: `fonte/sincronizar.sh` e servidor local na porta 4783.
- Conferências: `node fonte/miniaturas.mjs <base> <pasta>` (texto sobreposto ou fora da tela), `node fonte/celular.mjs <base> <saida.jpg>` (iPhone), `node fonte/fora.mjs`.
- PDF: `node fonte/gerar-pdf.mjs http://localhost:4783/ bordon-75lab-trade-2027.pdf`.
- Teclas: setas navegam, M abre o sumário, N mostra o roteiro de fala.

## Fontes de material
KV "Mais que bom", logomarca e Manual de Identidade Visual de embalagem enviados pela Friboi (latas recortadas do manual e do KV).
Dados de mercado e teorias com a fonte no pé de cada tela.
