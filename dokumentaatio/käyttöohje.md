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

Funktiolle `compile` annettavan säännöllisen lausekkeen syntaksia ei ole vielä dokumentoitu kattavasti. Säännöllinen lauseke voi koostua tällä hetkellä seuraavista merkeistä:
* `a`–`z`, `A`–`Z`, `0`–`9`, säännöllisen lausekkeen aakkoston merkit
* `.`, tyhjä merkkijono
* `|`, yhdiste
* `*`,  Kleenen tähti
* `(` ja `)`, säännöllisen lausekkeen merkkien ryhmittely

Esimerkkejä:
* `a`, pelkästä merkistä a koostuva säännöllinen lauseke
* `ab`, merkkien a ja b konkatenaatio
* `a|b`, merkkien a ja b yhdiste
* `a*`, merkin a Kleenen tähti
* `(ab)*`, merkkijonon ab Kleenen tähti
* `a(b|.)`, merkkijonot `a` ja `ab` tunnistava säännöllinen lauseke
* säännöllisiä lausekkeita kielelle, jonka aakkosto on {0, 1}:
    * `0*10*`, kieli, jossa jokainen merkkijono sisältää vain yhden kerran merkin 1
    * `(0|1)*1(0|1)*`, kieli, jossa jokainen merkkijono sisältää vähintään kerran merkin 1
    * `(0|1)*001(0|1)*`, kieli, jossa jokainen merkkijono sisältää osamerkkijonon 001
    * `((0|1)(0|1))*`, kieli, jossa jokaisen merkkijonon pituus on parillinen
    * `((0(0|1)*0|1(0|1)*1)|0)|1`, kieli jossa jokainen merkkijono alkaa ja loppuu samalla merkillä
