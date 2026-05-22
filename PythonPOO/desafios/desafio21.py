# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, 
# podendo escrever frases na cor relativa
# faz cores azul, vermelho e verde

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2) #Pula linha 2x

# Se a caneta não estiver destampada diga:
# A caneta está tampada!
