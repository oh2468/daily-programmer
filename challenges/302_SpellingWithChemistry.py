## https://old.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/

chem_map = {
    "Ac": "Actinium", "Al": "Aluminum", "Am": "Americium",
    "Sb": "Antimony", "Ar": "Argon", "As": "Arsenic",
    "At": "Astatine", "Ba": "Barium", "Bk": "Berkelium",
    "Be": "Beryllium", "Bi": "Bismuth", "B":  "Boron",
    "Br": "Bromine", "Cd": "Cadmium", "Ca": "Calcium",
    "Cf": "Californium", "C":  "Carbon", "Ce": "Cerium",
    "Cs": "Cesium", "Cl": "Chlorine", "Cr": "Chromium",
    "Co": "Cobalt", "Cu": "Copper", "Cm": "Curium",
    "Dy": "Dysprosium", "Es": "Einsteinium", "Er": "Erbium",
    "Eu": "Europium", "Fm": "Fermium", "F":  "Fluorine",
    "Fr": "Francium", "Gd": "Gadolinium", "Ga": "Gallium",
    "Ge": "Germanium", "Au": "Gold", "Hf": "Hafnium",
    "He": "Helium", "Ho": "Holmium", "H":  "Hydrogen",
    "In": "Indium", "I":  "Iodine", "Ir": "Iridium",
    "Fe": "Iron", "Kr": "Krypton", "La": "Lanthanum",
    "Lr": "Lawrencium", "Pb": "Lead", "Li": "Lithium",
    "Lu": "Lutetium", "Mg": "Magnesium", "Mn": "Manganese",
    "Md": "Mendelevium", "Hg": "Mercury", "Mo": "Molybdenum",
    "Nd": "Neodymium", "Ne": "Neon", "Np": "Neptunium",
    "Ni": "Nickel", "Nb": "Niobium", "N":  "Nitrogen",
    "No": "Nobelium", "Os": "Osmium", "O":  "Oxygen",
    "Pd": "Palladium", "P":  "Phosphorus", "Pt": "Platinum",
    "Pu": "Plutonium", "Po": "Polonium", "K":  "Potassium",
    "Pr": "Praseodymium", "Pm": "Promethium", "Pa": "Protactinium",
    "Ra": "Radium", "Rn": "Radon", "Re": "Rhenium",
    "Rh": "Rhodium", "Rb": "Rubidium", "Ru": "Ruthenium",
    "Rf": "Rutherfordium", "Sm": "Samarium", "Sc": "Scandium",
    "Se": "Selenium", "Si": "Silicon", "Ag": "Silver",
    "Na": "Sodium", "Sr": "Strontium", "S":  "Sulfur",
    "Ta": "Tantalum", "Tc": "Technetium", "Te": "Tellurium",
    "Tb": "Terbium", "Tl": "Thallium", "Th": "Thorium",
    "Tm": "Thulium", "Sn": "Tin", "Ti": "Titanium",
    "W":  "Tungsten", "U":  "Uranium", "V":  "Vanadium",
    "Xe": "Xenon", "Yb": "Ytterbium", "Y":  "Yttrium",
    "Zn": "Zinc", "Zr": "Zirconium"
}

def spell(word):
    codes = []
    i = 0
    back = False
    while i < len(word):
        p1, p2 = word[i].capitalize(), word[i:i + 2].capitalize()
        if back:
            if p1 in chem_map:
                codes.append(p1)
                i += 1
                back = False
            else:
                i -= len(codes.pop())
        elif p2 in chem_map:
            codes.append(p2)
            i += 2
        elif p1 not in chem_map:
            back = True
            i -= len(codes.pop())
        else:
            codes.append(p1)
            i += 1        
    return f"{''.join(codes)} ({', '.join(chem_map[c].lower() for c in codes)})"

print(spell("genius"))
print(spell("functions"))
print(spell("bacon"))
print(spell("poison"))
print(spell("sickness"))
print(spell("ticklish"))
print(spell("nbe"))
print(spell("nbenbenbeonc"))
