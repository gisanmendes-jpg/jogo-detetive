import streamlit as st
import random

# ==========================================
# 1. BANCOS DE DADOS
# ==========================================
banco_suspeitos = [
    {"nome": "Gabi Aura Monster", "sexo": "F", "cabelo": "Castanho", "detalhes": "Jóia"},
    {"nome": "Denji",  "sexo": "M", "cabelo": "Loiro", "detalhes": "Tapa olho"},
    {"nome": "Nana",  "sexo": "F", "cabelo": "Ruivo", "detalhes": "Jóia"},
    {"nome": "Makima",  "sexo": "F", "cabelo": "Ruivo", "detalhes": "Tatuagem"},
    {"nome": "Douma",  "sexo": "M", "cabelo": "Loiro", "detalhes": "Tatuagem"},
    {"nome": "Muzan",  "sexo": "M", "cabelo": "Branco", "detalhes": "Cicatriz"}
] # Resumido para o exemplo, você pode colocar todos!

mapa_mundi = {
    "Rio de Janeiro": {"conexoes": ["Lima", "Nova York"], "fatos": ["Queria ver o Cristo.", "Tinha Reais."]},
    "Lima": {"conexoes": ["Rio de Janeiro", "Nova York"], "fatos": ["Queria ver Machu Picchu.", "Comeu Ceviche."]},
    "Nova York": {"conexoes": ["Rio de Janeiro", "Lima"], "fatos": ["Foi para Manhattan.", "Tinha Dólares."]}
}

locais_fisicos = ["Hotel", "Spa", "Restaurante"]
locais_geograficos = ["Banco", "Aeroporto", "Museu"]

# ==========================================
# 2. INICIALIZAÇÃO DO ESTADO (O SETUP)
# ==========================================
# Esta função roda APENAS UMA VEZ quando o jogo abre ou é reiniciado
def iniciar_novo_jogo():
    st.session_state.vilao = random.choice(banco_suspeitos)
    todas_cidades = list(mapa_mundi.keys())
    
    # Rota simples de 3 cidades para este exemplo
    cidade_1 = random.choice(todas_cidades)
    opcoes_2 = [c for c in mapa_mundi[cidade_1]["conexoes"]]
    cidade_2 = random.choice(opcoes_2)
    cidade_3 = [c for c in mapa_mundi[cidade_2]["conexoes"] if c != cidade_1][0]
    
    st.session_state.rota_fuga = [cidade_1, cidade_2, cidade_3]
    st.session_state.local_atual = cidade_1
    st.session_state.horas_restantes = 72
    st.session_state.mandado_ativo = None
    st.session_state.mensagem_tela = ""
    st.session_state.jogo_acabou = False
    
    # Sorteia os locais da cidade atual para não mudarem a cada clique
    sortear_locais()

def sortear_locais():
    st.session_state.locais_cidade = random.sample(locais_fisicos, 1) + random.sample(locais_geograficos, 2)
    random.shuffle(st.session_state.locais_cidade)

# Se o jogo ainda não começou, inicializa as variáveis
if 'horas_restantes' not in st.session_state:
    iniciar_novo_jogo()

# ==========================================
# 3. INTERFACE E LÓGICA (O "GAME LOOP")
# ==========================================
st.title("🕵️ Agência ACME")

# Checagem de Fim de Jogo por Tempo
if st.session_state.horas_restantes <= 0 and not st.session_state.jogo_acabou:
    st.session_state.mensagem_tela = f"⏰ O TEMPO ACABOU! O vilão escapou. Era {st.session_state.vilao['nome']}."
    st.session_state.jogo_acabou = True

# --- BARRA LATERAL: INTERPOL ---
st.sidebar.header("💻 Computador da Interpol")
st.sidebar.write("Cruze os dados para emitir o mandado.")

# Menus Suspensos!
p_sex = st.sidebar.selectbox("Sexo", ["---", "F", "M"])
p_cab = st.sidebar.selectbox("Cabelo", ["---", "Castanho", "Preto", "Loiro", "Ruivo", "Branco"])
p_det = st.sidebar.selectbox("Detalhe", ["---", "Jóia", "Tatuagem", "Cicatriz", "Tapa olho"])

if st.sidebar.button("🚨 Buscar no Banco", disabled=st.session_state.jogo_acabou):
    st.session_state.horas_restantes -= 1
    
    # Filtra os suspeitos com base nas escolhas
    filtrados = [s for s in banco_suspeitos if 
                 (p_sex == "---" or s["sexo"] == p_sex) and
                 (p_cab == "---" or s["cabelo"] == p_cab) and
                 (p_det == "---" or s["detalhes"] == p_det)]
    
    if len(filtrados) == 1:
        st.session_state.mandado_ativo = filtrados[0]["nome"]
        st.sidebar.success(f"MANDADO EMITIDO PARA: {filtrados[0]['nome'].upper()}")
    else:
        st.session_state.mandado_ativo = None
        st.sidebar.warning(f"Inconclusivo. {len(filtrados)} suspeitos batem com a descrição.")

# --- TELA PRINCIPAL ---
st.subheader(f"📍 Local Atual: {st.session_state.local_atual.upper()}")
st.progress(st.session_state.horas_restantes / 72) # Barra de progresso visual para o tempo!
st.write(f"⏳ Horas Restantes: **{st.session_state.horas_restantes}h**")

# Exibe mensagens (dicas de testemunhas ou alertas)
if st.session_state.mensagem_tela:
    st.info(st.session_state.mensagem_tela)

if not st.session_state.jogo_acabou:
    # Divide a tela em duas colunas (Ação de Investigar vs Viajar)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Investigar (2h)")
        for local in st.session_state.locais_cidade:
            if st.button(f"Ir para: {local}"):
                st.session_state.horas_restantes -= 2
                
                # Lógica de encontrar o vilão
                if st.session_state.local_atual in st.session_state.rota_fuga:
                    indice = st.session_state.rota_fuga.index(st.session_state.local_atual)
                    
                    if indice == len(st.session_state.rota_fuga) - 1:
                        if st.session_state.mandado_ativo == st.session_state.vilao["nome"]:
                            st.session_state.mensagem_tela = f"🎉 PARABÉNS! Você prendeu {st.session_state.vilao['nome']} com sucesso!"
                            st.balloons() # Animação de balões do Streamlit
                        else:
                            st.session_state.mensagem_tela = "❌ Você achou o vilão, mas ele fugiu por falta de mandado!"
                        st.session_state.jogo_acabou = True
                        st.rerun() # Atualiza a tela imediatamente
                        
                    else:
                        # Dar a dica
                        if local in locais_fisicos:
                            dica = f"O suspeito tem cabelo {st.session_state.vilao['cabelo']}."
                        else:
                            proximo_destino = st.session_state.rota_fuga[indice + 1]
                            dica = random.choice(mapa_mundi[proximo_destino]["fatos"])
                        st.session_state.mensagem_tela = f"Testemunha no {local}: '{dica}'"
                else:
                    st.session_state.mensagem_tela = f"Testemunha no {local}: 'Não vi ninguém suspeito por aqui.'"
                st.rerun() # Atualiza a tela para descontar as horas

    with col2:
        st.markdown("### ✈️ Viajar (8h)")
        destinos = mapa_mundi[st.session_state.local_atual]["conexoes"]
        
        for dest in destinos:
            if st.button(f"Voo para {dest}"):
                st.session_state.local_atual = dest
                st.session_state.horas_restantes -= 8
                st.session_state.mensagem_tela = f"Você viajou para {dest}."
                sortear_locais() # Sorteia novos locais para a nova cidade
                st.rerun()
else:
    # Jogo Acabou - Botão para reiniciar
    if st.button("🔄 Jogar Novamente"):
        iniciar_novo_jogo()
        st.rerun()
