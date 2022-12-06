# Changelog

## Viikko 3

* Tehty `Evaluator`-luokka, joka laskee aritmeettisten lausekkeiden arvoja
    * Lausekkeessa voi olla numeroita, sulkumerkkejä, unaarisia operaattoreita `+` ja `-` sekä binäärisiä operaattoreita `+`, `-`, `*`, `/` ja `%`
    * Nämä operaatiot, niiden laskujärjestys sekä sulkumerkit toimivat niin kuin voisi olettaa
    * Luokalle on kattavat testit

* Aloitettu graafisen käyttöliittymän toteutus
    * Käyttöliittymässä on aluksi yksi rivi, jonka vasemmassa laidassa on tekstikenttä
    * Käyttäjä voi kirjoittaa kenttään lausekkeen, jolloin sen arvo lasketaan käyttäen `Evaluator`-luokkaa ja näytetään käyttäjälle
    * Käyttäjä voi lisätä uusia rivejä painamalla enteriä
    * Kursoria voi siirtää riviltä toiselle hiiren tai eri näppäinten avulla

## Viikko 4

* Jaettu käyttöliittymän taulukon koodi `Table`- `Row`- ja `Column`- luokkiin
* Sarakkeita voi lisätä painamalla Ctrl+N
* Jokaiselle sarakkeelle voi asettaa lukujärjestälmäksi 32- tai 64-bittiset liukuluvut

## Viikko 5

* Jokaisen sarakkeen asetuksille on oma ikkuna, joka avautuu klikkaamalla sarakkeen päällä olevaa nappia
* Ikkunassa voidaan valita 16-, 32- tai 64-bittiset liukuluvut
* Ikkuna on toteutettu siten, että siihen on myöhemmin helppo lisätä eri näkymä kiintoluvuille ja niiden asetuksille
