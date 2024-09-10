while True:
    n1 = input("Primeiro numero:")
    n2 = input("Segundo numero:")
    operacao = input("O que deseja fazer: + \n- \n* \n/ \n")

    n_validos = None

    try:
      n1_flo = float(n1)
      n2_flo = float(n2)
      n_validos = True

    except:
        n_validos = None

    if n_validos == None:
        print("erro, por favor insira um valor numerico")
        continue
    op_permitidos = '+-*/'

    if operacao not in op_permitidos:
        print("erro, por favor insira uma operação permitida")
        continue
    if len(operacao) > 1:
        print("erro, por favor insira apenas uma operação")
        continue

    if operacao == '+':
        print(f'{n1_flo} + {n2_flo} = {n1_flo + n2_flo}')
    elif operacao == '-':
        print(f'{n1_flo} - {n2_flo} = {n1_flo - n2_flo}')
    elif operacao == '*':
        print(f'{n1_flo} * {n2_flo} = {n1_flo * n2_flo}')
    elif operacao == '/':
        if n2_flo == 0:
            print("Erro: Não é possível dividir por zero.")
    else:
        print(f'{n1_flo} / {n2_flo} = {n1_flo / n2_flo}')

    sair = input("Deseja sair? Sim \nNão \n")
    if sair == "Sim":
        print("Você saiu!")
        break
