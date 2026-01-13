# 🌦️ Météo Pro 2.0 - Rapport Complet & Guide Détaillé

## 📖 Introduction : Qu'est-ce que ce projet ?

Bienvenue sur **Météo Pro 2.0**. Ce projet n'est pas simplement une page web qui affiche la température ; c'est une application interactive complète, construite entièrement en langage **Python**.

L'objectif était de créer une interface météo qui soit aussi belle que fonctionnelle, capable de rivaliser avec les applications professionnelles que vous trouvez sur votre smartphone. Nous avons mis l'accent sur **l'expérience visuelle** : l'application "ressent" la météo et change d'apparence pour vous immerger dans l'ambiance actuelle (pluie, soleil, nuit étoilée, etc.).

---

## 🎨 L'Expérience Visuelle (Ce qu'on voit)

Nous avons utilisé une technique de design moderne appelée **"Glassmorphism"**.

- **C'est quoi ?** Imaginez des panneaux de verre dépoli flottant sur une image de fond. Cela donne un aspect transparent, léger et très élégant.
- **Pourquoi ?** Pour que les informations (texte, chiffres) soient parfaitement lisibles tout en laissant voir la magnifique image d'arrière-plan.

### 🖼️ Les Fonds d'Écran Intelligents

L'application est "vivante". Elle ne se contente pas d'afficher un soleil quand il fait beau. Elle analyse deux choses :

1.  **La Météo** : La pluie, la neige, l'orage, le brouillard...
2.  **Le Moment de la Journée** : Jour ou Nuit.

**Exemple concret :**

- S'il fait beau à midi : Vous verrez un **ciel bleu éclatant**.
- S'il fait beau à minuit : Vous verrez un **ciel nocturne étoilé**.
- S'il y a du brouillard la nuit : Vous verrez une **rue mystérieuse éclairée par des lampadaires**.

> **Note :** Si jamais une image spécifique manque, l'application est assez maligne pour prendre l'image de jour et l'assombrir artificiellement pour créer une ambiance de nuit convaincante.

---

## ⚙️ La Mécanique (Comment ça marche ?)

Pour qu'une application fonctionne, c'est comme une voiture : il y a plusieurs pièces, et chacune a un rôle précis. Voici le détail de chaque fichier de notre projet, expliqué simplement :

### 1. Le Chef d'Orchestre : `app.py`

C'est le fichier principal. Quand vous lancez l'application, c'est lui qui démarre.

- **Son rôle** : Il dirige tout le monde. Il demande à l'API la météo, il choisit quelle image afficher, et il dessine la page (titres, colonnes, boutons).
- _Analogie_ : C'est le réalisateur du film.

### 2. Le Messager : `weather_api.py`

Ce fichier est chargé d'aller chercher les informations à l'extérieur.

- **Son rôle** : Il se connecte à Internet (vers le service "Open-Meteo") pour demander : "Quel temps fait-il à Paris ?". Il reçoit la réponse (des chiffres) et la rapporte au Chef d'Orchestre.
- _Analogie_ : C'est le facteur qui va chercher votre courrier.

### 3. Le Traducteur : `weather_analyzer.py`

Les ordinateurs parlent en chiffres (ex: Code météo "45"). Les humains préfèrent les mots (ex: "Brouillard").

- **Son rôle** : Il traduit les codes compliqués en phrases simples. Il calcule aussi si c'est confortable (Indice de chaleur) ou s'il faut mettre un manteau.
- _Analogie_ : C'est un interprète qui traduit un langage technique en français courant.

### 4. Le Décorateur : `ui_components.py`

C'est lui qui gère la beauté de l'application.

- **Son rôle** : Il contient les instructions pour les couleurs, les styles de texte, et surtout, c'est lui qui décide quelle image de fond correspond à la météo actuelle. Il gère aussi le fameux effet de "verre dépoli".
- _Analogie_ : C'est l'architecte d'intérieur.

### 5. Le Livre de Règles : `config.py`

Ce fichier contient toutes les listes fixes.

- **Son rôle** : Il stocke la liste des villes (Paris, Londres...), les codes couleurs, et les traductions officielles des codes météo.
- _Analogie_ : C'est le dictionnaire ou le manuel de référence.

---

## 🚀 Guide d'Installation (Pas à pas pour débutant)

Vous voulez lancer ce projet sur votre ordinateur ? Suivez ces étapes simples.

### Étape 1 : Préparer le terrain

Assurez-vous d'avoir **Python** installé sur votre ordinateur. C'est le moteur qui fait tourner le code.

### Étape 2 : Récupérer les "ingrédients"

Les développeurs utilisent des bibliothèques (des morceaux de code déjà faits par d'autres) pour gagner du temps. La liste de ces ingrédients est dans le fichier `requirements.txt`.

Ouvrez votre terminal (l'écran noir où on tape des commandes) et écrivez ceci :

```bash
pip install -r requirements.txt
```

_Cela veut dire : "Python, s'il te plaît (pip), installe tous les outils listés dans le fichier requirements.txt"._

### Étape 3 : Démarrer le moteur

Une fois que tout est installé, lancez l'application avec cette commande :

```bash
streamlit run app.py
```

_Cela veut dire : "Streamlit (notre outil d'affichage), exécute le fichier principal app.py"._

🎉 **Magie !** Votre navigateur internet va s'ouvrir tout seul avec l'application météo.

---

## 🛠️ Le "Mode Test" (Secret de fabrication)

Nous avons ajouté une fonctionnalité cachée pour les créateurs : le **Mode Test Visuel**.
Dans la barre latérale de gauche, il y a une option "Mode Test". Si vous l'activez, vous pouvez **forcer** l'application à afficher n'importe quelle météo (Orage, Neige, Soleil...).

- **À quoi ça sert ?** Cela permet de vérifier que toutes les images et les couleurs fonctionnent bien, sans attendre qu'il neige vraiment dehors !

---

## 📝 Conclusion

Ce projet montre comment on peut partir de simples lignes de code pour arriver à un outil visuel, utile et agréable. Il combine :

- De la **Logique** (Python)
- De la **Donnée** (API Météo)
- Du **Design** (CSS & Images)

C'est un exemple parfait de ce qu'est "l'informatique créative".

**Auteur :** Yassmine
**Cours :** Compétences numériques et informatique (Python)
**Année :** 2026
