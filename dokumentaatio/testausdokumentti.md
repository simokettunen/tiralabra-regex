# Testausdokumentti

Ohjelman pystyy jakamaan seuraaviin peräkkäisiin toimintoihin:
1. Parsiminen: parsitaan säännöllinen lauseke syntaksipuuksi
2. Thompsonin algoritmi: muunnetaan syntaksipuu äärelliseksi epädeterministiseksi automaatiksi
3. Rabin–Scottin konstruktio: muunnetaan äärellinen epädeterministinen automaatti äärelliseksi deterministiseksi automaatiksi
4. Merkkijonon tarkastaminen: tarkastetaan äärellistä determinististä automaattia vasten, kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen.

## Parsinnan testaaminen
Parsinnan testaaminen on suoritettu yksikkötesteillä. Testitapaukset löytyvät testikansion tiedostosta [parser_test.py](../src/tests/parser_test.py). Jäsentimen testaamissa perusperiaatteena jäsentimelle annetaan syötteeksi säännöllinen lauseke merkkijonona, minkä jälkeen tarkastetaan, tuottiko jäsennin oikean jäsennyspuun. Yksikkötesteissä jokaiselle tiedostossa [props.py](../src/props.py) esitetylle säännölle, missä säännön vasen puoli on `empty`, `kleene`, `concatenation` ja `union`, on muodostettu oma yksikkötesti. Lisäksi on muodostettu yksi yksikkötesti säännöille, joissa vasen puoli on `single`, sillä kaikki nämä säännöt ovat käytännössä samanlaisia ainoana erona päätesymbolina käytetty merkki. Kaiki sallitut säännöllisen lausekkeen aakkoston merkit testataan kollektiivisesti kolmessa eri testitapauksessa.

Koska jäsentimessä oikean lopputuloksen saaminen riippuu joissain tapauksissa siitä, onko säännöllisessä lausekkeessa shift-toimenpiteessä juuri pinoon pushatun merkin jälkeen oleva seuraava merkki asteriski, *, eivät edellä mainitut sääntöihin perustuvat yksikkötestit eivät kata kaikkia mahdollisia tapauksia. Tällaisia ovat tilanteet, joissa säännöllisessä lausekkeessa konkatenaation jälkimmäisenä operandina on kaksinkertainen Kleenen tähti tai yhdisteen Kleenen tähti. Jokaiselle tällaiselle tilanteelle on tehty oma testitapaus, eli tilanteille, joissa konkatenaation ensimmäisenä operandina on tyhjä merkkijono, yksittäinen merkki, konkatenaatio, yhdiste tai Kleenen tähti ja toisena operandina kaksinkertainen Kleenen tähti tai yhdisteen Kleenen tähti.

Kaiki tilanteet, joissa yhdisteen jälkimmäinen operandi sisältää sulkuja, eivät myöskään sisälly edellä mainittujen yksikkötestien kattavuuteen. Näille tilanteille on tehty omat testitapaukset, ja näitä on esimerkiksi tilanteet, joissa yhdisteen jälkimmäinen operandi on yhdisteen Kleenen tähti tai kahden yhdisteen konkatenaatio.

## Thompsonin algoritmin testaaminen
Thompsonin algoritmin testaaminen on suoritettu yksikkötesteillä. Thompsonin algoritmi toimii rekursiivisesti perustuen jäsennyspuun solmun tyyppiin, joka voi olla tyhjä merkkijono, yksittäinen merkki, yhdiste, konkatenaatio tai Kleenen tähti. Yksikkötesteissä on oma testitapaus jokaiselle tyypille. Testitapauksissa muodostetaan tyyppiä vastaava jäsennyspuu, joka annetaan syötteenä Thompsonin algoritmille, ja testataan, muodostiko algoritmi jäsennyspuuta vastaavan NFA:n. NFA:sta tarkistetaan, NFA:n tilat, siirtymät sekä alkutila ja hyväksyvä tila.

## Rabin–Scottin algoritmin testaaminen
Rabin–Scottin algoritmi testaaminen on suoritettu yksikkötesteillä. Testitapauksissa syötteenä annetaan NFA ja tarkistetaan, tuottiko algoritmi oikean DFA:n. Testitapaukset on tehty seuraaville NFA:ille:
* NFA, joka sisältää kaksi tilaa, ja näiden välillä epsilon-siirtymä
* NFA, joka sisältää kaksi tilaa, ja näiden välillä tavallisen siirtymän
* NFA, joka sisältää yhdestä tilasta kaksi siirtymää
* NFA, joka sisältää kaksi peräkkäistä siirtymää
* NFA, joka sisältää silmukan

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
