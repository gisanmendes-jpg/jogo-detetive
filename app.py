import streamlit as st
import random
import time
from PIL import Image

# ==========================================
# FUNÇÃO DE OTIMIZAÇÃO DE MEMÓRIA (CACHE)
# ==========================================
@st.cache_data
def carregar_banner():
    imagem_original = Image.open("banner.jpg")
    return imagem_original.resize((1200, 400))
    
# ==========================================
# 1. SETUP DE PÁGINA (DEVE SER A PRIMEIRA COISA!)
# ==========================================
st.set_page_config(page_title="DIE - Investigações", page_icon="🕵️", layout="wide")

# ==========================================
# 2. BANCOS DE DADOS (COM IMAGENS E ARTEFATOS)
# ==========================================
banco_capangas = [
    {"nome": "Gabi Aura Monster", "sexo": "F", "cabelo": "Castanho", "olho" : "Castanho", "detalhes": "Jóia", "imagem": "gabi.png", "imagem_preso": "gabi_triste.gif", "imagem_fuga": "gabi_feliz.gif"},
    {"nome": "Denji",  "sexo": "M", "cabelo": "Loiro", "olho" : "Castanho", "detalhes": "Tapa olho", "imagem": "denji.jpg", "imagem_preso": "denji_triste.gif", "imagem_fuga": "denji_feliz.gif"},
    {"nome": "Nana",  "sexo": "F", "cabelo": "Ruivo", "olho" : "Amarelo", "detalhes": "Jóia", "imagem": "nana.jpeg", "imagem_preso": "nana_triste.gif", "imagem_fuga": "nana_feliz.gif"},
    {"nome": "Gisa Estrela",  "sexo": "F", "cabelo": "Castanho", "olho" : "Castanho", "detalhes": "Tatuagem", "imagem": "gisa.png", "imagem_preso": "gisa_triste.gif", "imagem_fuga": "gisa_feliz.gif"},
    {"nome": "Scarlet",  "sexo": "F", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Cicatriz", "imagem": "https://placehold.co/300x400/8B0000/FFFFFF?text=Scarlet"},
    {"nome": "Ryan",  "sexo": "M", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Jóia", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Ryan"},
    {"nome": "Mayah",  "sexo": "F", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Tapa olho", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Mayah"},
    {"nome": "Elsa",  "sexo": "F", "cabelo": "Preto", "olho" : "Azul", "detalhes": "Jóia", "imagem": "elsa.jpg", "imagem_preso": "elsa_triste.gif", "imagem_fuga": "elsa_feliz.gif"},
    {"nome": "Douma",  "sexo": "M", "cabelo": "Loiro", "olho" : "Amarelo", "detalhes": "Tatuagem", "imagem": "douma.jpg", "imagem_preso": "douma_triste.gif", "imagem_fuga": "douma_feliz.gif"},
    {"nome": "Haru",  "sexo": "M", "cabelo": "Branco", "olho" : "Amarelo", "detalhes": "Tapa olho", "imagem": "haru.jpg", "imagem_preso": "haru_triste.gif", "imagem_fuga": "haru_feliz.gif"},
    {"nome": "Roger",  "sexo": "M", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Tatuagem", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Roger"},
    {"nome": "Clara",  "sexo": "F", "cabelo": "Preto", "olho" : "Azul", "detalhes": "Cicatriz", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Clara"},
    {"nome": "Loira Burrinha",  "sexo": "F", "cabelo": "Loiro", "olho" : "Azul", "detalhes": "Jóia", "imagem": "lb.jpg", "imagem_preso": "lb_triste.gif", "imagem_fuga": "lb_feliz.gif"},
    {"nome": "Victor",  "sexo": "M", "cabelo": "Branco", "olho" : "Castanho", "detalhes": "Cicatriz", "imagem": "victor.jpg", "imagem_preso": "victor_triste.gif", "imagem_fuga": "victor_feliz.gif"}
]

banco_chefes = [
    {"nome": "Makima",  "sexo": "F", "cabelo": "Ruivo", "olho" : "Amarelo", "detalhes": "Tatuagem", "imagem": "makima.jpg"},
    {"nome": "Muzan",  "sexo": "M", "cabelo": "Branco", "olho" : "Vermelho", "detalhes": "Cicatriz", "imagem": "muzan.jpg"}
]

banco_suspeitos = banco_capangas + banco_chefes

banco_artefatos = [
    "o Cetro de Ouro do Imperador",
    "a fórmula secreta de um novo supercomputador",
    "o famoso diamante 'Estrela da Noite'",
    "a pintura original mais cara do mundo",
    "os códigos de acesso de satélites globais",
    "uma relíquia arqueológica inestimável",
    "os planos secretos da agência rival",
    "o projeto original do motor de dobra espacial"
]

mapa_mundi = {
    "Rio de Janeiro": {
        "conexoes": ["Lima", "Nova York", "Tóquio", "Buenos Aires", "Cidade do Cabo"],
        "imagem": "rj.jpg",
        "fatos": [
            "O suspeito queria ver o Cristo Redentor.",
            "Trocou dinheiro por Reais.",
            "Disse que pretendia subir de bondinho até o Pão de Açúcar.",
            "Foi visto caminhando pelo calçadão de Copacabana.",
            "Perguntou onde poderia assistir a um desfile de escolas de samba.",
            "Comprou uma camisa de futebol perto do Maracanã."
        ]
    },
    "Lima": {
        "conexoes": ["Rio de Janeiro", "Nova York", "Cidade do México", "Buenos Aires", "Sydney"],
        "imagem": "lima.jpg",
        "fatos": [
            "Queria conhecer o estádio Monumental.",
            "Perguntou sobre as ruínas de Machu Picchu.",
            "Trocou seu dinheiro por Soles Peruanos.",
            "Foi visto comendo um Ceviche tradicional."
        ]
    },
    "Nova York": {
        "conexoes": ["Rio de Janeiro", "Lima", "Paris", "Cidade do México", "Toronto", "Londres", "Los Angeles"],
        "imagem": "ny.jpg",
        "fatos": [
            "Perguntou onde ficava a balsa para a Estátua da Liberdade.",
            "Tinha um mapa detalhado da ilha de Manhattan.",
            "Trocou toda a sua moeda por Dólares Americanos.",
            "Disse que estava indo para a 'cidade que nunca dorme'."
        ]
    },
    "Cidade do México": {
        "conexoes": ["Lima", "Londres", "Nova York", "Toronto", "Buenos Aires", "Los Angeles"],
        "imagem": "mx.jpg",
        "fatos": [
            "Comeu muitos tacos com pimenta e guacamole.",
            "Comprou um sombreiro gigante em uma feira de rua.",
            "Trocou dinheiro por Pesos Mexicanos.",
            "Perguntou como chegar às enormes pirâmides de Teotihuacán."
        ]
    },
    "Buenos Aires": {
        "conexoes": ["Rio de Janeiro", "Lima", "Cidade do México"],
        "imagem": "ba.jpg",
        "fatos": [
            "Foi visto comendo um alfajor de doce de leite.",
            "Perguntou onde poderia assistir a um show de Tango.",
            "Trocou seu dinheiro por Pesos Argentinos.",
            "Disse que queria ver a Casa Rosada."
        ]
    },
    "Toronto": {
        "conexoes": ["Nova York", "Cidade do México"],
        "imagem": "toro.jpg",
        "fatos": [
            "Reclamou do frio e comprou um casaco muito pesado.",
            "Tinha um broche com uma folha de bordo vermelha.",
            "Trocou o dinheiro por Dólares Canadenses.",
            "Foi visto comprando ingressos para um jogo de hóquei."
        ]
    },
    "Los Angeles": {
        "conexoes": ["Nova York", "Cidade do México", "Sydney", "Tóquio"],
        "imagem": "la.jpg",
        "fatos": [
            "Estava procurando o letreiro gigante de Hollywood.",
            "Perguntou onde ficava a Calçada da Fama.",
            "Foi visto andando de patins em Venice Beach.",
            "Disse que iria visitar o primeiro parque da Disneylândia."
        ]
    },
    "Paris": {
        "conexoes": ["Nova York", "Londres", "Roma", "Berlim"],
        "imagem": "paris.jpg",
        "fatos": [
            "Disse que faria um piquenique aos pés da Torre Eiffel.",
            "Trocou seu dinheiro por Euros.",
            "Foi visto comendo um croissant em uma padaria local.",
            "Disse que queria ver de perto o quadro da Mona Lisa."
        ]
    },
    "Londres": {
        "conexoes": ["Paris", "Cidade do México", "Nova York", "Berlim", "Roma", "Nova Délhi", "Dubai"],
        "imagem": "londres.jpg",
        "fatos": [
            "Estava tomando chá preto pontualmente às 17h.",
            "Queria ajustar o relógio para bater com o horário do Big Ben.",
            "Pagou a conta da pousada usando Libras Esterlinas.",
            "Entrou em uma clássica cabine telefônica vermelha."
        ]
    },
    "Roma": {
        "conexoes": ["Paris", "Londres", "Cairo", "Berlim"],
        "imagem": "roma.jpg",
        "fatos": [
            "Perguntou como chegar às ruínas do Coliseu.",
            "Foi visto jogando uma moeda na Fonte de Trevi.",
            "Pediu uma autêntica pizza margherita no almoço.",
            "Estava tomando um gelato de pistache."
        ]
    },
    "Berlim": {
        "conexoes": ["Paris", "Londres", "Roma", "Moscou"],
        "imagem": "berlim.jpg",
        "fatos": [
            "Perguntou onde ficavam os restos do famoso muro.",
            "Foi tirar uma foto no Portão de Brandemburgo.",
            "Estava comendo salsichão e bebendo cerveja local.",
            "Queria visitar o prédio do Parlamento."
        ]
    },
    "Moscou": {
        "conexoes": ["Tóquio", "Berlim", "Pequim"],
        "imagem": "moscou.jpg",
        "fatos": [
            "Comprou um conjunto de bonecas Matrioscas.",
            "Queria passear pela famosa Praça Vermelha.",
            "Trocou o dinheiro por Rublos.",
            "Reclamou do frio congelante e comprou um chapéu de pele."
        ]
    },
    "Tóquio": {
        "conexoes": ["Rio de Janeiro", "Moscou", "Pequim", "Sydney", "Los Angeles"],
        "imagem": "toquio.jpg",
        "fatos": [
            "Estava estudando o alfabeto japonês.",
            "Mencionou que queria escalar o Monte Fuji.",
            "Trocou notas grandes por Ienes.",
            "Foi visto comprando mangás em Akihabara."
        ]
    },
    "Pequim": {
        "conexoes": ["Tóquio", "Sydney", "Moscou", "Nova Délhi", "Bangkok"],
        "imagem": "pequim.jpg",
        "fatos": [
            "Perguntou qual era o melhor trecho para visitar a Grande Muralha.",
            "Queria entrar no palácio imperial da Cidade Proibida.",
            "Trocou dinheiro por Yuans.",
            "Foi visto comendo pato laqueado tradicional."
        ]
    },
    "Nova Délhi": {
        "conexoes": ["Londres", "Cairo", "Pequim", "Dubai", "Bangkok"],
        "imagem": "nd.jpg",
        "fatos": [
            "Tinha um bilhete de trem para ver o Taj Mahal.",
            "Trocou o dinheiro por Rúpias.",
            "Foi visto comendo frango ao curry bem apimentado.",
            "Tirou fotos de vacas andando livremente pelas ruas."
        ]
    },
    "Bangkok": {
        "conexoes": ["Pequim", "Nova Délhi", "Sydney"],
        "imagem": "bk.jpg",
        "fatos": [
            "Reclamou do forte calor tropical.",
            "Foi visto negociando com o motorista de um tuk-tuk.",
            "Pediu um Pad Thai bem temperado no mercado de rua.",
            "Perguntou como chegar aos famosos Mercados Flutuantes."
        ]
    },
    "Dubai": {
        "conexoes": ["Cairo", "Nova Délhi", "Londres"],
        "imagem": "dubai.jpg",
        "fatos": [
            "Perguntou sobre o prédio mais alto do mundo.",
            "Trocou seu dinheiro por Dirhams.",
            "Agendou um passeio de luxo pelas dunas do deserto.",
            "Foi visto entrando em um hotel em formato de vela."
        ]
    },
    "Cairo": {
        "conexoes": ["Roma", "Cidade do Cabo", "Nova Délhi", "Dubai"],
        "imagem": "cairo.jpg",
        "fatos": [
            "Queria fazer um passeio de camelo ao entardecer.",
            "Foi visto navegando em um barco tradicional pelo Rio Nilo.",
            "Trocou a moeda por Libras Egípcias.",
            "Tirou uma foto na frente de uma gigantesca Esfinge."
        ]
    },
    "Cidade do Cabo": {
        "conexoes": ["Rio de Janeiro", "Cairo"],
        "imagem": "cc.jpg",
        "fatos": [
            "Perguntou como subir a Montanha da Mesa.",
            "Agendou um safári para tentar ver leões e elefantes.",
            "Trocou o dinheiro por Rands.",
            "Foi fotografar uma colônia de pinguins na praia."
        ]
    },
    "Sydney": {
        "conexoes": ["Tóquio", "Lima", "Pequim", "Los Angeles", "Bangkok"],
        "imagem": "sy.jpg",
        "fatos": [
            "Queria ir a um santuário ver cangurus e coalas.",
            "Foi fotografar a famosa Casa de Ópera.",
            "Comprou uma prancha de surfe e foi para Bondi Beach.",
            "Trocou seu dinheiro por Dólares Australianos."
        ]
    }
}

locais_fisicos = ["Hotel", "Clube Esportivo", "Restaurante", "Cafeteria", "Spa"]
locais_geograficos = ["Banco", "Aeroporto", "Porto", "Livraria", "Mercado Central", "Museu", "Agência de Turismo"]

# ==========================================
# 3. SISTEMA DE PROGRESSÃO E PATENTES
# ==========================================
def calcular_dificuldade(casos):
    # Retorna: Patente, tamanho_rota, horas_restantes, enfrenta_chefe, chance_mentira
    if casos == 0: return "Recruta", 4, 120, False, 0.1          # 10% de chance de mentira
    elif casos == 1: return "Detetive Júnior", 5, 110, False, 0.15 # 15% de chance
    elif casos == 2: return "Detetive Particular", 6, 100, False, 0.25 # 25% de chance
    elif casos == 3: return "Investigador", 7, 90, False, 0.35   # 35% de chance
    elif casos == 4: return "Detetive de Elite", 8, 80, False, 0.45 # 45% de chance
    else: return "Super Detetive", 9, 80, True, 0.55             # 55% de chance

def sortear_locais():
    st.session_state.locais_cidade = random.sample(locais_fisicos, 1) + random.sample(locais_geograficos, 2)
    random.shuffle(st.session_state.locais_cidade)

def mudar_tela(nova_tela):
    st.session_state.tela_atual = nova_tela

def iniciar_nova_partida(venceu_anterior=False):
    if venceu_anterior:
        st.session_state.casos_resolvidos += 1

    st.session_state.interpol_sexo = "---"
    st.session_state.interpol_cabelo = "---"
    st.session_state.interpol_olho = "---"
    st.session_state.interpol_detalhe = "---"

    # Agora a função recebe a chance_mentira também!
    patente, tamanho_rota, horas_restantes, enfrenta_chefe, chance_mentira = calcular_dificuldade(st.session_state.casos_resolvidos)
    
    if enfrenta_chefe:
        vilao = random.choice(banco_chefes) if random.choice([True, False]) else random.choice(banco_capangas)
    else:
        vilao = random.choice(banco_capangas)

    todas_cidades = list(mapa_mundi.keys())
    cidade_atual_setup = random.choice(todas_cidades)
    rota_fuga = [cidade_atual_setup]

    while len(rota_fuga) < tamanho_rota:
        opcoes = [c for c in mapa_mundi[rota_fuga[-1]]["conexoes"] if c not in rota_fuga]
        if not opcoes: break
        proxima = random.choice(opcoes)
        rota_fuga.append(proxima)

    st.session_state.patente = patente
    st.session_state.vilao = vilao
    st.session_state.rota_fuga = rota_fuga
    st.session_state.local_atual = rota_fuga[0]
    st.session_state.horas_restantes = horas_restantes
    st.session_state.chance_mentira = chance_mentira # Salvando a chance na memória
    st.session_state.mandado_ativo = None
    st.session_state.jogo_acabou = False
    st.session_state.mensagem_tela = ""
    st.session_state.venceu_atual = False
    st.session_state.artefato_roubado = random.choice(banco_artefatos)
    sortear_locais()
    mudar_tela("briefing")

# ==========================================
# 4. SETUP INICIAL DAS VARIÁVEIS DE SESSÃO
# ==========================================
if 'casos_resolvidos' not in st.session_state:
    st.session_state.casos_resolvidos = 0
if 'tela_atual' not in st.session_state:
    st.session_state.tela_atual = "inicio"
if 'nome_jogador' not in st.session_state:
    st.session_state.nome_jogador = ""
if 'artefato_roubado' not in st.session_state:
    st.session_state.artefato_roubado = ""
if 'exibir_aviso_suspeito' not in st.session_state:
    st.session_state.exibir_aviso_suspeito = False
if 'nome_temporario' not in st.session_state:
    st.session_state.nome_temporario = ""

if 'horas_restantes' not in st.session_state:
    iniciar_nova_partida()
    st.session_state.tela_atual = "inicio"

if st.session_state.nome_jogador == "":
    st.session_state.tela_atual = "inicio"

# ==========================================
# 5. GERENCIADOR DE TELAS
# ==========================================

# ----------------- TELA: INÍCIO -----------------
if st.session_state.tela_atual == "inicio":
    try:
        # Puxa o banner achatado da memória instantaneamente!
        st.image(carregar_banner()) 
    except:
        st.warning("Banner não encontrado.")
        
    st.markdown("<h1 style='text-align: center;'>Bem-vindo à DIE</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Divisão de Investigações Especiais</h4>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.info("Para acessar o painel confidencial, identifique-se.")
        
        if not st.session_state.exibir_aviso_suspeito:
            nome_digitado = st.text_input("Qual o seu nome, detetive?")
            
            if st.button("Identificar-se e Entrar", use_container_width=True):
                if nome_digitado.strip() == "":
                    st.error("Você precisa digitar um nome!")
                else:
                    nome_formatado = nome_digitado.strip().title()
                    nomes_bandidos_minusculos = [v["nome"].lower() for v in banco_suspeitos]
                    
                    if nome_digitado.strip().lower() in nomes_bandidos_minusculos:
                        st.session_state.nome_temporario = nome_formatado
                        st.session_state.exibir_aviso_suspeito = True
                        st.rerun()
                    else:
                        st.session_state.nome_jogador = nome_formatado
                        st.session_state.casos_resolvidos = 0
                        iniciar_nova_partida()
                        st.rerun()
        
        else:
            st.warning(f"Huuuum, {st.session_state.nome_temporario}... você tem o nome de um dos bandidos cadastrados no nosso banco de dados do mal. Isso é muito suspeito! 🤨")
            st.write("Deseja continuar com esse nome mesmo assim?")
            
            col_sim, col_nao = st.columns(2)
            with col_sim:
                if st.button("Sim, continuar", use_container_width=True):
                    st.session_state.nome_jogador = st.session_state.nome_temporario
                    st.session_state.casos_resolvidos = 0
                    st.session_state.exibir_aviso_suspeito = False
                    iniciar_nova_partida()
                    st.rerun()
            with col_nao:
                if st.button("Não, trocar de nome", use_container_width=True):
                    st.session_state.exibir_aviso_suspeito = False
                    st.session_state.nome_temporario = ""
                    st.rerun()

# ----------------- TELA: BRIEFING -----------------
elif st.session_state.tela_atual == "briefing":
    st.title("📁 Arquivo Confidencial - Novo Caso")
    st.write("---")
    
    col_texto, col_dados = st.columns([2, 1])
    
    with col_texto:
        st.markdown(f"### Olá, {st.session_state.nome_jogador}!")
        st.write(f"Vejo no sistema que sua patente atual é **{st.session_state.patente.upper()}**.")
        st.write("Temos uma emergência e precisamos das suas habilidades imediatas.")
        
        st.warning(f"**ALERTA DE ROUBO:**\nOcorreu um crime na cidade de **{st.session_state.local_atual.upper()}**. Suspeitamos que agentes da V.I.L.E roubaram **{st.session_state.artefato_roubado}** nas últimas horas.")
        st.write("O suspeito já iniciou a rota de fuga ao redor do mundo e você tem tempo limitado para interceptá-lo.")
        st.write("Você está pronto para liderar esta investigação?")
        
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            st.button("✅ Aceitar o Caso", on_click=mudar_tela, args=("jogo",), use_container_width=True)
        with col_b2:
            def recusar_caso():
                st.session_state.nome_jogador = ""
                st.session_state.tela_atual = "inicio"
            st.button("❌ Recusar e Sair", on_click=recusar_caso, use_container_width=True)
            
    with col_dados:
        st.metric(label="Casos Solucionados", value=st.session_state.casos_resolvidos)
        st.metric(label="Prazo Estipulado", value=f"{st.session_state.horas_restantes}h")

# ----------------- TELA: JOGO -----------------
elif st.session_state.tela_atual == "jogo":
    try:
        imagem_original = Image.open("banner.jpg")
        imagem_achatada = imagem_original.resize((1200, 400))
        st.image(imagem_achatada)
    except:
        st.warning("Banner não encontrado.")

    col_header1, col_header2 = st.columns([3, 1])
    with col_header1:
        st.markdown(f"### Detetive: {st.session_state.nome_jogador} | Operação Ativa")
    with col_header2:
        st.metric(label="Casos Resolvidos", value=st.session_state.casos_resolvidos)
        st.caption(f"Patente: **{st.session_state.patente.upper()}**")

    st.divider()

    if st.session_state.horas_restantes <= 0 and not st.session_state.jogo_acabou:
        st.session_state.mensagem_tela = f"⏰ O TEMPO ACABOU! O vilão escapou com {st.session_state.artefato_roubado}. O culpado era: {st.session_state.vilao['nome']}."
        st.session_state.jogo_acabou = True
        st.session_state.venceu_atual = False

    st.sidebar.header("💻 Computador da Interpol")
    st.sidebar.write("Cruze os dados para emitir o mandado. Custa 1h.")

    p_sex = st.sidebar.selectbox("Sexo", ["---", "F", "M"], key="interpol_sexo")
    p_cab = st.sidebar.selectbox("Cabelo", ["---", "Castanho", "Preto", "Loiro", "Ruivo", "Branco"], key="interpol_cabelo")
    p_olh = st.sidebar.selectbox("Cor dos Olhos", ["---", "Castanho", "Amarelo", "Vermelho", "Azul"], key="interpol_olho")
    p_det = st.sidebar.selectbox("Detalhe", ["---", "Jóia", "Tatuagem", "Cicatriz", "Tapa olho"], key="interpol_detalhe")

    if st.sidebar.button("🚨 Emitir Mandado", disabled=st.session_state.jogo_acabou):
        st.session_state.horas_restantes -= 1
        
        sexo_filtro = p_sex if p_sex != "---" else None
        cabelo_filtro = p_cab if p_cab != "---" else None
        olho_filtro = p_olh if p_olh != "---" else None
        detalhe_filtro = p_det if p_det != "---" else None

        filtrados = [s for s in banco_suspeitos if 
                     (sexo_filtro is None or s["sexo"] == sexo_filtro) and
                     (cabelo_filtro is None or s["cabelo"] == cabelo_filtro) and
                     (olho_filtro is None or s["olho"] == olho_filtro) and
                     (detalhe_filtro is None or s["detalhes"] == detalhe_filtro)]
        
        if len(filtrados) == 1:
            st.session_state.mandado_ativo = filtrados[0]["nome"]
            st.sidebar.success(f"🚨 MANDADO EMITIDO: {filtrados[0]['nome'].upper()}")
            st.sidebar.image(filtrados[0]["imagem"], caption=f"FOTO ARQUIVO: {filtrados[0]['nome']}")
        else:
            st.session_state.mandado_ativo = None
            st.sidebar.warning(f"Inconclusivo. {len(filtrados)} suspeitos na lista.")
            for s in filtrados:
                st.sidebar.caption(f"- {s['nome']}")

    st.subheader(f"📍 Local Atual: {st.session_state.local_atual.upper()}")

    url_imagem_cidade = mapa_mundi[st.session_state.local_atual]["imagem"]
    try:
        st.image(url_imagem_cidade, use_container_width=True)
    except:
        st.warning(f"Imagem da cidade não encontrada: {url_imagem_cidade}")

    st.progress(max(0, st.session_state.horas_restantes) / 120) 
    st.write(f"⏳ Horas Restantes: **{st.session_state.horas_restantes}h**")

    # ==========================================
    # LÓGICA DO JOGO RODANDO (NÃO ACABOU)
    # ==========================================
    if not st.session_state.jogo_acabou:
        
        # AQUI APARECEM AS MENSAGENS DAS TESTEMUNHAS E VIAGENS!
        if st.session_state.mensagem_tela:
            st.info(st.session_state.mensagem_tela)

        col_inv, col_via = st.columns(2)
        
        with col_inv:
            st.markdown("### 🔍 Investigar (2h)")
            for local in st.session_state.locais_cidade:
                if st.button(f"🏢 Ir para: {local}"):
                    st.session_state.horas_restantes -= 2
                    
                    if st.session_state.local_atual in st.session_state.rota_fuga:
                        indice = st.session_state.rota_fuga.index(st.session_state.local_atual)
                        
                        if indice == len(st.session_state.rota_fuga) - 1:
                            st.session_state.mensagem_tela = f"🕵️ Você invadiu o(a) {local} e achou o esconderijo do vilão!"
                            st.session_state.jogo_acabou = True
                            
                            if st.session_state.mandado_ativo == st.session_state.vilao["nome"]:
                                st.session_state.mensagem_tela += f"\n🎉 PARABÉNS! Você recuperou {st.session_state.artefato_roubado} e prendeu {st.session_state.vilao['nome']} com sucesso!"
                                st.session_state.venceu_atual = True
                                st.balloons()
                            else:
                                st.session_state.mensagem_tela += "\n❌ O vilão escapou! A polícia não tinha um mandado de prisão válido no nome dele."
                                st.session_state.venceu_atual = False
                                
                            st.rerun()
                        else:
                            proximo_destino = st.session_state.rota_fuga[indice + 1]
                            
                            # ROLA O DADO: É mentiroso ou testemunha real?
                            sorteio = random.random()
                            
                            if sorteio < st.session_state.chance_mentira:
                                # ====== COMPARSA MENTIROSO ======
                                
                                # Frases que dão a dica de que ele está mentindo!
                                comparsas_frases = [
                                    f"Um homem no(a) {local} gaguejou:",
                                    f"Uma mulher falou apressadamente:",
                                    f"Um sujeito com um sorriso forçado tentou te despistar:",
                                    f"Alguém olhando para os lados falou:",
                                    f"Um funcionário passando rápido declarou:",
                                    f"Uma pessoa guardando um maço de dinheiro no bolso disse:"
                                ]
                                intro_mentirosa = random.choice(comparsas_frases)
                                
                                if local in locais_fisicos:
                                    # Pega um vilão diferente para dar a dica física errada
                                    vilao_falso = random.choice([v for v in banco_suspeitos if v["nome"] != st.session_state.vilao["nome"]])
                                    dicas_erradas = [
                                        f"'E-eu tenho quase certeza que vi alguém do sexo {vilao_falso['sexo']}.'",
                                        f"'Se não me engano, a pessoa tinha cabelo {vilao_falso['cabelo']}...'",
                                        f"'Olha, eu reparei muito nos olhos, acho que eram de cor {vilao_falso['olho']}.'"
                                    ]
                                    dica_texto = random.choice(dicas_erradas)
                                else:
                                    # Pega uma cidade diferente para dar a dica geográfica errada
                                    cidades_erradas = [c for c in mapa_mundi.keys() if c != proximo_destino]
                                    cidade_falsa = random.choice(cidades_erradas)
                                    dica_texto = f"'{random.choice(mapa_mundi[cidade_falsa]['fatos'])}'"

                                st.session_state.mensagem_tela = f"{intro_mentirosa} {dica_texto}"
                                
                            else:
                                # ====== TESTEMUNHA REAL (A VERDADE) ======
                                if local in locais_fisicos: 
                                    dicas_fisicas = [
                                        f"Notei que era uma pessoa do sexo {st.session_state.vilao['sexo']}.",
                                        f"A pessoa tinha cabelo {st.session_state.vilao['cabelo']}.",
                                        f"Reparei que a pessoa tinha olhos de cor {st.session_state.vilao['olho']}."
                                    ]
                                    if st.session_state.vilao["detalhes"] == "---":
                                        dicas_fisicas.append("Não notei nenhuma joia, tatuagem, cicatriz ou tapa olho.")
                                    else:
                                        dicas_fisicas.append(f"Me chamou a atenção que a pessoa tinha um(a) {st.session_state.vilao['detalhes']}.")
                                        
                                    dica_texto = random.choice(dicas_fisicas)
                                else: 
                                    dica_texto = random.choice(mapa_mundi[proximo_destino]["fatos"])
                                    
                                st.session_state.mensagem_tela = f"Testemunha no(a) {local} relatou: '{dica_texto}'"

        with col_via:
            st.markdown("### ✈️ Viajar (8h)")
            destinos = mapa_mundi[st.session_state.local_atual]["conexoes"]
            
            for dest in destinos:
                if st.button(f"🛫 Voo para {dest}"):
                    st.session_state.local_atual = dest
                    st.session_state.horas_restantes -= 8
                    st.session_state.mensagem_tela = f"Você viajou para {dest}."
                    sortear_locais() 
                    st.rerun()

        st.divider()
        def abandonar_caso():
            st.session_state.jogo_acabou = True
            st.session_state.venceu_atual = False
            st.session_state.nome_jogador = ""
            st.session_state.mensagem_tela = f"Você entregou seu distintivo e abandonou a investigação. O culpado era: {st.session_state.vilao['nome']}."
            
        st.button("🚪 Abandonar o Caso (Entregar Distintivo)", on_click=abandonar_caso)

    # ==========================================
    # TELA FINAL DA MISSÃO
    # ==========================================

    else:
        st.divider()
        
        # 1. CRIAMOS O "TELEVISOR" MÁGICO (O espaço exato que vai trocar de conteúdo)
        televisor = st.empty()
        
        # Vamos pegar a mensagem de vitória ou derrota (cortando a frase "você invadiu o aeroporto...")
        partes_msg = st.session_state.mensagem_tela.split('\n')
        texto_resultado_final = partes_msg[-1] 

        # 2. SE HOUVE INVASÃO (E a animação ainda não rodou nesta rodada)
        if "achou o esconderijo" in st.session_state.mensagem_tela:
            
            # LIGA O TELEVISOR NO CANAL 1: O POLICIAL
            with televisor.container():
                # Título que vai sumir depois
                st.markdown("<h3 style='text-align: center; color: orange;'>🚨 INVASÃO EM ANDAMENTO... 🚨</h3>", unsafe_allow_html=True)
                
                # O GIF no centro
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    try:
                        st.image("policial.gif", use_container_width=True) 
                    except:
                        st.warning("⚠️ Arquivo 'policial.gif' não encontrado.")
                        
                # O TEMPO DE SUSPENSE
                time.sleep(7) 

            # Troca a frase para a animação não rodar duas vezes se o navegador piscar
            st.session_state.mensagem_tela = st.session_state.mensagem_tela.replace("achou o esconderijo", "covil localizado")

        # 3. LIGA O TELEVISOR NO CANAL 2: O VILÃO E O RESULTADO (Sobrescreve exatamente no mesmo lugar!)
        with televisor.container():
            
            # A. Coloca o texto final (Parabéns ou O vilão escapou) no mesmo lugar onde estava "INVASÃO EM ANDAMENTO"
            if st.session_state.venceu_atual:
                st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>{texto_resultado_final}</h3>", unsafe_allow_html=True)
                gif_vilao = st.session_state.vilao.get("imagem_preso", st.session_state.vilao["imagem"])
                legenda = f"VILÃO CAPTURADO: {st.session_state.vilao['nome'].upper()}"
            else:
                st.markdown(f"<h3 style='text-align: center; color: #FF4B4B;'>{texto_resultado_final}</h3>", unsafe_allow_html=True)
                gif_vilao = st.session_state.vilao.get("imagem_fuga", st.session_state.vilao["imagem"])
                legenda = f"VILÃO FORAGIDO: {st.session_state.vilao['nome'].upper()}"

            # B. Coloca o GIF do vilão no mesmo espaço central
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                try:
                    st.image(gif_vilao, use_container_width=True, caption=legenda)
                except:
                    st.warning(f"⚠️ Imagem não encontrada: {gif_vilao}")
            
            # C. Botão para jogar de novo aparece embaixo do vilão
            st.write("---")
            st.button("🚔 Solicitar Novo Caso à DIE", on_click=iniciar_nova_partida, kwargs={"venceu_anterior": st.session_state.venceu_atual}, use_container_width=True)
