import threading


class NFT:
    def __init__(self, nombre, riesgo, precio):
        self.nombre = nombre
        self.riesgo = riesgo
        self.precio = precio


class User:
    def __init__(self, nombre, tipo_usuario):
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario


def Interesa(user, nft):
    # Criterio para decidir si el NFT interesa al cliente
    # Retorna True si el NFT es de interés, False en caso contrario
    return True  # Ejemplo: Se asume que todos los NFTs son de interés para el cliente


def Nivel_Riesgo(nft):
    # Criterio para decidir el nivel de riesgo del NFT
    # Retorna el nivel de riesgo del NFT (bajo, medio, alto)
    return "bajo"  # Ejemplo: Se asume que todos los NFTs tienen un nivel de riesgo bajo

class Server:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.ads = []
        self.lock = threading.Lock()

    def add_ad(self, nft):
        with self.lock:
            if len(self.ads) < self.capacidad:
                self.ads.append(nft)
            else:
                print("El servidor esta completo. No puedes añadir más.")

    def provide_ad(self, riesgo, discarded_ads):
        with self.lock:
            for ad in self.ads:
                if ad not in discarded_ads and ad.riesgo == riesgo:
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
        self.discarded_ads = []

    def run(self):
        max_risk_level = Nivel_Riesgo(self.user)
        while True:
            ad = self.server.provide_ad(max_risk_level, self.discarded_ads)
            if ad is not None:
                if Interesa(self.user, ad):
                    print(f"{self.user.nombre} esta interesado en  {ad.nombre}")
                    # Realizar acciones adicionales cuando el NFT interesa al comprador
                    break
                else:
                    self.discarded_ads.append(ad)
            else:
                print(f"No hay anuncios disponibles para {self.user.nombre}")
                break


class Seller(threading.Thread):
    def __init__(self, server, user, nft):
        super().__init__()
        self.server = server
        self.user = user
        self.nft = nft

    def run(self):
        # Criterio de venta de NFTs por el vendedor
        pass

# Un ejemplo de como podría usarse:

server = Server(100)

user1 = User("Manolo", "buyer")
user2 = User("Alicia", "seller")

nft = NFT("Obra de Arte", "Bajo", 200)

buyer = Buyer(server, user1)
seller = Seller(server, user2, nft)

buyer.start()
seller.start()
