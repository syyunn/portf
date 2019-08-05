class Portfolio:
    def __init__(self,
                 asset_kinds,
                 values):
        for key, val in zip(asset_kinds, values):
            self.portf = dict()
            self.portf[key] = val

        self.kinds = self.portf.keys()

    def add_kind(self, key, value=0):
        self.portf = self.portf + {key: value}


class Asset:
    def __init__(self,
                 name):
        self.name = name
        self.total = 0
        self.volume = 0
        self.history = []
        self.unit = None
        if name == "USD":
            self.unit = "USD"
        elif name == "GOLD":
            self.unit = "g"

    def add_volume(self,
                   volumes):
        assert isinstance(volumes, list), "volumes must be list instance."

        self.history += volumes
        self.total = sum(self.history)


if __name__ == "__main__":
    usd = Asset("USD")
    history = [1700, 830, 826, 818.5, 1650, 818.5, 1637.6, 1636.8]
    usd.add_volume(history)
    print(usd.total)


    pass
