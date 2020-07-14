from my_logic_of_knowledge import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
AStatement0 = And(AKnight, AKnave)
knowledge0 = And(Or(AKnave, AKnight), Biconditional(AKnight, Not(AKnave)),
                 Implication(AKnight, AStatement0), Implication(AKnave,
                                                                Not(
                                                                    AStatement0)))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
AStatement1 = And(AKnave, BKnave)
knowledge1 = And(Or(AKnave, AKnight), Or(BKnave, BKnight), Biconditional(
    AKnight, Not(AKnave)), Biconditional(BKnight, Not(BKnave)), Implication(
    AKnight, AStatement1), Implication(AKnave, Not(AStatement1)))

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
AStatement2 = And(Biconditional(AKnave, BKnave),
                  Biconditional(AKnight, BKnight))
BStatement2 = And(Biconditional(AKnave, Not(BKnave)),
                  Biconditional(AKnight, Not(BKnight)))

knowledge2 = And(Or(AKnave, AKnight), Or(BKnight, BKnave), Biconditional(
    AKnave, Not(AKnight)), Biconditional(BKnave, Not(BKnight)), Implication(
    AKnight, AStatement2), Implication(AKnave, Not(AStatement2)),
                 Implication(BKnight, Not(BStatement2)), Implication(BKnave,
                                                                     Not(BStatement2)))

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AStatement3 = Biconditional(AKnight, Not(AKnave))
BStatement3 = And(Implication(AKnight, BKnave), Implication(AKnave,
                                                            Not(BKnave)), CKnave)
CStatement3 = AKnight
knowledge3 = And(Or(AKnave, AKnight), Or(BKnight, BKnave), Or(CKnight, CKnave),
                 Biconditional(AKnave, Not(AKnight)),
                 Biconditional(BKnave, Not(BKnight)),
                 Biconditional(CKnave, Not(CKnight)),
                 Implication(AKnight, AStatement3),
                 Implication(AKnave, Not(AStatement3)),
                 Implication(BKnight, BStatement3),
                 Implication(BKnave, Not(BStatement3)),
                 Implication(CKnight, CStatement3),
                 Implication(CKnave, CStatement3))


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.arguments) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(symbol.symbols())


if __name__ == "__main__":
    main()
