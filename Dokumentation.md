# Dokumentation Projekt Erkennug Normteile - Gruppe Kariertes Blatt

## **Allgemeine Informationen**

### **Auswahl des Projekts**
Das Modul "PSE" hat die Besonderheit, dass dieses semesterübergreifend durchgeführt wird. Neben dem Modul "PSE", welches im 5. Semester des Informatik-Bachelors angeboten wird, gibt es auch das Modul "Projekt Multimedia" im dritten Semester des KMI Studiengangs. Beide Module werden zusammengefasst, sodass Dritt- und Fünftsemester an einem Projekt zusammenarbeiten können.

Das Modul haben wir im Wintersemester 2020/2021 bei Professor Dr. Rapp belegt. Es geht hauptsächlich um die Datensammlung und das Machine Learning.

Jede Gruppe konnte sich für ein Thema aus der folgenden Liste entscheiden:
- Erkennung von Normteilen für den Maschinenbau
- Erkennung von Warnsignalen für eine visuelle Hörhilfe
- Erkennung von unterschiedlichen Schallquellen für eine visuelle Hörhilfe
- Akustische Drohnendetektion

Unsere Gruppe hat sich für den ersten Vorschlag entschieden. Aufgrund der Tatsache, dass sich drei Gruppen mit diesem Thema auseinandersetzen wollten, entschied sich Herr Rapp, das Projekt in verschiedene Ansätze zu teilen. 


### **Unterschied zu anderen Gruppen**
Wir haben uns für den Ansatz "kariertes Blatt" entschieden. Genauer, wir verwenden für die Erkennung der einzelnen Normteile ein kariertes Blatt als Größenreferenz. 

Die anderen Ansätze sind die Gruppe "Münze" und die Gruppe "Freestyle". Die Gruppe Münze verwendet eine 1€ Münze als Referenz. Beide Gruppen verwenden die Photobox als Methode zur Datensammlung.

Im Unterschied zu den vorherigen Gruppen verwendet die Gruppe "Freestyle" nichts als Referenz und führt die Datensammlung unter realen Bedingungen mit dem Smartphone durch.


### **Problemdefinition**
- Tägliche Verwendung von großer Menge an Normteilen
- Bestände der Bauteile nehmen sehr schnell ab
- Ist der Vorrat aufgebraucht, dann muss das Teil umständlich im System herausgesucht werden
- hoher Zeitaufwand


### **Projektziel**
- Unsere Anwendung wird anhand eines Fotos verschiedene Normteile ermitteln können
    - Kariertes Blatt als Referenz
- Augenmerk auf verschiedene Arten von Stiften
- Was kann die App erkennen?
    - Länge, Dicke, Endbearbeitung
- Sind Stifte leicht zu verwechseln, dann kann der Nutzer zwischen Lösungen entscheiden

### **Relevanz des Projekts**
- Zeitersparnis seitens des Kunden
- Wirtschaftlichkeit
    - viele kleine und mittelständische Unternehmen, die ihre Bestellungen noch manuell durchführen
- Einsparung von Arbeitskraft

### **Team**
Unsere Gruppe besteht aus drei Mitgliedern. Dies ist unser erstes Pojekt zusammen als Gruppe. 

| Michael Helsper | Giang Long Tran | Hai Ninh Bui |
| ------------------ | ------------------ | ------------------ |
|<img src="https://i.ibb.co/8MvwSF1/Michael.png" alt="Michael" style="zoom:50%;" />| <img src="https://i.ibb.co/X3F95Vc/Long.png" alt="Long" style="zoom:50%;" />|<img src="https://i.ibb.co/9hH3yvF/Ninh.png" alt="Ninh" style="zoom:50%;" />|
|3. Semester|5. Semester|6. Semester|
|C++ Vorkenntnisse|Full Stack Developer|Front End Developer|
|Scrum|Team Leader||


### **Zeitplanung**
Dieses Semester standen uns 13 Wochen für unser Projekt zur Verfügung. Im Folgenden sieht man die zeitliche Verteilung der Aufgaben :


| November|Dezember |Januar |Februar|
| ------------------ | ------------------ | ------------------ | ------------------ |
|Project Proposal Presentation|Abschluss Datensammlung|Image Segmentation Abschluss|Projektabschluss|
|Problemdefinition|Ordnerstruktur erstellen|Modell zur Positionserkennung| Abschlusspräsentation|
|Beginn Datensammlung|Labelling|Modell Training||
||Zwischenpräsentation|Modell zur Größen- und Normerkennung||
|    |Start Image Segmentation|||



### **Koordination im Team**
Wir haben uns projektbegleitend für Trello und Gitlab als Koordinationsplattform entschieden. Trello verwenden wir hauptsächlich, um die Aufgabenverteilung zu überblicken und die noch fälligen Aufgaben im Blick zu behalten. Daneben verwenden wir auch Gitlab. Wir sind sehr zufrieden mit der Funktionalität. Diese Plattform macht die Arbeit im Team unkompliziert. Des Weiteren haben wir uns einen eigenen Server (Jupiter Server) aufgesetzt, um unsere Testdaten einfach verwalten und teilen zu können. Ein weiterer Grund für diese Entscheidung ist die Tatsache, dass es bei den anderen Gruppen Probleme mit der Speicherung des Datasets gab und wir diese umgehen wollten. Bei den Meisten war nicht mehr genug Cloud Speicher vorhanden. Außerdem hat das Bereitstellen der Ressourcen seitens der Hochschule etwas länger gedauert. Ebenfalls haben wir uns durch regelmäßige Gruppenmeetings immer auf dem Laufenden gehalten.

**Trello:**

<img src="https://i.ibb.co/0crQq75/trello.png" alt="Photobox" style="zoom:50%;" />


### **"Corona Besonderheiten"** 
Auch dieses Semester (WiSe2020/2021) war wieder ein Coronasemester, d.h. alle Präsenzveranstaltungen konnten leider nicht wie gewohnt stattfinden. An der virtuellen Lehre als Ausweichmöglichkeit fuhr kein Weg vorbei. Meiner Meinung nach haben die Online Meetings in unserer Gruppe gut funktioniert..


### **Verwendete Tools**
Für unserer Projekt haben wir folgende Tools verwedet:
- PyCharm als IDE
- OpenCV
- Keras 
- Git


### **Verwendete Hardware**
Für das Trainieren des Modells haben wir einen Desktop mit folgender Spezifikation verwednet: 
- Desktop
    - i7-8705G CPU @ 3.10GHz
    - 16GB RAM

Bei 1400 Bildern hat das Trainieren knappe vier Stunden gedauert.

Außerdem haben wir für die Erstellung des Datasets eine **Canon EOS 6D Mark II** und eine **Canon EOS R** verwendet und die Photobox an sich. Die Verwaltung der Datensammlung haben wir auf unserem eigenen Server realisiert, welcher auf einem PaspberryPi läuft.

---

## **Vorgehen**

### ****Data****
 
|Anzahl Fotos |Anzahl einzigartiger Stifte|Auflösung   | Speicherbenutzung    | Aufnahmewinkel |Arten Normteile|
|---    |---| ---        |---   |---            |---|
|1400       | 46 | 6240 x 4160         | 6GB     |            von oben, seitlich, von unten   |Zylinderstift, Kegelstift|


### **Datensammlung**
Nach unserer Project Proposal Präsentation und nach dem ersten Vertrautmachen mit dem Thema ging es an die Datensammlung. Wir haben als Gruppe Normteile von der Firma "DEMA Präzisionsteile GmbH" zur Verfügung gestellt bekommen, welche wir mit der Gruppe "Münze" geteilt haben. Da die Box mit den Normteilen bereits mehrere Male durch die Hände von Studierenden gegangen ist, waren wir nicht überrascht zu sehen, dass die Teile unsortiert darin lagen. Ein Dank geht an die Gruppe "Münze", welche die notwendigen Teile mit einem Messschieber nachmaß und richtig sortierte.

Für die Datensammlung haben wir uns im Grafiklabor getroffen und anhand der Photobox unsere Daten aus 3 verschiedenen Perspektiven (oben, seitlich, unten) aufgenommen. Die Photobox besteht aus einem "Teller" im Zentrum und einem weißen Hintergrund. Dieser Teller wird von zwei Lichtpaneelen angestrahlt, sodass bei der Aufnahme keine Schatten zu sehen sind. Wir haben jedes Bauteil immer um 45° gedreht und ein Foto davon gemacht. Zu jeder Zeit lag unsere Referenz, das karierte Blatt, unter den Normteilen. 

Wir haben im Zuge der Datensammlung ein Data Set mit 46 unterschiedlichen Normteilen und ca. 1500 Bildern aufbauen können. Die 46 verschiedenen Normteile können in vier DIN-Normen unterteilt werden (DIN7978-A, DIN7977, DIN6325, DIN7979-D). Jeweils zwei DIN-Normen können wiederum in die Oberkategorien Zylinderstift respektive Kegelstift unterteilt werden.    

**Die drei verschiedenen Ansichten:**

<img src="https://i.ibb.co/wcf41Rs/Datensammlung.png" alt="Daten" style="zoom:50%;" />  

**Photobox:**

<img src="https://i.ibb.co/rfj4CfR/image0.jpg" alt="Photobox" width="500;" />

### **Daten Aufbereitung**
Das automatische Kategorisieren mithilfe der Photobox hat leider nicht funktioniert. Aus diesem Grund mussten wir alle Daten, welche auf zwei Kameras verteilt waren, nach dem spezifischen Bauteil sortieren. Das Zuordnen haben wir uns erleichtert, indem wir beim Aufnehmen der Bilder bereits an das Problem gedacht haben und vor jedem neuen Bauteil die Spezifikationen mit abfotografierten. So konnten wir die 1500 Bilder erfolgreich gliedern. Der nächste Schritt ist nun die Ordnerstruktur.

### **Ordnerstruktur**
Das besondere an unserer Ordnerstruktur ist die Tatsache, dass sich alle drei Gruppen auf eine einheitliche Ordnerstruktur geeinigt haben und diese auch in die hochschuleigene Datenbank geladen haben. Die Verständigung auf eine einheitliche Ordnerstruktur hat definitiv etwas Zeit gekostet, allerdings ist dies für mögliche Weiterentwicklungen in der Zukunft eine gute Basis.

Die beiden "Hauptordner" sind Kegelstift und Zylinderstift. Im nächsttieferen Verzeichnis werden die der Stiftform zugeordneten DINs angezeigt. Eine Schicht tiefer findet man die einzelnen Variationen der DIN (e.g. 10mmx100mm). In der vorletzten Schicht werden die Daten mit ihrem Aufnahmewinkel verglichen. In der "letzten Schicht" sind dann die eigentlichen Bilder zu sehen.

<img src="https://i.ibb.co/Z2c6Cwr/dfg.png" alt="Ordnerstruktur" style="zoom:65%;" />


### **Labelling**
Nach dem Erfassen der Daten und der Speicherung in der Ordnerstruktur haben wir mit dem Labelling der Daten begonnen. Für das weitere Arbeiten konnten wir mit der Spezifikation des Teils nicht viel anfangen. Deshalb haben wir jedes Foto mit solch einer Spezifikation "example.JPG" genannt. Um mit unserem späteren Modell die Endabrundung des Bauteils besser bestimmen zu können, haben wir das Bauteil mit dem besten Blick auf die Endbearbeitung mit dem Kürzel "_E" versehen.

<img src="https://i.ibb.co/0GqMfrM/labelling.png" alt="Labelling" style="zoom:90%;" />

### **Daten auf Server**
Im Team hat sich schnell die Frage gestellt, wo genau wir unsere Daten speichern, um gemeinsam damit arbeiten zu können. GoogleDrive ist bei uns schnell ausgeschlossen worden. Da zu diesem Zeitpunkt der Hochschulserver für uns noch nicht freigeschaltet wurde, haben wir einen eigenen Server verwendet, um unsere Daten zu teilen. Wir haben einen Jupiter Server dafür verwendet. Im weiteren Verlauf des Semesters haben wir dann auch Platz auf dem Hochschulserver bekommen, sodass wir unsere finale Datensammlung für alle bereitstellen konnten. Der Plan ist die Daten für zukünftige Projekte zu speichern, damit die nächsten Gruppen eine solide Basis für mögliche Weiterentwicklungen haben.

### **Vorbereitung eines neuen Datasets**
- **Image Segmentation** 
    - Nach dem Labelling der Daten ist der nächste Schritt das Erstellen eines neuen Datasets. Das neue Dataset wird benötigt, um die Position des Stiftes in dem Bild zu bestimmen.
    - Hierfür haben wir ein Python Script geschrieben (Code siehe weiter unten) 
    - Mithilfe von OpenCV haben wir die Image Segmentation realisieren können. Wir haben eine Maske über das Bild gelegt. Im folgenden Bild kann man beispielhaft 2 Ergebnisse des Prozesses sehen. 
        - Die Stifte werden im neuen Dataset als weiß dargestellt, alles andere darum ist schwarz
    - 90% unserers neuen Datasets konnte durch OpenCV automatisch erzeugt werden. Die restlichen Daten konnten leider nicht zuverlässlich erkannt werden. Diese mussten wir händisch nachtragen. 
    - der gesamte Prozess hat insgesamt vier Stunden gedauert 

**Ergebnis der Image Segmentation:**

<img src="https://i.ibb.co/X87SXqC/segmentation.png" alt="ImageSegmentation" width="500;" />

<img src="https://i.ibb.co/2Mhnmfm/mask.png" alt="ImagageSegmentation" style="zoom:58%;" />



**Der folgende Code zeigt wie die Mask extrahiert wird:** 

```
# Extract target mask
def extract_target_mask(imagePath, paperPath, region, threshold, output_root='data_build'):
    print(imagePath)
    
    # lesen des Fotos
    image = cv.imread(imagePath, 1)
    paper = cv.imread(paperPath, 1)

    # Return a new array of given shape and type, filled with ones
    kernel = np.ones((3, 3), np.uint8)

    # Morphological operations apply: Removing noise, 
    # Isolation of individual elements and joining disparate elements in an image, Finding of intensity bumps or holes in an image.
    paper = cv.dilate(paper, kernel, iterations=5)
    paper = cv.erode(paper, kernel, iterations=5)
    target = cv.dilate(image, kernel, iterations=5)
    target = cv.erode(target, kernel, iterations=5)

    # subtract two images then add two images to have a mask
    mask = cv.subtract(paper, target)
    mask = cv.add(mask, mask)

    # crop image demension
    crop = mask[region[0], region[1]]

    # convert RGB image to gray image
    grayImage = cv.cvtColor(crop, cv.COLOR_BGR2GRAY)
    grayImage = cv.GaussianBlur(grayImage, (9, 9), 0)

    # Return a new array of given shape and type, filled with ones. Then apply Morphological operation.
    kernel = np.ones((3, 3), np.uint8)
    grayImage = cv.erode(grayImage, kernel, iterations=3)
    grayImage = cv.dilate(grayImage, kernel, iterations=20)
    grayImage = cv.erode(grayImage, kernel, iterations=20)

    # If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value.
    edge, thresh = cv.threshold(grayImage, threshold, 255, cv.THRESH_BINARY)

    # Finding contours in your image
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    meta = image.copy()
    contour_sizes = [(cv.contourArea(contour), contour) for contour in contours]
    contour_sizes.sort(key=lambda x: x[0], reverse=True)
    
    # draw a rectangle
    cv.rectangle(meta, (region[1].start, region[0].start), (region[1].stop, region[0].stop), (0, 255, 0), 3)

    output = np.zeros((image.shape[0], image.shape[1]), np.uint8)
    output[region[0], region[1]] = thresh

    # add specific mark to output name xxx_mask.JPG
    outputPath = os.path.splitext(imagePath)[0].replace('data', output_root)
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)

    # write out result image
    cv.imwrite(outputPath + '_mask.JPG', output)
    cv.imwrite(outputPath + '_meta.JPG', meta)
```


### **Modell zur Positionserkennung erstellt**

Im Anschluss zum Ersellen des Datasets haben wir ein Modell erstellt, welches die Position eines Stiftes erkennen kann. Der **input** ist das **originale Foto**. Als **output** bekommen wir ein **segmentation image**.

Das folgende dargetstellte Bild ist ein Beispiel von einer Convolutional-network Architecture. Wir haben das U-Net verwendet. Die detallierte Architectur kann man in ```deep_learing/segmentation_training.ipynb``` finden. Man braucht ungefähr 3 Stunden für das Trainieren der drei Modelle (oben, seitlich und unten).
![U_Net](documentations/u_net_architecture_example.png)


Die Daten, die wir am Ende der Image Segmentation bekommen haben, haben wir in zwei Teile geteilt. 80% der Daten wurden verwendet, um das Modell zu trainierung. Die restlichen 20% wurden verwendet, um das Modell im Nachhinein zu validieren.

**Beispielergebnisse aus dem Validation Dataset:**

<img src="https://i.ibb.co/09BDwJn/1.png" alt="Input" width="600"/>


Wir haben auch "Fremddaten" verwendet, um unser Modell zu überprüfen. Die Ergebnisse sind nicht perfekt, kann sich aber als erster Ansatz sehen lassen.

<img src="https://i.ibb.co/m5mhQkT/Unbenannt.png" alt="Input" width="600"/>

Mithilfe des Segmentation Images erstellen wir ein Bild. In diesem Bild ist nur der Stift zu erkennen un kein anderes Objekt. Dieses neu erstellte Bild wird für den nächsten Schritt (für das Modell zur Normerkennung) benötigt. Dabei ist es wichtig, dass jeder input die gleiche Größe hat.

Die Graphen zeigen die Genauigkeit der Modelle zur Positionserkennung aus den verschiedenen Perspektiven nach 5 Durchgängen. Die Modelle fürdie Seite und Unten sind mit knapp 70% sehr gut geworden. Aufgrund der wenigen Daten, die wir von oben aufgenommen haben, bekamen wir kein gutes Ergebnis für diese Position.

<img src="https://i.ibb.co/pPdP0XZ/3.png" alt="Input" width="1000"/>

Und hier sieht man es nochmal umgekehrt. Hier sieht man die Prozentzahl an Fehlern.

<img src="https://i.ibb.co/h94V0qk/4.png" alt="Input" width="1000"/>


### Modell zur Normerkennung erstellt 
Wir verwenden eine VGG16-architectur für die Klassifizierung. Das Training hat 30 Minuten gedauert. Der **Input** sind Bilder mit einer Auflösung von 256x256 Pixel. Das Training mit hochauflösenden Fotos war nicht erfolgreich und hat auch zu viel Zeit gekostet.

<img src="documentations/vgg16.png" alt="vgg16"/>


Anwendungsbeispiel. Wir nehmen Fotos der Stifte aus unterschiedlichen Positionen auf. Das trainierte Modell wird dann vorhersagen zu welcher "Klasse" der Stift gehört. Hier an dem Bild kann man die Funktionalität unseres Modells sehr gut erkennen. Wir haben drei Fotos des gleichen Stifts in unterschiedlichen Positionen verwendet. In zwei von drei Fällen wurde das Normteil vollständig richtig erkannt. Die erste Zeile bezieht sich auf das angestrebte Ergebnis, die zweite Zeile ist das Ergebnis des Modells.  

<img src="https://i.ibb.co/b6M1n4Q/5.png" alt="classification" width="600"/>


Hier sehen wir die Normerkennung mit Fremddaten von der Gruppe Münze. Die Bilder wurden manuell zugeschnitten. Leider hat unser Modell die Größe nicht zuverlässig bestimmen können. Unsere Vermutung ist die Tatsache, dass wir das Modell mit einem karierten Blatt trainierten und dies jetzt aus diesem Grund nicht funktioniert.

<img src="https://i.ibb.co/RB0DJQh/6.png" alt="classification" width="600"/>


Die Graphen zeigen die Genauigkeit der Modelle zur Normerkennung aus den verschiedenen Perspektiven nach 16 Durchgängen. Die Modelle für sind mit knapp 90% (Trainingsdaten) sehr gut geworden. 

<img src="https://i.ibb.co/pKSbTcK/7.png" alt="Input" width="1000"/>

Und hier sieht man es nochmal umgekehrt. Hier sieht man die Prozentzahl an Fehlern.

<img src="https://i.ibb.co/p2MRgD2/9.png" alt="Input" width="1000"/>


**Bessere Herangehensweise:**

Momentan haben wir 46 unterschiedliche Ausprägungen der Normteile. Zurzeit wählen wir aus dem gesamten Pool von 46 Möglichkeiten den richtigen Stift aus. Eine bessere Herangehensweise ist im ersten Schritt eine Unterscheidung, basierend auf dem input (Foto), zwischen Kegelstift und Zylinderstift. Danach wird die DIN-Norm vorhergesagt und die Größe des Stifts wird bestimmt. Anhand dieser Vorgehensweise haben wir Schritt für Schritt weniger mögliche Varianten und somit ein genaueres Ergebnis.   

-> mögliche Weiterentwicklung 


### Ergebnis

**Positionserkennung**
- Nach 5 maligen Trainieren des Modells
- 70% der Modelle erfolgreich erkannt
- Für Fremddaten liegt kein genauer Wert vor (funktioniert teilweise)

**Norm- / Größenerkennung**
- Nach 16 maligen Trainieren des Modells
    - 80 90% der Trainingsdaten richtig erkannt (inkl. Norm und Größe)
    - 60% der Validierungsdaten richtig erkannt (inkl. Norm und Größe)
    - 40% der Fremddaten von Gruppe Münze werden richtig erkannt
        - Dabei nur auf DIN konzentriert
            - Größe konnte nicht zuverlässig ermittelt werden
            - Vermutung: da unser Modell mit Karos trainiert wurde, kann die Länge und Breite der Stifte nicht korrekt bestimmt werden
        - Modell Positionserkennung bei Fremddaten ausgelassen
            - Aufgrund Zeitmangel händisch „ gecroppt “



## **Probleme**
### **Unbekannte Teile**
Zu Beginn der Datensammlung hatten wir das Problem, dass alle Stifte kreuz und quer in der bereitgestellten Box lagen. 
Die Gruppe "Münze" hat die Aufgabe des Sortierens übernommen und alle Teile der jeweiligen Norm zugeordnet.

Im Verlauf der Datensammlung sind wir aber auf das Problem gestoßen, dass es mehrere Gruppierungen der gleichen Teile gab, was wir in der Datenaufbereitung berücksichtigen mussten.
Für alle zukünftigen Projekte mit den Normteilen der DEMA Präzisionsteile GmbH haben wir dafür gesorgt, dass nach dem Abschluss der Datensammlung alle Teile wieder geordnet den Weg in die Box zurückgefunden haben.
 
### **Photobox**
Es dauerte seine Zeit, bis wir einen Termin zur Benutzung der Photobox bekommen haben. Außerdem hatten wir das Problem, dass die Software zum automatischen Verarbeiten der Bilder nicht funktionierte. Aus diesem Grund musste alles per Hand gemacht werden. 

### **Image Segmentation**
Bei der Vorbereitung des Datasets bestand das Problem darin, alle Stifte auf dem Foto genau zu erkennen. Es lag daran, dass die Grenzen des Stifts teilweise mit dem karierten Blatt "verschwommen" sind. Deshalb konnten nicht alle Fotos automatisch extrahiert werden. Der Rest wurde dann per Hand durchgeführt.

### **Klassifizierung**
Wie vorher schon erwähnt hatten wir ein Problem mit der Klassifizierung der Teile. Der Versuch eine höhere Auflösung als 256x256 zu verwenden ist fehlgeschlagen. Unsere Vermutung ist, dass der verwendete Laptop dafür nicht stark genug war. Das war aber für den weiteren Verlauf kein Problem, da es mit der genannten Auflösung dann zu guten Ergebnissen geführt hat.

## **Projektaussicht**
Im Rahmen dieses Projekts haben wir schon einiges erreichen können. Gleichwohl gibt es noch Möglichkeiten das Projekt auf unserer Basis weiter zu entwickeln. Beispielsweise haben wir noch keine Anwendung entwickelt, die es einem erlaubt ein Foto hochzuladen und dann ausgibt, um welche Norm und Größe es sich handelt. Wie vorher bereits beschrieben kann man eine bessere Herangehensweise beim Erkennen der Normteile verwenden. Nicht passende Kategorien zu Beginn auszusortieren und erst gar nicht mit als Möglichkeit in die weitere Auswahl zu nehmen ist vielleicht ein Ansatz, den man in Zukunft weiterverfolgen kann. 
