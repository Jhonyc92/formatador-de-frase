# Definindo a classe FormatadorDeFrase
class FormatadorDeFrase:
    
    # Método construtor, que é chamado quando um novo objeto da classe é instanciado
    def __init__(self, frase):
        
        # Inicializa a variável de instância 'frase' com o valor passado como argumento
        self.frase = frase
        
        self.frase_atual = frase
        
    # Método para converter todos os caracteres da frase para maiúsculas
    def para_maiusculas(self):
        
        # Usa o método upper() para converter a frase para maiúsculas e 
        # armazena na variável de instância 'frase'
        self.frase = self.frase.upper()
        
        print(f"A frase foi convertida para Maiúsculas")
        
    # Método para converter todos os caracteres da frase para minúsculas
    def para_minusculas(self):
        
        # Usa o método lower() para converter a frase para minúsculas e 
        # armazena na variável de instância 'frase'
        self.frase = self.frase.lower()
        
        print(f"A frase foi convertida para Minúsculas")
        
    # Método para capitalizar a primeira letra da frase
    def capitalizar(self):
        
        # Usa o método capitalize() para capitalizar a primeira letra da 
        # frase e armazena na variável de instância 'frase'
        self.frase = self.frase.capitalize()
        
        print(f"A primeira letra da frase foi Capitalizada")
        
    # Método para converter a frase para o formato de título
    def formato_titulo(self):
        
        # Usa o método title() para capitalizar a primeira letra de cada
        # palavra na frase
        self.frase = self.frase.title()
        
        print(f"A primeira letra de cada palavra foi convertida para Maiúscula")
        
    # Método para contar o número de vogais na frase
    def contar_vogais(self):
        
        # Define uma string contendo todas as vogais
        vogais = "aàáâãäeèéêëiìíîïoòóôõöuùúûü"
        
        # Inicializa uma variável de contagem para armazenar o número de vogais
        contagem = 0
        
        # Converte a frase para minúsculas para simplificar a comparação
        frase_min = self.frase.lower()
        
        # Percorre cada letra da frase
        for letra in frase_min:
            
            # Verifica se a letra atual é uma vogal
            if letra in vogais:
                
                # Incrementa a variável de contagem
                contagem += 1
                
        # Caso encontre vogais na frase
        if contagem > 0:
            
            # Imprime o total de vogais encontradas
            print(f"A frase possui {contagem} vogais")
            
        else: 
            
            # Informa que a frase não possui vogais
            print(f"A frase não possui vogais")
            
    # Método para contar o número de consoantes na frase
    def contar_consoantes(self):
        
        # Define uma string contendo todas as consoantes
        consoantes = "bcdfghjklmnpqrstvwxyz"
        
        # Inicializa uma variável de contagem para armazenar o número de consoantes
        contagem = 0
        
        # Converte a frase para minúsculas para facilitar a comparação
        frase_min = self.frase.lower()
        
        # Loop para percorrer cada letra da frase
        for letra in frase_min:
            
            # Checa se a letra atual é uma consoante
            if letra in consoantes:
                
                # Incrementa a variável de contagem
                contagem += 1
                
        # Se encontrar consoantes na frase
        if contagem > 0:
            
            # Informa o total de consoantes encontradas
            print(f"A frase possui {contagem} consoantes")
            
        else: 
            
            # Informa que a frase não possui consoantes
            print(f"A frase não possui consoantes")
            
    # Método para contar o número de ocorrências da letra 'a' na frase
    def contar_letra_a(self):
        
        # Usa o método count() para contar o número de ocorrências da 
        # letra 'a' na frase (convertida para minúsculas)
        print(f"A letra 'a' aparece {self.frase.lower().count("a")} vez(es) na frase")
        
    # Método para procurar e contar o número de ocorrências de uma palavra específica na frase
    def procurar_palavra(self):
        
        # Solicita ao usuário a palavra que deseja pesquisar
        palavra = input("Insira a palavra que deseja contar: ")
        
        # Usa o método count() para contar o número de ocorrências da 
        # palavra na frase (ambas convertidas para minúsculas)
        print(f"A palavra '{palavra}' aparece {self.frase.lower().count(palavra.lower())} vez(es) na frase")
        
    # Método para obter a frase atual
    def obter_frase(self):
        
        # Retorna a variável de instância 'frase'
        print(f"Esta é a frase atual: {self.frase}")
        
# Definindo a função menu, que será a interface do usuário para o programa
def menu():
    
    print("Formatador de Frases")
    
    # Solicita ao usuário que digite uma frase
    frase = input("Insira a frase desejada: ")
    
    # Cria um objeto 'frase' da classe FormatadorDeFrase, 
    # passando a frase digitada como argumento
    frase = FormatadorDeFrase(frase)
    
    print()
    
    # Enquanto verdadeiro, o menu ficará em execução
    while True:
        
        print()
        
        # Imprime as opções do menu
        print("Menu:")
        
        print()
        
        print("1 - Converter Frase para Maiúscula")
        
        print("2 - Converter Frase para Minúscula")
        
        print("3 - Capitalizar a primeira Letra da Frase")
        
        print("4 - Converter a primeira Letra de cada Palavra para Maiúscula")
        
        print("5 - Contar Número de Vogais")
        
        print("6 - Contar Número de Consoantes")
        
        print("7 - Contar quantidade de letra 'a'")
        
        print("8 - Procurar Palavra na Frase")
        
        print("9 - Exibir Frase Atual")
        
        print("10 - Sair")
        
        # Solicita ao usuário que escolha uma opção
        op = input("Digite a opção desejada: ")
        
        print()
        
        # Verifica qual opção foi escolhida e chama o método correspondente
        # do objeto 'frase'
        if op == "1":
            
            # Chama o método para converter a frase para maiúsculas
            frase.para_maiusculas()
            
        elif op == "2":
            
            # Chama o método para converter a frase para minúsculas
            frase.para_minusculas()
            
        elif op == "3":
            
            # Chama o método para capitalizar a primeira letra da frase
            frase.capitalizar()
            
        elif op == "4":
            
            # Chama o método para converter a frase para o formato de título
            frase.formato_titulo()
            
        elif op == "5":
            
            # Chama o método para contar as vogais na frase e imprime o resultado
            frase.contar_vogais()
            
        elif op == "6":
            
            # Chama o método para contar as consoantes na frase e imprime o resultado
            frase.contar_consoantes()
            
        elif op == "7":
            
            # Chama o método para contar ocorrências da letra 'a' na frase e imprime o resultado
            frase.contar_letra_a()
            
        elif op == "8":
            
            # Chama o método para contar ocorrências da palavra escolhida pelo Usuário na frase e imprime o resultado
            frase.procurar_palavra()
            
        elif op == "9":
            
            # Mostra a frase atualizada
            frase.obter_frase()
            
        elif op == "10":
            
            # Informa que o Programa está sendo Encerrado
            print("Encerrando o programa")
            
            # Encerra o programa
            break
            
        else:
            
            print("Opção Inválida")
            
# Verifica se o script está sendo executado como programa 
# principal e, nesse caso, chama a função menu
if __name__ == "__main__":
    
    menu()
