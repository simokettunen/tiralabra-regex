# Käyttöohjeet

Ohjelman asennus:
    
    poetry install

## Käyttäminen käyttöliittymän kautta

Ohjelman suoritus:

    python3 src/main.py
    
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
* `|`, yhdiste
* `*`,  Kleenen tähti
* `(` ja `)`, säännöllisen lausekkeen merkkien ryhmittely

Esimerkkejä:
* `a`, pelkästä merkistä a koostuva säännöllinen lauseke
* `ab`, merkkien a ja b konkatenaatio
* `a|b`, merkkien a ja b yhdiste
* `a*`, merkin a Kleenen tähti
* `(ab)*`, merkkijonon ab Kleenen tähti

Tyhjiin merkkijonoihin liittyviä ominaisuuksia ja toimintoja ei ole vielä implementoitu.
