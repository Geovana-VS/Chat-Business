import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

context = [
    {"role": "system", "content": (
        "Você é um especialista em análise de negócios e Gestão empresarial. "
        "Responda apenas sobre gestão empresarial, KPIs, modelagem de processos, "
        "e tomadas de decisão estratégicas. "
        "Se alguém perguntar algo fora desse contexto, diga que só pode responder sobre análise de negócios. "
        "Além disso, ao responder a terceita pergunta feita pelo usuario, finalise a conversa educadamente"
        "Ao finalizar, contextualise as perguntas e crie um resumo dos temas perguntados de modo que fique claro o que o usuário buscou saber."
    )}
]

def collect_messages():
    temas = []
    iterations = 0
    while iterations < 3:
        prompt = input("Digite sua pergunta sobre análise de negócios: ")
        context.append({'role': 'user', 'content': prompt} )  

        
        user_messages = sum(1 for msg in context if msg["role"] == "user")

        response = client.chat.completions.create(
            messages=context,
            model="llama-3.3-70b-versatile"
        ).choices[0].message.content
        
        context.append({'role': 'assistant', 'content': response})  

        temas.append(prompt)
       
        
        print("Assistant:", response)

        iterations += 1  

       
if __name__ == "__main__":
    collect_messages()
