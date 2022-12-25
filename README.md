# Ohjelmoijan laskin
Sovellus on laskin, jolla voidaan laskea aritmeettisia lausekkeita kahdella eri tietokoneiden käyttämällä lukujärjestelmällä, liukuluvuilla ja kiintoluvuilla. Nykyinen versio tukee erikokoisten liuku- ja kiintolukujen yhteen-, vähennys-, kerto- ja jakolaskua, jakojäännöstä, bittisiirtoja, negaatiota, sekä sulkeita, joilla voidaan muuttaa edellä mainittujen operaatioiden laskujärjestystä.

[Lopullisen palautuksen release](https://github.com/pants64DS/ot-harjoitustyo/releases/tag/viikko7)

## Dokumentaatio
* [Käyttöohje](dokumentaatio/kayttoohje.md)
* [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
* [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
* [Changelog](dokumentaatio/changelog.md)

## Asennus
Kun Python 3.8 ja Poetry ovat asennettuina, tarvittavat riippuvuudet voidaan asentaa suorittamalla komento:
```
poetry install
```

Tämän jälkeen ohjelma voidaan käynnistää komennolla:
```
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman suorittaminen:
```
poetry run invoke start
```

### Testien suorittaminen:
```
poetry run invoke test
```

### Testikattavuusraportin generointi:
```
poetry run invoke coverage-report
```

### Laatutarkistus:
```
poetry run invoke lint
```
