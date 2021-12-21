# Totetusdokumentti

## Yleisrakenne

Ohjelma kääntää syötteenä saadun säännöllisen lausekkeen äärelliseksi epädeterministiseksi automaatiksi, jota vasten voidaan tarkastaa, kuuluuko syötteenä annettu merkkijono säännöllisen lausekkeen muodostamaan kieleen. Kääntäminen koostuu seuraavista peräkkäisistä toiminnoista:
1. Jäsentäminen
2. Thompsonin algoritmi
3. Rabin–Scottin algoritmi

Kääntämisen vaiheet on esitetty kuvassa 1. Ohjelma saa syötteeksi säännöllisen lausekkeen tavallisena merkkijonoa. Jäsennin jäsentää säännöllisen lausekkeen jäsennyspuuksi. Thompsonin algoritmilla jäsennyspuusta muodostetaan äärellinen epädeterministinen automaatti (NFA). Rabin–Scottin algoritmi muuntaa äärellisen epädeterministisen automaatin äärelliseksi deterministiseksi automaatiksi (DFA). 

![compiling](./imgs/compiling.png)

**Kuva 1**: Kääntämisen vaiheet säännöllisestä lausekkeesta DFA:ksi.

Merkkijonon tarkastaminen säännöllistä lauseketta vasten on esitetty kuvassa 2. Rabin–Scottin algoritmin muodostama DFA on olio, joka on luokan `DFA` ilmentymä. Olio sisältää metodin `match`, jolla merkkijonon tarkastus tehdään. Metodi `match` antaa paluuarvona totuusarvon.

![matching](./imgs/matching.png)

**Kuva 2**: Merkkijonon tarkastaminen säännöllistä lauseketta vasten.

### Tietorakenteet

Ohjelmaan on implementoitu tietorakenteet jäsennyspuusta, äärellisestä epädeterministisestä automaatista ja äärellisestä deterministisestä automaatista.

Jäsennyspuu koostuu solmuista, joissa jokaisella solmulla voi olla nolla, yksi tai kaksi solmua riippuen sen tyypistä. Jos solmun tyyppi on konkatenaatio (`concatenation`) tai yhdiste (`union`), sisältää solmu kaksi lapsisolmua ja jos solmun tyyppi on Kleenen tähti (`kleene`), sisältää solmu yhden lapsisolmun. Solmun tyypillä yksittäinen merkki (`single`), ei ole yhtään lapsisolmua, vaan solmun tietovarastossa on kyseinen merkki. Samoin on myös solmun tyypillä tyhjä (`empty`), jolla ei ole yhtään lapsisolmua, vaan tietovarasto sisältää tyhjän merkin.

NFA ja DFA sisältävät tiedon automaatin tiloista, siirtymistä sekä aloitus- ja hyväksymistiloista. Sekä NFA että DFA sisältävät metodit uuden tilan ja uuden siirtymän lisäämiseen automaattin. Lisäksi NFA:ssa on toteuttu funktio, jolla kaikkien tilojen indekseihin voidaan lisätä jokin kokonaisluku.

NFA sisältää laskentafunktiot:
* epsilon-sulkeuma, jossa lasketaan kaikki tilat, joihin päästään syötteenä annetusta tilasta epsilon-siirtymillä
* siirtymä, jossa lasketaan kaikki tilat, joihin päästään annetusta tilajoukosta annetulla symbolilla

DFA sisältää seuraavan laskentafunktion:
* merkkijonon tarkastaminen DFA:n määrittää kieltä vasten

### Algoritmit

Syötteenä saatava säännöllinen lauseke on merkkijono, jonka tarkempi syntaksi on esitetty [käyttöohjeessa](./käyttöohje.md#säännöllisen-lausekkeen-syntaksi). Jäsennin on bottom-up shift-reduce -tyyppinen. Se käy syötteenä saadun merkkijonon merkki kerrallaan läpi, ja suorittaa merkeille aina shift-operaation, minkä jälkeen mahdollisesti yhden tai useamman reduce-operaation. Shift-operaatioissa merkki siirretään pinoon, ja reduce-operaatiossa pinon alkioita muunnetaan toisiksi alkioiksi säännöllisen lausekkeen merkkijonon sääntöjen mukaisesti. Mikäli säännöllisen lausekkeen syntaksi on ollut oikein, lopputuloksena pinon ainoa alkio on kokonainen jäsennyspuu.

Thompsonin algoritmi toimii rekursiivisesti ja saa syötteeksi jäsennyspuun juuren. Jos solmun tyyppi on `empty`tai `single`, konstruoidaan sitä vastaava NFA. Kummatkin lapsisolmut syötetään uudestaan Thompsonin algoritmille tyypeillä `concatenation` sekä`union` ja näistä saadut NFA:t yhdistetään uudeksi NFA:ksi. Tyypillä `kleene` toinen lapsisolmuista syötetään Thompsonin algoritmille ja lopputuloksesta konstruoidaan uusi NFA.

Rabin–Scottin algoritmissa määritetään ensin NFA:n aloitustilan epsilon-sulkeuma, ja tästä muodostetaan DFA:n aloitustila. Epsilon-sulkeumasta määritetään eri symboleille siirtymien epsilon-sulkeumat, ja jos tuloksena on sellainen epsilon-sulkeuma, lisätään se DFA:n uudeksi tilaksi. Prosessia jatketaan niin kauan, kunnes kaikki epsilon-sulkeumat ovat käsitelty, eikä uusia enää ole.

Merkkijonon tarkastus tapahtuu luokan `DFA` funktiolla `match`. Merkkijono käydään merkki kerrallaan läpi ja siirrytään siirtymätaulukon mukainen siirtymä tarkastelun alla olevan merkin ja tilan perusteella. Merkkijono hyväksytään, jos kaikkien merkkien läpikäymisen jälkeen viimeisenä tilana on jokin hyväksyvistä tiloista, muuten merkkijono hylätään.

## Saavutetut aika- ja tilavaativuudet

TODO

## Puutteet ja parannusehdotukset

Ohjelmassa on havaittu seuraavat puutteet:
* Jäsennin vaatii, että säännöllisen lausekkeen sulut ovat mahdollisimman sievennetyt. Esimerkiksi säännöllinen lauseke `(a*)|b` tuottaa syntaksivirheen. Ohjelma hyväksyy yhtäpitävän säännöllisen lausekkeen `a*|b`.
* Jäsennin ei hyväksy mielivaltaista määrää yhdisteitä ilman sulkujen käyttöä. Esimerkiksi `a|b|c` tuottaa syntaksivirheen. Ohjelma hyväksyy yhtäpitävät säännölliset lausekkeet `(a|b)|c` sekä `a|(b|c)`. 

Parannusehdotukset:

* Pahimmassa tapauksessa Rabin–Scottin algoritmi saattaa tuotta *n* tilaa sisältävästä NFA:sta DFA:n, joka sisältää 2<sup>*n*</sup> tilaa. Määrittelydokumentissa mahdollisesti toteuttavaksi ehdotettua DFA:n tilojen minimointia ei ole toteuttu, sillä projektin laajuus on jo tällä toteutuksella kattava. Ahon et al. (2007, s. 153) mukaan tilojen eksponentiaalinen kasvu ei tule käytännössä ongelmaksi, sillä *-- part of the power of the automaton-based approach to lexical analysis is that for real languages, the NFA and DFA have approximately the same number of states, and the exponential behavior is not seen*. Ongelmaa ei ole myöskään havaittu ohjelmassa.

## Lähteet
* Aho, Alfred V.; Lam, Monica S.; Sethi, Ravi; Ullman, Jeffrey D. 2007. Compilers : Principles, Techinques & Tools. 2. painos. ISBN 0-321-49169-6.
* Sipser, Michael. 1997. Introduction to the Theory of Computation. 1. painos. ISBN 0-534-94728-X