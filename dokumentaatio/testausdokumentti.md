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

Tällä hetkellä testausta ei ole tehty.

## Merkkijonon tarkastaminen

Tällä hetkellä testausta ei ole tehty.

## Muut yksikkötestaukset

Yksikkötestejä on tehty luokille `NFA` ja `DFA`.

## Suoriuskykytestaus

Suorituskykyä on testattu tiedostossa `src/performance_test.py`.

Suorituskykyä on testattu merkkijonon testaamiselle säännöllisen lausekkeen muodostamaa kieltä vasten. Testauksessa on muodostettu DFA säännölliselle lausekkeelle `a*` ja testattu a-merkeistä koostuvan merkkijonon kuulumista säännöllisen lausekkeen muodostamista kieleen. Syötteen pituus alkaa pituudesta 1 kasvaen aina kertaluokalla ja päättyen pituuteen 10&nbsp;000&nbsp;000. Tuloksista nähdään, että merkkijonon testaamisella säännöllistä lauseketta vasten on aikavaativuus *O*(|*x*|), missä *x* on merkkijono.

    $ python3 src/performance_test.py
    Pituus   Aika (s)
           1 1.1920928955078125e-06
          10 3.814697265625e-06
         100 2.9802322387695312e-05
        1000 0.00029349327087402344
       10000 0.0029954910278320312
      100000 0.029306888580322266
     1000000 0.2908966541290283
    10000000 2.8829681873321533
