
# 📊 Consulta de Dados via Supabase (Somente Leitura)

Este projeto permite que qualquer usuário consulte dados públicos de uma tabela no banco de dados **Supabase**, utilizando **Python**, com **acesso somente leitura**, seguro e fácil de usar.

---

## ✅ Requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3.8 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) (opcional, mas recomendado)

---

## 🚀 Como usar este projeto

### 🔹 Passo 1: Baixar o projeto

#### Opção A: Usando Git (recomendado)

Abra o terminal (CMD, PowerShell ou Terminal) e digite:

```bash
git clone https://github.com/Fabio13Gomes/consulta_dados.git
cd consulta_dados
```

#### Opção B: Baixando como ZIP

1. Acesse: [https://github.com/Fabio13Gomes/consulta_dados](https://github.com/Fabio13Gomes/consulta_dados)
2. Clique em **Code > Download ZIP**
3. Extraia o arquivo ZIP no seu computador
4. Abra a pasta extraída

---

### 🔹 Passo 2: Instalar as bibliotecas necessárias

Abra o terminal dentro da pasta do projeto e digite:

```bash
pip install -r requirements.txt
```

Isso instalará as seguintes bibliotecas:

- `pandas`: manipulação de dados
- `sqlalchemy`: conexão com banco de dados
- `psycopg2-binary`: driver PostgreSQL
- `python-dotenv`: leitura de variáveis de ambiente seguras

---

### 🔹 Passo 3: Entendendo o `.env`

Dentro da pasta do projeto existe um arquivo `.env` com as informações de conexão. **Você não precisa alterar nada**, pois ele já vem pronto para uso com acesso de leitura.

Exemplo do conteúdo:

```env
DB_USER=cliente_leitor
DB_PASS=cliente123
DB_HOST=aws-0-sa-east-1.pooler.supabase.com
DB_PORT=6543
DB_NAME=postgres
DB_PREFIX=cliente_leitor.uonexuswclkemtamrljp
```

---

### 🔹 Passo 4: Executar a consulta

Execute no terminal:

```bash
python main.py
```

Este comando irá:

✅ Conectar ao banco Supabase  
✅ Buscar a tabela `minha_tabela`  
✅ Exibir os dados no terminal  
✅ Salvar os dados em um arquivo local chamado `dados_consultados.csv`

---

### 🔹 Passo 5: Visualizar os dados

Após executar o script, será criado o arquivo:

```
dados_consultados.csv
```

Você pode abrir esse arquivo em:

- Microsoft Excel
- LibreOffice Calc
- Google Planilhas
- Ou importar para outros projetos em Python

---

## 📁 Estrutura do Projeto

```
consulta_dados/
├── main.py                # Script principal de consulta
├── .env                   # Variáveis de ambiente (seguras)
├── requirements.txt       # Lista de bibliotecas a instalar
└── README.md              # Este manual de instruções
```

---

## 🔐 Segurança

- O acesso é feito com um usuário que **só pode ler os dados**.
- Nenhuma modificação pode ser feita no banco.
- A senha pode ser alterada ou desativada a qualquer momento.

---

## 📞 Suporte

Se tiver dúvidas ou quiser adaptar o projeto para outro banco, entre em contato com:

**Desenvolvedor:** [@Fabio13Gomes](https://github.com/Fabio13Gomes)

---

✔️ Projeto pronto para uso profissional com segurança, simplicidade e compatível com clientes que não têm experiência técnica.
