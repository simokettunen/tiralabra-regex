# Viikkoraportti 6

Kuudennella viikolla kävin läpi vertaisarvioinnissa saadut kommentit ja tein muokkauksia sen perusteella, esimerkiksi otin Codecovin käyttöön. Lisäksi laajensin ohjelmaa siten, että myös tyhjät merkkijonot otetaan huomioon. Tämän myötä löysin ohjelmasta yhden bugin Rabin–Scottin algoritmista, ilman korjausta ohjelma ei olisi hyväksynyt tyhjää merkkijonoa silloin kun olisi pitänyt. Tämä viikko jäi hieman vajaaksi kiireiden vuoksi. Dokumentaatiota laajensin jonkin verraus toteutusdokumentin osalta ja tein pieniä päivityksiä muihin dokumentteihin. Suorituskykytestausta en ehtinyt jatkaa.

Seuraavalla viikolla aion jatkaa suorituskykytestausta ja dokumentointia. Lisäksi aion suorittaa toisen vertaisarvionnin.

Aikaa viikolla 6 käytin noin 6 tuntia.

Ohessa tämänhetkinen testauskattavuus:

    $ coverage report -m
    Name                            Stmts   Miss Branch BrPart  Cover   Missing
    ---------------------------------------------------------------------------
    src/algorithms/parser.py          112      1     54      3    98%   19, 65->69, 81->84, 107->111
    src/algorithms/rabin_scott.py      45      0     18      0   100%
    src/algorithms/thompson.py         17      0     10      1    96%   23->exit
    src/entities/dfa.py                33      1     14      0    98%   16
    src/entities/nfa.py               101      1     18      2    97%   103, 128->131, 131->134
    src/entities/node.py               14      1      6      1    90%   19
    ---------------------------------------------------------------------------
    TOTAL                             322      4    120      7    98%
