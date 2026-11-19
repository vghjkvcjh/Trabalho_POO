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

## 4. Conceitos de Programação Orientada a Objetos aplicados

O projeto contempla os seguintes requisitos de POO:

| Requisito | Conceito | Aplicação |
|---|---|---|
| R1 | Classes e objetos | Representação das entidades do sistema por meio de classes e instâncias. |
| R2 | Composição | Relacionamento entre eventos, ingressos, organizadores e participantes. |
| R3 | Encapsulamento | Utilização de atributos protegidos e propriedades para controlar o acesso aos dados. |
| R4 | Métodos de classe e estáticos | Utilização de `@classmethod` e `@staticmethod` para operações específicas. |
| R5 | Properties | Utilização de `@property` e setters para consultar, modificar e validar atributos. |
| R6 | Atributos de classe | Utilização de constantes e atributos compartilhados entre instâncias. |
| R7 | Herança e `super()` | Especialização de classes por meio de uma classe base e suas subclasses. |
| R8 | Sobrescrita e polimorfismo | Implementação de métodos com comportamentos diferentes nas classes derivadas. |
| R9 | Classes abstratas | Utilização de `ABC` e `@abstractmethod` para estabelecer contratos entre classes. |
| R10 | Interface / Protocol | Utilização de `Protocol` para definir comportamentos que podem ser implementados por classes independentes. |

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
- **Bibliotecas:** Apenas bibliotecas nativas da linguagem Python.
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
