## Käyttöohjeet

Ohjelman asennus:
    
    poetry install
    
Ohjelman suoritus:

    python3 src/main.py
    
Säännöllisen lausekkeen kääntäminen DFA:ksi onnistuu `src/utils.py`-moduulin funktiolla `compile`. Esimerkiksi

    from utils import compile
    regex = '(ab|aac)*'
    dfa = compile(regex)
    
Merkkijonon testaaminen säännöllistä lauseketta vasten onnistuu luokan `DFA` funktiolla `match`. Esimerkiksi

    dfa.match('ab')
    
Funktiolle `compile` annettavan säännöllisen lausekkeen syntaksia ei ole vielä dokumentoitu kattavasti. Säännöllinen lauseke voi koostua tällä hetkellä seuraavista merkeistä:
* `a`, `b`, `c`, `d`, säännöllisen lausekkeen aakkoston merkit
* `|`, yhdiste
* `*`,  Kleenen tähti
* `(` ja `)`, säännöllisen lausekkeen merkkien ryhmittely

Esimerkkejä:
* `a`, pelkästä merkistä a koostuva säännöllinen lauseke
* `ab`, merkkien a ja b konkatenaatio
* `a|b`, merkkien a ja b yhdiste
* `a*`, merkin a Kleenen tähti
* `(ab)*`, merkkijonon ab Kleenen tähti