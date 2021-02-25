# Kariertes Blatt

## Erkennung von Normteilen für den Maschinenbau

Im Maschinenbau gibt es standardisierte Bauteile, die immer wieder in Maschinen und im Formenbau verwendet werden. Wir haben einen Kontakt zu einem Hersteller solcher Normteile, der uns Beispielteile zur Verfügung gestellt hat.

Ziel ist es, die Form (also die DIN- oder ISO-Norm, DIN 7, DIN 7979, ISO 8737 etc.) als auch die Größe (z.B. Durchmesser 6 mm, 40 mm lang) zu erkennen. Die Bauteile sind unterschiedlich leicht voneinander zu unterscheiden und es gibt sie in fest vorgegebenen, abgestuften Größen. Wir befassen uns im Wesentlichen mit sogenannten Stiften, die es in unterschiedlichen Endbearbeitungen gibt *(Linsenkuppen, Kegelkuppen, ohne Kuppen, mit Bohrung und Innengewinde, mit Außengewinde etc).*

- Systematischer Aufbau einer Datensammlung der Bauteile mit der Photobox im Graphiklabor
- Unterschiedliche Größenreferenzen: Kariertes Blatt Papier, Münze
- Training eines Klassifikators
- Erkennung direkt der Art (Norm) als Ganzes oder der Morphologie, also einzelne Eigenschaften (welche Endbearbeitung, mit Innen-/Außengewinde etc.)
- Erkennung der Größe (Die Teile gibt es nur in 'diskreten' Größen, z.B. 6x50mm  und 6x60 mm, aber nicht z.B. 5,8x51,3 mm.)

Das Interessante an dieser Aufgabe ist die Arbeit mit der Photobox zum **automatisierten Erstellen** von qualitativ hochwertigen Bildern, die **Erkennung** von Längen und gegebenenfalls die Ausgabe von mehreren Lösungen bei leicht zu verwechselnden Teilen.

## Project

### Instruction
1. Run ```bottom_extraction.sh```, ```side_extraction```, ```top_extraction``` scripts in ```extract_mask``` folder.
2. Run ```resize_data.py```, ```resize_data_build.py``` scripts.
3. Run ```training.py``` in ```deep_learining``` folder for training a model. The result is a model for segmentation task.

## Connect to dataset

### Using ```sshfs```
```
sshfs [name]@[gianglong.me]:/media/disk2/project_system_data ./project_system_data
```

## Code Guide

### Autocompletion for pycharm

https://towardsdatascience.com/how-to-install-opencv-and-extra-modules-from-source-using-cmake-and-then-set-it-up-in-your-pycharm-7e6ae25dbac5

### Git merge with rebase strategy

```
[Your new feature]
git checkout master
git pull
git checkout feature/feature-name
git rebase -i main
git push --force-with-lease

[Code review]
git checkout master
git merger feature/feature-name
```