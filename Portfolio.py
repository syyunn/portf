class Portfolio:
    def __init__(self,
                 kinds,
                 values):
        for key, val in zip(kinds, values):
            self.portf = dict()
            self.portf[key] = val

        self.kinds = self.portf.keys()

    def add_kind(self, key, value=0):
        self.portf = self.portf + {key: value}


if __name__ == "__main__":
    kinds = []
    pass
