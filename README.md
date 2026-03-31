# Cisco Packet Tracer – LAN

## Výpočet X a Y

Jméno: Gracjan
Příjmení: Cemerys

X = součet ASCII hodnot příjmení mod 256
C(67) + e(101) + m(109) + e(101) + r(114) + y(121) + s(115) = 728
X = 728 mod 256 = 216

Y = součet ASCII hodnot jména mod 10
G(71) + r(114) + a(97) + c(99) + j(106) + a(97) + n(110) = 694
Y = 694 mod 10 = 4

---

## Síť

Rozsah: **10.216.0.0 /20**
Maska: **255.255.240.0**

---

## Topologie

* PC1, PC2 → S1
* PC3, PC4 → S2
* S1 ↔ S2
* Laptop → S1 (console kabel)

---

## IP adresace

* PC1: 10.216.0.1
* PC2: 10.216.0.2
* PC3: 10.216.0.3
* PC4: 10.216.0.4

Default gateway není nastavena, protože v síti není router.

---

## Postup

1. Přidal jsem zařízení (2× switch, 4× PC, 1× laptop)
2. Propojil jsem zařízení správnými kabely
3. Nastavil IP adresy na všech PC
4. Připojil laptop ke switchi a nastavil hostname S1 a S2
5. Otestoval jsem konektivitu pomocí ping

---

## Testování

Na PC1 jsem spustil příkaz:

ping 10.216.0.4

Ping byl úspěšný, takže síť funguje správně.

---

## Screenshoty

<img width="656" height="654" alt="Snímek obrazovky 2026-03-30 155305" src="https://github.com/user-attachments/assets/26d612e4-71f0-4b94-83ac-bcd62ad232a0" />
<img width="694" height="656" alt="Snímek obrazovky 2026-03-30 155254" src="https://github.com/user-attachments/assets/232d1c04-3e77-404f-8977-b9a0a6161f1f" />
<img width="685" height="652" alt="Snímek obrazovky 2026-03-31 085816" src="https://github.com/user-attachments/assets/2cfe3733-fa4b-4102-aff3-693f61691d1e" />
