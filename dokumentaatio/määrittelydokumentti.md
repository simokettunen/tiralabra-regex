# Määrittelydokumentti

## Johdanto

Projektissa toteutetaan säännöllisten lausekkeiden kääntäjä, joka muuntaa syötteenä saadun säännöllisen lausekkeen äärelliseksi deterministiseksi automaatiksi. Tälle annetaan syötteeksi merkkijono, jolloin saadaan tulokseksi tieto siitä, kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen. Ohjelmointikielenä projektissa käytetään Pythonia. Ohjelmassa laadittavat algoritmit ovat Thompsonin algoritmi sekä Rabin–Scottin konstruktio.

Säännöllisellä lausekkeella tarkoitetaan Sipserin (1997) esittämää määritelmää. Säännöllinen lauseke on jokin seuraavasti:

1. jokin aakkoston merkki
2. tyhjä merkkijono
3. tyhjä joukko
4. kahden säännöllisen lausekkeen yhdiste
5. kahden säännöllisen lausekkeen konkatenaatio
6. säännöllisen lausekkeen Kleenen tähti

## Ohjelman syötteet ja tulosteet

Ohjelmalle annetaan kaksi syötettä: säännöllinen lauseke sekä säännöllistä lauseketta vasten testattava merkkijono.

Säännöllinen lauseke on merkkijono, joka koostuu aakkoston merkeistä sekä mahdollisesti kontrollimerkeistä. Tässä vaiheessa aakkostoksi määritellään merkkien `a`–`z`, `A`–`Z` sekä `0`–`9` muodostama joukko. Kontrollimerkit ovat alustavasti seuraavat

* `|`, yhdiste
* `*`,  Kleenen tähti
* `(` ja `)`, säännöllisen lausekkeen merkkien ryhmittely

Konkatenaatiolle ei ole omaa kontrollimerkkiä, vaan kaksi aakkoston peräkkäistä merkkiä tulkitaan automaattisesti konkatenaatioksi.

Säännöllistä lauseketta vasten testattava merkkijono koostuu merkeistä `a`–`z`, `A`–`Z` sekä `0`–`9`.

Tulosteena ohjelma antaa tiedon siitä, kuuluuko säännöllistä lauseketta vasten testattava merkkijono kieleen, jonka säännöllinen lauseke muodostaa.

## Ohjelman toiminta ja vaativuusluokat

Alustavasti ohjelma toimii seuraavasti:

1. Annetaan ohjelmalle syötteeksi säännöllinen lauseke
2. Käännetään säännöllinen lauseke äärelliseksi epädeterministiseksi automaatiksi käyttäen Thompsonin algoritmia
3. Muunnetaan äärellinen epädeterministinen automaatti äärelliseksi deterministiseksi automaatiksi käyttäen Rabin–Scottin konstruktiota
4. Annetaan äärelliselle deterministiselle automaatille syötteeksi merkkijono
5. Ohjelma antaa tuloksen kuuluuko merkkijono säännöllisen lausekkeen muodostamaan kieleen

Tavoiteltavat aikavaativuudet ovat seuraavat:
* Thompsonin algoritmille *O*(|*r*|), missä *r* on säännöllinen lauseke
* Merkkijonon testaamiselle deterministiä automaattia vasten *O*(|*x*|), missä *x* on merkkijono

Rabin-Scottin konstruktio tuottaa pahimmassa mahdollisessa tapauksessa deterministisen automaatin, jossa 2<sup>*n*</sup> tilaa, kun epädeterministisessa automaatissa on *n* tilaa. Projektiin voisi mahdollisesti myös sisällyttää äärellisen deterministisen automaatin minimoinnin. Tämä olisi mahdollista muun muassa Hopcroftin, Mooren ja Brzozowskin algoritmeilla. 

## Muuta

Projektissa luonnollisen kielen kielivalinnat ovat seuraavat:
* Ohjelman vaadittavat dokumentaatiot tehdään suomen kielellä.
* Ohjelman kommentointi tehdään suomen kielellä.
* Projektin koodissa (muuttujien nimet, luokkien nimet yms.) käytetään englannin kieltä.

Vertaisarvioinnin pystyn tekemään Pythonin lisäksi Matlabilla, JavaScriptillä sekä Haskelilla tehtyihin projekteihin. Opinto-ohjelmani on matemaattisten tieteiden kandiohjelma, jossa opintosuuntanani on tietojenkäsittelyteoria.

## Lähteet
* Sipser, Michael. 1997. Introduction to the Theory of Computation. 1. painos. ISBN 0-534-94728-X
* [StackExchange](https://cs.stackexchange.com/questions/136477/doubt-in-understanding-the-time-complexities-of-algorithms-to-recognize-regular)
* [Wikipedia: DFA minimization](https://en.wikipedia.org/wiki/DFA_minimization)
* [Wikipedia: Powerset construction](https://en.wikipedia.org/wiki/Powerset_construction)
* [Wikipedia: Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
* [Wikipedia: Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)