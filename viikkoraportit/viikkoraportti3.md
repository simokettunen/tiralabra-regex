# Viikkoraportti 3

Kolmannella viikolla toteutin ohjelmaan Rabin–Scottin algoritmin, joka luo syötteenä annetusta äärellisestä epädeterministisestä automaatista äärellisen deterministisen automaatin. Alustavaa parsinta-algoritmia en ehtinyt vielä tehdä, mutta käytin muutaman tunnin aiheeseen tutustumiseen Aho et al. kirjasta Compilers: Principles, Techniques, & Tools. Ohjelmassa on otettu käyttöön pylint koodin laadun varmistamiseksi, mutta docstringejä en ehtinyt kirjoitella.

Seuraavalla viikolla aion saada ohjelman ydintoiminnallisuuden valmiiksi. Käytännössä tämä tarkoittaa sopivan parsinta-algoritmin laatimista.

Aikaa viikolla 3 käytin noin 8 tuntia.

Ohessa tämänhetkinen testauskattavuus:

    Name                 Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------------
    src/dfa.py              25      1      8      1    94%   12, 26->25
    src/main.py             21     21      2      0     0%   1-26
    src/nfa.py             101      1     18      2    97%   94, 116->119, 119->122
    src/parser.py           12      5      4      0    44%   9-15
    src/rabin_scott.py      43     39     16      0     7%   5-13, 17-62
    src/thompson.py         17      0     10      1    96%   21->exit
    ----------------------------------------------------------------
    TOTAL                  219     67     58      4    66%
