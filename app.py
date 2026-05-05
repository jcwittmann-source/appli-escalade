import streamlit as st
import time

st.set_page_config(page_title="Coach Escalade", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ffcc00; color: black; height: 3em; width: 100%;
        border-radius: 10px; border: none; font-weight: bold; font-size: 18px;
    }
    .desc { font-size: 14px; color: #666; font-style: italic; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'Accueil'

def compte_a_rebours(secondes, message="C'est parti !"):
    placeholder = st.empty()
    barre = st.progress(0)
    for i in range(secondes):
        restant = secondes - i
        placeholder.metric("Temps restant", f"{restant}s")
        barre.progress((i + 1) / secondes)
        time.sleep(1)
    placeholder.empty()
    barre.empty()
    st.success(message)

# --- PAGES ---
if st.session_state.page == 'Accueil':
    st.title("🧗 Coach Perso : Objectif Bloc")
    st.write("Sélectionne ta séance du jour :")
    
    if st.button("💪 ENTRAÎNEMENT 1 : Traction & Grip (Haltères/Barre)"):
        st.session_state.page = 'Jour 1'
        st.rerun()
    if st.button("🦵 ENTRAÎNEMENT 2 : Gainage & Poussée (Kettlebell)"):
        st.session_state.page = 'Jour 2'
        st.rerun()
    if st.button("🖐️ ENTRAÎNEMENT 3 : Bureau (Planche uniquement)"):
        st.session_state.page = 'Jour 3'
        st.rerun()

elif st.session_state.page == 'Jour 1':
    st.header("💪 Entraînement 1 : Dos & Bras")
    st.info("Équipement : Barre de traction et Haltères")
    
    st.subheader("1. Échauffement (3 min)")
    st.write("Mobilisation des épaules, des coudes et des poignets.")

    st.subheader("2. Tractions (4 x 8)")
    st.markdown("<p class='desc'>Tirer le menton au-dessus de la barre. Travail du grand dorsal.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Rowing unilatéral (3 x 10)")
    st.markdown("<p class='desc'>Avec haltère. Un genou sur un banc, tirer l'haltère vers la hanche.</p>", unsafe_allow_html=True)
    
    st.subheader("4. Curl Marteau (3 x 12)")
    st.markdown("<p class='desc'>Haltères en prise neutre (pouces vers le haut) pour le brachial.</p>", unsafe_allow_html=True)
    
    st.subheader("5. Dead Hang (3 x 30s)")
    st.markdown("<p class='desc'>Rester suspendu à la barre pour le grip.</p>", unsafe_allow_html=True)
    if st.button("Démarrer 30s de suspension"):
        compte_a_rebours(30, "Lâche !")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 2':
    st.header("🦵 Entraînement 2 : Abdos & Cuisses")
    st.info("Équipement : Kettlebell")
    
    st.subheader("1. Échauffement (3 min)")
    st.write("Squats à vide et rotations du buste.")

    st.subheader("2. Gobelet Squat (4 x 12)")
    st.markdown("<p class='desc'>Maintenir la Kettlebell contre la poitrine, descendre les fesses bas.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Soulevé de terre (3 x 10)")
    st.markdown("<p class='desc'>Dos bien droit, pousser dans les jambes pour lever la Kettlebell.</p>", unsafe_allow_html=True)
    
    st.subheader("4. Relevé de genoux (3 x 12)")
    st.markdown("<p class='desc'>Suspendu à la barre ou au sol, monter les genoux vers la poitrine (Abdos).</p>", unsafe_allow_html=True)
    
    st.subheader("5. Planche dynamique (3 x 45s)")
    st.markdown("<p class='desc'>Gainage en alternant appui coudes et mains.</p>", unsafe_allow_html=True)
    if st.button("Démarrer 45s de planche"):
        compte_a_rebours(45, "Repos !")

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()

elif st.session_state.page == 'Jour 3':
    st.header("🖐️ Entraînement 3 : Spécial Bureau")
    st.info("Équipement : Planche d'escalade uniquement")
    
    st.subheader("1. Suspensions Passives (4 x 15s)")
    st.markdown("<p class='desc'>Suspendu sur réglettes, bras tendus, épaules verrouillées.</p>", unsafe_allow_html=True)
    if st.button("Démarrer 15s"):
        compte_a_rebours(15)

    st.subheader("2. Tirages de doigts (3 x 10)")
    st.markdown("<p class='desc'>Sur une prise moyenne, passer de tendu à demi-arqué uniquement par la force des doigts.</p>", unsafe_allow_html=True)
    
    st.subheader("3. Blocage 90° (3 x 10s)")
    st.markdown("<p class='desc'>Bloquer en traction à angle droit. Si trop dur, garder les pieds au sol pour délester.</p>", unsafe_allow_html=True)
    if st.button("Démarrer 10s de blocage"):
        compte_a_rebours(10)
        
    st.subheader("4. Gainage suspendu (3 x 20s)")
    st.markdown("<p class='desc'>Bras tendus sur la planche, lever les jambes à 45° pour engager les abdos et les doigts.</p>", unsafe_allow_html=True)
    if st.button("Démarrer 20s"):
        compte_a_rebours(20)

    if st.button("⬅️ Retour"):
        st.session_state.page = 'Accueil'; st.rerun()
