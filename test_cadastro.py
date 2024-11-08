from cliente import Cliente
from cadastro_cliente import CadastroCliente
def test_cadastro_cliente_com_sucesso():
    cliente = Cliente('will',20,'will@teste.com')
    cadastro_cliente = CadastroCliente ()
    resposta =cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro realizado com sucesso"
    
def test_cadastro_cliente_com_nome_menor_que_tres_caracteres():
        cliente = Cliente('wi',20,'will@teste.com')
        cadastro_cliente = CadastroCliente ()
        resposta =cadastro_cliente.cadastrar_cliente(cliente)
        assert resposta == "Cadastro não realizado nome curto demais"

def test_cadastro_cliente_menor_que_18_anos():
        cliente = Cliente('will',5,'will@teste.com')
        cadastro_cliente = CadastroCliente ()
        resposta =cadastro_cliente.cadastrar_cliente(cliente)
        assert resposta == "Cadastro negado voce e menor de idade"
    
def test_lista_de_clientes():
        cliente = Cliente('will',20,'will@teste.com')
        cadastro_cliente = CadastroCliente ()
        resposta =cadastro_cliente.cadastrar_cliente(cliente)
        assert resposta == "Cadastro realizado com sucesso"
    
    