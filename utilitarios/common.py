def confirmar(o_que):
    confirma = ""
    while confirma.upper() != "S" and confirma.upper() != "N":

        confirma = input(f"\nConfirma {o_que} (S/N)? ")

        if confirma.upper() == "N":
            return False

        elif confirma.upper() == "S":
            return True

        else:
            print("Digite 'S' para Sim e 'N' para não.\n")
