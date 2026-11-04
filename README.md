# Objetivos do trabalho: 

1. **Mapear as entidades** do cenário escolhido (quem são os "objetos" do problema, quais dados possuem e o que sabem fazer).
2. **Desenhar o modelo** (diagrama de classes simples) mostrando atributos, métodos e relacionamentos. (opcional)
3. **Implementar** o modelo em Python, aplicando os conceitos de POO.
4. **Criar um terminal interativo** (`input()` / `print()`) para operar o sistema.

Tema: | 9 | **Eventos e Ingressos**
Entidades Sugeridas: Evento (Show, Palestra, Esportivo), Participante, Ingresso, Organizador
Ideia de polimorfia/hierarquia: Cada evento calcula lotação, preço e regras de acesso


### Requisitos de Orientação a Objetos (obrigatórios)

Cada item abaixo deve aparecer **pelo menos uma vez** no código e o grupo deve saber **apontar onde** durante a apresentação.

| # | Conceito |  O que se espera |
|---|---|---|---|
| R1 | **Classes e objetos** | No mínimo **4 classes** de domínio (sem contar exceções e o menu) com `__init__` e `self` |
| R2 | **Composição** | Objetos que contêm outros objetos (ex.: `Turma` possui lista de `Aluno`) |
| R3 | **Encapsulamento** | Atributos protegidos (`_attr`) e/ou privados (`__attr`) acessados apenas via métodos/properties |
| R4 | **Métodos de classe e estáticos** | Pelo menos um `@classmethod` (ex.: construtor alternativo `from_string`, contador) e um `@staticmethod` (ex.: validador) |
| R5 | **Properties** | `@property` com **setter validando dados** e pelo menos uma **property calculada** |
| R6 | **Atributos de classe** | Constantes ou contadores compartilhados (ex.: `LIMITE_VAGAS`, `total_criados`) |
| R7 | **Herança e `super()`** | Pelo menos **uma hierarquia** com 1 classe base e **no mínimo 2 subclasses** |
| R8 | **Sobrescrita e polimorfismo** | Métodos reescritos nas subclasses e chamados de forma uniforme (ex.: loop sobre uma lista mista) |
| R9 | **Classe abstrata** | Uso de `ABC` e `@abstractmethod` definindo o contrato da hierarquia |
| R10 | **Interface / Protocol** | Pelo menos um `Protocol` (ex.: `Pagavel`, `Exportavel`, `Notificavel`) usado por classes **sem relação de herança** 

### Requisitos do Terminal Interativo

- Menu principal em loop com opção **Sair**.
- No mínimo **5 opções funcionais**, contemplando:
  - **Cadastrar** pelo menos 2 tipos de entidade diferentes;
  - **Listar / consultar** (incluindo uma listagem polimórfica);
  - **Buscar** um objeto por identificador (código, CPF, placa, etc.);
  - Pelo menos **2 operações de negócio** que relacionem objetos (ex.: matricular, reservar, alugar, fechar conta, lançar nota);
  - Pelo menos **1 relatório / cálculo** (ex.: faturamento do dia, boletim, ranking, ocupação).
- O sistema deve iniciar com alguns **dados de exemplo** já carregados (para agilizar a demonstração).
- As regras de negócio **devem estar nas classes de domínio**, não no menu. O menu apenas lê os dados, chama os métodos e exibe o resultado/erros.

### Organização do Código

Estrutura sugerida (pode ser adaptada):

```
trabalho-poo/
├── README.md
├── docs/
│   └── diagrama-classes.png      # ou .md com diagrama em texto / Mermaid
├── src/
│   ├── main.py                   # ponto de entrada: python src/main.py
│   ├── menu.py                   # terminal interativo
│   ├── excecoes.py               # exceções customizadas (opctional)
│   ├── interfaces.py             # Protocols
│   └── modelos/
│       ├── __init__.py
│       ├── pessoa.py
│       └── ...
```

- Usar **type hints** e **docstrings** nas classes e métodos públicos (padrão das aulas).
- Nomes de classes em `PascalCase`.
- Não utilizar bibliotecas externas (apenas biblioteca padrão do Python).
