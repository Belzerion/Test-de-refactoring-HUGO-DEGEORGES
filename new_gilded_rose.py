products = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros", "Conjured"]

class GildedRose(object):
  def __init__(self, items):
    self.items = items
  
  
  def computeNewQualityBackstage(item):
    if item.sell_in < 0:
      return 0
    if item.sell_in < 6:
      return item.quality + 3
    if item.sell_in < 11:
      return item.quality + 2
    return item.quality + 1


  def update_quality(self):
    for item in self.items:
      if item.name == "Aged Brie":
       item.quality += 1
       item.sell_in -= 1 
      if item.name == "Backstage passes to a TAFKAL80ETC concert":
       item.quality = computeNewQualityBackstage(item)
       item.sell_in -= 1
      if item.name == "Sulfuras, Hand of Ragnaros":
       return
      if item not in products:
        item.quality -= 1
        item.sell_in -= 1
      if item.name == "Conjured":
        item.quality -= 2
        item.sell_in -= 1


class Item:
  def __init__(self, name, sell_in, quality):
    self.name = name
    self.sell_in = sell_in
    self.quality = quality

  def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
