import os
import google.generativeai as genai
from dotenv import load_dotenv
import hashlib
import random

def listAvailableModels():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

def fazerPergunta(prompt):
    pastaRespostas = __file__.replace(f"<your script name>.py", "")[:-11]+'respostas'
    os.makedirs(pastaRespostas, exist_ok=True)

    onlyfiles = [os.path.join(pastaRespostas, f) for f in os.listdir(pastaRespostas) if os.path.isfile(os.path.join(pastaRespostas, f))]

    hash = hashlib.shake_128(prompt.encode("utf-8")).hexdigest(8)
    filename =  pastaRespostas+ '/p'+hash+'.txt'

    if filename in onlyfiles:
        print('lendo resposta velha')
        f = open(filename, "r")
        response = f.read()
        f.close()
    else:
        print('pedindo resposta nova')
        
        responseCompleta = model.generate_content(prompt)

        try:
            response = responseCompleta.text
        except:
            print('Erro: ',responseCompleta)
            exit(1)

        f = open(filename, "w")
        f.write(response)
        f.close()
    return response

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


textos = [
    '''– Deveríamos regressar – insistiu Gared quando os bosques começaram a escurecer ao re‑
dor do grupo. – Os selvagens estão mortos.
– Os mortos o assustam? – perguntou Sor Waymar Royce com não mais do que uma suges‑
tão de sorriso no rosto.
Gared não mordeu a isca. Era um homem velho, com mais de cinquenta anos, e vira os nobres
chegar e partir.
– Um morto é um morto – respondeu. – Nada temos a tratar com os mortos.
– Mas estão mortos? – perguntou Royce com suavidade. – Que prova temos disso?
– Will os viu – disse Gared. – Se ele diz que estão mortos, é prova suficiente para mim.
Will já sabia que o arrastariam para a disputa mais cedo ou mais tarde. Desejou que tivesse
sido mais tarde.
– Minha mãe disse­‑me que os mortos não cantam – contou Will.
– Minha ama de leite disse a mesma coisa, Will – respondeu Royce. – Nunca acredite em
nada do que ouvir junto à mama de uma mulher. Há coisas a aprender mesmo com os mortos
– sua voz gerou ecos, alta demais na penumbra da floresta.
– Temos perante nós uma longa cavalgada – salientou Gared. – Oito dias, talvez nove. E a
noite está para cair.
Sor Waymar Royce olhou o céu de relance, com desinteresse.
– Isso acontece todos os dias por esta hora. Você perde a virilidade com o escuro, Gared?
Will via o aperto em torno da boca de Gared, a ira só a custo reprimida nos olhos que esprei‑
tavam sob o espesso capuz negro de seu manto. Ele passara quarenta anos na Patrulha da Noite,
em homem e em rapaz, e não estava acostumado a ser desvalorizado. Mas era mais do que isso.
Will conseguia detectar no homem mais velho algo mais sob o orgulho ferido. Era possível sentir‑
‑lhe o gosto: uma tensão nervosa que se aproximava perigosamente do medo.
Will partilhava o desconforto do outro homem. Estava havia quatro anos na Muralha. Da
primeira vez que fora enviado para lá, todas as velhas histórias lhe tinham acorrido ao cérebro, e
suas entranhas se tinham feito em água. Era agora um veterano de cem patrulhas, e a es­cura
e infi­nita terra selvagem a que os sulistas chamavam floresta assombrada já não tinha terrores para si.
Até aquela noite. Algo era diferente então. Havia naquela escuridão algo de cortante que lhe
fazia eriçar os pelos da nuca. Cavalgavam havia nove dias, para norte e noroeste, e depois de novo
para norte, cada vez para mais longe da Muralha, seguindo sem desvios a trilha de um bando de
salteadores selvagens. Cada dia fora pior que o anterior. Aquele tinha sido o pior de todos. Um
vento frio soprava do norte e fazia as árvores sussurrarem como coisas vivas. Durante todo o dia ''',
'''
Desde tempos imemoriais houve menos que meia dúzia de mortais cujas mentes foram capazes de contemplar o universo em sua totalidade: Einstein, Hubble, Feynman e Douglas Adams são os nomes que surgem em meu cérebro comparativamente ínfimo e inútil. Destes poucos gênios especiais, Douglas Adams é, sem dúvida, o pensador mais hilariantemente original, embora seja consenso geral que Einstein era melhor dançarino de funk. O Guia do Mochileiro das Galáxias começou sua história como uma série de rádio e, depois, uma compilação em fita cassete. Transformado em livro, tornou-se um best-seller mundial e foi parar, de forma curiosa, na televisão britânica. Com uma galeria de personagens bizarros e tantas viradas abruptas na trama que você se sentirá em uma montanha-russa, O Guia do Mochileiro é, sem dúvida, uma das mais criativas e cômicas histórias de aventura jamais escritas. Arthur Dent, um inglês azarado, escapa de um evento dramático - a destruição da Terra -, graças a um amigo de Betelgeuse que, enquanto estava ilhado em nosso planeta, havia se disfarçado de ator desempregado. Arthur se vê arrastado, apesar de seus protestos histéricos (bem, "histérico" dentro da habitual fleuma britânica), para as situações mais alucinadas nos pontos mais distantes do tempo e do espaço. O que realmente sustenta este livro hilariante, através de sua viagem freneticamente bizarra pela galáxia rumo ao legendário planeta de Magrathea - e além -, é a pergunta profunda sobre o porquê. De onde viemos? Por que estamos aqui? Para onde vamos? Onde vamos almoçar hoje? Além disso, enquanto Arthur tenta se entender com as formas de vida mais estranhas e os nomes ainda mais estranhos dessas formas de vida estranhas, nosso anti-herói descobre a verdadeira história da Terra e a resposta final à grande pergunta da Vida, do Universo e Tudo o Mais. No geral, um resultado bastante satisfatório, devo dizer.
''',
'''
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
novo. Um rapaz.'''
]

# textoAnalisado = input('Digite o texto para ser analisado: ')
textoAnalisado = textos[2]

resposta = fazerPergunta('Coontextualize o seguinte texto, frase por frase. Começe cada contextualização com o marcador ctx=. Analise:  '+textoAnalisado)
print('\n\n')
for linha in resposta.split('\n\n'):
    achou = False
    for marcador in ['Ctx','ctx','CTX']:
        index = linha.index(marcador)
        if(index>=0):
            contexto = (linha[index + len(marcador)+1:]).replace('**','')
            print(contexto,'\n')
            achou = True
            break
    if not achou:
        print('marcador não encontrado: ',linha)