# Viikkoraportti 2

Toisella viikolla alustin projektin sekä aloitin ohjelman toteuttamista. Tällä hetkellä ohjelma sisältää Thompsonin algoritmin, joka syötteenä saadusta syntaksipuusta palauttaa sitä vastaavan äärellisen epädeterministisen automaatin.

Seuraavalla viikolla aion toteuttaa alustavan version jäsentimestä, joka muuntaa syötteenä saadun säännöllisen lausekkeen merkkijonon sopivaksi syntaksipuuksi. Lisäksi aion toteuttaa myös alustavan version Rabin–Scottin algoritmista. Projektissa tulen ottamaan lisäksi käyttöön pylintin koodin laadun seuraamista varten sekä docstringin. Koodin kommentointi ei ole kovin kattavaa tällä hetkellä, mutta parantuu docstringin käyttöönoton myötä.

Tällä hetkellä ei ole merkittäviä haasteita. Tosin pohdinnan alla on, kuinka yllä mainittu jäsennin kannattaisi toteuttaa.

Aikaa viikolla 2 käytin noin 15 tuntia.

Ohessa tämänhetkinen testauskattavuus:

$ coverage report -m
Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
src/main.py          34     34      2      0     0%   1-48
src/nfa.py           85      1      8      2    97%   94, 116->119, 119->122
src/parser.py        12      5      4      0    44%   9-15
src/thompson.py      17      0     10      1    96%   21->exit
-------------------------------------------------------------
TOTAL               148     40     24      3    72%