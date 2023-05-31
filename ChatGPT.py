import openai

openai.api_key = ''
#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

def interactuar_con_chatgpt(mensaje):
     respuesta = openai.Completion.create(
         engine='text-davinci-003',
         prompt=mensaje,         
         max_tokens=150,         
     )    
     return respuesta.choices[0].text.strip()







