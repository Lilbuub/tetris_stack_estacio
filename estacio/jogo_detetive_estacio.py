print("=== DETECTIVE QUEST ===")
print("Um crime aconteceu na mansão, e tem três suspeitos:")
print("1 - Maria\n2 - João\n3 - Clara\n")

resposta = input("Quem é o culpado? ")

if resposta.strip() == "2" or resposta.lower() == "joao":
    print("Você acertou! João era o culpado.")
else:
    print("Errado! O culpado era o João.")