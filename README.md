# Sistema de Autenticação - **Monte Seu Login**

## Descrição

Este projeto tem como objetivo criar um sistema simples de cadastro, login e visualização de usuários utilizando **banco de dados SQLite**. O sistema permite registrar usuários, realizar login e visualizar os usuários cadastrados.

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Cadastrar Usuário**: O usuário pode se cadastrar com nome de usuário e senha.
2. **Login**: O usuário pode fazer login verificando nome de usuário e senha.
3. **Exibir Usuários**: O sistema exibe todos os usuários cadastrados no banco de dados.

---

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para o desenvolvimento.
- **SQLite**: Banco de dados embutido utilizado para armazenar dados de usuários de forma persistente.
- **Git**: Controle de versão do código-fonte.

---

## Como Funciona o Sistema

O sistema utiliza um banco de dados SQLite para armazenar informações de login de usuários de forma persistente. As informações dos usuários são armazenadas em uma tabela **`usuarios`** no banco de dados **`sistema_autenticacao.db`**.

### Estrutura do Banco de Dados

O banco de dados **`sistema_autenticacao.db`** contém uma tabela chamada **`usuarios`**, com as seguintes colunas:

- **id** (inteiro, chave primária, autoincremento)
- **nome_usuario** (texto, único)
- **senha** (texto)

---


