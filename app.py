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
    .log { padding: 5px; border-bottom: 1px solid #eee; font-family: monospace; font-size: 12px; }
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
        placeholder.metric("Chrono", f"{restant}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    placeholder.empty()
    barre.empty()
    st.success(f"Terminé : {nom}")
    heure = datetime.now().strftime("%H:%M")
    st.session_state.historique.insert(0, f"{heure} - {nom} ({secondes}s)")

# --- PAGES ---
if st.session_state.page == 'Accueil':
    st.title("🧗 Coach Perso : Objectif Bloc")
    st.write("Sélectionne ton chantier :")
    
    if st.button("💪 ENTRAÎNEMENT 1 : Traction & Grip (Haltères/Barre)"):
        st.session_state.page = 'Jour 1'; st.rerun()
    if st.button("🦵 ENTRAÎNEMENT 2 : Gainage & Poussée (Kettlebell)"):
        st.session_state.page = 'Jour 2'; st.rerun()
    if st.button("🖐️ ENTRAÎNEMENT 3 : Bureau (Planche uniquement)"):
        st.session_state.page = 'Jour 3'; st.rerun()

    st.divider()
    st.subheader("📜 Historique de la séance")
    if not st.session_state.historique:
        st.write("Rien pour l'instant. Allez, au boulot !")
    else:
        for item in st.session_state.historique:
            st.markdown(f"<div class='log'>✅ {item}</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Jour 1':
    st.header("💪 Entraînement 1 : Dos & Bras")
    
    st.subheader("1. Échauffement (3 min)")
    st.write("Mobilisation des épaules et poignets.")

    st.subheader("2. Tractions (4 x 8)")
    st.markdown("<p class='desc'>Tirer le menton au-dessus de la barre.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Rowing unilatéral (3 x 10)")
    st.markdown("<p class='desc'>Un genou sur un banc, tirer l'haltère vers la hanche.</p>", unsafe_allow_html=True)
    
    st.subheader("4. Curl Marteau (3 x 12)")
    st.markdown("<p class='desc'>Haltères pouces vers le haut pour le brachial.</p>", unsafe_allow_html=True)
    
    st.subheader("5. Dead Hang (3 x 30s)")
    st.markdown("<p class='desc'>Suspension passive pour le grip.</p>", unsafe_allow_html=True)
    if st.button("Lancer Chrono 30s"):
        lancer_chrono(30, "Dead Hang")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Entraînement 2 : Abdos & Cuisses")
    
    st.subheader("1. Échauffement (3 min)")
    st.write("Squats à vide.")

    st.subheader("2. Gobelet Squat (4 x 12)")
    st.markdown("<p class='desc'>Kettlebell contre la poitrine, descendre bas.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Soulevé de terre (3 x 10)")
    st.markdown("<p class='desc'>Dos droit, poussée jambes avec Kettlebell.</p>", unsafe_allow_html=True)
    
    st.subheader("4. Relevé de genoux (3 x 12)")
    st.markdown("<p class='desc'>Suspendu ou au sol, monter genoux poitrine.</p>", unsafe_allow_html=True)
    
    st.subheader("5. Planche dynamique (3 x 45s)")
    st.markdown("<p class='desc'>Gainage alternant coudes et mains.</p>", unsafe_allow_html=True)
    if st.button("Lancer Chrono 45s"):
        lancer_chrono(45, "Planche dynamique")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Entraînement 3 : Spécial Bureau")
    
    st.subheader("1. Suspensions Passives (4 x 15s)")
    st.markdown("<p class='desc'>Sur réglettes, bras tendus.</p>", unsafe_allow_html=True)
    if st.button("Lancer Chrono 15s"):
        lancer_chrono(15, "Suspension Passive")

    st.subheader("2. Tirages de doigts (3 x 10)")
    st.markdown("<p class='desc'>Passer de tendu à demi-arqué.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Blocage 90° (3 x 10s)")
    st.markdown("<p class='desc'>Bloquer à angle droit sur la planche.</p>", unsafe_allow_html=True)
    if st.button("Lancer Chrono 10s"):
        lancer_chrono(10, "Blocage 90°")

    st.subheader("4. Gainage suspendu (3 x 20s)")
    st.markdown("<p class='desc'>Bras tendus, lever jambes à 45°.</p>", unsafe_allow_html=True)
    if st.button("Lancer Chrono 20s"):
        lancer_chrono(20, "Gainage suspendu")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()
