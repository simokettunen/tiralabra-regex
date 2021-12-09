# Testausdokumentti

Ohjelman pystyy jakamaan seuraaviin peräkkäisiin toimintoihin:
1. Parsiminen: parsitaan säännöllinen lauseke syntaksipuuksi
2. Thompsonin algoritmi: muunnetaan syntaksipuu äärelliseksi epädeterministiseksi automaatiksi
3. Rabin–Scottin konstruktio: muunnetaan äärellinen epädeterministinen automaatti äärelliseksi deterministiseksi automaatiksi
4. Merkkijonon tarkastaminen: tarkastetaan äärellistä determinististä automaattia vasten, kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen.

## Parsinnan testaaminen
Parsinnan testaaminen on suoritettu yksikkötesteillä. Yksikkötesteissä on testitapauksen seuraaville:
* yksittäinen merkki
* Kleenen tähti yksittäiselle merkille, yhdisteelle, konkatenaatiolle ja Kleenen tähdelle
* konkatenaatio seuraavien operaatioiden kombinaatioille: yksittäinen merkki, yhdiste, konkatenaatio, Kleenen tähti
* yhdiste seuraavien operaatioiden kombinaatioille: yksittäinen merkki, yhdiste, konkatenaatio, Kleenen tähti

## Thompsonin algoritmin testaaminen
Thompsonin algoritmin testaaminen on suoritettu yksikkötesteillä. Yksikkötesteissä on testitapaukset seuraaville toiminnoille:
* tyhjä merkkijono
* yksittäinen merkki
* kahden säännöllinen lausekkeen yhdiste
* kahden säännöllisen lausekkeen konkatenaatio
* säännöllisen lausekkeen Kleenen tähti

Yksikkötesteissä muodostetaan syntaksipuu, joka sisältää operaation, jonka jälkeen siitä muodostetaan NFA.

## Rabin–Scottin algoritmin testaaminen

Yksikkötestejä tehty luokalle `Parser`.

## Merkkijonon tarkastaminen

Tällä hetkellä testausta ei ole tehty.

## Muut yksikkötestaukset

Yksikkötestejä on tehty luokille `NFA` ja `DFA`.

## Suoriuskykytestaus

Suorituskykyä on testattu tiedostossa `src/performance_test.py`.

Suorituskykyä on testattu merkkijonon testaamiselle säännöllisen lausekkeen muodostamaa kieltä vasten. Testauksessa on muodostettu DFA säännölliselle lausekkeelle `a*` ja testattu a-merkeistä koostuvan merkkijonon kuulumista säännöllisen lausekkeen muodostamista kieleen. Syötteen pituus alkaa pituudesta 1 kasvaen aina kertaluokalla ja päättyen pituuteen 10&nbsp;000&nbsp;000. Tuloksista nähdään, että merkkijonon testaamisella säännöllistä lauseketta vasten on aikavaativuus *O*(|*x*|), missä *x* on merkkijono.

    Input length  Time (s)
               1  2.1457672119140625e-06
              10  3.0994415283203125e-06
             100  1.71661376953125e-05
            1000  0.00016236305236816406
           10000  0.00165557861328125
          100000  0.01728367805480957
         1000000  0.1640462875366211
        10000000  1.6296327114105225
