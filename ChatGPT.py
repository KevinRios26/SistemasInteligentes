import openai

# Configurar la API de OpenAI con tu clave de API
openai.api_key = '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'
#openai.api_key = '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'

# Definir una función para interactuar con ChatGPT
def interactuar_con_chatgpt(mensaje):
     respuesta = openai.Completion.create(
         engine='text-davinci-003',
         prompt=mensaje,
         max_tokens=150,
         n=1,
         #stop=None,
         temperature=0.7,
         #top_p=None,
         #frequency_penalty=None,
         #presence_penalty=None
     )
    
     return respuesta.choices[0].text.strip()

 # Ejemplo de uso
pregunta = "Hola, ¿cómo estás?"
respuesta = interactuar_con_chatgpt(pregunta)
print(respuesta)


