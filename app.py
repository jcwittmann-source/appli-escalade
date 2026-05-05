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
    .hist-item { padding: 10px; border-bottom: 1px solid #eee; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION DE LA MÉMOIRE ---
if 'page' not in st.session_state:
    st.session_state.page = 'Accueil'
if 'historique' not in st.session_state:
    st.session_state.historique = []
if 'records' not in st.session_state:
    st.session_state.records = {}

# --- FONCTIONS OUTILS ---
def ajouter_log(exercice):
    heure = datetime.now().strftime("%H:%M")
    st.session_state.historique.insert(0, f"✅ {heure} - {exercice}")

def compte_a_rebours(secondes, nom_exercice):
    placeholder = st.empty()
    barre = st.progress(0)
    start_time = time.time()
    for i in range(secondes):
        restant = secondes - i
        placeholder.metric("Chrono", f"{restant}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    placeholder.empty()
    barre.empty()
    st.success(f"Terminé : {nom_exercice}")
    ajouter_log(nom_exercice)

# --- PAGES ---
if st.session_state.page == 'Accueil':
    st.title("🧗 Coach Perso : Suivi Perf")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💪 J1 : Traction"): st.session_state.page = 'Jour 1'; st.rerun()
    with col2:
        if st.button("🦵 J2 : Gainage"): st.session_state.page = 'Jour 2'; st.rerun()
    
    if st.button("🖐️ J3 : Bureau / Planche"):
        st.session_state.page = 'Jour 3'; st.rerun()

    st.divider()
    st.subheader("📊 Journal de session")
    if not st.session_state.historique:
        st.write("Aucun exercice terminé pour le moment.")
    for item in st.session_state.historique:
        st.markdown(f"<div class='hist-item'>{item}</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Jour 1':
    st.header("💪 Entraînement 1")
    
    # Exercice avec suivi de perf (Répétitions)
    st.subheader("1. Tractions (Max)")
    perf = st.number_input("Nombre de tractions réalisées", min_value=0, step=1, key="perf_traction")
    if st.button("Enregistrer ma perf"):
        st.session_state.records['Tractions'] = perf
        ajouter_log(f"Tractions : {perf} reps")
        st.balloons()

    # Exercice avec Chrono
    st.divider()
    st.subheader("2. Dead Hang (Suspension)")
    if st.button("Lancer 30s de chrono"):
        compte_a_rebours(30, "Dead Hang (30s)")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Entraînement 2")
    
    st.subheader("1. Gobelet Squat")
    poids = st.number_input("Poids utilisé (kg)", min_value=0, step=1)
    if st.button("Valider la série"):
        ajouter_log(f"Gobelet Squat : {poids}kg")

    st.divider()
    st.subheader("2. Planche dynamique")
    if st.button("Lancer 45s de chrono"):
        compte_a_rebours(45, "Planche (45s)")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Entraînement 3 : Bureau")
    
    st.subheader("1. Suspension Planche")
    if st.button("Lancer 15s de chrono"):
        compte_a_rebours(15, "Suspension Bureau (15s)")

    st.divider()
    st.subheader("2. Record de tenue (Max temps)")
    if st.button("Démarrer le chrono de performance"):
        start = time.time()
        stop_btn = st.button("STOP !")
        # Note : Streamlit est un peu limité pour un chrono "live" sans bouton d'arrêt complexe
        # On va rester simple : on enregistre quand tu as fini.
        st.info("Chrono en cours dans ta tête... Clique sur Valider quand tu lâches !")
    
    duree = st.number_input("Secondes tenues :", min_value=0)
    if st.button("Enregistrer le record"):
        ajouter_log(f"Record Planche : {duree}s")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()
