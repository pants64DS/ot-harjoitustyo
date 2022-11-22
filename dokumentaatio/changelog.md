# Changelog

## Viikko 3

* ### Tehty `Evaluator`-luokka, joka laskee aritmeettisten lausekkeiden arvoja
    * Lausekkeessa voi esiintyä *literaaleja* eli numeroita, sulkumerkkejä, unaarisia operaattoreita `+` ja `-` sekä binäärisiä operaattoreita `+`, `-`, `*`, `/`, ja `%`.
    * Nämä operaatiot, niiden laskujärjestys sekä sulkumerkit toimivat niin kuin voisi olettaa.
    * Jos oikean ja vasemman puoleiset sulut eivät sovi yhteen, lausekkeen molemmille puolille lisätään juuri niin paljon sulkeita että ne täsmäävät. Tämä tekee lausekkeiden kirjoittamisesta helpompaa käyttäjälle.
    * Luokalle on kattavat testit:
        * Yhdessä niistä lasketaan kaikki mahdolliset alle kahdeksan merkin pituiset lausekkeet tietyin rajoituksin ja verrataan tulosta Pythonin sisäänrakennetun `eval`-funktion tulokseen samalla lausekkeella. Testattavien lausekkeiden maksimipituutta ja sallittuja lukuja ja operaattoreita on helppo muuttaa, mutta testin suoritusaika voi kasvaa tällöin hyvin rajusti.
        * Muissa testeissä eri laskutoimituksia testataan erikseen, mutta jokaisessa käydään läpi monia eri lukuja.
* ### Aloitettu graafisen käyttöliittymän toteutus
    * Käyttöliittymässä on aluksi yksi rivi, jonka vasemmassa laidassa on tekstikenttä.
    * Kun tekstikenttään kirjoittaa lausekkeen, sen arvo lasketaan käyttäen `Evaluator`-luokkaa ja näytetään käyttäjälle kentän oikealla puolella.
        * Lausekkeen tulos päivittyy aina kun sitä muutetaan, eli sen nähdäkseen ei tarvitse erikseen painaa mitään.
        * Jos lauseke ei ole kelvollinen, näytetäänkin teksti "Invalid".
        * Jos lausekkeessa tapahtuu nollalla jako, näytetäänkin teksti "Undefined". Tämä todennäköisesti muuttuu jatkossa, koska liukuluvuilla nollalla jako on määritelty.
    * Kun tietyn rivin tekstikenttä on aktiivinen ja käyttäjä painaa enteriä, sen alle ilmestyy uusi vastaavanlainen rivi. Kursori siirtyy heti uudelle riville.
    * Kursoria voi siirtää hiiren lisäksi näppäimistön avulla:
        * Alanuolinäppäin siirtää kursoria yhden rivin alammas, ellei se ole viimeisellä rivillä.
        * Ylänuolinäppäin siirtää kursoria yhden rivin ylemmäs, ellei se ole ensimmäisellä rivillä.
        * Tab siirtää kursoria yhden rivin alemmas tai ensimmäiselle riville, jos se on viimeisellä rivillä.
        * Shift+tab siirtää kursoria yhden rivin ylemmäs tai viimeiselle riville, jos se on ensimmäisellä rivillä.
        * Ctrl+home siirtää kursorin ensimmäiselle riville.
        * Ctrl+end siirtää kursorin viimeiselle riville.
