class CadastroCliente ():
    def __init__(self):
        self.cadastro = []


    def cadastrar_cliente (self,cliente):
        self.cadastro.append(cliente)
        return "Cadastro realizado com sucesso"