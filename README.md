# Sistema de Gerenciamento de Eventos e Ingressos

## 1. Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema de gerenciamento de eventos e venda de ingressos, utilizando Python e os conceitos de Programação Orientada a Objetos (POO).

O sistema permite cadastrar eventos, gerenciar participantes e organizadores, criar contas de usuários, realizar autenticações e administrar ingressos.

O objetivo é aplicar os principais conceitos de POO na construção de uma aplicação funcional, organizada e que represente um cenário real.

## 2. Objetivos do trabalho

O desenvolvimento do projeto busca atender aos seguintes objetivos:

1. **Mapear as entidades:** identificar os principais elementos do sistema, seus atributos, responsabilidades e comportamentos.
2. **Modelar o sistema:** representar as classes, seus atributos, métodos e relacionamentos por meio de um diagrama de classes.
3. **Implementar o modelo:** desenvolver as classes em Python, aplicando os conceitos de Programação Orientada a Objetos.
4. **Desenvolver uma interface interativa:** criar um terminal com utilização de `input()` e `print()` para permitir a interação do usuário com o sistema.

## 3. Tema escolhido: Eventos e Ingressos

O projeto tem como tema o gerenciamento de eventos e ingressos, contemplando diferentes modalidades de eventos, como:

- Shows;
- Palestras;
- Eventos esportivos.

### Principais entidades

- **Pessoa:** classe base para representar os usuários do sistema.
- **Cliente:** representa os usuários que podem adquirir ingressos.
- **Organizador:** representa os responsáveis pela criação e administração dos eventos.
- **Evento:** representa os eventos cadastrados no sistema.
- **Ingresso:** representa os ingressos disponibilizados para os participantes.

A estrutura utiliza hierarquias de classes para especializar comportamentos e responsabilidades, permitindo que diferentes tipos de eventos e usuários possuam características próprias.

## Onde cada requisito é cumprido

### R1 - Classes e objetos
- Classes em `src/modelos/`: `Pessoa` (`pessoa.py:6`), `Cliente` (`cliente.py:5`), `Organizador` (`organizador.py:5`), `Ingresso` (`ingresso.py:3`), `Evento` (`evento.py:16`) e `Sistema` (`sistema.py:9`).
- Instâncias criadas em `dados_exemplo.py:17-54`.

### R2 - Composição
- `Organizador` possui uma lista de eventos (`organizador.py:9`).
- `Evento` possui seus ingressos (`evento.py:23`) e referencia o organizador (`evento.py:29`).
- `Cliente` guarda seus ingressos (`cliente.py:8`).
- `Ingresso` referencia cliente e evento (`ingresso.py:8-9`).
- `Sistema` agrega as contas (`sistema.py:11`).

### R3 - Encapsulamento
- Atributos protegidos `_cpf`, `_nome` e `_senhaH` (`pessoa.py:15, 33, 65`).
- Em `Evento`: `_nome`, `_data`, `_local`, `_valor_base`, `_capacidade` e `_ingressos` (`evento.py:23, 52-102`), com `_ingressos` exposto apenas como tupla somente leitura (`evento.py:116-118`).
- Em `Sistema`: `_contas`, `_eventos` e `_gerarHash` (`sistema.py:11-14`).

### R4 - Métodos de classe e estáticos
- `@classmethod total_de_eventos` (`evento.py:155-157`).
- `@staticmethod _validar_texto` e `_validar_idade` (`evento.py:34-44`).
- `@staticmethod _gerarHash` (`sistema.py:14-18`).

### R5 - Properties
- Em `Pessoa`: `cpf`, `senhaH` e `nome`, com validação nos setters (`pessoa.py:18-65`).
- Em `Evento`: `nome`, `data`, `local`, `idade_minima`, `valor_base` e `capacidade`, com setters validados (`evento.py:46-102`), e propriedades somente leitura `vagas_disponiveis`, `ocupacao`, `faturamento` e `ingressos` (`evento.py:104-118`).
- Em `Show`: `preco_com_taxa` (`evento.py:176-178`).

### R6 - Atributos de classe
- Contadores de id compartilhados: `Pessoa.id_user` (`pessoa.py:7`), `Ingresso.id_ing` (`ingresso.py:4`) e `Evento._contador_id` (`evento.py:19`).
- Contador `Evento.total_criados` (`evento.py:20, 32`).
- Constante `Show.TAXA_SERVICO` (`evento.py:170`).

### R7 - Herança e `super()`
- `Cliente(Pessoa)` (`cliente.py:5`, `super().__init__` na linha 7).
- `Organizador(Pessoa)` (`organizador.py:5`, `super().__init__` na linha 8 e `super().__str__()` na linha 45).
- `Show`, `Palestra` e `Esportivo` herdam de `Evento` (`evento.py:167, 194, 214`).

### R8 - Sobrescrita e polimorfismo
- `tipo`, `calcular_preco`, `pode_acessar` e `exportar` são sobrescritos em `Show` (`evento.py:172-191`), `Palestra` (`evento.py:197-211`) e `Esportivo` (`evento.py:217-232`), cada um com regras próprias de preço e acesso.
- `Organizador.__str__` sobrescreve o de `Pessoa` (`organizador.py:44`).
- Polimorfismo em uso: `vender_ingresso` chama `self.calcular_preco` e `self.pode_acessar` sem saber o tipo do evento (`evento.py:138, 144`), e o menu chama `evento.exportar()` para qualquer tipo (`menu.py:216`).

### R9 - Classes abstratas
- `Pessoa(ABC)` com `__init__` abstrato (`pessoa.py:6, 9-10`).
- `Evento(ABC)` com `tipo`, `calcular_preco`, `pode_acessar` e `exportar` abstratos (`evento.py:16, 120-135`).

### R10 - Interface / Protocol
- Não há `Intergace`, porém os protocolos estam inseridos em `cpf` e `senha`


## 5. Funcionalidades do sistema

O sistema disponibiliza funcionalidades para o gerenciamento de contas, eventos e ingressos.

Entre as principais operações estão:

- Cadastro de clientes e organizadores;
- Autenticação e login de usuários;
- Criação e gerenciamento de eventos;
- Consulta e listagem de eventos cadastrados;
- Busca de eventos e usuários por identificadores;
- Criação e gerenciamento de ingressos;
- Relacionamento entre clientes, eventos e ingressos;
- Consulta de informações e valores dos eventos;
- Cálculos e relatórios relacionados aos eventos e ingressos.

O sistema também possui dados de exemplo para facilitar a demonstração de suas funcionalidades.

## 6. Interface de interação

A interação com o sistema ocorre por meio de um terminal interativo, desenvolvido utilizando as funções nativas `input()` e `print()` do Python.

O menu permite que o usuário selecione as operações disponíveis, informe os dados necessários e visualize os resultados das ações realizadas.

As regras de negócio são implementadas nas classes de domínio, enquanto o menu é responsável pela interação com o usuário e pela apresentação das informações.

## 7. Organização do projeto

A estrutura do projeto foi organizada para separar as responsabilidades e facilitar a manutenção do código.

```text
trabalho-poo/
│
├── README.md
│
├── docs/
│   └── diagrama-classes.png
│
└── src/
    ├── main.py
    ├── menu.py
    ├── excecoes.py
    │
    └── modelos/
        ├── __init__.py
        ├── pessoa.py
        ├── cliente.py
        ├── organizador.py
        ├── evento.py
        └── ingresso.py
```

*A estrutura acima é uma referência organizacional e pode variar conforme a implementação final.*

## 8. Tecnologias e padrões utilizados

- **Linguagem:** Python 3.10 ou superior.
- **Paradigma:** Programação Orientada a Objetos.
- **Interface:** Terminal interativo.
- **Tipagem:** Type Hints para melhorar a clareza e a organização do código.
- **Documentação:** Docstrings para descrever classes e métodos públicos.
- **Nomenclatura:** Classes utilizando o padrão `PascalCase`.

## 9. Como executar o projeto

No terminal, acesse a pasta principal do projeto e execute:

```bash
python src/main.py
```

O sistema iniciará o menu principal, permitindo acessar as funcionalidades disponíveis.

## 10. Considerações finais

Caso haja alguma dúvida, uma documentação não muito detalhada, mas ainda útil está presente em: https://docs.google.com/document/d/16CV4fPdcpRlNkwmoKA_s9GnVgVjiy4YReXRAEYD4YdY/edit?usp=sharing
