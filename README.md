
# tree_maker

Ez a projekt egy Python szkriptet tartalmaz, amely egy CSV fájlból olvassa be a könyvtár- és fájlszerkezetet, majd egy jól olvasható TXT formátumú könyvtárfát generál.

## Használat

```bash
python script.py <bemeneti_csv> <kimeneti_txt>
```

Példa:

```bash
python script.py query.csv out.txt
```

## Bemenet

- Egy pontosvesszővel tagolt CSV fájl (pl. `query.csv`), amely legalább az alábbi oszlopokat tartalmazza:
	- `Name` (fájl vagy mappa neve)
	- `Item Type` ("Mappa" vagy fájl)
	- `Path` (a mappa/fájl elérési útja)

## Kimenet

- Egy TXT fájl (pl. `out.txt`), amely a könyvtárstruktúrát jeleníti meg, például:



## Hibakezelés

- A szkript ellenőrzi, hogy a bemeneti fájl létezik-e, CSV-e, illetve hogy a kimeneti fájl TXT-e.
- Hibás bemenet vagy hiányzó fájl esetén hibaüzenetet ír ki.

