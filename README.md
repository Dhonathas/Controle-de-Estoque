
# 🌾 Projeto Agro - Controle de Estoque Agrícola

Este projeto é um sistema simples de **cadastro e controle de insumos agrícolas**, utilizando:

- 🐍 **Flask** como framework backend (API RESTful)
- 🗃️ **SQLite** como banco de dados local
- 🧠 **Flask SQLAlchemy** como ORM
- 🎨 **HTML + CSS + JS** para a interface frontend

---

## 🚀 Como Executar o Projeto

### 1. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 2. Execute o Projeto

```bash
python app.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Endpoints da API

### ➕ Criar Item

`POST /itens`

```json
{
  "nome": "Adubo NPK",
  "descricao": "Fertilizante orgânico",
  "quantidade": 50
}
```

### 📋 Listar Itens

`GET /itens`

```json
[
  {
    "id": 1,
    "nome": "Adubo NPK",
    "descricao": "Fertilizante orgânico",
    "quantidade": 50
  }
]
```

### ❌ Remover Item

`DELETE /itens/<id>`

Exemplo: `DELETE /itens/1`

---

## 📁 Estrutura do Projeto

```
projeto_agro/
├── app.py                    # Inicializa e configura a aplicação Flask
├── database.py               # Conexão e setup do banco de dados
├── requirements.txt          # Lista de dependências
├── view/
│   ├── index.html            # Interface Web com HTML + JS
│   └── CSS/
│       └── Style.css         # Estilização do site
├── models/
│   └── item.py               # Modelo do banco de dados
├── controllers/
│   └── item_controller.py    # Rotas da API para os itens
└── README.md                 # Este arquivo
```

---

## 🎯 Objetivo

O objetivo deste projeto é demonstrar um sistema web simples de **controle de estoque agrícola**, com possibilidade de expansão para:

- Gerenciamento de insumos (fertilizantes, sementes, defensivos)
- Apoio à agricultura familiar e sustentável
- Registro de atividades e histórico de movimentações
