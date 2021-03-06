# Käyttöohjeet

Ohjelman asennus:
    
    poetry install
    
Ohjelman yksikkötestien suoritus:

    poetry run invoke unit-test
    
Ohjelman integraatiotestien suoritus:

    poetry run invoke integration-test
    
Ohjelman suorituskykytestien suoritus:

    poetry run invoke performance-test
    
Ohjelman testikattavuuden tulostus:

    poetry run invoke coverage-report
    
Ohjelman pylint-raportin tulostus:

    poetry run invoke pylint

## Käyttäminen käyttöliittymän kautta

Ohjelman suoritus:

    poetry run invoke start
    
Ohjelmassa on tekstipohjainen käyttöliittymä, joka sisältää seuraavat komennot:
* 1 – Säännöllisen lausekkeen kääntäminen DFA:ksi
* 2 – Merkkijonon testaaminen säännöllistä lausekketta vasten
* 3 – Ohjeiden tulostaminen
* 0 – Poistuminen ohjelmasta

## Käyttäminen suoraan kirjastona

Säännöllisen lausekkeen kääntäminen DFA:ksi onnistuu `src/utils.py`-moduulin funktiolla `compile`. Esimerkiksi

    from utils import compile
    regex = '(ab|aac)*'
    dfa = compile(regex)
    
Merkkijonon testaaminen säännöllistä lauseketta vasten onnistuu luokan `DFA` funktiolla `match`. Esimerkiksi

    dfa.match('ab')

## Säännöllisen lausekkeen syntaksi

Säännöllinen lauseke voi koostua tällä hetkellä seuraavista merkeistä:
* `a`–`z`, `A`–`Z`, `0`–`9`, säännöllisen lausekkeen aakkoston merkit
* `.`, tyhjä merkkijono
* `|`, yhdiste
* `*`,  Kleenen tähti
* `(` ja `)`, säännöllisen lausekkeen merkkien ryhmittely

Syntaksi mahdollistaa konkatenaation, yhdisteen ja Kleenen tähden seuraavasti:
* `ab`, konkatenaatio
* `a|b`, yhdiste
* `a*`, Kleenen tähti

Syntaksi sallii operaatioiden yhdistämisen. Mikäli jokin operaatio on toisen operaation sisällä, täytyy sisällä olevan operaation ympärillä olla sulut. Sulkujen täytyy olla mahdollisimman yksinkertaisessa muodossa. Yksittäistä merkkiä ei ympäröidä suluilla. Esimerkkejä:
* `(ab)*`, merkkien `a` ja `b` konkatenaation Kleenen tähti
* `a(b|.)`, merkkijonot `a` ja `ab` tunnistava säännöllinen lauseke
* `a|b` on sallittu säännöllinen lauseke, mutta `(a|b)` ei ole sallittu säännöllinen lauseke
* `a|(b|c)` on sallittu säännöllinen lauseke, mutta `(a)|(b|c)` ei ole sallitty säännöllinen lauseke

Esimerkkejä säännöllisistä lausekkeista kielelle, jonka aakkosto on {0, 1}:
* `0*10*`, kieli, jossa jokainen merkkijono sisältää vain yhden kerran merkin 1
* `(0|1)*1(0|1)*`, kieli, jossa jokainen merkkijono sisältää vähintään kerran merkin 1
* `(0|1)*001(0|1)*`, kieli, jossa jokainen merkkijono sisältää osamerkkijonon 001
* `((0|1)(0|1))*`, kieli, jossa jokaisen merkkijonon pituus on parillinen
* `((0(0|1)*0|1(0|1)*1)|0)|1`, kieli jossa jokainen merkkijono alkaa ja loppuu samalla merkillä
