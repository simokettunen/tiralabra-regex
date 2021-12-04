# Viikkoraportti 4

Viidennellä viikolla eniten aikaa kului vertaisarvioitavaan projektiin tutustumiseen ja sen katselmointiin. Omaan projektiini lisäsin puuttuvat testit Rabin–Scottin algoritmilta. Lisäksi toteutin yksinkertaisen tekstipohjaisen käyttöliittymän. Käyttäliittymässä on toiminnot säännöllisen lausekkeen kääntämiseksi DFA:ksi ja merkkijonon testaaminen säännöllistä lauseketta vasten.

Aiemmin säännöllisen lausekkeen oli mahdollista koostua vain merkeistä `a`–`d`, mutta nyt ohjelma sallii vaatimusmäärittelyssä esitetyt merkit `a`–`z`, `A`–`Z` ja `0`–`9`. Tämän jälkeen huomasin, että viime viikolla tekemässä suorituskykytestissä merkkijonon testaukseen kuluva aika kymmenkertaistui. Refaktoroin hieman tapaa, jolla DFA:ssa oli tallessa kahden tilan väliset siirtymät, jolloin pääsin takaisin samaan samaan, tai oikeastaan pikkuisen parempaan suorituskykyyn.

Vertaisarvioinnissa sain hyviä kommentteja ja aion käydä ne läpi ensi viikolla. Lisäksi seuraavalla viikolla aion jatkaa suorituskykytestausta ja dokumentointia. Tyhjiin merkkijonoihin liittyvät toiminnallisuudet ja ominaisuudet on jäänyt tekemättä, joten ne pitää vielä lisätä.

Aikaa viikolla 5 käytin noin 17 tuntia vertaisarviointi mukaan lukien.

Ohessa tämänhetkinen testauskattavuus:

    $ coverage report -m
    Name                 Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------------
    src/dfa.py              33      1     14      0    98%   16
    src/main.py             35     35     12      0     0%   1-47
    src/nfa.py             101      1     18      2    97%   103, 128->131, 131->134
    src/parser.py          111      2     52      4    96%   23, 61->65, 77->80, 103->107, 171
    src/rabin_scott.py      43      0     16      0   100%
    src/rules.py             1      0      0      0   100%
    src/thompson.py         17      0     10      1    96%   23->exit
    src/utils.py             9      5      0      0    44%   8-12
    ----------------------------------------------------------------
    TOTAL                  350     44    122      7    87%
