from gilded_rose import GildedRose, Item
import unittest


class testGildedRose(unittest.TestCase):
    def testAgeBried(self):
        items = [
            Item("Aged Brie", 2, 0),
            Item("Aged Brie", 2, 51),
            Item("Aged Brie", -5, 51),
            Item("Aged Brie", -5, 49),
        ]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(gildedRose.items[0].quality, 1)
        self.assertEqual(gildedRose.items[1].quality, 51)
        self.assertEqual(gildedRose.items[0].sell_in, 1)
        self.assertEqual(gildedRose.items[2].quality, 51)
        self.assertEqual(gildedRose.items[3].quality, 50)

    def testSulfuras(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 2, 0),
            Item("Sulfuras, Hand of Ragnaros", -2, 0)
        ]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(gildedRose.items[0].quality, 0)
        self.assertEqual(gildedRose.items[1].quality, 0)

    def testBackStage(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 48),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 47)
        ]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(gildedRose.items[0].quality, 50)
        self.assertEqual(gildedRose.items[1].quality, 50)
        self.assertEqual(gildedRose.items[1].quality, 50)
        self.assertEqual(gildedRose.items[1].quality, 50)

    def testConjured(self):
        items = [Item("Conjured", 45, 45)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(gildedRose.items[0].quality, 44)
