# Viikkoraportti 4

Neljännellä viikolla toteutin viimein säännöllisen lausekkeen jäsentimen, joka muuntaa syötteeksi saadun säännöllisen lausekkeen abstraktiksi syntaksipuuksi Thompsonin algoritmia varten. Jäsentimen laatiminen oli vaativampi tehtävä kuin mitä odotin, mutta lopputuloksena syntyi onnistuneesti bottom-up shift-reduce -tyyppinen jäsennin lisättynä muutamalla omalla säännöllä. Jonkin verran meni aikaa myös kirjan Compilers: Principles, Techniques, & Tools lukemiseen, josta tuli ainakin opittua erilaisten jäsentimien periaatteita. Erityisen mielenkiintoinen aihe, mutta tarkempaan tutustumiseen esimerkiksi LR- tai LL-jäsentimen kehittämisen myötä ei valitettavasti tämän projektin puitteissa aika riitä teknisten yksityiskohtien runsauden ja aiemman kokemuksen puutteen takia. Jäsentimeen kirjoitin yksikkötestit eri operaattoreiden kombinaatioille (esim. yksittäisen merkin ja Kleenen tähden konkatenaatio tai kahden yhdisteen yhdiste).

Ohjelmassa on nyt käytännössä toteutettu kaikki vaatimusmäärittelyssä esitetyt toimintavaiheet. Tällä hetkellä ohjelma toimii siis seuraavasti:
1. annetaan syötteenä säännöllinen lauseke
2. säännöllinen lauseke jäsennetään syntaksipuuksi jäsentimellä
3. syntaksipuusta konstruoidaan NFA Thompsonin algoritmilla
4. NFA muunnetaan DFA:ksi Rabin–Scottin konstruktiolla
5. testataan DFA:lla kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen

Tällä hetkellä käytännössä siis annetaan säännöllinen lauseke funktiolle `compile`, joka kääntää lausekkeen DFA:ksi, minkä jälkeen voidaan testata merkkijono DFA:n funktiolla `match`:

    dfa = compile('(ab|aac)*')
    print(dfa.match('ab'))       # True
    print(dfa.match('aac'))      # True
    print(dfa.match('abaac'))    # True
    print(dfa.match('aacaac'))   # True
    print(dfa.match('a'))        # False
    print(dfa.match('acab'))     # False
    
Seuraavalla viikolla aion lähteä tutkimaan suorituskykytestausta. Rabin–Scottin algoritmista on jäänyt yksikkötestit laatimatta, joten ne pitää tehdä.

Aikaa viikolla 4 käytin noin 19 tuntia.

Ohessa tämänhetkinen testauskattavuus:

    $ coverage report -m
    Name                 Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------------
    src/dfa.py              25      1      8      1    94%   14, 28->27
    src/main.py             21     21      2      0     0%   1-26
    src/nfa.py             101      1     18      2    97%   96, 118->121, 121->124
    src/parser.py          111      2     52      4    96%   21, 57->61, 73->76, 99->103, 163
    src/rabin_scott.py      43     39     16      0     7%   5-13, 17-62
    src/rules.py             1      0      0      0   100%
    src/thompson.py         17      0     10      1    96%   21->exit
    ----------------------------------------------------------------
    TOTAL                  319     64    106      8    79%
