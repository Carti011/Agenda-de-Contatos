import re
import json


def validar_nome():
    '''Função destinada a usar na hora de adicionar a chave Nome.
    Valida se o nome é válido e retorna o próprio nome.'''
    while True:
        try:
            nome = input('Digite o nome:').strip().lower()
            if len(nome.split()) > 1:
                print('Por favor digite apenas o primeiro nome')
            elif any(letra.isdigit() for letra in nome):
                print('Nome não pode possuir números')
            elif not nome:
                print('Nome não pode ser vazio')
            else:
                print('Nome válido!')
                return nome
        except ValueError:
            print('Erro inesperado. Tente novamente')


def validar_numero():
    '''Função destinada a ser usada quando precisar pedir
    para o usuário digitar um número de telefone.
    Valida e retorna o número.'''
    while True:
        numero = input("Digite o número no formato 119XXXXXXXX: ").strip()
        if len(numero) != 11:
            print("O número deve conter exatamente 11 dígitos.")
        elif not numero.isdigit():
            print("O número deve conter apenas dígitos.")
        elif numero[2] != '9':
            print("O terceiro dígito deve ser '9'.")
        else:
            print('Número válido')
            return numero


def formatar_numero(numero):
    '''Função criada para exibir um número
    formatado de um modo mais bonito.
    Retorna uma string com o número formatado.'''
    return f'({numero[:2]}){numero[2:7]}-{numero[7:]}'


def validar_email():
    '''Função destinada para pedir para o usuário digitar um email.
    Retorna um email válido.'''
    while True:
        email = input("Digite seu email: ").strip()
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.fullmatch(padrao_email, email):
            print("Email válido!")
            return email
        else:
            print("Email inválido. Tente novamente.")


def preencher(dicionario: dict) -> dict:
    '''Função destinada a preencher um dicionário.
    Retorna um dicionário preenchido com:
    - nome como chave principal
    - chave telefone com uma lista de números
    - chave email com o email do contato'''
    nome = validar_nome()
    numero = validar_numero()
    email = validar_email()
    dicionario[nome] = {'telefone': [numero], 'email': email}
    return dicionario


def contatos_disponiveis(dicionario: dict):
    '''Exibe todas as CHAVES dos contatos disponíveis.'''
    if dicionario:
        print('Esses são os contatos disponíveis:')
        for chave in dicionario:
            print(f'- {chave}')
    else:
        print('Nenhum contato disponível.')


def apagar_contato(dicionario: dict, chave):
    '''Função criada para apagar um contato.
    Quando apagado, os valores da chave nome são removidos juntos.'''
    try:
        del dicionario[chave]
        print(f'Contato "{chave}" removido com sucesso.')
    except KeyError:
        print(f'Erro: O contato "{chave}" não existe no dicionário.')


def consultar_contato(dicionario: dict, chave_consulta):
    '''Função destinada a verificar se uma chave existe.'''
    if chave_consulta in dicionario:
        print(chave_consulta, dicionario[chave_consulta])
    else:
        print(f'{chave_consulta} não existe.')


def inserir_telefone(dicionario: dict, chave_contato):
    '''Função destinada a adicionar um valor à chave telefone.'''
    if chave_contato in dicionario:
        numero = validar_numero()
        dicionario[chave_contato]['telefone'].append(numero)
        print(f'Número {numero} adicionado com sucesso ao contato "{chave_contato}".')
    else:
        print(f'Erro: O contato "{chave_contato}" não existe.')


def exibir_telefones(dicionario, nome_contato):
    '''Função que exibe os telefones de um contato.'''
    if nome_contato in dicionario:
        telefones = dicionario[nome_contato]['telefone']
        print(f'Telefones de {nome_contato}:')
        for telefone in telefones:
            print(f'- {formatar_numero(telefone)}')
    else:
        print(f'O contato "{nome_contato}" não existe.')


def exibir_email(dicionario, nome_contato):
    '''Função destinada a exibir o email de um contato.'''
    if nome_contato in dicionario:
        print(f'Email de {nome_contato}: {dicionario[nome_contato]["email"]}')
    else:
        print(f'O contato "{nome_contato}" não existe.')


def apagar_numero(dicionario: dict, chave_contato, numero):
    '''Função criada para apagar um número de telefone específico de um contato.'''
    if chave_contato in dicionario:
        if numero in dicionario[chave_contato]['telefone']:
            dicionario[chave_contato]['telefone'].remove(numero)
            print(f'Telefone "{numero}" removido com sucesso do contato "{chave_contato}".')
        else:
            print(f'O telefone "{numero}" não existe para o contato "{chave_contato}".')
    else:
        print(f'O contato "{chave_contato}" não existe no dicionário.')


def alterar_email(dicionario: dict, chave_contato):
    '''Função para alterar o email de um contato.'''
    if chave_contato in dicionario:
        email_alterado = validar_email()
        dicionario[chave_contato]['email'] = email_alterado
        print(f'O email {email_alterado} foi atualizado com sucesso para o contato "{chave_contato}".')
    else:
        print(f'Erro: O contato "{chave_contato}" não existe.')

def exibir_tudo(dicionario: dict):
    # Opção para imprimir a lista completa de contatos
    while True:
        try:
            x = input('Deseja imprimir a lista de contatos inteira? (S/N): ').lower().strip()
            if x == 's':
                print(json.dumps(dicionario, indent=2))
                break
            elif x == 'n':
                break
            else:
                print('Por favor, digite "S" para Sim ou "N" para Não.')
        except ValueError:
            print('Erro: Tente novamente.')


def main(dicionario: dict):
    while True:
        try:
            print('[0] Sair \n'
                  '[1] Adicionar Contato \n'
                  '[2] Apagar Contato \n'
                  '[3] Consultar Contato \n'
                  '[4] Inserir Novo Telefone \n'
                  '[5] Remover Telefone \n'
                  '[6] Alterar Email \n'
                  '[7] Exibir tudo')
            menu = int(input('Digite uma opção:'))
            if menu > 7 or menu < 0:
                print('Digite um número de 0 a 7')
                continue
        except ValueError:
            print('Você digitou uma letra. Tente novamente.')
            continue

        if menu == 0:
            break

        elif menu == 1:
            preencher(dicionario)

        elif menu == 2:
            contatos_disponiveis(dicionario)
            apagar = input('Digite o nome do contato que deseja apagar: ').strip()
            apagar_contato(dicionario, apagar)

        elif menu == 3:
            contatos_disponiveis(dicionario)
            consultar = input('Qual contato deseja consultar:').strip()
            consultar_contato(dicionario, consultar)

        elif menu == 4:
            contatos_disponiveis(dicionario)
            contato = input('Qual contato gostaria de inserir um novo número:').strip()
            inserir_telefone(dicionario, contato)

        elif menu == 5:
            contatos_disponiveis(dicionario)
            contato = input('Qual contato deseja remover o telefone:').strip()
            if contato in dicionario:
                exibir_telefones(dicionario, contato)
                excluir = input('Qual número você deseja excluir:').strip()
                if excluir in dicionario[contato]['telefone']:
                    apagar_numero(dicionario, contato, excluir)
                else:
                    print(f'Erro: O número "{excluir}" não está na lista.')
            else:
                print(f'Erro: O contato "{contato}" não existe.')

        elif menu == 6:
            contatos_disponiveis(dicionario)
            contato = input('Qual contato deseja alterar o email:').strip()
            alterar_email(dicionario, contato)
        
        elif menu == 7:
            exibir_tudo(contatos)


contatos = {}
main(contatos)





