import streamlit as st

st.set_page_config(
    page_title="Mapa Cultural",
    page_icon="🗺️"
)

st.title("🗺️ Mapa Cultural")

st.write("Descubra e registre o interesse cultural da sua região.")

pesquisa = st.text_input(
    "🔎 O que você quer pesquisar?",
    placeholder="Ex: comida típica de Nossa Senhora do Socorro"
)

if pesquisa:
    st.success(f"Você pesquisou: {pesquisa}")

st.subheader("📊 Interesse cultural")

col1, col2, col3 = st.columns(3)

col1.metric("🍲 Gastronomia", "120")
col2.metric("🎵 Música", "75")
col3.metric("🎭 Festas", "95")
