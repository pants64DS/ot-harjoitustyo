# Käyttöohje

## Asennus
Kun Python 3.8 ja Poetry ovat asennettuina, tarvittavat riippuvuudet voidaan asentaa suorittamalla komento:
```
poetry install
```

Tämän jälkeen ohjelma voidaan käynnistää komennolla:
```
poetry run invoke start
```

## Käyttäminen
* Kun käynnistät sovelluksen, siinä on yksi rivi ja yksi sarake.
* Rivejä saa lisää painamalla Enteriä kun jonkin rivin tekstikenttä on aktiivinen.
* Sarakkeita saa lisää painamalla Ctrl+N.
* Jokaisen rivin tekstikentän lauseke lasketaan jokaiselle sarakkeelle erikseen.
* Laskin tukee yhteen-, vähennys-, kerto- ja jakolaskua, negaatiota sekä operaattoreita `<<` ja `>>`, jotka vastaavat kertomista ja jakamista kahden potensseilla. Lisää tuetuista operaatioista voit lukea [vaatimusmäärittelyssä](vaatimusmaarittely.md#lausekkeet-ja-operaatiot).
* Rivejä pystyy selamaan nuolinäppäimillä sekä Tabilla ja Shift+Tabilla.
* Klikkaamalla sarakkeen otsikkoa pääset muokkaamaan sen asetuksia.
* Voit valita sarakkeen asetuksista joko 16-, 32- tai 64-bittiset liukuluvut tai kiintoluvut, joiden kokonaisosassa on rajoittamaton määrä bittejä ja murto-osassa on valitsemasi määrä.
* Kun kirjoitat kiintoluvun käyttäen desimaalipistettä, se pyöristetään lähimpään esitettävissä olevaan lukuun tai rajatapauksissa ylospäin.
* Kerto- ja jakolaskuissa kiintoluvut pyöristyvät aina alaspäin.
