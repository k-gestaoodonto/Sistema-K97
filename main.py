
import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Odonto Excellence 360", layout="wide")

# --- LÓGICA DE RESET VWAP / BINANCE (00:00 UTC) ---
# Sistema configurado para reset automático conforme solicitado
agora_utc = datetime.utcnow()
st.sidebar.caption(f"Reset Sistema (UTC): 00:00 | Atual: {agora_utc.strftime('%H:%M')}")

# --- LAYOUT E ESTILO ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #0E1117; color: white; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; }
    .metric-card {
        background-color: #f0f2f6; padding: 15px; border-radius: 10px;
        text-align: center; border-left: 5px solid #0068c9;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
with st.sidebar:
    st.title("🦷 Odonto 360")
    aba = st.radio("O QUE DESEJA FAZER?", 
                    ["📊 Dashboard", "💰 Cobrança", "🚀 Vendas (Novos)", "📅 Agenda"])
    
    st.divider()
    if st.button("🔄 Sincronizar Planilha"):
        st.cache_data.clear()
        st.success("Dados Atualizados!")

# --- FUNÇÃO SIMULADA DE DADOS (Depois conectamos sua Planilha real) ---
def carregar_dados():
    # Aqui depois trocamos pelo link do seu Google Sheets
    return pd.DataFrame({
        'Nome': ['João Exemplo', 'Maria Teste'],
        'Telefone': ['5511999999999', '5511888888888'],
        'Status': ['Atrasado', 'Interessado']
    })

df = carregar_dados()

# --- CONTEÚDO DAS ABAS ---
if aba == "📊 Dashboard":
    st.title("Bem-vinda, Gerente!")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><b>Dívidas Ativas</b><br>R$ 12.450</div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><b>Novos Leads</b><br>8 Hoje</div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><b>Conversão</b><br>15%</div>', unsafe_allow_html=True)

elif aba == "💰 Cobrança":
    st.title("💸 Recuperação de Crédito")
    for i, row in df.iterrows():
        col1, col2 = st.columns([3, 1])
        col1.write(f"👤 {row['Nome']} - {row['Telefone']}")
        link = f"https://wa.me/{row['Telefone']}?text=Olá%20{row['Nome']},%20temos%20uma%20pendência..."
        col2.markdown(f"[![Enviar](https://img.shields.io/badge/ENVIAR-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)]({link})")

elif aba == "🚀 Vendas (Novos)":
    st.title("🎯 Prospecção de Novos Clientes")
    st.info("Aqui aparecerão os contatos que vieram dos seus anúncios.")

elif aba == "📅 Agenda":
    st.title("⏰ Confirmação de Consultas")
    st.write("Mande lembretes para evitar faltas amanhã.")

