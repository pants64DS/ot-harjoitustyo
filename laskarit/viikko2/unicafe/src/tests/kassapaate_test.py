import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_alussa_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_lisaa_riittavan_maksun_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)

    def test_syo_edullisesti_kateisella_palauttaa_riittavan_maksun_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha, 0)

        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)

    def test_syo_edullisesti_kateisella_merkitsee_myydyn_lounaan(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_ei_muuta_mitaan_kun_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_palauttaa_riittamattoman_maksun(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(vaihtoraha, 239)

    def test_syo_maukkaasti_kateisella_lisaa_riittavan_maksun_kassaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)

    def test_syo_maukkaasti_kateisella_palauttaa_riittavan_maksun_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha, 0)

        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_merkitsee_myydyn_lounaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_ei_muuta_mitaan_kun_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_palauttaa_riittamattoman_maksun(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(vaihtoraha, 399)

    def test_syo_edullisesti_kortilla_laskee_riittavaa_saldoa_oikein(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 0)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 260)

    def test_syo_edullisesti_kortilla_palauttaa_true_kun_saldo_riittaa(self):
        kortti = Maksukortti(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))

        kortti.lataa_rahaa(500)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_syo_edullisesti_kortilla_merkitsee_myydyn_lounaan(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_ei_muuta_mitaan_kun_maksu_ei_riita(self):
        kortti = Maksukortti(239)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_palauttaa_false_kun_saldo_ei_riita(self):
        kortti = Maksukortti(239)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_syo_edullisesti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_laskee_riittavaa_saldoa_oikein(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 0)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_palauttaa_true_kun_saldo_riittaa(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))

        kortti.lataa_rahaa(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_syo_maukkaasti_kortilla_merkitsee_myydyn_lounaan(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_ei_muuta_mitaan_kun_maksu_ei_riita(self):
        kortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_palauttaa_false_kun_saldo_ei_riita(self):
        kortti = Maksukortti(399)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        kortti.lataa_rahaa(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kasvattaa_saldoa_oikein(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(kortti.saldo, 150)

    def test_lataa_rahaa_kortille_lisaa_rahaa_kassaan_oikein(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100050)

    def test_lataa_rahaa_kortille_ei_muuta_mitaan_kun_summa_on_negatiivinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
