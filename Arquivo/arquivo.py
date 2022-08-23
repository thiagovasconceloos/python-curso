with open("teste.txt", "a") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")
    arquivo.write("\nContinuação do texto.")
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
