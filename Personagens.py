import streamlit as st
st.set_page_config(layout='wide')

st.sidebar.title('Valnoxar')
st.sidebar.image('capa.png')

personagens = ['Azael Vharros','Tomy de Muitos Nomes', 'Nox de Lamaferro', 'Kelamvara Noctis']
personagem = st.sidebar.selectbox('Personagens', personagens)

_1, _2, _3 = st.columns(3)
with _2:
    st.title(personagem)
    st.image(personagem+'.png', width=300)

if personagem == 'Azael Vharros':
    historia_azael, a_fuga, eldrin_thalos, o_ensinamento, a_queda_de_elturel, o_juramento = st.tabs(['História', 'A Fuga', 'Eldrin Thalos', 'O Ensinamento','A Queda de Elturel', 'O Juramento'])
    with historia_azael:
        st.markdown("""
Azael nunca soube o que era ser acolhido.
Foi deixado ainda bebê à porta de um pequeno orfanato nas terras de Elturgard, próximo à antiga Estrada do Comércio, em uma região onde as pessoas ainda fingiam que o Inferno era apenas uma palavra distante, citada em sermões e histórias para assustar crianças.
Não houve despedida.
Não houve bilhete.
Não houve promessa.
Apenas o frio da pedra sob seu corpo frágil, o choro fraco de um recém-nascido… e o peso de um destino que ninguém quis carregar.
Desde os primeiros anos, sua existência foi marcada pelo olhar dos outros.
Pele vermelha demais.
Chifres que surgiram cedo demais.
Olhos que nunca pareceram pertencer ao mesmo mundo que os deles.
As crianças não o chamavam pelo nome.
Para elas, nomes eram dados a pessoas.
Azael era monstro.
Aberração.
Coisa.

Cada palavra era como uma pedra lançada, e com o tempo ele aprendeu a abaixar a cabeça — não para se proteger, mas porque passou a acreditar que merecia.
Cresceu assim.
Não apenas sozinho…
mas rejeitado pela própria ideia de normalidade.
""")
    with a_fuga:
        st.html("""
Quando finalmente teve forças para correr, correu.<br>
Fugiu do orfanato como quem foge de uma prisão sem grades visíveis. Caminhou pela Estrada do Comércio, sem rumo, sem mapa, sem esperança. Apenas com a certeza de que qualquer lugar seria melhor do que aquele onde sua existência era tratada como um erro constante.<br>
A chuva o encontrou antes do fim da noite.<br>
O frio o venceu antes do amanhecer.<br>
Seu corpo caiu à beira da estrada, entre as terras ao sul de Portão de Baldur e as florestas antigas que cercam Elturgard. A consciência se apagou como uma vela cansada.
""")
    with eldrin_thalos:
        _1, _2 = st.columns(2)
        with _1:
            st.markdown("""
Foi assim que Eldrin Thalos o encontrou.
Um velho mago errante, conhecido entre os estudiosos da Fortaleza de Velas como um pesquisador excêntrico das artes arcanas defensivas. Havia se afastado das grandes cidades depois de perder a visão para o tempo — mas jamais perdeu a curiosidade.
Ao despertar, o instinto falou mais alto.
Azael pensou em fugir. Sempre fugia.
Mas algo o impediu.
O homem à sua frente não recuava.
Não gritava.
Não buscava armas nem preces apressadas.
Havia apenas preocupação em sua voz.
Foi então que Azael percebeu:
Eldrin Thalos não o via como um monstro.
Talvez porque…
não pudesse vê-lo.
Os olhos leitosos do mago jamais julgaram a pele vermelha, a cauda ou os chifres. Para ele, Azael era apenas alguém ferido, exausto… vivo.
Quando Azael, ainda desconfiado, falou do ódio que conhecia desde criança, do medo que despertava sem querer, Eldrin respondeu com uma simplicidade quase cruel:

— Todos devem ser como são.
As palavras não curaram nada.
Mas plantaram algo.
A torre e o refúgio

Azael ficou.
Ficou dias.
Meses.
Anos.

A torre de Eldrin Thalos, erguida próxima a uma antiga clareira  entre os bosques do troll, ao norte de Elturel, tornou-se seu mundo.
Durante toda a juventude, Azael foi seus olhos.
Lia grimórios em voz alta.
Descrevia símbolos arcanos.
Organizava pergaminhos gastos pelo tempo.
Foi assim que aprendeu magia —
não como poder,
mas como linguagem.
Como proteção.
Como refúgio.
Ainda assim, quase nunca saía.
Não queria assustar ninguém.
Não queria ser lembrado.
Apenas à noite, quando o mundo dormia e o julgamento silenciava, caminhava até a floresta próxima para observar as estrelas sobre o Mar das Espadas. Elas jamais respondiam…
mas também jamais o rejeitavam.
""")
        with _2:
            st.image('Eldrin Thalos.png', width=400)
    with o_ensinamento:
            st.markdown("""
Foi Eldrin Thalos quem lhe deu o ensinamento que moldaria sua alma:
— Azael, você precisa aprender a se proteger. Existem conhecimentos arcanos capazes de impedir que a maldade das pessoas te alcance.
A ideia o consumiu.
Azael passou a estudar obsessivamente magias de proteção, selos, círculos defensivos e barreiras invisíveis — tradições antigas que remontavam aos tempos de Netheril e aos primeiros grandes arcanistas humanos de Faerûn.
Ele não queria ferir o mundo.
Queria sobreviver a ele.
""")
    with a_queda_de_elturel:
        st.markdown("""
Com o passar dos anos, o tempo cobrou seu preço.
Eldrin Thalos adoeceu, vítima de uma enfermidade rara, resistente até mesmo às magias que dominara por toda a vida. Seu poder arcano falhou. Seus dias tornaram-se curtos.
Desesperado, Azael partiu em direção a uma das cidades próximas a Elturel, em busca de ajuda: clérigos, alquimistas, qualquer esperança.
Então o céu se partiu.    
                                 
Um raio rasgou as nuvens, e a sombra colossal de Elturel sendo arrastada para o Inferno projetou-se sobre a terra. Os sinos soaram. Gritos ecoaram como vidro quebrado.

— Monstro!
Azael gritava que não era um monstro.
                    
Que só queria salvar seu mestre.
Mas o medo corre mais rápido que a razão.
Quando a guarda surgiu, ele correu de volta para a torre.
Lá, encontrou o fim.
Flechas incendiárias cortaram o ar, disparadas por homens que acreditavam estar salvando o antigo sábio da região. Ninguém sabia. Ninguém perguntou.
Quando Azael entrou na torre…
o silêncio respondeu.
A chama de vida de Eldrin Thalos havia se apagado.
""")

    with o_juramento:
        st.markdown("""Azael ajoelhou-se ao lado do corpo…
e então viu seu reflexo em um espelho antigo:
pele vermelha,
cauda longa,
três chifres curvados como uma sentença.
Ali, sozinho, amaldiçoou sua origem.
Prometeu a Eldrin Thalos que faria de tudo para se proteger com os conhecimentos que aprendera.
Prometeu que buscaria uma forma de impedir que outros nascessem marcados como ele —
condenados pelo Inferno antes mesmo do primeiro suspiro.
Sem olhar para trás, saltou pela janela e fugiu para a floresta.
E se alguém o tivesse observado naquela noite, teria visto apenas uma coisa:
uma única lágrima descendo lentamente pelo rosto de um tiefling que jamais quis ser um monstro.""")
elif personagem == 'Tomy de Muitos Nomes':
    historia_tomy, os_mascarados, a_rede_negra, dupla_vida, o_verdadeiro_conflito, o_legado = st.tabs(['História', 'Os Mascarados', 'A Rede Negra', 'Dupla Vida', 'O Verdadeiro Conflito', 'O Legado de Luiren'])
    with historia_tomy:
        st.markdown("""
(A Voz que Sussurra na multidão)

Tomy nasceu nas colinas verdes de Luiren, a Terra dos Pequenos — onde o cheiro de pão fresco mistura-se ao som de violinos ao entardecer e onde cada colina guarda uma história mais antiga que os reinos humanos.

Filho de uma trupe itinerante, ele cresceu entre carroças pintadas, lanternas coloridas e palcos improvisados nas feiras de Beluir e Ormpur. Enquanto os outros halflings celebravam a alegria do espetáculo, Tomy fazia algo diferente:

Ele observava.

Aprendeu cedo que aplausos escondem inveja.
Que sorrisos podem mascarar dívidas.
Que silêncios prolongados são mais reveladores que discursos inflamados.

Em Luiren, onde todos parecem simples, ele descobriu que ninguém é.
        """)
    with os_mascarados:
        st.markdown("""
Seu talento não passou despercebido.
Durante uma apresentação em um festival nas colinas do sul, um grupo discreto o avaliava entre a plateia: os Mascarados de Virelyn, uma guilda secreta de artistas-espiões que acreditava que o teatro era a forma mais refinada de política.

Eles não brandiam espadas.
Eles plantavam ideias.

Tomy foi recrutado ainda jovem. Sob sua tutela, aprendeu:

A assumir identidades como quem troca de chapéu, alterar postura, sotaque e respiração para se tornar outra pessoa.

A usar venenos não letais para extrair informações.

A desenvolver resistência gradual às toxinas que manipulava.

Ele transformou fragilidade em arma.
Transformou aparência em escudo, e acima de tudo, aprendeu que a informação é a moeda mais poderosa de Faerûn.
        """)
    with a_rede_negra:
        st.markdown("""
Mas o mundo fora de Luiren é menos gentil.

Durante uma missão em Portão de Baldur, infiltrado como músico em uma caravana mercante, Tomy cometeu um erro calculado — um sussurro no ouvido errado.

Ele foi descoberto pelos Zhentarim.
A Rede Negra não executa talentos raros.

Ela os captura.

Os Zhentarim perceberam algo nele:
Um halfling invisível entre gigantes.
Um artista capaz de ouvir o que ninguém percebe.
Um manipulador que poderia desmantelar conspirações antes mesmo de nascerem.

Em vez de matá-lo, ofereceram uma escolha, Trabalhar para a Rede… ou desaparecer sem deixar eco.

Tomy aceitou — mas não se dobrou.

Hoje ele atua como uma peça delicada dentro da estrutura zhentarim, oficialmente um informante itinerante.
Na prática… um presa observando seus próprios predadores.
        """)
    with dupla_vida:
        st.markdown("""
Para os Mascarados, ele ainda é Tomy.
Para os Zhentarim, ele é apenas mais um PRESA.
Para cada cidade que visita, um novo nome nasce.

Ele nunca usa o mesmo duas vezes.

Viaja com alaúde nas mãos, sorriso leve e olhos atentos, enquanto nobres discutem tratados, ele percebe quem treme, enquanto mercadores brindam, ele identifica quem mente.
Enquanto líderes discursam, ele escolhe quem cairá primeiro.

⚖️ O VERDADEIRO CONFLITO

Tomy não deseja poder.

Ele busca equilíbrio.

Mas está preso entre duas forças:

Uma guilda que acredita na arte como instrumento de harmonia. Uma rede que usa o comércio e o medo para dominar reinos.
Ele sabe que um dia terá que escolher.

Ou talvez…
Manipular ambos até que se anulem.
        """)
    with o_verdadeiro_conflito:
        st.markdown("""
Tomy não deseja poder.

Ele busca equilíbrio.

Mas está preso entre duas forças:

Uma guilda que acredita na arte como instrumento de harmonia. Uma rede que usa o comércio e o medo para dominar reinos.
Ele sabe que um dia terá que escolher.

Ou talvez…
Manipular ambos até que se anulem.

        """)
    with o_legado:
        st.markdown("""
Apesar das intrigas, Tomy carrega consigo algo que os Zhentarim jamais entenderão:

O espírito de Luiren.

A crença de que o pequeno pode derrubar o grande.
Que uma palavra certa pode impedir uma guerra.
E que a sombra mais perigosa não é a que grita —
Mas a que sussurra.

        """)

elif personagem == 'Nox de Lamaferro':
    st.markdown("""
Fui deixada ainda bebê nas trilhas enlameadas próximas ao Subterrâneo, nas rotas esquecidas que margeiam o Rio Chionthar. Não havia carta. Não havia símbolo. Não havia promessa de retorno.

Apenas frio. E lama.

Não fui abandonada dentro dos muros de Portal de Baldur.
Fui deixada em Lamaferro.

Lamaferro não existe nos registros dos patriarcas. Não é reconhecida pela Cidade Alta. É o amontoado de casas tortas, ferrarias improvisadas e vielas sufocadas por fumaça que cresceu grudado às muralhas externas, como uma cicatriz que a cidade se recusa a tratar.

Quando chove em Eleint, o mês das tempestades, o chão vira um mar espesso de barro escuro misturado a fuligem e sangue seco. Foi ali que aprendi a andar. Foi ali que aprendi a correr.

A fome foi minha primeira mestra.
O silêncio, minha primeira oração.

Aprendi que dormir profundamente é um luxo perigoso, que confiança mal colocada dói mais do que qualquer lâmina.
Que a Guarda dos Punhos Flamejantes só pisa em Lamaferro quando quer demonstrar força — nunca quando alguém precisa de ajuda.

Roubei pão das carroças vindas dos Campos dos Mortos.
Atravessei telhados frágeis sob chuva pesada.
Aprendi os horários das docas, os vícios dos mercadores e os atalhos que nem mesmo a Guilda dominava por completo.

Ouvi o nome de Ulder Ravengard ecoar nas tavernas como um líder severo, mas justo.
Ouvi sussurros sobre patriarcas vendendo favores.
Ouvi histórias sobre deuses mortos que ainda exigiam sangue.

Mas ninguém ouvia as crianças de Lamaferro.

Até ADÉLIA...

Ela não tinha ouro. Não tinha poder. Não tinha proteção política, ainda assim, recolhia crianças como quem desafia o próprio destino.

Sua casa ficava na parte mais alta de Lamaferro, onde a lama secava primeiro e o vento levava embora a fumaça das forjas improvisadas. Lá aprendi o que era ter um prato quente esperando por mim. Aprendi que algumas pessoas valem o risco.

Nunca deixei de ser desconfiada.
Mas aprendi a baixar a guarda… um pouco.

Quando Adélia adoeceu, a Cidade Alta não enviou curandeiros.

A Guarda não apareceu.
Os patriarcas continuaram brindando sob lustres dourados.

Então voltei às ruas.

Não por desespero.
Por escolha.

Roubei melhor. Mais limpa. Mais rápida.
Nunca toco em velhos. Nunca em crianças. Quem faz isso em Lamaferro deixa de ser gente.

Foi nessa época que começaram a sussurrar um nome nas vielas:

Nox.

A sombra que atravessa telhados durante tempestades, a lâmina que corta bolsas, não gargantas — a menos que seja preciso.
A ladina que protege a casa na colina de madeira torta.

Mas Portal de Baldur começou a apodrecer mais rápido do que o normal.

Refugiados de Elturel chegaram em massa.
Medo virou moeda, Cultos surgiram nas sombras.
Rumores sobre contratos infernais circularam entre os mais ricos.

E eu senti.

Algo maior estava se movendo.

Talvez meu abandono não tenha sido simples descaso.
Talvez tenha sido necessidade.
Talvez alguém soubesse que Lamaferro me tornaria forte.

Hoje viajo quando preciso. Volto quando escolho.
Não pertenço à Cidade Alta.
Não pertenço à Cidade Baixa.

Eu pertenço às poucas pessoas que decido proteger.

E se o Inferno acredita que pode tomar Baldur’s Gate começando pelas bordas…

Vai descobrir que as sombras de Lamaferro não se curvam.

""")

elif personagem == 'Kelamvara Noctis':
    st.markdown("""
Criado entre túmulos e ritos fúnebres, ele foi acolhido ainda jovem pelo clero de Kelemvor. Desde cedo demonstrou uma estranha afinidade com a morte: espíritos inquietos se aquietam em sua presença, e lugares marcados por tragédias parecem mais silenciosos quando ele passa.
Treinado como paladino, aprendeu que a morte não é punição nem recompensa, mas uma etapa que deve ser respeitada. Ele não busca glória, apenas garantir que aquilo que deveria descansar, descanse.
Às vezes sonha com chamas distantes e uma queda sem rosto, imagens confusas que carregam um peso antigo demais para alguém tão jovem. Não sabe o que significam, apenas que não são sonhos comuns.
Agora enviado para fora do cemitério a serviço de sua fé, ele caminha entre os vivos como julgador, não como herói, empunhando uma foice consagrada como símbolo de que todo fim chega.


Véu de Kelemvor<br>
Nome comum:<Br>
Véu de Kelemvor<br>
Nome ritualístico (usado por clérigos):<br>
Kelemvara Noctis

🌸 Descrição<br>
O Véu de Kelemvor é uma flor rara que cresce em solos consagrados à morte natural — especialmente em cemitérios antigos, campos de batalha purificados e colinas onde corpos foram enterrados com honra.
Ela floresce apenas durante a noite.
Pétalas finas, de cor branco-acinzentada, quase translúcidas
O centro da flor é negro profundo, como um vazio silencioso
Exala um perfume leve, frio e limpo — lembrando terra molhada após chuva
Quando o primeiro raio do sol toca suas pétalas, elas se fecham lentamente, como olhos que terminaram de julgar.

⚖️ Simbolismo<br>
As pétalas claras representam a alma despida de mentiras
O centro negro simboliza o julgamento inevitável
O florescer noturno indica que a morte não é escuridão… mas passagem
Devotos de Kelemvor acreditam que a flor só nasce onde:
Não houve necromancia
O morto aceitou seu destino
O ciclo natural foi respeitado
Se mortos-vivos forem erguidos perto de onde ela cresce, o Véu de Kelemvor murcha imediatamente.

🕯️ Uso nos rituais<br>
Durante funerais:<br>
Uma única flor é colocada sobre o peito do falecido<br>
O sacerdote recita:<br>
“Que teu espírito caminhe sem correntes,
que teu peso seja medido com justiça,
e que teu nome não tema a balança.”
Após três noites, a flor desaparece sozinha — não apodrece, não seca.
Os fiéis acreditam que isso significa que a alma foi julgada.
""", unsafe_allow_html=True)

