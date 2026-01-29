import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
from datetime import datetime

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Odonto Master 360", layout="wide")

# Lógica de Tempo (Reset Binance 00:00 UTC)
st.sidebar.caption(f"🕒 Sistema Sincronizado (UTC): {datetime.utcnow().strftime('%H:%M')}")

# --- MENU LATERAL ---
with st.sidebar:
    st.title("🦷 ODONTO MASTER")
    aba = st.radio("NAVEGAÇÃO", 
                    ["📋 Tarefas/Agenda", "💬 Chat Interno", "💰 Cobranças", "🚀 Vendas", "📉 Gastos", "🔑 ADM", "🖼️ QR Code"])

# --- 📋 ABA: AGENDA DE TAREFAS ---
if aba == "📋 Tarefas/Agenda":
    st.title("📋 Agenda da Gerente")
    nova_tarefa = st.text_input("Adicionar nova tarefa do dia:")
    if st.button("Adicionar"):
        st.success("Tarefa salva na planilha!") # Aqui ligaremos ao Sheets dps
    
    st.write("---")
    st.checkbox("Confirmar agendamentos de amanhã")
    st.checkbox("Conferir fechamento do caixa")
    st.checkbox("Reposição de estoque de luvas/máscaras")

# --- 💬 ABA: CHAT / NOTAS ---
elif aba == "💬 Chat Interno":
    st.title("💬 Mural de Avisos")
    msg = st.text_area("Deixe um aviso para a equipe:")
    if st.button("Postar Aviso"):
        st.info("Aviso postado com sucesso!")

# --- 🖼️ ABA: GERADOR DE QR CODE ---
elif aba == "🖼️ QR Code":
    st.title("🖼️ Gerador de QR Code")
    link = st.text_input("Cole o link ou Chave PIX aqui:", "https://")
    if link:
        img = qrcode.make(link)
        buf = BytesIO()
        img.save(buf)
        st.image(buf)
        st.download_button("Baixar QR Code", buf, "qrcode_odonto.png")

# --- 📉 ABA: GASTOS ---
elif aba == "📉 Gastos":
    st.title("📉 Controle de Despesas")
    col1, col2 = st.columns(2)
    col1.text_input("Descrição do Gasto")
    col2.number_input("Valor (R$)", min_value=0.0)
    st.button("Lançar Despesa")

# --- 🔑 ABA: ADM ---
elif aba == "🔑 ADM":
    st.title("🔑 Painel Administrativo")
    st.metric("Lucro Líquido Estimado", "R$ 8.450,00", "+12%")
    # Aqui faremos o cálculo Vendas - Gastos
