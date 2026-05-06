import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Coach Escalade SNCF", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ffcc00; color: black; height: 3em; width: 100%;
        border-radius: 10px; border: none; font-weight: bold; font-size: 18px;
    }
    .desc { font-size: 14px; color: #666; font-style: italic; margin-bottom: 10px; }
    .log { padding: 5px; border-bottom: 1px solid #eee; font-family: monospace; font-size: 12px; }
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
    
    # Phase d'effort
    st.warning(f"⚡ ACTION : {nom}")
    for i in range(secondes):
        placeholder.metric("EFFORT", f"{secondes - i}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    
    # Log dans l'historique
    heure = datetime.now().strftime("%H:%M")
    st.session_state.historique.insert(0, f"{heure} - {nom} ({secondes}s)")
    
    # Phase de repos automatique
    st.success(f"✅ Terminé ! Repos forcé : {repos}s")
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
    
    if st.button("💪 ENTRAÎNEMENT 1 : Dos & Bras"):
        st.session_state.page = 'Jour 1'; st.rerun()
    if st.button("🦵 ENTRAÎNEMENT 2 : Gainage & Poussée"):
        st.session_state.page = 'Jour 2'; st.rerun()
    if st.button("🖐️ ENTRAÎNEMENT 3 : Spécial Bureau (Planche)"):
        st.session_state.page = 'Jour 3'; st.rerun()

    st.divider()
    st.subheader("📜 Journal de session")
    if not st.session_state.historique:
        st.write("Aucun exercice validé. On s'y met ?")
    else:
        for item in st.session_state.historique:
            st.markdown(f"<div class='log'>🚂 {item}</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Jour 1':
    st.header("💪 Jour 1 : Dos & Bras (Haltères)")
    st.subheader("1. Tractions (4 x 8)")
    st.subheader("2. Rowing unilatéral (3 x 10)")
    st.subheader("3. Curl Marteau (3 x 12)")
    st.subheader("4. Dead Hang (3 x 30s)")
    if st.button("Démarrer Dead Hang (30s)"):
        executer_exercice(30, "Dead Hang", 60)
    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Jour 2 : Abdos & Cuisses (Kettlebell)")
    st.subheader("1. Gobelet Squat (4 x 12)")
    st.subheader("2. Soulevé de terre (3 x 10)")
    st.subheader("3. Relevé de genoux (3 x 12)")
    st.subheader("4. Planche dynamique (3 x 45s)")
    if st.button("Démarrer Planche (45s)"):
        executer_exercice(45, "Planche dynamique", 45)
    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Session Bureau : Renfort Poulies")
    taille = st.select_slider("Taille de la prise (mm)", options=[25, 20, 18, 15, 12, 10], value=20)
    
    st.subheader("1. Suspensions Passives (15s)")
    st.markdown("<p class='desc'>Bras tendus, épaules verrouillées.</p>", unsafe_allow_html=True)
    if st.button("GO 15s + 45s repos"):
        executer_exercice(15, f"Suspension {taille}mm", 45)

    st.subheader("2. Tirages de doigts (3 x 10)")
    st.markdown("<p class='desc'>Passer de tendu à demi-arqué sans lâcher.</p>", unsafe_allow_html=True)

    st.subheader("3. Blocage 90° (10s)")
    st.markdown("<p class='desc'>Force de contact pure.</p>", unsafe_allow_html=True)
    if st.button("GO 10s + 60s repos"):
        executer_exercice(10, f"Blocage 90° ({taille}mm)", 60)

    st.subheader("4. Gainage suspendu (20s)")
    if st.button("GO 20s + 60s repos"):
        executer_exercice(20, "Gainage Planche", 60)

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()
