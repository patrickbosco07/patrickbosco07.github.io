'''
UM DIA
UM CHAVEIRO
12 ATEND P DIA
TRÊS LISTAS
'''
ceps = [0] * 12
valorOrc = [0] * 12
status = [0] * 12

for i in range(12):
    print("digite o cep da rua do cliente",i+1)
    ceprua = int(input())
    ceps[i] = ceprua
    print("digite o orçamento do cliente",i+1)
    orcamento = float(input())
    valorOrc[i] = orcamento
    print("digite o status do pedido do cliente (1 realizado, 0 não realizado)",i+1)
    sttPedido = int(input())
    status[i] = sttPedido
opcaoDesejada = 0
while opcaoDesejada != 4:
        print("Menu:")
        print("1 - Listar atendimentos agendados")
        print("2 - Calcular a soma do dinheiro recebido pelo chaveiro")
        print("3 - Encontrar o CEP do orçamento mais caro e o mais barato")
        print("4 - Finalizar o programa")
        print("escolha a opção desejada")
        opcaoDesejada = int(input())
        if opcaoDesejada == 1:
            print("CEPS dos agendamentos:",ceps,"valores dos orçamentos:",valorOrc)
        if opcaoDesejada == 2:
            somador = 0
            for a in range(12):
                if status[a] == 1:
                    numerotemp = valorOrc[a]
                    somador+= numerotemp
            print("os ganhos até agora são",somador)
        if opcaoDesejada == 3:
            omaiscaro = 0
            omaisbarato = 0
            contador = 0
            cepAchadoMaior = 0
            cepAchadoMenor = 0
            for o in range(12):
                if valorOrc[o] > omaiscaro:
                    omaiscaro = valorOrc[o]
                    cepAchadoMaior = ceps[o]
                if contador == 0:
                    omaisbarato = valorOrc[o]
                if valorOrc[o] < omaisbarato:
                    omaisbarato = valorOrc[o]
                    cepAchadoMenor = ceps[o]
                contador = contador + 1
            print("o mais caro foi:",omaiscaro,"e seu CEP é de",cepAchadoMaior,"e o mais barato foi",omaisbarato,"de CEP",cepAchadoMenor)
        if opcaoDesejada == 4:
            opcaoDesejada = 4
            break
print("programa encerrado")          