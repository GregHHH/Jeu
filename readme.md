### Tout est possible,

### Tout est réalisable,

# c'est  **LE JEU DE LA VIE!**

## Règles:

Le jeu se déroule sur une grille à deux dimensions (matrice) dont les cases sont appelées « cellules », par analogie avec les cellules vivantes.

Chaque cellule peut  prendre deux états distincts : « **vivante** » ou « **morte** » (1 ou 0).

Une cellule possède **huit voisins**, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes :

- une cellule **morte** possédant exactement trois cellules voisines vivantes devient vivante
- une cellule **vivante** possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt

---

## Utilisation du programme:

### Étape N°1: Géneration de la grille:

Pour commencer, il est nécéssaire de choisir la taille de notre grille. Pour cela, on éxecute le  fichier main.py avec comme arguments le nombre de lignes, de colonnes et le pourcentage de cellules vivantes lors de la première itération:

```shell
python3 main.py {nbr_lignes} {nbr_colonnes} {pourcentage}
```


```shell
python3 main.py 8 2 40
```

⚠️ La valeur par defaut des lignes / colonnes est de **20** en l'absence de valeurs choisies par l'utilisateur.

⚠️ La valeur par defaut de la proportion de cellules vivantes est de **30%** en l'absence de valeurs choisies par l'utilisateur.

si le programme est exécuté avec l'option '-c', la grille personnalisée présente dans main.py sera utilisée.

```p
python3 main.py -c
```

Lors de l'éxecution du programme, il est possible de faire varier **la vitesse d'affichage** en appuyant sur la touche **ENTRER**.
La **couleur** des cellules vivantes peut varier grâce à la **barre d'espace**.

---

## Problèmes rencontrés:

* Utilisation de pygame, nottament à cause des grosses différences entre la version 1 et 2 qui rendent plus difficile la recherche d'exemples.
  Les erreurs renvoyées par pygame ne sont pas toujours très explicites et parfois même renvoient des erreurs complètement différentes du problème réelement rencontré.
* L'organisation du code afin de le rendre lisible facilement:

```
```



## Liste de paterns sympathiques:

```
densité maximale:

python3 20 20 100
```


```
la grenouille:

[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]

```

```
La fleur:

[
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

```

## TODO:

Ci-dessous, les élements que l'ont aurait aimé ajouter en plus dans notre programme.



* Ajouter un systeme afin de créer une grille aléatoire via la fenètre de pygame
* Ajouter un menu
