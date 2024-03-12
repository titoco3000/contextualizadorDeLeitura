let texto = `
A espada clara veio pelo ar, tremendo.
Sor Waymar parou­‑a com o aço. Quando as lâminas se encontraram, não se ouviu nenhum
ressoar de metal com metal, apenas um som agudo e fino, no limiar da audição, como um animal
a guinchar de dor. Royce deteve um segundo golpe, e um terceiro, e depois recuou um passo. Ou‑
tra chuva de golpes, e recuou outra vez.
Atrás dele, para a direita, para a esquerda, em seu redor, os observadores mantinham­‑se em
pé, pacientes, sem rosto, silenciosos, com os padrões mutáveis de suas delicadas armaduras a
torná­‑los quase invisíveis na floresta. Mas não faziam um gesto para intervir.
Uma vez e outra, as espadas encontraram­‑se, até Will querer tapar os ouvidos, protegendo­‑os
do estranho e angustiado lamento de seus choques. Sor Waymar já arquejava por causa do es‑
forço, e a respiração gerava nuvens ao luar. Sua lâmina estava branca de gelo; a do Outro dançava
com uma pálida luz azul.
Então, a parada de Royce chegou um momento tarde demais. A espada cristalina trespassou
a cota de malha por baixo de seu braço. O jovem senhor gritou de dor. Surgiu sangue por entre os
aros, correu ao frio, e as gotas pareciam vermelhas como fogo onde tocavam a neve. Os dedos de
Sor Waymar esfregaram o flanco. Sua luva de pele de toupeira veio empapada de vermelho.
O Outro disse qualquer coisa numa língua que Will não conhecia; sua voz era como o que‑
brar do gelo num lago de inverno, e as palavras, escarnecedoras.
Sor Waymar Royce encontrou sua fúria.
– Por Robert! – gritou, e atacou, rosnando, erguendo com ambas as mãos a espada coberta
de gelo e brandindo­‑a num golpe lateral paralelo ao chão, carregado com todo seu peso. A parada
do Outro foi quase displicente.
Quando as lâminas se tocaram, o aço despedaçou­‑se.
Um grito ecoou pela noite da floresta, e a espada quebrou­‑se numa centena de pedaços quebra‑
diços, espalhando os estilhaços como uma chuva de agulhas. Royce caiu de joelhos, guinchando, e
cobriu os olhos. Sangue jorrou­‑lhe por entre os dedos.
Os observadores aproximaram­‑se uns dos outros, como que em resposta a um sinal. Espadas
ergueram­‑se e caíram, tudo num silêncio mortal.
Era um assassinato frio. As lâminas pálidas atravessaram a cota de malha como se fosse seda.
Will fechou os olhos. Muito abaixo, ouviu as vozes e os risos, aguçados como pingentes.
Quando reuniu coragem para voltar a olhar, um longo tempo se passara, e a colina lá em­baixo
estava vazia.
Ficou na árvore, quase sem se atrever a respirar, enquanto a lua foi rastejando lentamente pelo
céu negro. Por fim, com os músculos cheios de cãibras e os dedos dormentes de frio, desceu.
O corpo de Royce jazia na neve de barriga para baixo, com um braço aberto. O espesso man‑
to de zibelina tinha sido cortado numa dúzia de lugares. Jazendo assim morto, via­‑se como era
novo. Um rapaz.
        `

let saida = '';
texto.split(/(?<=[.?!])/).forEach(linha=>{
    saida += '<p>';
    linha.split(/(?<=[ \n])/).forEach(palavra=>{
        saida+='<span>'+palavra+'</span>';
    });
    saida += '</p>';
});
let el = document.getElementById("texto");
el.innerHTML = saida;

let ultimaFrase = '';
let momentoHoverInicial;
let buscou;
function update(){
    if(window.getSelection().toString().length){
        el.classList.remove("hover-habilitado");
        let exactText = window.getSelection().toString();
        if(exactText!=ultimaFrase){
            ultimaFrase = exactText;
            momentoHoverInicial = new Date();
            buscou = false;
        }
        else if(new Date() -momentoHoverInicial > 1000 && !buscou){
            console.log(exactText);
            buscou = true;
        }
     }
    else{
        el.classList.add("hover-habilitado");
        
        let e = el.querySelector(':hover:not(:has(span:hover))');
    
        if(e){
            if(ultimaFrase != e.innerText){
                // console.log(e.innerText);
                ultimaFrase = e.innerText;
                momentoHoverInicial = new Date();
                buscou = false;
            }
            else if(new Date() -momentoHoverInicial > 1000 && !buscou){
                    console.log(e.innerText);
                    buscou = true;
            }
        }
        else{
            ultimaFrase = "";
        }

    }    

    window.requestAnimationFrame(update)
}

update();