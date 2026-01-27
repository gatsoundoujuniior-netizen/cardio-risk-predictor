import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Maladie Cardiaque",
    page_icon="❤️",
    layout="wide"
)

# Titre principal
st.title("❤️ Prédiction du Risque de Maladie Cardiaque")
st.markdown("---")

# Charger le modèle
@st.cache_resource
def load_model():
    try:
        model = joblib.load('Model2.pkl')
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return None

model = load_model()

if model is not None:
    st.success("✅ Modèle chargé avec succès !")
    
    # Création de deux colonnes pour l'interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Variables Physiologiques")
        
        sbp = st.number_input(
            "Pression artérielle systolique (mmHg)",
            min_value=80.0,
            max_value=250.0,
            value=120.0,
            step=1.0,
            help="Valeur normale : 90-120 mmHg"
        )
        
        ldl = st.number_input(
            "Cholestérol LDL (mg/dL)",
            min_value=1.0,
            max_value=20.0,
            value=5.0,
            step=0.1,
            help="Valeur normale : < 3.4 mg/dL"
        )
        
        adiposity = st.number_input(
            "Adiposité",
            min_value=5.0,
            max_value=50.0,
            value=25.0,
            step=0.5,
            help="Pourcentage de graisse corporelle"
        )
        
        obesity = st.number_input(
            "Obésité (IMC)",
            min_value=15.0,
            max_value=50.0,
            value=25.0,
            step=0.5,
            help="IMC normal : 18.5-24.9"
        )
    
    with col2:
        st.subheader("🧬 Facteurs de Risque")
        
        age = st.number_input(
            "Âge (années)",
            min_value=15,
            max_value=100,
            value=45,
            step=1
        )
        
        tobacco = st.number_input(
            "Consommation de tabac (kg cumulé)",
            min_value=0.0,
            max_value=50.0,
            value=0.0,
            step=0.1,
            help="Tabac cumulé sur la vie"
        )
        
        typea = st.number_input(
            "Score de personnalité Type A",
            min_value=10,
            max_value=100,
            value=50,
            step=1,
            help="Score de stress/compétitivité"
        )
        
        alcohol = st.number_input(
            "Consommation d'alcool (unités/semaine)",
            min_value=0.0,
            max_value=150.0,
            value=0.0,
            step=0.5
        )
        
        famhist = st.selectbox(
            "Antécédents familiaux de maladie cardiaque",
            options=["Absent", "Present"],
            help="Présence de maladie cardiaque dans la famille"
        )
    
    st.markdown("---")
    
    # Bouton de prédiction
    if st.button("🔍 Faire la prédiction", type="primary", use_container_width=True):
        # Créer le DataFrame avec les valeurs saisies
        input_data = pd.DataFrame({
            'sbp': [sbp],
            'tobacco': [tobacco],
            'ldl': [ldl],
            'adiposity': [adiposity],
            'typea': [typea],
            'obesity': [obesity],
            'alcohol': [alcohol],
            'age': [age],
            'famhist': [famhist]
        })
        
        try:
            # Faire la prédiction
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            # Afficher les résultats
            st.markdown("---")
            st.subheader("📋 Résultats de la Prédiction")
            
            # Créer trois colonnes pour les résultats
            res_col1, res_col2, res_col3 = st.columns(3)
            
            with res_col1:
                if prediction == 1:
                    st.error("⚠️ **Risque PRÉSENT**")
                    st.metric("Classe prédite", "1 (Maladie)")
                else:
                    st.success("✅ **Risque ABSENT**")
                    st.metric("Classe prédite", "0 (Sain)")
            
            with res_col2:
                prob_absence = probability[0] * 100
                st.metric(
                    "Probabilité d'absence",
                    f"{prob_absence:.2f}%",
                    delta=None
                )
            
            with res_col3:
                prob_presence = probability[1] * 100
                st.metric(
                    "Probabilité de présence",
                    f"{prob_presence:.2f}%",
                    delta=None
                )
            
            # Barre de progression visuelle
            st.markdown("### 📊 Niveau de risque")
            st.progress(prob_presence / 100)
            
            # Interprétation
            st.markdown("---")
            st.subheader("💡 Interprétation")
            
            if prob_presence < 30:
                st.info("**Risque faible** - Les facteurs analysés indiquent un risque réduit de maladie cardiaque.")
            elif prob_presence < 60:
                st.warning("**Risque modéré** - Il serait prudent de consulter un professionnel de santé pour évaluation.")
            else:
                st.error("**Risque élevé** - Consultation médicale fortement recommandée pour examen approfondi.")
            
            # Afficher les données saisies
            with st.expander("📝 Voir les données saisies"):
                st.dataframe(input_data, use_container_width=True)
        
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")

    # Informations supplémentaires
    st.markdown("---")
    with st.expander("ℹ️ À propos de cette application"):
        st.markdown("""
        Cette application utilise un modèle de machine learning (K-Nearest Neighbors avec SMOTE et PCA) 
        pour prédire le risque de maladie cardiaque basé sur plusieurs facteurs de santé.
        
        **Variables utilisées :**
        - Pression artérielle systolique
        - Cholestérol LDL
        - Adiposité et obésité
        - Âge
        - Consommation de tabac et d'alcool
        - Type de personnalité A
        - Antécédents familiaux
        
        ⚠️ **Avertissement** : Cette prédiction est à titre indicatif uniquement et ne remplace pas 
        un diagnostic médical professionnel.
        """)

else:
    st.error("❌ Impossible de charger le modèle. Assurez-vous que le fichier 'Model2.pkl' est dans le même répertoire.")
