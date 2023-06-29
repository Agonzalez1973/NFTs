import threading

class NFT:
    def __init__(self, name, risk_level, price):
        self.name = name
        self.risk_level = risk_level
        self.price = price

class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type

class Server:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ads = []
        self.lock = threading.Lock()

    def add_ad(self, nft):
        with self.lock:
            if len(self.ads) < self.capacity:
                self.ads.append(nft)
            else:
                print("Server is full. Can't add more ads.")

    def provide_ad(self, risk_level, discarded_ads):
        with self.lock:
            for ad in self.ads:
                if ad not in discarded_ads and ad.risk_level == risk_level:
                    return ad
            return None

    def remove_ad(self, ad):
        with self.lock:
            self.ads.remove(ad)

class Buyer(threading.Thread):
    def __init__(self, server, user):
        super().__init__()
        self.server = server
        self.user = user

    def run(self):
        # Lógica de compra de NFTs por parte del comprador
        pass

class Seller(threading.Thread):
    def __init__(self, server, user, nft):
        super().__init__()
        self.server = server
        self.user = user
        self.nft = nft

    def run(self):
        # Lógica de venta de NFTs por parte del vendedor
        pass

# Ejemplo de uso

server = Server(100)

user1 = User("Alice", "buyer")
user2 = User("Bob", "seller")

nft = NFT("Artwork1", "low", 200)

buyer = Buyer(server, user1)
seller = Seller(server, user2, nft)

buyer.start()
seller.start()
