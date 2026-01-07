from langchain_ollama import OllamaLLM

def get_llm():
    """
    Cria a conexão com o servidor Ollama rodando localmente.
    Não precisa de API KEY, pois é local.
    """
    try:
        # 'llama3' deve ser o mesmo nome que você baixou no terminal
        llm = OllamaLLM(model="llama3") 
        return llm
    except Exception as e:
        print(f"Erro ao conectar com Ollama: {e}")
        return None

if __name__ == "__main__":
    # Teste rápido para ver se funciona
    print("Tentando conectar ao Llama 3...")
    model = get_llm()
    resposta = model.invoke("Diga 'Olá, TCC!' em português.")
    print(f"Resposta da IA: {resposta}")