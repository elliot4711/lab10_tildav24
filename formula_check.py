from linkedQfile import LinkedQ
from molgrafik import *

periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu',
'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', "Lv"]


def create_atomdict():
    """Creates and returns dictionary of atom weights"""
    
    atomdata = "H 1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B 10.811;\
    C 12.0107;\
    N 14.0067;\
    O 15.9994;\
    F 18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P 30.973762;\
    S 32.065;\
    Cl 35.453;\
    K 39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V 50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y 88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I 126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W 183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U 238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atom_list = atomdata.split(";")
    weight_dict = {}
    for atom in atom_list:
        name, weight = atom.split()
        weight_dict[name] = float(weight)
    
    return weight_dict

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

DEBUG = False

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass

def formula():
    if DEBUG:
        print("formula")
    
    take_input = True
    while take_input == True:
        molecule = input("")
        if molecule == ("#"):
            take_input = False
        else:
            try:
                que = LinkedQ()
                for letter in molecule:
                    que.enqueue(letter)
                while not que.isEmpty():
                    mol = ismolecule(que)
                print("Formeln är syntaktiskt korrekt")
                atom_dict = create_atomdict()
                print(f"Molecule weight is: {weight(mol, atom_dict)}")
                mg = Molgrafik()
                mg.show(mol)
            except Syntaxfel as err:
                returnvalue = str(err.args[0])
                print(returnvalue)
    
def ismolecule(que):
    if DEBUG:
        print("ismolecule")
        print(que)
    mol = isgroup(que)
    if que.peek() == (")"):
        pass
        print("pass")
    else:
        if not que.isEmpty():
            mol.next = ismolecule(que)

    return mol


def isgroup(que):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """
    if DEBUG:
        print("isgroup")
        print(que)
    
    rutan = Ruta()

    if que.peek() is None:
        raise Syntaxfel("Enter something")

    elif que.peek().isalpha():
        rutan.atom = isatom(que)
        rutan.num = isnum(que)
        return rutan
    
    elif que.peek() == "(":
        que.dequeue()
        while not que.isEmpty():
            rutan.down = ismolecule(que)
            if que.peek() == (")"):
                que.dequeue()
                if que.isEmpty():
                    word = get_word(que)
                    raise Syntaxfel(f"Saknad siffra vid radslutet {word}")
                
                elif que.peek().isdigit():
                    rutan.num = isnum(que)
                    return rutan
                
                else:
                    word = get_word(que)
                    raise Syntaxfel(f"Saknad siffra vid radslutet {word}")

        word = get_word(que)
        raise Syntaxfel(f"Saknad högerparentes vid radslutet {word}") 
    

   
    else:
        word = get_word(que)
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {word}")        
      

def isatom(que):
    if DEBUG:
        print("isatom")

    firstletter = que.peek()
    if isbigletter(firstletter):
        que.dequeue()
        secondletter = que.peek()
        if secondletter == None or not secondletter.isalpha():
            if firstletter in periodic_table:
                return firstletter
            else: 
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")


        elif issmallletter(secondletter):
            secondletter = que.dequeue()
            atom = firstletter + secondletter
            if atom in periodic_table:
                return atom
            else:
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
        
        else:
            if firstletter in periodic_table:
                return firstletter
            else:
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
    
    else:
        word = get_word(que)
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {word}")
    
def isnum(que):
    if DEBUG:
        print("isnum")

    if que.isEmpty() or que.peek() is None:
        return 1
    
    elif not que.peek().isdigit():
        return 1
    
    else:
        if que.peek() == "0":
            que.dequeue()
            word = get_word(que)
            raise Syntaxfel(f"För litet tal vid radslutet {word}")

        else:
            number = ""
            while not que.isEmpty() and que.peek().isdigit():
                number += que.dequeue()
            number = int(number)

            if number >= 2:
                return number
            
            else:
                word = get_word(que)
                raise Syntaxfel(f"För litet tal vid radslutet {word}")

def isbigletter(value):
    """ 
    Function for testing if a value is a capital letter
    Parameters: value to check
    Returns: True or False
    """
    if DEBUG:
        print("isbigletter")

    if value is not None:
        return value.isupper()
    else:
        return False 

def issmallletter(value):
    """ 
    Function for testing if a value is a lowercase letter
    Parameters: value to check
    Returns: True or False
    """
    
    if DEBUG:
        print("issmallletter")

    if value is not None:
        return value.islower()
    else:
        return False 

def get_word(que):
    word = ""
    if not que.isEmpty():
        while not que.isEmpty():
            l = que.dequeue()
            word += l
    return word

def weight(mol, atom_dict):

    if mol.atom.isalpha() and mol.next != None:
        mol_weight = atom_dict(mol.atom) * mol.num + weight(mol.next, atom_dict)

    elif mol.atom == "( )" and mol.next != None: 
        mol_weight = weight(mol.down) * mol.num + weight(mol.down, atom_dict)

    elif mol.atom.isalpha():
        mol_weight = atom_dict(mol.atom) * mol.num
    
    return mol_weight



if __name__ == '__main__':
    formula()