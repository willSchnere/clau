class CadastroCliente ():
    def __init__(self):
        self.cadastro = []


    def cadastrar_cliente (self,cliente):
        self.cadastro.append(cliente)
        if len(self.cadastro) > 0:
            return "Cadastro realizado com sucesso"
        if not '@' in cliente.email:
            return"Cadastro não realizado,email invalido"
        if len(cliente.nome) < 3:
            return"Cadastro não realizado nome curto demais"
        if (cliente.idade) < 18:
            return"Cadastro negado voce e menor de idade"
        
        