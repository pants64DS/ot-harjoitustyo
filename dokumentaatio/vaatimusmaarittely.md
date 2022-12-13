# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksesta tulee laskin, jonka tarkoitus on auttaa ohjelmoijaa:
* Kokeilemaan, miten eri lausekkeet käyttäytyvät kun niitä lasketaan eri lukujärjestelmissä, joita tietokoneet käyttävät
* Selvittämään, tapahtuuko annetun lausekkeen laskennassa ylitsevuotoja tai pyöristysvirheitä
* Löytämään riittävän tarkka lukujärjestelmä halutun tarkkuuden saavuttamiseksi

## Käyttöliittymä ja ydintoiminnallisuudet
### :heavy_check_mark: Kaikki ydintoiminnallisuudet on toteutettu sarakkeiden poistoa lukuun ottamatta

Käyttäjän pitää siis pystyä määrittelemään eri lausekkeita, joita hän haluaa laskea, sekä eri lukujärjestelmiä, joilla laskenta tapahtuu. Sovelluksen käyttöliittymässä nämä vastaavat eräänlaisen taulukon rivejä ja sarakkeita, joita käyttäjä voi lisätä ja poistaa mielensä mukaan.

Ennen taulukon jokaista riviä on käyttäjän kirjoittama lauseke, ja sen jokainen solu näyttää kyseisen lausekkeen tuloksen tietyillä asetuksilla, jotka käyttäjä voi määritellä itse jokaiselle sarakkeelle erikseen. Sarakkeen asetuksiin kuuluu ainakin sen käyttämä lukujärjestelmä, mikä on perusversiossa joko 32- tai 64-bittiset liukuluvut. Perusversiossa laskin tukee ainakin yhteen-, vähennys-, kerto- sekä jakolaskua, joiden järjestystä voidaan muuttaa sulkeiden avulla.



## Jatkokehitysideoita

* Liukulukujen lisäksi laskin voisi tukea [kiintolukuja](https://en.wikipedia.org/wiki/Fixed-point_arithmetic), joille käyttäjä voisi vapaasti valita kokonais- ja murto-osien koot bitteinä. Tällöin kokonaisluvut saataisiin käyttöön asettamalla murto-osan kooksi nolla bittiä. Kokonaisosan bittien määrä voisi olla myös rajoittamaton.
    * Kiintoluvuille voitaisiin määritellä sarakkeen asetuksissa *pyöristysmoodi*, esimerkiksi "aina alaspäin", "aina ylöspäin", tai "aina kohti nollaa"
    * :heavy_check_mark: Tällä hetkellä laskin tukee kiintolukuja, joiden kokonaisosan bittien määrä on rajoittamaton. Käyttäjä pystyy valitsemaan murto-osan bittien määrän väliltä 0-65536
* Sarakkeen asetuksissa voitaisiin määritellä tuloksen esitysmuoto, kuten binääri-, desimaali- tai heksadesimaaliluvut. Liukuluvuille voisi olla vaihtoehto näyttää luvun esitys tietokoneen muistissa
  * Jos tuloksen saisi näiden lisäksi *little-endian* -muotoon, niin se olisi kätevä copy-pasteta heksaeditoriin
* Laskin voisi tukea myös bittioperaatioita, jakojäännöstä, neliöjuurta, itseisarvoa ja trigonometrisiä funktioita
    * :heavy_check_mark: Näistä on toteutettu bittisiirtoa vastaava operaatio (operaattorit `<<` ja `>>`) liukuluvuille
* Laskimessa voisi olla mahdollisuus tallentaa nykyinen sessio (eli kaikki rivit ja sarakkeet) tiedostoon tai tietokantaan
* Käyttöliittymästä tulisi joustavampi, jos rivien ja sarakkeiden paikkoja voitaisiin vaihtaa hiirellä raahaaten
* Olisi kätevää, jos tuloksen voisi kopioida leikepöydälle pelkästään klikkaamalla solua
