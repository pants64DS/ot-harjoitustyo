# Ohjelmoijan laskin
Sovelluksesta tulee laskin, jolla voidaan laskea aritmeettisia lausekkeita tietokoneiden käyttämillä lukujärjestelmillä, kuten liukuluvuilla. Nykyinen versio tukee 16-, 32- ja 64-bittisten liukulukujen yhteen-, vähennys-, kerto- ja jakolaskua, jakojäännöstä, negaatiota, "bittisiirtoja" vasemmalle ja oikealle sekä sulkeita, joilla voidaan muuttaa edellä mainittujen operaatioiden laskujärjestystä.

[Viikon 5 release](https://github.com/pants64DS/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
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
