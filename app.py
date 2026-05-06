import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Coach Escalade SNCF", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    /* Style des boutons */
    div.stButton > button:first-child {
        background-color: #ffcc00; color: black; height: 3.5em; width: 100%;
        border-radius: 10px; border: none; font-weight: bold; font-size: 16px;
        margin-bottom: 10px;
    }
    /* Centrage du texte des descriptions */
    .desc { font-size: 14px; color: #666; font-style: italic; text-align: center; margin-bottom: 15px; }
    .log { padding: 5px; border-bottom: 1px solid #eee; font-family: monospace; font-size: 12px; }
    h1, h2, h3 { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- MÉMOIRE DE LA SESSION ---
if 'page' not in st.session_state:
    st.session_state.page = 'Accueil'
if 'historique' not in st.session_state:
    st.session_state.historique = []

# --- MOTEUR DE SESSION (EFFORT + REPOS) ---
def executer_exercice(secondes, nom, repos=45):
    placeholder = st.empty()
    barre = st.progress(0)
    
    st.warning(f"⚡ ACTION : {nom}")
    for i in range(secondes):
        placeholder.metric("EFFORT", f"{secondes - i}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    
    heure = datetime.now().strftime("%H:%M")
    st.session_state.historique.insert(0, f"{heure} - {nom} ({secondes}s)")
    
    st.success(f"✅ Terminé ! Repos : {repos}s")
    barre_repos = st.progress(0)
    for i in range(repos):
        placeholder.metric("REPOS", f"{repos - i}s", delta="-1s", delta_color="inverse")
        barre_repos.progress((i + 1) / repos)
        time.sleep(1)
    
    placeholder.empty()
    st.info("Prêt pour la suite !")

# --- PAGES ---
if st.session_state.page == 'Accueil':
    st.title("🧗 Coach Perso : Objectif Bloc")
    
    # Système de colonnes pour centrer les boutons (1/6 vide, 4/6 bouton, 1/6 vide)
    col_l, col_btn, col_r = st.columns([1, 4, 1])
    
    with col_btn:
        if st.button("💪 ENTRAÎNEMENT 1 : Dos & Bras"):
            st.session_state.page = 'Jour 1'; st.rerun()
        if st.button("🦵 ENTRAÎNEMENT 2 : Gainage & Poussée"):
            st.session_state.page = 'Jour 2'; st.rerun()
        if st.button("🖐️ ENTRAÎNEMENT 3 : Spécial Bureau"):
            st.session_state.page = 'Jour 3'; st.rerun()
        if st.button("🔥 ENTRAÎNEMENT 4 : Affinage Ventre"):
            st.session_state.page = 'Jour 4'; st.rerun()

    st.divider()
    st.subheader("📜 Journal de session")
    if not st.session_state.historique:
        st.write("Aucun exercice validé.")
    else:
        for item in st.session_state.historique:
            st.markdown(f"<div class='log'>🚂 {item}</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Jour 1':
    st.header("💪 Jour 1 : Dos & Bras")
    st.subheader("1. Tractions (4 x 8)")
    st.markdown("<p class='desc'>Menton au-dessus de la barre.</p>", unsafe_allow_html=True)
    st.subheader("2. Rowing (3 x 10)")
    st.subheader("3. Curl Marteau (3 x 12)")
    st.subheader("4. Dead Hang (3 x 30s)")
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        if st.button("Démarrer Dead Hang"): executer_exercice(30, "Dead Hang", 60)
        if st.button("⬅️ Retour"): st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Jour 2 : Abdos & Cuisses")
    st.subheader("1. Gobelet Squat (4 x 12)")
    st.subheader("2. Soulevé de terre (3 x 10)")
    st.subheader("3. Relevé de genoux (3 x 12)")
    st.subheader("4. Planche dynamique (45s)")
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        if st.button("Démarrer Planche"): executer_exercice(45, "Planche dynamique", 45)
        if st.button("⬅️ Retour"): st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Session Bureau")
    taille = st.select_slider("Prise (mm)", options=[25, 20, 18, 15, 12, 10], value=20)
    
    st.subheader("1. Suspensions (15s)")
    st.subheader("2. Tirages de doigts")
    st.subheader("3. Blocage 90° (10s)")
    st.subheader("4. Gainage suspendu (20s)")
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        if st.button("Lancer Suspension"): executer_exercice(15, f"Suspension {taille}mm", 45)
        if st.button("Lancer Blocage"): executer_exercice(10, f"Blocage 90° {taille}mm", 60)
        if st.button("⬅️ Retour"): st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 4':
    st.header("🔥 Entraînement 4 : Sangle Abdo")
    st.subheader("1. Hollow Body (30s)")
    st.subheader("2. Mountain Climbers (45s)")
    st.subheader("3. Russian Twists")
    st.subheader("4. Planche Latérale (30s)")
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        if st.button("Démarrer Hollow Body"): executer_exercice(30, "Hollow Body", 30)
        if st.button("Démarrer Climbers"): executer_exercice(45, "Mountain Climbers", 30)
        if st.button("⬅️ Retour"): st.session_state.page = 'Accueil'; st.rerun()
