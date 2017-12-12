from game_input import game_input
from game_input import game_loop
from puzzle import puzzle
from enum import Enum

class SymbolEnum(Enum):
    CIRCLE_POST =   "0. Circle with post"
    A_T         =   "1. A with T in it"
    LAMBDA_DASH =   "2. Lambda with a dash"
    JAGGED_N    =   "3. Flipped N, jagged"
    SQUID       =   "4. Squid with a rake"
    FANCY_H     =   "5. Cursive looking H"
    BACK_C_DOT  =   "6. Backwards C with dot"
    BACK_EP     =   "7. Backwards epsilo"
    FANCY_O     =   "8. Fancy, loopy O"
    HOLLOW_STAR =   "9. Hollow star"
    FLIPPED_Q   =   "10. Flipped question mark"
    COPYRIGHT   =   "11. Copyright"
    APO_W       =   "12. Curvy W, Apostrophe"
    K_BACK_K    =   "13. Back to back Ks"
    HALF_3      =   "14. 3 missing a bottom"
    FLAT_6      =   "15. Flattened 6"
    PARAGRAPH   =   "16. Paragraph"
    T_B         =   "17. T over a lower b"
    SMILE       =   "18. Smiley face"
    PSI         =   "19. Psi or pitchfork"
    C_DOT       =   "20. C with a dot"
    ANTEN_3     =   "21. Three with antennae"
    FULL_STAR   =   "22. Filled star"
    TIC_TAC_TOE =   "23. Tic tac toe"
    AE          =   "24. ae"
    TALL_N      =   "25. Backwards N, tall"
    OMEGA       =   "26. Omega"

@puzzle("Symbols")
class Symbols:
    lists = [[SymbolEnum.CIRCLE_POST, SymbolEnum.A_T, SymbolEnum.LAMBDA_DASH, SymbolEnum.JAGGED_N, SymbolEnum.SQUID, SymbolEnum.FANCY_H, SymbolEnum.BACK_C_DOT],
             [SymbolEnum.BACK_EP, SymbolEnum.CIRCLE_POST, SymbolEnum.BACK_C_DOT, SymbolEnum.FANCY_O, SymbolEnum.HOLLOW_STAR, SymbolEnum.FANCY_H, SymbolEnum.FLIPPED_Q],
             [SymbolEnum.COPYRIGHT, SymbolEnum.APO_W, SymbolEnum.FANCY_O, SymbolEnum.K_BACK_K, SymbolEnum.HALF_3, SymbolEnum.LAMBDA_DASH, SymbolEnum.HOLLOW_STAR],
             [SymbolEnum.FLAT_6, SymbolEnum.PARAGRAPH, SymbolEnum.T_B, SymbolEnum.SQUID, SymbolEnum.K_BACK_K, SymbolEnum.FLIPPED_Q, SymbolEnum.SMILE],
             [SymbolEnum.PSI, SymbolEnum.SMILE, SymbolEnum.T_B, SymbolEnum.C_DOT, SymbolEnum.PARAGRAPH, SymbolEnum.ANTEN_3, SymbolEnum.FULL_STAR],
             [SymbolEnum.FLAT_6, SymbolEnum.BACK_EP, SymbolEnum.TIC_TAC_TOE, SymbolEnum.AE, SymbolEnum.PSI, SymbolEnum.TALL_N, SymbolEnum.OMEGA]]

    def __init__(self):
        self.name = "Button"

    def run(self, bomb_info):
        with game_loop(self.name) as loop:
            while True:
                for symbol in list(SymbolEnum):
                    print(symbol.value)

                symbols_str = game_input("Input the list of symbol numbers with commas between: ")
                print("")
                try:
                    symbols = list(map(int, symbols_str.split(',')))
                    if (len(symbols) != 4):
                        print("Incorrect number of symbols")
                        continue

                    correctList = None
                    for symbolList in Symbols.lists:
                        succeed = True
                        for symbol in symbols:
                            if not (list(SymbolEnum)[symbol] in symbolList):
                                succeed = False
                                break
                        if succeed:
                            correctList = symbolList
                            break

                    if correctList == None:
                        print("No matching sequence found")
                        continue

                    symbol_values = []
                    for symbol in symbols:
                        symbol_values.append(list(SymbolEnum)[symbol])

                    sorted_symbols = sorted(set(symbol_values).intersection(set(correctList)), key = lambda x: correctList.index(x))
                    print("\nClick in the following order: ")
                    for symbol in sorted_symbols:
                        print(symbol.value)

                    break

                except ValueError:
                    print("Not numbers")