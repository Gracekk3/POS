import re


class PDU:
    def __init__(self, payload):
        if type(self) == PDU:
            raise Exception("Nelze vytvořit PDU přímo")
        self._payload = payload

    def getPayload(self):
        return self._payload

    def setPayload(self, data):
        self._payload = data

    def isValid(self):
        raise Exception("Musí být implementováno v potomkovi")


class EthFrame(PDU):
    def __init__(self, dmac, smac, typ, payload, fcs=None):
        super().__init__(payload)

        if not self.isValidMac(dmac) or not self.isValidMac(smac):
            raise Exception("Špatná MAC adresa")

        self._dmac = dmac
        self._smac = smac
        self._typ = typ

        if fcs is None:
            self._fcs = self.calculateFcs()
        else:
            self._fcs = fcs

    def isValidMac(self, mac):
        return re.match(r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$", mac)

    def calculateFcs(self):
        text = self._dmac + self._smac + str(self._typ) + self._payload
        soucet = 0
        for znak in text:
            soucet += ord(znak)
        return soucet

    def isValid(self):
        return self.calculateFcs() == self._fcs

    def __str__(self):
        return "[EthFrame] SRC: " + self._smac + " DST: " + self._dmac + " DATA: " + self._payload

    def setPayload(self, data):
        self._payload = data
        self._fcs = self.calculateFcs()

    def corruptData(self):
        self._payload = "ROZBITE"
        self._fcs = 12345

#TEST
ramec = EthFrame(
    "aa:bb:cc:dd:ee:ff",
    "11:22:33:44:55:66",
    2048,
    "Ahoj"
)

print(ramec)
print("Validní:", ramec.isValid())

ramec.setPayload("Nová data")
print("Po změně:", ramec.isValid())

ramec.corruptData()
print("Po rozbití:", ramec.isValid())