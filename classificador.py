import openai, json, re, os
from dotenv import load_dotenv


# --- Carregar variáveis do .env ---
load_dotenv(override=True)  
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("⚠️ Chave da OpenAI não encontrada. Coloque no .env")
    exit()

print(">>> CHAVE CARREGADA:", openai.api_key[:10])



def classify_and_respond(email_text):

    prompt = f"""
Você é um classificador de emails.  
Retorne apenas JSON válido no formato:

{{
  "categoria": "Produtivo" ou "Improdutivo",
  "resposta": "Texto da resposta sugerida"
}}

Regras:
- "Produtivo": requer ação ou resposta (ex.: solicitação, dúvidas, documentos).
- "Improdutivo": não requer ação (ex.: agradecimento, parabéns, mensagens sociais).

Email:
\"\"\"{email_text}\"\"\"
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0
        )

        content = response.choices[0].message.content.strip()
        # Extrair apenas JSON
        start = content.find("{")
        end = content.rfind("}") + 1
        result = json.loads(content[start:end])

        categoria = result.get("categoria", "").strip().capitalize()
        resposta = result.get("resposta", "").strip()
        if categoria not in ["Produtivo", "Improdutivo"]:
            categoria = "Indefinido"

        return dict(categoria=categoria, resposta=resposta, msg=email_text)

    except Exception as e:
        print("Erro IA:", e)
        return dict(categoria="Indefinido", resposta="Não consegui classificar este email.", msg=email_text)
