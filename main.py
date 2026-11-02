class ItemShop:
    def __init__(self, nama_item, harga_item, stok_item):
        self.nama_item = nama_item
        self.harga_item = harga_item
        self.stok_item = stok_item
        
    def beli_item(self, jumlah):
        if jumlah <= self.stok_item:
            self.stok_item -= jumlah
            print(f"Berhasil membeli {jumlah} {self.nama_item}!")
        else:
            print(f"Stok dari {self.nama_item} telah habis. ")
        
item1 = ItemShop("Pedang", 20000, 10)
item2 = ItemShop("Perisai", 10000, 5)

item1.beli_item(5)