# CodeScribe: Automated Documentation Generator using GenAI 🧠

> Trabalho de Conclusão de Curso (TCC) - Engenharia de Software - Universidade Católica do Salvador

## 📌 Sobre o Projeto
O **CodeScribe** é uma ferramenta de linha de comando (CLI) projetada para resolver o problema da falta de documentação em sistemas legados. Utilizando **Inteligência Artificial Generativa (LLMs)** e Análise Estática de Código (AST), a ferramenta lê arquivos de código fonte e gera documentação técnica detalhada, docstrings e diagramas automaticamente.

## 🚀 Funcionalidades Principais
- **Análise via AST:** Processa o código estruturalmente para economizar tokens e melhorar o contexto.
- **Suporte a Modelos:** Integração com modelos locais via Ollama (Llama 3).
- **Saída Flexível:** Gera documentação em Markdown (.md) ou Docstrings (in-code).
- **CLI Intuitiva:** Uso simples via terminal.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Orquestração de IA:** LangChain
- **Análise de Código:** Python `ast` module
- **LLMs:** Ollama
- **CLI:** Click ou Typer

## ⚙️ Instalação e Uso

1. Clone o repositório:
   ```bash
   git clone [https://github.com/DevGuijas/codescribe.git](https://github.com/DevGuijas/codescribe.git)
