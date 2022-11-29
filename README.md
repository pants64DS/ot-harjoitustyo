# Ohjelmoijan laskin
Sovelluksesta tulee laskin, jolla voidaan laskea aritmeettisia lausekkeita tietokoneiden käyttämillä lukujärjestelmillä, kuten liukuluvuilla. Nykyinen versio tukee 32- ja 64-bittisten liukulukujen yhteen-, vähennys-, kerto- ja jakolaskua, jakojäännöstä, negaatiota sekä sulkeita, joilla voidaan muuttaa edellä mainittujen operaatioiden laskujärjestystä. 

## Dokumentaatio
* [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
* [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
* [Changelog](dokumentaatio/changelog.md)

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
