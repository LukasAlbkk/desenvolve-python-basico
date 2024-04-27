import emoji 

print(f"Emojis disponíveis: ")
print(emoji.emojize(':pink_heart:'))#O red_heart estava saindo pequeno por algum motivo , coloquei o pink
print(emoji.emojize(':thumbs_up:')) 
print(emoji.emojize(':thinking_face:'))
print(emoji.emojize(':partying_face:'))

frase = input("Digite uma frase e ela será emojizada: ")
print(emoji.emojize(frase))