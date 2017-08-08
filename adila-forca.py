import random # essa instrução importa uma biblioteca da internet. 
palavras = [] #essa instrução cria uma lista.



letrasErradas = ''#essa instrução cria uma variável, que é o mesmo que uma lista uma com apenas um valor.
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def inserir (): # inserir as palavras que a pessoa digitar.
    while True:
        x= input("Digite a palavra: ")
        palavras.append(x)
        if x == "": #se a variavel x estiver vazia o jogo para de pedir palavras
            break
def principal(): #A instrução def é utilizada em Phyton para "criar" funções.
    """
    Função Princial do programa
    """
    print('F O R C A') #imprime determinada mensagem na tela.
    inserir ()
    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True: # executa o bloco enquanto a condição for verdadeira.
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo(): # essa instrução significa se, ela executa o bloco se a condição nela for verdadeira.
            print('Voce Perdeu!!!')
            break # para de rodar o bloco se a condição for verdadeira ou falsa dependendo do seu if.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG # essa instrução indica que esse comando é global e não local, ele vai puxar uma nova variável que ta fora do bloco.
    if len(letrasErradas) == len(FORCAIMG): 
        return True 
    else:
        return False 
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta: #A instrução for em Phyton cria um laço de repetição ele irá realizar uma sequencia de forma ordenada e acabará alterando valores que são especificados em variáveis por você.
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1: # o len retorna o tamanho da lista.
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: #elif significa se ou se não essa condição é verdadeira.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": # se o palpite não estiver entre a e z irá imprimir na tela "por favor escolha apenas letras".
        print('Por favor escolha apenas letras')
    else: # essa instrução é ativada se o if for falso.
        return palpite #return define o que vai retornar quando você chamar a função.
    
    
def desenhaJogo(palavraSecreta,palpite): 
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta: 
        letrasCertas += palpite
    else:
        letrasErradas += palpite 

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra(): # essa função pega todas as palavras da função palavra secreta e retorna uma aleatória.
    global palavras
    return random.choice(palavras).upper()

    
principal()
