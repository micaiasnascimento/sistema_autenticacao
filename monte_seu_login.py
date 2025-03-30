import sqlite3

# Conectar ao banco de dados SQLite (ele cria o arquivo se não existir)
def conectar_bd():
    conn = sqlite3.connect('sistema_autenticacao.db')  # O banco será criado automaticamente
    return conn

# Criar a tabela de usuários (apenas na primeira execução)
def criar_tabela():
    conn = conectar_bd()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL)''')
    conn.commit()  # Salva as mudanças no banco
    conn.close()

# Função para registrar um novo usuário
def registrar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")

    conn = conectar_bd()
    c = conn.cursor()

    # Verificar se o nome de usuário já existe
    c.execute("SELECT * FROM usuarios WHERE nome_usuario = ?", (nome_usuario,))
    if c.fetchone():  # Se o usuário já existe
        print("Nome de usuário já cadastrado! Escolha outro.")
        conn.close()
        return
    
    senha = input("Digite a senha: ")

    # Inserir o novo usuário no banco de dados
    c.execute("INSERT INTO usuarios (nome_usuario, senha) VALUES (?, ?)", (nome_usuario, senha))
    conn.commit()  # Salva as mudanças no banco
    print(f"Cadastro realizado com sucesso! Usuário {nome_usuario} registrado.")
    
    conn.close()

# Função para realizar login
def login():
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    conn = conectar_bd()
    c = conn.cursor()

    # Verificar se o nome de usuário e a senha estão corretos
    c.execute("SELECT * FROM usuarios WHERE nome_usuario = ? AND senha = ?", (nome_usuario, senha))
    usuario = c.fetchone()  # Verifica se há uma correspondência no banco
    
    if usuario:
        print(f"Login bem-sucedido! Bem-vindo(a), {nome_usuario}.")
    else:
        print("Nome de usuário ou senha incorretos.")
    
    conn.close()

# Função para exibir os usuários cadastrados
def exibir_usuarios():
    conn = conectar_bd()
    c = conn.cursor()

    c.execute("SELECT nome_usuario FROM usuarios")  # Seleciona os nomes de usuário cadastrados
    usuarios = c.fetchall()  # Pega todos os resultados
    
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"- {usuario[0]}")  # Exibe o nome do usuário cadastrado

    conn.close()

# Função principal do programa
def menu():
    criar_tabela()  # Garante que a tabela será criada assim que o programa iniciar

    while True:
        print("\n=== Sistema de Autenticação ===")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Exibir usuários cadastrados")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            login()
        elif opcao == "3":
            exibir_usuarios()
        elif opcao == "4":
            print("Saindo... Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa apenas se for rodado diretamente
if __name__ == "__main__":
    menu()
