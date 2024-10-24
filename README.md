# EasyPyI

EasyPyI est une application graphique développée en Python avec `tkinter` qui permet de faciliter la compilation de projets Python en binaires exécutables. L'interface vous permet de sélectionner des options de compilation visuellement et de suivre le déroulement de la compilation en temps réel via une console intégrée.

## Fonctionnalités

- **Sélection du répertoire du projet** : Choisissez le répertoire où se trouve votre projet Python.
- **Sélection du fichier principal** : Choisissez le fichier Python principal (`.py`) qui sera compilé.
- **Options PyInstaller** :
  - Créer un fichier exécutable unique (`--onefile`)
  - Générer une application sans console (`--windowed`)
  - Ajouter des fichiers supplémentaires (e.g., fichiers `.ui`)
  - Spécifier des imports cachés (`--hidden-import`)
  - Ajouter des fichiers binaires supplémentaires (`--add-binary`)
  - Utiliser une icône personnalisée pour l'exécutable (`--icon`)
  - Spécifier un nom personnalisé pour l'exécutable (`--name`)
  - Désactiver la compression UPX (`--noupx`)
  - Nettoyer les fichiers temporaires avant la compilation (`--clean`)
  - Pas de confirmation pendant la compilation (`--noconfirm`)
  - Choisir les chemins de sortie, de travail et du fichier `.spec`
- **Console intégrée** : Affiche le retour en temps réel de la commande PyInstaller.

## Prérequis

- **Python 3.x**
- **Tkinter** (inclus par défaut avec la plupart des installations Python)
- **PyInstaller** (à installer séparément)

### Installation de PyInstaller

Vous pouvez installer PyInstaller via `pip` si vous ne l'avez pas encore :

```bash
pip install pyinstaller
```

## Installation

Clonez ce dépôt ou téléchargez les fichiers source.

```bash
git clone https://github.com/Kell0x/EasyPyI.git
cd EasyPyI
```

## Utilisation

1. **Exécuter l'application** :

   Dans le terminal, exécutez la commande suivante pour démarrer l'interface graphique :

   ```bash
   python EasyPyI.py
   ```

2. **Sélectionner les options** :

   - Utilisez l'interface pour sélectionner votre répertoire de projet et le fichier principal à compiler.
   - Cochez les options de compilation dont vous avez besoin.
   - Appuyez sur le bouton "Compiler" pour lancer la compilation.

3. **Console intégrée** :

   La zone "Console" en bas de la fenêtre affichera le retour de la commande PyInstaller en temps réel, vous permettant de suivre la progression de la compilation.

## Exemple d'utilisation

### Compilation simple

Pour créer un fichier exécutable unique (`--onefile`) d'un script Python sans interface graphique, suivez ces étapes :

1. Sélectionnez votre projet et le fichier principal.
2. Cochez l'option "Créer un seul fichier exécutable".
3. Appuyez sur "Compiler".

### Compilation avec une icône personnalisée

Si vous souhaitez ajouter une icône personnalisée à l'exécutable, suivez ces étapes :

1. Sélectionnez votre projet et le fichier principal.
2. Cochez l'option "Créer un seul fichier exécutable".
3. Choisissez un fichier `.ico` en appuyant sur le bouton "Sélectionner" à côté du champ "Icône".
4. Appuyez sur "Compiler".

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des issues ou des pull requests pour améliorer l'application.

## Licence

Ce projet est sous licence MIT :

1. Les utilisateurs sont libres d'utiliser le logiciel pour tout projet, y compris à des fins commerciales ou privées.
2. Les utilisateurs peuvent modifier, copier, fusionner, publier, distribuer, sous-licencier et même vendre des copies du logiciel.
3. Les utilisateurs doivent inclure la notice de droits d'auteur d'origine dans toutes les copies ou portions du logiciel distribuées, mais ils ne sont pas obligés de partager leurs modifications sous la même licence.
4. Le logiciel est fourni "tel quel", sans garantie d'aucune sorte. L'auteur n'est pas responsable des problèmes qui pourraient survenir en utilisant le logiciel.
