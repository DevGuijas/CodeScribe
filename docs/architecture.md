# Arquitetura do Sistema CodeScribe

## 1. Visão Geral
O CodeScribe é uma ferramenta de linha de comando (CLI) baseada em uma arquitetura de **Pipeline (Pipe and Filter)**. O dado (código-fonte) entra, passa por estágios de transformação e sai enriquecido (documentação).

## 2. Diagrama de Fluxo de Dados

[Código Legado (.py)] 
       ⬇
(1) Módulo de Leitura (I/O)
       ⬇
(2) Parser AST (Abstract Syntax Tree) -> *Extrai apenas assinaturas de funções e classes*
       ⬇
(3) Motor de Prompt (LangChain) -> *Monta o contexto otimizado*
       ⬇
(4) LLM Inference (Ollama/Llama3) -> *Geração de texto Local*
       ⬇
(5) Gerador de Markdown -> *Formatação final*
       ⬇
[Arquivo README.md ou Docstrings]

## 3. Componentes Principais

### A. Interface CLI (Typer)
Responsável por interagir com o usuário, receber argumentos (caminho dos arquivos, modelo desejado) e exibir barras de progresso.

### B. O Parser AST (Core Engineering)
Diferente de ferramentas comuns que leem o arquivo como texto bruto (`string`), o CodeScribe converte o código Python em uma árvore sintática.
- **Entrada:** Código Fonte.
- **Processamento:** Identificação de nós `FunctionDef` e `ClassDef`.
- **Saída:** Metadados (Nome da função, argumentos, retorno e decoradores) sem o "ruído" do código imperativo interno. Isso economiza tokens e foca a IA na intenção do método.

### C. Camada de LLM (Local Inference)
Utiliza o `LangChain` para abstrair a conexão com o modelo.
- **Backend:** Ollama (rodando em background na máquina host).
- **Modelo Padrão:** Llama 3 (8B parâmetros) ou Mistral.
- **Vantagem:** Privacidade total dos dados (Air-gapped) e custo zero.

## 4. Decisões de Design
1. **Modelos Locais:** Para eliminar custos de API e latência de rede.
2. **AST vs RegEx:** O uso de AST previne erros de leitura em códigos mal formatados que expressões regulares não capturariam.