# 🐍 Snake AI — Reinforcement Learning with PPO

An autonomous Snake agent trained using **Reinforcement Learning (RL)** and the **Proximal Policy Optimization (PPO)** algorithm.

This project involves developing a custom Snake game environment and training an AI agent to learn how to play through interactions with its environment.

## 🎯 Project Overview

The goal is to develop an intelligent agent capable of playing Snake autonomously.

The agent observes the game state, selects actions, receives rewards or penalties, and progressively improves its strategy through reinforcement learning.

## 🧠 Reinforcement Learning Approach

The project uses **Proximal Policy Optimization (PPO)**, a policy-gradient reinforcement learning algorithm.

The learning process follows these steps:

1. Observe the current game state.
2. Select an action.
3. Execute the action in the environment.
4. Receive a reward based on the outcome.
5. Update the policy to improve future decisions.

### Environment Design

A custom environment was developed using Gymnasium.

- **Action Space:** 3 discrete actions — turn left, turn right, or continue straight.
- **Observation Space:** 11 binary features (`MultiBinary(11)`) representing relevant information about the snake and its surroundings.
- **Reward System:** Rewards and penalties guide the agent's learning process.
- **Game Rendering:** Pygame is used to visualize the environment and the agent's behavior.

## 🛠️ Technologies

| Technology        | Purpose                                       |
| ----------------- | --------------------------------------------- |
| Python            | Main programming language                     |
| Gymnasium         | Custom Reinforcement Learning environment     |
| Stable-Baselines3 | PPO implementation and training               |
| PyTorch           | Neural network framework                      |
| Pygame            | Game development and visualization            |
| NumPy             | Numerical operations and state representation |

## 📂 Project Structure

```text
projet_RL_game/
│
├── .gitignore
├── game.py          # Game logic
├── play.py          # Run the trained agent
├── snake_game.py    # Snake game environment
├── test.py          # Environment testing
├── train.py         # PPO agent training
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AisFa/projet_RL_game.git
cd projet_RL_game
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install gymnasium stable-baselines3 pygame-ce numpy torch
```

## ▶️ Running the Project

### 1. Train the AI agent

```bash
python train.py
```

This starts the PPO training process.

### 2. Play with the trained agent

```bash
python play.py
```

This launches the Snake environment with the trained agent, provided the model has already been saved by the training script.

### 3. Test the environment

```bash
python test.py
```

## 📚 Key Learning Outcomes

- Understanding Reinforcement Learning fundamentals.
- Designing a custom Gymnasium environment.
- Implementing and training a PPO agent.
- Defining observation and action spaces.
- Designing reward functions.
- Analyzing agent behavior and learning performance.

---

# 🇫🇷 Version française

# 🐍 Snake AI — Apprentissage par renforcement avec PPO

Un agent autonome Snake entraîné grâce à l'**apprentissage par renforcement (Reinforcement Learning)** et à l'algorithme **Proximal Policy Optimization (PPO)**.

Ce projet consiste à développer un environnement de jeu Snake personnalisé et à entraîner un agent intelligent à apprendre à jouer en interagissant avec son environnement.

## 🎯 Présentation du projet

L'objectif est de développer un agent capable de jouer à Snake de manière autonome.

L'agent observe l'état du jeu, sélectionne des actions, reçoit des récompenses ou des pénalités et améliore progressivement sa stratégie grâce à l'apprentissage par renforcement.

## 🧠 Approche par apprentissage par renforcement

Le projet utilise **Proximal Policy Optimization (PPO)**, un algorithme d'apprentissage par renforcement basé sur les gradients de politique.

Le processus d'apprentissage suit ces étapes :

1. Observer l'état actuel du jeu.
2. Sélectionner une action.
3. Exécuter l'action dans l'environnement.
4. Recevoir une récompense selon le résultat.
5. Mettre à jour la politique pour améliorer les décisions futures.

### Conception de l'environnement

Un environnement personnalisé a été développé avec Gymnasium.

- **Espace d'actions :** 3 actions discrètes — tourner à gauche, tourner à droite ou continuer tout droit.
- **Espace d'observation :** 11 caractéristiques binaires (`MultiBinary(11)`) représentant les informations pertinentes sur le serpent et son environnement.
- **Système de récompenses :** des récompenses et des pénalités guident le processus d'apprentissage.
- **Visualisation :** Pygame permet d'afficher l'environnement et le comportement de l'agent.

## 🛠️ Technologies utilisées

| Technologie       | Utilisation                                    |
| ----------------- | ---------------------------------------------- |
| Python            | Langage principal                              |
| Gymnasium         | Création de l'environnement                    |
| Stable-Baselines3 | Implémentation et entraînement de PPO          |
| PyTorch           | Framework de réseaux de neurones               |
| Pygame            | Développement du jeu et visualisation          |
| NumPy             | Calculs numériques et représentation des états |

## 📂 Structure du projet

```text
projet_RL_game/
│
├── .gitignore
├── game.py          # Logique du jeu
├── play.py          # Exécution de l'agent entraîné
├── snake_game.py    # Environnement Snake
├── test.py          # Tests de l'environnement
├── train.py         # Entraînement de l'agent PPO
└── README.md
```

## 🚀 Installation

Cloner le dépôt :

```bash
git clone https://github.com/AisFa/projet_RL_game.git
cd projet_RL_game
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

L'activer sous Windows :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install gymnasium stable-baselines3 pygame-ce numpy torch
```

## ▶️ Exécution du projet

### 1. Entraîner l'agent IA

```bash
python train.py
```

Cette commande lance l'entraînement de l'agent avec PPO.

### 2. Jouer avec l'agent entraîné

```bash
python play.py
```

Cette commande lance l'environnement Snake avec l'agent entraîné, à condition que le modèle ait été sauvegardé pendant l'entraînement.

### 3. Tester l'environnement

```bash
python test.py
```

## 📚 Compétences développées

- Compréhension des fondamentaux du Reinforcement Learning.
- Conception d'un environnement personnalisé avec Gymnasium.
- Implémentation et entraînement d'un agent PPO.
- Définition des espaces d'observation et d'action.
- Conception de fonctions de récompense.
- Analyse du comportement et des performances d'apprentissage de l'agent.
