# cardio-risk-predictor
ML-powered cardiovascular risk prediction web app
 Prédicteur de Risque Cardiovasculaire
# 🫀 Prédicteur de Risque Cardiovasculaire

Application web interactive pour prédire le risque de maladie cardiovasculaire basée sur des facteurs physiologiques et comportementaux.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Description

Cette application utilise un modèle de machine learning (K-Nearest Neighbors optimisé) pour prédire le risque de maladie cardiovasculaire en fonction de variables physiologiques et de facteurs de risque comportementaux.

### Caractéristiques principales

- ✅ Prédiction en temps réel du risque cardiovasculaire
- 📊 Visualisation interactive des facteurs de risque
- 🎯 Interface utilisateur intuitive avec Streamlit
- 📈 Graphiques et métriques détaillées
- 🔍 Validation complète sur 7 cas de test cliniques

## 🚀 Démo en ligne

🔗 [Essayer l'application](https://votre-app.streamlit.app)

## 📊 Variables d'entrée

### Variables physiologiques
- **Pression artérielle systolique** (mmHg)
- **Cholestérol LDL** (mg/dL)
- **Adiposité**
- **Indice de masse corporelle (IMC)**

### Facteurs de risque
- **Âge** (années)
- **Consommation de tabac** (kg cumulé)
- **Score de personnalité Type A**
- **Consommation d'alcool** (unités/semaine)
- **Antécédents familiaux** de maladie cardiaque (Oui/Non)

## 🛠️ Installation

### Prérequis

- Python 3.8 ou supérieur
- pip

### Installation locale

1. Cloner le dépôt
```bash
git clone https://github.com/votre-username/cardio-risk-predictor.git
cd cardio-risk-predictor
```

2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Lancer l'application
```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## 📁 Structure du projet

```
cardio-risk-predictor/
│
├── app.py                    # Application Streamlit principale
├── requirements.txt          # Dépendances
├── README.md                # Ce fichier
├── .gitignore               # Fichiers ignorés par Git
│
├── models/
│   ├── cardio_model.pkl     # Modèle entraîné
│   └── scaler.pkl           # Scaler
│
├── src/
│   ├── preprocessing.py     # Prétraitement
│   ├── model.py            # Classe modèle
│   └── utils.py            # Utilitaires
│
└── docs/
    └── rapport_validation.docx  # Rapport d'analyse
```

## 🧪 Validation du modèle

Le modèle a été rigoureusement testé sur 7 cas cliniques représentatifs :

| Cas | Profil | Risque prédit | Statut |
|-----|--------|---------------|--------|
| 1 | 25 ans, profil optimal | 9.09% | ✅ Validé |
| 2 | 45 ans, bonne santé | 18.18% | ✅ Validé |
| 3 | 55 ans, HTA + surpoids | 63.64% | ⚠️ Surestimé |
| 4 | 65 ans, multiples facteurs | 63.64% | ⚠️ Compression |
| 5 | 70 ans, profil critique | 72.73% | ✅ Validé |
| 6 | 30 ans, facteurs de risque | 63.64% | ⚠️ Surestimé |
| 7 | 68 ans, très sain | 45.45% | ⚠️ Surestimé |

📄 [Rapport de validation complet](docs/rapport_validation.docx)

## 🎯 Performance du modèle

- **Précision** : À compléter avec vos métriques
- **F1-Score** : À compléter
- **ROC-AUC** : À compléter
- **Sensibilité** : À compléter
- **Spécificité** : À compléter

## 🔮 Améliorations futures

- [ ] Améliorer la granularité (sortie continue au lieu de 11 niveaux)
- [ ] Rééquilibrer la pondération de l'âge
- [ ] Intégrer les antécédents familiaux plus efficacement
- [ ] Ajouter plus de visualisations
- [ ] Support multilingue
- [ ] Export PDF des résultats
- [ ] Historique des prédictions

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Votre Nom**
- GitHub: [gatsoundoujuniior-netizen(https://github.com/votre-username)
- LinkedIn: [Votre Profil](https://linkedin.com/in/votre-profil)

## 🙏 Remerciements

- Dataset source : CHD(disponible dans le repository)
- Inspiré par les modèles Framingham et SCORE
- Construit avec Streamlit

## ⚠️ Disclaimer

**Cette application est destinée à des fins éducatives et de recherche uniquement. Elle ne doit PAS remplacer un avis médical professionnel. Consultez toujours un professionnel de santé qualifié pour toute question concernant votre santé cardiovasculaire.**

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !
