# SUTOM

## Aperçu du projet

Sutom est un jeu de mots innovant qui combine des éléments de stratégie, de vocabulaire et de créativité spécialement créé pour les Français. Il présente aux joueurs une grille de lettres à partir de laquelle ils doivent former des mots horizontalement, verticalement ou en diagonale.
**L'objectif de ce projet est de créer le jeu SUTOM avec le langage de programmation Python.**

| Liens                                                                                           | Desc.                                          |
|-------------------------------------------------------------------------------------------------|------------------------------------------------|
| [Documentations](https://code.up8.edu/aanpukkody/sutom_groupe2/-/tree/main/Docs?ref_type=heads) | Cahier des charges, conceptions, diagrammes... |
| [Git repository](https://code.up8.edu/aanpukkody/sutom_groupe2)                                 | Le lien vers le projet sur Git                 |

## Utilisation
⚠️ **Avant de commencer, il est important de s'assurer que la bibliothèque art est installée.**
Pour ce faire, vous pouvez ouvrir un terminal et taper :
**Avec `pip`:**

```bash
pip install art==6.1
```

## Exemple d'utilisation

- Lancez le fichier main.py
```bash
$python main.py

  ###              ##
 ##       ##   ##  ####      #####    ## ##
 ######   ##   ##  ####     #######  #######
  ######  ##   ##  ##       ##   ##  ## # ##
      ##  ##   ##  ##   ##  ##   ##  ## # ##
 #######  #######  #######  #######  ##   ##
 ######    #####    #####    #####   ##   ##

Règles : si la lettre est entre [], elle est correcte et à la bonne place.
Si la lettre est entre (), elle est correcte, mais n'est pas à la bonne place.
Une lettre non correcte sera laissée telle quelle.
Vous avez 6 essais !

A   _   _   _   _   _   _
>
```
- Entrez un mot avec la bonne longueur

```bash
>Absinthe
[A]  B   S   I   N  (T)  H  [E] 

>
```

- Si vous n'arrivez pas à trouver le mot en 6 essais
```bash
Dommage ! Le mot était ATTROUPE
```

- Si vous trouvez le mot
```bash
>amblytere
[A] [M] [B] [L] [Y] [T] [E] [R] [E] 

Vous avez trouvé le mot en 2 essais !
```

## Auteurs du projet
Si vous voulez utiliser notre projet, merci de bien vouloir citer les informations suivantes :
*Edouard Crocq and Anparasan Anpukkody* **SUTOM_Groupe2**. OIC, UP8, 2024.

```LaTeX
@inproceedings{sutom_groupe2,
  title={Sutom en Python},
  author={Crocq, Edouard and Anpukkody, Anparasan},
  year={2024}
}
```

## Autres projets

Pour le cours d'OIC, nous avons aussi créé un projet qui permet de calculer les notes de plusieurs étudiants, soit avec un fichier, soit directement dans le terminal.
- [Projet lecture et calcul de notes](https://code.up8.edu/aanpukkody/code-lecture-et-calcul-de-notes-oic-groupe_3)


