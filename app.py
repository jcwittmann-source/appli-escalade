import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Coach Escalade", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ffcc00; color: black; height: 3em; width: 100%;
        border-radius: 10px; border: none; font-weight: bold; font-size: 18px;
    }
    .desc { font-size: 14px; color: #666; font-style: italic; margin-bottom: 10px; }
    .log { padding: 5px; border-bottom: 1px solid #eee; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- MÉMOIRE DE LA SESSION ---
if 'page' not in st.session_state:
    st.session_state.page = 'Accueil'
if 'historique' not in st.session_state:
    st.session_state.historique = []

# --- FONCTION CHRONO + LOG ---
def lancer_chrono(secondes, nom):
    placeholder = st.empty()
    barre = st.progress(0)
    for i in range(secondes):
        restant = secondes - i
        placeholder.metric("Temps restant", f"{restant}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    placeholder.empty()
    barre.empty()
    st.success(f"Terminé : {nom}")
    # Ajout à l'historique
    heure = datetime.now().strftime("%H:%M")
    st.session_state.historique.insert(0, f"{heure} - {nom} ({secondes}s)")

# --- PAGES ---
if st.session_state.page == 'Accueil':
    st.title("🧗 Coach Perso : Objectif Bloc")
    
    if st.button("💪 ENTRAÎNEMENT 1 : Traction & Grip"):
        st.session_state.page = 'Jour 1'; st.rerun()
    if st.button("🦵 ENTRAÎNEMENT 2 : Gainage & Poussée"):
        st.session_state.page = 'Jour 2'; st.rerun()
    if st.button("🖐️ ENTRAÎNEMENT 3 : Bureau (Planche)"):
        st.session_state.page = 'Jour 3'; st.rerun()

    st.divider()
    st.subheader("📜 Historique de la séance")
    if not st.session_state.historique:
        st.write("Rien pour l'instant. Allez, au boulot !")
    else:
        for item in st.session_state.historique:
            st.markdown(f"<div class='log'>✅ {item}</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Jour 1':
    st.header("💪 Jour 1 : Dos & Bras")
    st.subheader("1. Tractions (4 x 8)")
    st.subheader("2. Rowing unilatéral (3 x 10)")
    st.subheader("3. Dead Hang (3 x 30s)")
    if st.button("Lancer Chrono 30s"):
        lancer_chrono(30, "Dead Hang")
    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Jour 2 : Abdos & Cuisses")
    st.subheader("1. Gobelet Squat (4 x 12)")
    st.subheader("2. Planche dynamique (3 x 45s)")
    if st.button("Lancer Chrono 45s"):
        lancer_chrono(45, "Planche dynamique")
    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Entraînement 3 : Bureau")
    st.subheader("1. Suspensions Passives (4 x 15s)")
    if st.button("Lancer Chrono 15s"):
        lancer_chrono(15, "Suspension Passive")
    st.subheader("2. Blocage 90° (3 x 10s)")
    if st.button("Lancer Chrono 10s"):
        lancer_chrono(10, "Blocage 90°")
    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()
