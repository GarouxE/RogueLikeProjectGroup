# Projet de jeu Rogue Like en groupe de 3

###########  Ewan Garoux      ###########
###########  Marius Barbaud   ###########
###########  Patel Lucah      ###########


Elements integres:
  interface graphique                    
  armure                   
  gestion des salles     
  salle de tresor         
  rapide                 
  diagonale              
  invisible               
  point d'xp              
  magasin                
  piege                   
  inventaire limité
  poison
 
  

                  Total Fait: 17



Table des matieres:
   - 1. Titre du projet : Jeu Rogue Like
   - 2. Description du projet 
   - 3. Comment installer et exécuter le projet 
   - 4. Comment utiliser le projet 
   - 5. Les crédits 
   - 6. Licence 


1. Titre du projet : Jeu Rogue Like
Le projet consiste à ajouter des éléments au jeu Rogue que nous avons programmé en TPs 
pendant ce semestre. A chaque élément est associé un degré de complexité, allant de 1 (facile) à 4 (difficile).

2. Description du projet :
Le Rogue Like (ou rogue-like) est un sous-genre de jeu vidéo de rôle dans lequel le joueur explore un donjon infesté de monstres qu’il doit combattre pour gagner de l’expérience et des trésors. Le genre se caractérise notamment par la génération procédurale de ses niveaux, son système de mort permanente, son gameplay au tour par tour et la représentation des éléments qui le composent par des symboles ASCII sur une carte constituée de tuiles. La plupart des Rogue Like se déroulent dans un univers de fantasy qui reflète l’influence du jeu de rôle sur table Donjons et Dragons sur le genre.
C'est une composante importante de votre projet que de nombreux développeurs négligent.

3. Comment installer et exécuter le projet :

-Les modules a installé sont:
      Math
      pygame
      sys
      time
      random 
      copy

- Au préalable : Installer tous les modules composant le projet dans le même répertoire, qui est propre à ce jeu.
- Sur Linux : Lancer le terminal, se déplacer vers le répertoire où se situe le projet rogue like puis lancer la commande : python3 main.py 
- Sur Windows : Lancer le terminal, se déplacer vers le répertoire où se situe le projet rogue like puis lancer la commande : python3 .\main.py 
- Sur VS code : ouvrir le fichier main.py puis lancer le jeu.

4. Comment utiliser le projet :

Pour lancer le jeu ouvre le fichier main dans le terminal et executer-le.

Lorsque le jeu est lancé vous vous situé sur une carte remplie de monstres, pour vous déplacer il suffit d’utiliser les touches :  
- Flèche de gauche ou ‘q’ (pour aller à gauche) 
- Flèche de droite ou ‘d’ (pour aller à droite) 
- Flèche du haut ou ‘z’ (pour aller en haut) 
- Flèche du bas ou ‘s’ (pour aller en bas) 
- ‘a’ pour se déplacer diagonalement (en haut à gauche) 
- ‘e’ pour se déplacer diagonalement (en haut à droite) 
- ‘w’ pour se déplacer diagonalement (en bas à gauche) 
- ‘c’ pour se déplacer diagonalement (en bas à droite) 
Les touches clé : 
- ‘u’ (use) pour utiliser un Equipment qui se situe dans l'inventaire 
- ‘k’ (kill) pour tue votre personnage et quitter le jeu


Les touches pour la selection d'un numero:
  -les touches SHIFT + NUMERO marche cependant pygame ne detecte pas le numeros Num Lock
5. Les crédits :
Ce projet a été effectué en trinôme avec :  
- Marius Barbaud (BbdMarius) 
- Garoux Ewan (GarouxE) 
- Patel Lucah (bogwee) 

6. Licence :
MIT License

Copyright (c) [2023] [Jeu Rogue Like]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
