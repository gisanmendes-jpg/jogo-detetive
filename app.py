import streamlit as st
import random

# ==========================================
# 1. BANCOS DE DADOS COMPLETOS
# ==========================================
banco_suspeitos = [
    {"nome": "Gabi Aura Monster", "sexo": "F", "cabelo": "Castanho", "detalhes": "Jóia"},
    {"nome": "Denji",  "sexo": "M", "cabelo": "Loiro", "detalhes": "Tapa olho"},
    {"nome": "Nana",  "sexo": "F", "cabelo": "Ruivo", "detalhes": "Jóia"},
    {"nome": "Gisa Estrela",  "sexo": "F", "cabelo": "Castanho", "detalhes": "Tatuagem"},
    {"nome": "Makima",  "sexo": "F", "cabelo": "Ruivo", "detalhes": "Tatuagem"},
    {"nome": "Scarlet",  "sexo": "F", "cabelo": "Preto", "detalhes": "Cicatriz"},
    {"nome": "Ryan",  "sexo": "M", "cabelo": "Preto", "detalhes": "Jóia"},
    {"nome": "Mayah",  "sexo": "F", "cabelo": "Preto", "detalhes": "Tapa olho"},
    {"nome": "Elsa",  "sexo": "F", "cabelo": "Preto", "detalhes": "Jóia"},
    {"nome": "Douma",  "sexo": "M", "cabelo": "Loiro", "detalhes": "Tatuagem"},
    {"nome": "Muzan",  "sexo": "M", "cabelo": "Branco", "detalhes": "Cicatriz"},
    {"nome": "Haru",  "sexo": "M", "cabelo": "Branco", "detalhes": "Tapa olho"},
    {"nome": "Roger",  "sexo": "M", "cabelo": "Preto", "detalhes": "Tatuagem"},
    {"nome": "Clara",  "sexo": "F", "cabelo": "Preto", "detalhes": "Cicatriz"}
]

mapa_mundi = {
    "Rio de Janeiro": {
        "conexoes": ["Lima", "Nova York", "Tóquio"],
        "fatos": ["O suspeito queria ver o Cristo Redentor.", "Trocou dinheiro por Reais."]
    },
    "Lima": {
        "conexoes": ["Rio de Janeiro", "Nova York", "Cidade do México"],
        "fatos": ["Queria conhecer o estádio onde o Flamengo foi campeão.", "Perguntou sobre Machu Picchu."]
    },
    "Tóquio": {
        "conexoes": ["Rio de Janeiro", "Nova York", "Londres"],
        "fatos": ["Estava estudando japonês.", "Mencionou o Monte Fuji."]
    },
    "Nova York": {
        "conexoes": ["Rio de Janeiro", "Lima", "Tóquio", "Paris", "Cidade do México"],
        "fatos": ["Perguntou sobre a Estátua da Liberdade.", "Tinha um mapa de Manhattan."]
    },
    "Paris": {
        "conexoes": ["Nova York", "Tóquio", "Londres"],
        "fatos": ["Disse que gostaria de ver a torre Eiffel.", "Tinha uma bandeira com as cores azul, branca e vermelha."]
    },
    "Londres": {
        "conexoes": ["Paris", "Tóquio", "Cidade do México"],
        "fatos": ["Estava tomando chá preto.", "Queria ajustar o relógio para ver o Big Ben."]
    },
    "Cidade do México": {
        "conexoes": ["Lima", "Londres", "Nova York"],
        "fatos": ["Comeu muitos tacos.", "Tinha um sombreiro na mala."]
    }
}

locais_fisicos = ["Hotel", "Clube Esportivo", "Restaurante", "Cafeteria", "Spa"]
locais_geograficos = ["Banco", "Aeroporto", "Porto", "Livraria", "Mercado Central", "Museu", "Agência de Turismo"]

# ==========================================
# 2. INICIALIZAÇÃO DO ESTADO
# ==========================================
def iniciar_novo_jogo():
    st.session_state.vilao = random.choice(banco_suspeitos)
    todas_cidades = list(mapa_mundi.keys())
    
    # ROTA LONGA (5 cidades) para dar tempo de investigar
    tamanho_rota = 5
    cidade_atual_setup = random.choice(todas_cidades)
    rota_fuga = [cidade_atual_setup]

    while len(rota_fuga) < tamanho_rota:
        opcoes = [c for c in mapa_mundi[rota_fuga[-1]]["conexoes"] if c not in rota_fuga]
        if not opcoes: 
            break
        proxima = random.choice(opcoes)
        rota_fuga.append(proxima)
    
    st.session_state.rota_fuga = rota_fuga
    st.session_state.local_atual = rota_fuga[0]
    st.session_state.horas_restantes = 100 # Tempo restaurado para 100h
    st.session_state.mandado_ativo = None
    st.session_state.mensagem_tela = ""
    st.session_state.jogo_acabou = False
    
    sortear_locais()

def sortear_locais():
    # Sorteia sempre 1 local físico e 2 geográficos
    st.session_state.locais_cidade = random.sample(locais_fisicos, 1) + random.sample(locais_geograficos, 2)
    random.shuffle(st.session_state.locais_cidade)

if 'horas_restantes' not in st.session_state:
    iniciar_novo_jogo()

# ==========================================
# 3. INTERFACE E LÓGICA
# ==========================================
st.set_page_config(page_title="Agência ACME", page_icon="🕵️")
st.title("🕵️ Agência ACME")

# Fim de Jogo por Tempo
if st.session_state.horas_restantes <= 0 and not st.session_state.jogo_acabou:
    st.session_state.mensagem_tela = f"⏰ O TEMPO ACABOU! O vilão escapou. O culpado era: {st.session_state.vilao['nome']}."
    st.session_state.jogo_acabou = True

# --- BARRA LATERAL: INTERPOL ---
st.sidebar.header("💻 Computador da Interpol")
st.sidebar.write("Cruze os dados para emitir o mandado. Custa 1h.")

# Menus Suspensos da Interpol
p_sex = st.sidebar.selectbox("Sexo", ["---", "F", "M"])
p_cab = st.sidebar.selectbox("Cabelo", ["---", "Castanho", "Preto", "Loiro", "Ruivo", "Branco"])
p_det = st.sidebar.selectbox("Detalhe", ["---", "Jóia", "Tatuagem", "Cicatriz", "Tapa olho"])

if st.sidebar.button("🚨 Emitir Mandado", disabled=st.session_state.jogo_acabou):
    st.session_state.horas_restantes -= 1
    
    filtrados = [s for s in banco_suspeitos if 
                 (p_sex == "---" or s["sexo"] == p_sex) and
                 (p_cab == "---" or s["cabelo"] == p_cab) and
                 (p_det == "---" or s["detalhes"] == p_det)]
    
    if len(filtrados) == 1:
        st.session_state.mandado_ativo = filtrados[0]["nome"]
        st.sidebar.success(f"🚨 MANDADO EMITIDO: {filtrados[0]['nome'].upper()}")
    else:
        st.session_state.mandado_ativo = None
        st.sidebar.warning(f"Inconclusivo. {len(filtrados)} suspeitos na lista.")
        for s in filtrados:
            st.sidebar.caption(f"- {s['nome']}") # Mostra quem sobrou na lista!

# --- TELA PRINCIPAL ---
st.subheader(f"📍 Local Atual: {st.session_state.local_atual.upper()}")
st.progress(max(0, st.session_state.horas_restantes) / 100) 
st.write(f"⏳ Horas Restantes: **{st.session_state.horas_restantes}h**")

# Exibe mensagens (dicas de testemunhas ou alertas de vitória/derrota)
if st.session_state.mensagem_tela:
    st.info(st.session_state.mensagem_tela)

if not st.session_state.jogo_acabou:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Investigar (2h)")
        for local in st.session_state.locais_cidade:
            if st.button(f"🏢 Ir para: {local}"):
                st.session_state.horas_restantes -= 2
                
                if st.session_state.local_atual in st.session_state.rota_fuga:
                    indice = st.session_state.rota_fuga.index(st.session_state.local_atual)
                    
                    # Se chegou na última cidade
                    if indice == len(st.session_state.rota_fuga) - 1:
                        st.session_state.mensagem_tela = f"🕵️ Você invadiu o(a) {local} e achou o esconderijo do vilão!"
                        
                        if st.session_state.mandado_ativo == st.session_state.vilao["nome"]:
                            st.session_state.mensagem_tela += f"\n🎉 PARABÉNS! Você prendeu {st.session_state.vilao['nome']} com sucesso!"
                            st.balloons()
                        else:
                            st.session_state.mensagem_tela += "\n❌ O vilão escapou! A polícia não tinha um mandado de prisão válido no nome dele."
                        st.session_state.jogo_acabou = True
                        st.rerun()
                        
                    else:
                        proximo_destino = st.session_state.rota_fuga[indice + 1]
                        
                        # Dica Física (Locais Físicos)
                        if local in locais_fisicos:
                            dicas_fisicas = [
                                f"Notei que era uma pessoa do sexo {st.session_state.vilao['sexo']}.",
                                f"A pessoa tinha cabelo {st.session_state.vilao['cabelo']}."
                            ]
                            if st.session_state.vilao["detalhes"] == "---":
                                dicas_fisicas.append("Não notei nenhuma joia, tatuagem, cicatriz ou tapa olho.")
                            else:
                                dicas_fisicas.append(f"Me chamou a atenção que a pessoa tinha um(a) {st.session_state.vilao['detalhes']}.")
                                
                            dica = random.choice(dicas_fisicas)
                        
                        # Dica Geográfica (Aeroporto, Banco, etc)
                        else:
                            dica = random.choice(mapa_mundi[proximo_destino]["fatos"])
                            
                        st.session_state.mensagem_tela = f"Testemunha no(a) {local}: '{dica}'"
                else:
                    st.session_state.mensagem_tela = f"Testemunha no(a) {local}: 'Não vi ninguém suspeito por aqui.'"
                st.rerun()

    with col2:
        st.markdown("### ✈️ Viajar (8h)")
        destinos = mapa_mundi[st.session_state.local_atual]["conexoes"]
        
        for dest in destinos:
            if st.button(f"🛫 Voo para {dest}"):
                st.session_state.local_atual = dest
                st.session_state.horas_restantes -= 8
                st.session_state.mensagem_tela = f"Você viajou para {dest}."
                sortear_locais()
                st.rerun()
else:
    if st.button("🔄 Jogar Novamente"):
        iniciar_novo_jogo()
        st.rerun()
