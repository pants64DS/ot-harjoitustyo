import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

        self.maksukortti.lataa_rahaa(1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.01 euroa")

        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.01 euroa")

    def test_ota_rahaa_vahentaa_saldoa_oikein_kun_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

        self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")

        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_ota_rahaa_ei_muuta_saldoa_kun_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_kertoo_riittiko_saldo(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1001))
        self.assertTrue(self.maksukortti.ota_rahaa(1000))
