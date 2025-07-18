# Test Data Manager (TDM) Application

O Test Data Manager (TDM) é uma aplicação para gerar, mascarar e gerenciar dados de teste realistas e reutilizáveis para diversos cenários de testes. O foco é garantir qualidade e privacidade dos dados, sendo uma ferramenta essencial para desenvolvedores e times de QA.

## Funcionalidades

- **Geração de Dados**: Cria dados de teste realistas para usuários brasileiros usando a biblioteca Faker, incluindo nome, CPF, endereço, CEP, número, e-mail, telefone, cidade, estado e país.
- **Mascaramento de Dados**: Anonimiza informações sensíveis como e-mail, telefone e CPF para proteger a privacidade.
- **Gestão de Dados**: Salva de forma eficiente tanto os dados originais (sem máscara) quanto os dados mascarados em arquivos separados, facilitando a comparação e validação.
- **Funções Utilitárias**: Funções auxiliares para validação, formatação e logging.

## Estrutura do Projeto

```
tdm-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── data_generation
│   │   └── generator.py
│   ├── data_masking
│   │   └── masker.py
│   ├── data_management
│   │   └── manager.py
│   └── utils
│       └── helpers.py
├── requirements.txt
├── setup.py
└── README.md
```

## Instalação

1. Clone o repositório:
   ```
   git clone <repository-url>
   cd tdm-app
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Como Usar

Para executar a aplicação e gerar os dados de teste:

```
python src/main.py
```

Isso irá criar dois arquivos na pasta `src`:
- `raw_data.txt`: Contém os dados originais (sem máscara) gerados.
- `masked_data.txt`: Contém os mesmos dados, mas com os campos sensíveis (e-mail, telefone, CPF) mascarados.

## Como Funciona

- A aplicação gera uma lista de usuários fictícios com dados realistas do Brasil.
- Salva os dados originais em `raw_data.txt`.
- Em seguida, mascara os campos sensíveis e salva em `masked_data.txt`.
- Você pode abrir ambos os arquivos para comparar os dados originais e mascarados.

## Contribuição

Contribuições são bem-vindas! Envie um pull request ou abra uma issue para sugestões de melhorias ou correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.