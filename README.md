# RailNL
### Sven Uitendaal, Susanne Binkhorst en Britt van Leeuwen

Deze case gaat over de lijnvoering van intercitytreinen.
Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet.
Een traject is een route van sporen en stations waarover treinen heen en weer rijden.
Een traject mag niet langer zijn dan het opgegeven tijdsframe.

Voor het eerste deel gaan wij naar de 22 belangrijkste intercitystations in provincies Noord- en Zuid-Holland kijken.
De verbindingen tussen die stations zijn in een bestand gegeven.
De getallen die achter een verbinding staan zijn de reistijden in minuten.

Van deze 22 stations zijn er 7 door RailNL als kritiek bestempeld: Alkmaar, Amsterdam Centraal, Den Haag Centraal, Gouda,
Haarlem, Rotterdam Centraal en Zaandam.
De stations staan in een bestand met bijbehorende coordinaten. Ook staat hierin of een station kritiek (extra belangrijk) is.

Tot nu toe zijn wij bezig geweest met een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur,
waarbij zoveel mogelijk van de kritieke sporen bereden wordt.

Hierbij houden wij rekening met de Scorefunctie om een zo goed mogelijke lijnvoering van trajecten te krijgen

Deze scorefunctie is als volgt:
S = p*10000 - (t*20 + min/100000)
waarin S de score is, p het percentage van de bereden kritieke verbindingen, t het aantal treinen en
m het totaal door alle treinen samen gereden aantal minuten in de lijnvoering.

Het totaal aantal verschillende trajecten hebben wij berekend op 2223. Dat is iets teveel om alles brute-force te controleren,
omdat het dan erg lang zou duren. Daarom experimenteren wij nu met pruning en algoritmes om daarmee de beste maximaal 7 trajecten te kiezen,
die voor de hoogste score zorgen.

Het eerste algoritme dat wij hebben gebruikt gaat als volgt; elk traject is apart in de Scorefunctie gestopt en de 20 trajecten met de hoogste score
zijn door middel van deep-breath gecombineerd en weer in de Scorefunctie gestopt. Hieruit komt een lijnvoering met de voor dit algoritme de beste score.

Momenteel zijn wij bezig andere algoritmes uit te werken.

