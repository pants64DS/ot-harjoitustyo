# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on laskin, jonka tarkoitus on auttaa ohjelmoijaa:
* Kokeilemaan, miten eri lausekkeet käyttäytyvät kun niitä lasketaan eri esitysmuodoilla
* Selvittämään, tapahtuuko annetun lausekkeen laskennassa pyöristysvirheitä
* Löytämään riittävän tarkka lukujärjestelmä halutun tarkkuuden saavuttamiseksi

## Käyttöliittymä

Käyttäjä pystyy kirjoittamaan eri lausekkeita, joita hän haluaa laskea, sekä valitsemaan eri esitysmuotoja, joilla laskenta tapahtuu. Sovelluksen käyttöliittymässä nämä vastaavat eräänlaisen taulukon rivejä ja sarakkeita. Jokaisen rivin alussa on tekstikenttä, johon käyttäjä voi kirjoittaa lausekkeen. Jokaisen sarakkeen yläpuolella on nappi, jota painamalla avautuu ikkuna, josta voidaan muokata sarakkeen asetuksia. Sovelluksen käynnistyttyä sen pääikkunassa on yksi rivi ja yksi sarake. Käyttäjä voi lisätä valitun rivin alle uuden rivin painamalla Enteriä. Hän voi myös lisätä taulukkoon uusia sarakkeita painamalla Ctrl+N. Jos kaikki rivit tai sarakkeet eivät mahdu ikkunaan, käyttäjä pystyy selaamaan niitä ikkunan ala- ja oikeassa laidassa olevien vierityspalkkien avulla.

## Esitysmuodot
Sarakkeen asetusikkunassa käyttäjä voi valita joko [kiintoluvut](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) tai 16-, 32- tai 64-bittiset liukuluvut. Kiintolukujen murto-osan bittien määrä voidaan valita vapaasti väliltä 0-65536 ja kokonaisosan koko on rajoittamaton. Kiintoluvuilla voidaan myös valita, kuinka monen desimaalin tarkkuudella tulos näytetään.

## Lausekkeet ja operaatiot
Laskin tukee seuraavia operaatioita:
   * Yhteenlasku binäärisellä operaattorilla `+`
   * Vähennyslasku binäärisellä operaattorilla `-`
   * Kertolasku binäärisellä operaattorilla `*`
   * Jakolasku binäärisellä operaattorilla `/`
   * Bittisiirto vasemmalle binäärisellä operaattorilla `<<`
   * Bittisiirto oikealle binäärisellä operaattorilla `>>`
   * Negaatio (eli vastaluku) unaarisella operaattorilla `-`
   * Unaarinen operaattori `+`, joka palauttaa luvun muuttumattomana

Liukuluvuilla operaattorit `<<` ja `>>` vastaavat kertomista ja jakamista kahden potensseilla, ei luvun esitysmuodon bittien siirtämistä. Kiintoluvuilla operaattori `>>` säilyttää etumerkin.

Lausekkeessa operaattorit noudattavat seuraavaa laskujärejstystä:
   1. Unaariset operaattorit `+` ja `-`
   2. Binääriset operaattorit `*`, `/` ja `%`
   3. Binääriset operaattorit `+` ja `-`
   4. Binääriset operaattorit `<<` ja `>>`

Tätä järjestystä voidaan kuitenkin muuttaa sulkeiden avulla. Jokainen sulkeilla rajattu alilauseke lasketaan kuin se olisi oma lausekkeensa.

## Jatkokehitysideoita

* Kiintoluvuilla kokonaisosan bittien määrää voisi pystyä rajoittamaan. Tällöin laskimella voitaisiin simuloita kiintolukujen ylivuotoa.
* Kiintoluvuille voitaisiin määritellä sarakkeen asetuksissa *pyöristysmoodi*, esimerkiksi "aina alaspäin", "aina ylöspäin", tai "aina kohti nollaa"
* Sarakkeen asetuksissa voitaisiin määritellä tuloksen esitysmuoto, kuten binääri-, desimaali- tai heksadesimaaliluvut. Kiintoluvuille tämä toiminnallisuus on oikeastaan jo toteutettu, mutta puuttuu vielä käyttöliittymästä.
* Näytettävien murto-osan numeroiden määrän voisi pystyä valitsemaan myös liukuluvuille.
* Lausekkeen tuloksesta voitaisiin pystyä näyttämään myös sen sisäinen esitysmuoto muistissa, esimerkiksi *little-endian* -muodossa.
* Laskin voisi tukea myös neliöjuurta, itseisarvoa, trigonometrisiä funktioita, sekä binäärisiä "and"-, "or"-, "xor"- ja "not"-operaatioita.
* Laskimessa voisi olla mahdollisuus tallentaa nykyinen sessio (eli kaikki rivit ja sarakkeet) tiedostoon.
* Käyttöliittymästä tulisi joustavampi, jos rivien ja sarakkeiden paikkoja voitaisiin vaihtaa hiirellä raahaten.
* Olisi kätevää, jos tuloksen voisi kopioida leikepöydälle klikkaamalla solua
* Olisi myös kätevää, jos lausekkeen tulos voitaisiin laskea liuku- ja kiintolukujen lisäksi myös mielivaltaisella tarkkuudella. Tällöin käyttäjä ei tarvitsisi toista laskinta tähän tarkoitukseen.
