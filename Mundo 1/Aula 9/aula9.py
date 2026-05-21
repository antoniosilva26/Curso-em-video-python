frase = "Curso em Video Python"
print(frase[9:21])#Começa no "Video" e termina no "Python"
print(frase[9:21:3])#começa na casa 9, termina na 21 e pula de 2 em 2(por exemplo< começou em video, pulou o I e o D)
print(frase[15:])#Começa no caractere 15, ou seja: no "Python"
print(frase[:5])#começa no caractere 0 e termina no 5, assim formando a palavra "Curso"
print(frase[9::])#Começa no caractere 0 e termina no ultimo
print(frase[9::3])#Mesma coisa do de cima, mas ele pula de 2 em 2(igual ao 9:21:3)
print(len(frase))#ler o comprimento da fase
print(frase.count('o'))#retorna quantas letras existem na string
print(frase.count('o', 0, 14))#retorna quantas letras existem na string, entre o caractere 0 e 13(coloquei 14 pq se colocar 13, ele nao conta o "O" de "Video")
print(frase.find('o'))#retorna quantas vezes ele encontra "deo"
print(frase.find("Python"))#Vai procurar o "Curso" na string, se retornar -1 é por que ele não achou
print('Curso' in frase)#Vai procurar o "Curso" na string, retorna 0 ou 1(True ou False)
print(frase.replace('Python', 'Android'))#Procura o "Python" na string e substitui por 'Android"
print(frase.upper())#Transforma todas as letras em maiúsculas
print(frase.lower())#Ao contrário do upper, o lower transforma todas as letras em minúscula
print(frase.capitalize())#Transforma todas as letras em minusculo, exceto a primeira(parecido com o lower, só mudando 1 detalhe)
print(frase.title())#Transforma todas as letras em minuscula, menos as que nao estao juntas, por exemplo: Curso, Video, Python
print(frase.strip())#transforma os finais desnecessarios da string
print(frase.rstrip())#transforma os espaços desnecessarios do lado direito da string
print(frase.lstrip())#transforma os finais desnecessarios do lado esquerdo da string
print(frase.split())#transforma as palavras em uma lista , por exemplo: ['Curso', 'em', 'Video', 'Python']
frase.split()
print('-'.join(frase))#Junta as palavras com um caractere(escolhi o "_")
print(frase.replace(" ", ""))

#tambem existe rfind e lfind!!!!
