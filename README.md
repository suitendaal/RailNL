# RailNL
### Sven Uitendaal, Susanne Binkhorst en Britt van Leeuwen

Deze case gaat over de lijnvoering van intercitytreinen.
Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet.
Een traject is een route van sporen en stations waarover treinen heen en weer rijden.
Een traject mag niet langer zijn dan het opgegeven tijdsframe.

Voor het eerste deel gaan wij naar de 22 belangrijkste intercitystations in provincies Noord- en Zuid-Holland kijken.
De verbindingen tussen die stations zijn in een bestand gegeven. Van deze 22 stations zijn er 7 door RailNL als kritiek bestempeld:
Alkmaar, Amsterdam Centraal, Den Haag Centraal, Gouda,Haarlem, Rotterdam Centraal en Zaandam. De stations staan in een bestand met bijbehorende coordinaten. Ook staat hierin of een station kritiek (extra belangrijk) is.

Tot nu toe zijn wij bezig geweest met een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van 
twee uur, waarbij zoveel mogelijk van de kritieke sporen bereden wordt. Hierbij houden wij rekening met de Scorefunctie om een zo
goed mogelijke lijnvoering van trajecten te krijgen.

Deze scorefunctie is als volgt:
S = p\*10000 - (t\*20 + min/100000)
waarin S de score is, p het percentage van de bereden kritieke verbindingen, t het aantal treinen en m het totaal door alle treinen
samen gereden aantal minuten in de lijnvoering.

Deze scorefunctie heeft een upper en een lower bound. De lower bound van deze scorefrucntie is 0, deze is gebaseerd op geen 
treinen, dus geen kritieke sporen en geen gereden minuten. De upper bound van deze scorefunctie hebben wij gezet op
999979.99714, deze is gebaseerd op de veronderstelling dat elk kritiek spoor aan elkaar verbonden is en dat je met 1 trein
alle kritieke sporen kan bereiken in een (minimum) tijd van 287 minuten.

De statespace hebben wij berekend op ongeveer 5 \* 10\^19. Dit getal komt voort uit 2223 (het totaal aantal mogelijke trajecten) 
kies 7. Dat is iets teveel om alles brute-force te controleren, omdat het dan erg lang zou duren. Daarom experimenteren wij nu met 
pruning en algoritmes om daarmee de beste maximaal 7 trajecten te kiezen, die voor de hoogste score zorgen.

Het eerste algoritme dat wij hebben gebruikt gaat als volgt; elk traject is apart in de Scorefunctie gestopt en de 20 trajecten met
de hoogste score zijn door middel van deep-breath gecombineerd en weer in de Scorefunctie gestopt. Hieruit komt een lijnvoering met
de voor dit algoritme de beste score.

Momenteel zijn wij bezig met onder andere Dijksta's algoritme. Hierna willen wij met Hillclimbing hier de beste score uit halen.
