## PROJET_MBDIA2

## Memmbre du groupe
    * Mahugnon Nadine AHOMAGNON
    * Fatou SARR
    * Jean Desire LATALLE

# PROCESSUS D'EXECUTION DE PROJET


- *1.* Cloner le projet sur votre ordinateur

- *2.* Ouvrir le projet avec VSCODE

- *3.* Ouvrir le terminal 

- *4.* Créer un dossier "Projet_MBDIA" dans votre dossier /Documents

- *5.* Copier le chemin du dossier "Projet_MBDIA" et coller le dans votre terminal

- *6.*  Taper la commande suivante pour cloner le projet sur votre ordinateur mais avant ça changer powershell par  git bash
bash
git clone https://github.com/Nadine3008/Streamlitbot.git


- *7.* Si vous n'avez pas "Git" installé sur votre machine, vous pouvez télécharger le projet en format zip et le décompresser dans le dossier "Projet_MBDIA"

- *8.* Verifier que vous avez bien que vous êtes dans le dossier "Projet_MBDIA" en tapant la commande suivante dans votre terminal
bash
ls


- *9.* Puis faites la commande suivante pour installer les dépendances du projet
bash
cd Projet_MBDIA


- *10.* Activez votre environnement virtuel en tapant la commande suivante
bash
source projetvenv/Scripts/activate | source projetvenv/bin/activate (bin pour Mac)


- *11.* Installer les dépendances du projet en tapant la commande suivante
bash
pip install -r requirements.txt


- *12.* Pour lancer l'application, tapez la commande suivante qui normalement devrait ouvrir votre navigateur par défaut : http://localhost:8501
bash
streamlit run chatbotgpt.py | streamlit run chatbot.py


- *13.* Testez l'application