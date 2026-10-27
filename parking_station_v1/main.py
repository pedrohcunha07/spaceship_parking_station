TABELA_PRECOS = {
    'X-Wing': 10.0,
    'Falcon': 50.0,
    'Tie Fighter': 15.0,
    'Bombardeiro Imperial': 100.0,
    'Destroyer': 300.00
}
patio = {}

def estacionar_nave():
    nome_nave = input('Qual o nome da nave? ').strip().title()
    modelo_nave = input('Qual o modelo da nave? ').strip().title()
    
    try:
        TABELA_PRECOS[modelo_nave]
        patio[nome_nave] = modelo_nave
        
        print(f'Nave {nome_nave} adicionada ao pátio com sucesso!')
        
    
    except KeyError:
        print(f'O modelo de nave {modelo_nave} não é aceito.')
        
        
def liberar_nave():
    preco = 0
    nome_nave = input('Qual o nome da nave que vai sair? ').strip().title()
    try:
        modelo_fora = patio.pop(nome_nave)
        
        horas = int(input('Quanto tempo ficou no pátio? ').strip())
        
        if horas < 0:
            return 0
        
        preco = horas * TABELA_PRECOS[modelo_fora]
        
        
    except KeyError:
        print('Nave não se encontra no sistema.')
    except ValueError:
        print('Valor inválido.')
        
    return preco
    

def exibir_patio():
    if not patio:
            print('O pátio está vazio.')
            return
    
    print('='*12,'NAVES NO PÁTIO','='*12)
    for nave, modelo in patio.items():
        print(f'Nave: {nave} | Modelo: {modelo}')
        
        
    
def main():
    total = 0
    while True:
        try:
            print('OPÇÕES: ESTACIONAR (1) | LIBERAR (2) | EXIBIR PÁTIO (3) | FECHAR SISTEMA (0)\n')
            option = int(input('Escolha uma opção: '))
            if option == 0:
                break
            
            if option == 1:
                estacionar_nave()
                
            elif option == 2:
                total += liberar_nave()
                print(f'Total: C${total:.2f}')
                
            elif option == 3:
                exibir_patio()
                
                
        except ValueError:
            print('Valor inválido.')
            continue
            
         
main()