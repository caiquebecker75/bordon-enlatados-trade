#!/usr/bin/env python3
# 17/11/2026: a tela aparece por baixo da cortina e só anima quando a cortina sai; cortina com as duas marcas.
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
p = R / 'src/deck.js'; s = p.read_text()
old = """    setTimeout(()=>{troca(n);},cap?520:380);
    setTimeout(()=>{wipe.classList.remove('vai');stage.classList.remove('cine');trocando=false;},cap?1150:860);
  }
  function troca(n){
    const ant=atual>=0?telas[atual]:null;
    if(ant){ant.classList.remove('ativa');ant.classList.add('saindo');setTimeout(()=>ant.classList.remove('saindo'),700);}
    atual=n;const t=telas[n];t.classList.add('ativa');"""
new = """    const cobre=cap?520:380,sai=cap?1150:860;
    setTimeout(()=>{troca(n,sai-cobre-120);},cobre);
    setTimeout(()=>{wipe.classList.remove('vai');stage.classList.remove('cine');trocando=false;},sai);
  }
  /* espera: a tela aparece por baixo da cortina e só começa a animar quando a cortina sai, para os infográficos serem vistos */
  function troca(n,espera){
    const ant=atual>=0?telas[atual]:null;
    if(ant){ant.classList.remove('ativa','visivel');ant.classList.add('saindo');setTimeout(()=>ant.classList.remove('saindo'),700);}
    atual=n;const t=telas[n];
    if(espera>0){t.classList.add('visivel');setTimeout(()=>{if(atual===n)entra(t);},espera);}else entra(t);
    prog.style.width=((n+1)/total*100)+'%';cont.textContent=dd(n+1)+' / '+dd(total);
    $('#ant').disabled=n===0;$('#prox').disabled=n===total-1;
    html.dataset.fundo=t.classList.contains('escuro')||t.classList.contains('capa')||t.classList.contains('q-tema-escuro')||t.classList.contains('vermelho')?'escuro':(t.classList.contains('amarelo')?'amarelo':'claro');
    $$('#sumLista button').forEach(b=>b.classList.toggle('atual',+b.dataset.i===n));
    history.replaceState(null,'','#'+(n+1));mostrarFala();
  }
  function entra(t){
    t.classList.remove('visivel');t.classList.add('ativa');"""
assert old in s; s = s.replace(old, new)
old2 = """    prog.style.width=((n+1)/total*100)+'%';cont.textContent=dd(n+1)+' / '+dd(total);
    $('#ant').disabled=n===0;$('#prox').disabled=n===total-1;
    html.dataset.fundo=t.classList.contains('escuro')||t.classList.contains('capa')||t.classList.contains('q-tema-escuro')||t.classList.contains('vermelho')?'escuro':(t.classList.contains('amarelo')?'amarelo':'claro');
    t.querySelectorAll('[data-conta]').forEach(el=>{if(!el.closest('.painel'))contar(el);});
    iniciaTimers(t);
    $$('#sumLista button').forEach(b=>b.classList.toggle('atual',+b.dataset.i===n));
    history.replaceState(null,'','#'+(n+1));mostrarFala();
  }"""
new2 = """    t.querySelectorAll('[data-conta]').forEach(el=>{if(!el.closest('.painel'))contar(el);});
    iniciaTimers(t);
  }"""
assert old2 in s; s = s.replace(old2, new2)
p.write_text(s)

c = R / 'src/base.css'
c.write_text(c.read_text() + """
.tela.visivel{opacity:1;visibility:visible;transform:none;filter:none;transition:none}
/* cortina com as duas marcas */
#wipe .wp-b .par-w{display:flex;align-items:center;gap:28px;transform:skewX(14deg);opacity:0}
#wipe .wp-b .par-w img{height:96px}
#wipe .wp-b .par-w img.l{height:54px}
#wipe .wp-b .par-w span{font-family:var(--mono);font-size:28px;font-weight:700}
#wipe.vai .par-w{animation:marca .86s ease both}
#wipe.vai.capitulo .par-w{animation:marca 1.1s ease both}
""")
h = R / 'src/shell.html'; t = h.read_text()
a = '<div class="wp-b"><img src="assets/img/logo-bordon.png" alt=""></div>'
assert a in t
h.write_text(t.replace(a, '<div class="wp-b"><div class="par-w"><img src="assets/img/logo-bordon.png" alt=""><span>×</span><img class="l" src="assets/logos/logo-preto.png" alt=""></div></div>'))
print('ok')
