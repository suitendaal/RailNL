# RailNL
Deze case gaat over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten
uitzet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn
dan het opgegeven tijdsframe.

Voor het eerste deel gaan wij naar de 22 belangrijkste intercitystations in provincies Noord- en Zuid-Holland kijken.
De verbindingen tussen die stations zijn in een bestand gegeven. Van deze 22 stations zijn er 7 door RailNL als kritiek bestempeld:
Alkmaar, Amsterdam Centraal, Den Haag Centraal, Gouda,Haarlem, Rotterdam Centraal en Zaandam. De stations staan in een bestand met
bijbehorende coordinaten. Ook staat hierin of een station kritiek (extra belangrijk) is.


Deze scorefunctie is als volgt:
S = p\*10000 - (t\*20 + min/100000)
waarin S de score is, p het percentage van de bereden kritieke verbindingen, t het aantal treinen en m het totaal door alle treinen
samen gereden aantal minuten in de lijnvoering.

Deze scorefunctie heeft een upper en een lower bound. De lower bound van deze scorefuntie is -140.00094, deze is gebaseerd op 7 (het maximum aantal)
treinen, geen kritieke verbindingen (dus alleen de niet kritieke verbindingen) en een totaal van 94 gereden minuten. De upper bound van deze scorefunctie hebben wij
gezet op 999939.99713, deze is gebaseerd op de veronderstelling dat elk kritiek spoor aan elkaar verbonden is en dat je met 3 treinen
alle kritieke sporen kan bereiken in een (minimum) tijd van 287 minuten.

De statespace hebben wij berekend op ongeveer 5 \* 10\^19. Dit getal komt voort uit 2223 (het totaal aantal mogelijke trajecten)
kies 7. Dat is iets teveel om alles brute-force te controleren, omdat het dan erg lang zou duren. Daarom experimenteren wij nu met
pruning en algoritmes om daarmee de beste maximaal 7 trajecten te kiezen, die voor de hoogste score zorgen.

## Getting Started

### Prerequisites
latest versions modules
### Installing

## Running the tests

### Explaination of the algoritms
Het eerste algoritme dat wij hebben gebruikt gaat als volgt; elk traject is apart in de scorefunctie gestopt en de 20 trajecten met
de hoogste score zijn door middel van depth-first gecombineerd en weer in de scorefunctie gestopt. Hieruit komt een lijnvoering met
de voor dit algoritme beste score.

Wij hebben ook het Dijkstra algoritme uitgewerkt. Deze werkt als volgt: Kies een beginstation, kijk of deze kritieke verbindingen
heeft, zo ja, kies de kortste van de kritieke verbindingen, anders kies de kortste niet-kritieke verbinding. Dit algoritme werkt
dus (nog) niet met score, maar met de tijd.

Wij hebben ook een hillclimber functie gemaakt die van een combinatie van trajecten elk traject 1000 keer vervangen met een random
ander traject, de score berekend en de score en de combinatie opslaat als deze beter is dan de vorige. Hier kun je een random
combinatie van trajecten invullen of al de beste uit bijvoorbeeld het Dijkstra algoritme.

Ten slotte hebben wij een zelfbedacht algoritme bedacht. Deze staat bekend als Sven's algoritme. Het kiest tussen 2 stations de beste route, gebaseerd op een zo kort mogelijke route met zoveel mogelijk kritieke verbindingen. Op deze manier wordt het aantal trajecten dus flink gereduceerd, hoewel er nog wel flink wat overblijven.
Vervolgens heb je een lijst met het beste traject tussen 2 stations. Hiermee kan brute-force worden toegepast of hillclimbing.

### Break down into end to end tests

### And coding style sheets

## Deployment

## Built With
* **Atom 1.22.1**
* **GitHub**

## Authors
* **Sven Uitendaal**
* **Britt van Leeuwen**
* **Susanne Binkhorst**

## License

# Acknowledgment

Tot nu toe zijn wij bezig geweest met een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van
twee uur, waarbij zoveel mogelijk van de kritieke sporen bereden wordt. Hierbij houden wij rekening met de Scorefunctie om een zo
goed mogelijke lijnvoering van trajecten te krijgen.
