# Testausdokumentti

Ohjelman pystyy jakamaan seuraaviin peräkkäisiin toimintoihin:
1. Parsiminen: parsitaan säännöllinen lauseke syntaksipuuksi
2. Thompsonin algoritmi: muunnetaan syntaksipuu äärelliseksi epädeterministiseksi automaatiksi
3. Rabin–Scottin konstruktio: muunnetaan äärellinen epädeterministinen automaatti äärelliseksi deterministiseksi automaatiksi
4. Merkkijonon tarkastaminen: tarkastetaan äärellistä determinististä automaattia vasten, kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen.

## Parsinnan testaaminen

Tällä hetkellä parsintaa ei ole implementoitu.

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

## Muut testaukset

Yksikkötestejä on tehty luokille `NFA` ja `DFA`.

