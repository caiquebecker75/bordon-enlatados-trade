#!/usr/bin/env python3
# 17/11/2026: "a linguagem precisa ser mais explicativa". Põe uma linha "Em outras palavras" no fim do miolo de cada tela.
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
E = {
 't07-depara.html': 'hoje a lata é comprada quando falta comida em casa. Queremos que ela seja escolhida para o jantar, de propósito.',
 't09-mercado.html': None,
 't10-shopper.html': 'o shopper não para para comparar: leva o que vê e reconhece rápido. Por isso é na loja que a Bordon ganha ou perde a venda.',
 't11-barreiras.html': 'para vender mais, a lata precisa estar na prateleira, ser lembrada na hora do jantar e ter o sabor provado.',
 't13-plataforma.html': 'o Ponto Pronto é um lugar fixo na loja, sempre com a mesma cara, onde o shopper encontra o jantar pronto da Bordon.',
 't14-pilares.html': 'o marketing diz o que a Bordon promete; o trade garante que essa promessa esteja na loja, todo dia.',
 't15-canais.html': 'cada tipo de loja tem um jeito de comprar, então cada uma recebe um kit e uma oferta diferentes.',
 't17-sistema.html': 'as peças grandes chamam de longe, as médias explicam no corredor e as pequenas ajudam a decidir na prateleira.',
 't19-ativacao.html': 'primeiro o shopper prova, depois leva com desconto e volta a comprar porque acha a lata fácil na próxima vez.',
 't20-calendario.html': 'a força da Bordon se concentra quando o shopper mais precisa: no lançamento, no inverno e no São João, e na Black Friday.',
 't20b-execucao.html': 'toda loja recebe uma nota de 0 a 100, e o time é premiado quando a nota sobe.',
 't22-medicao.html': 'cada peça tem um QR que comprova onde foi instalada e se continua no lugar, sem precisar mandar alguém conferir.',
 't23b-papeis.html': 'cada atividade tem um dono que faz e um que aprova, para nada ficar no meio do caminho.',
}
def fecha_div(s, i):
    # posição logo depois do </div> que fecha o <div> que começa em i
    n = 0
    for m in re.finditer(r'<div\b|</div>', s[i:]):
        n += 1 if m.group(0).startswith('<div') else -1
        if n == 0:
            return i + m.start()
    raise ValueError
for arq, txt in E.items():
    if not txt: continue
    p = R / 'src' / arq; s = p.read_text()
    if 'class="explica' in s: continue
    i = s.find('<div class="miolo')
    j = fecha_div(s, i)
    linha = f'      <p class="explica anima d5"><svg class="ico"><use href="#i-lampada"/></svg><span><b>Em outras palavras:</b> {txt}</span></p>\n    '
    s = s[:j] + linha + s[j:]
    p.write_text(s)
    print('ok', arq)
