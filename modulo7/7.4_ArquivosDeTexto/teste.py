def linha_valida(linha):
    return not linha.startswith('"track_name"')

musicas_por_ano = {}

with open("spotify-2023.csv", "r", encoding='latin-1') as spotify_data:
    next(spotify_data)  # Pula a primeira linha (cabeçalho)
    for linha in spotify_data:
        campos = linha.strip().split(',')
        if not linha_valida(linha):
            continue
        track_name = campos[0].strip('"')
        artist_name = campos[1].strip('"')
        released_year = campos[3].strip('"')
        if released_year and released_year.isdigit():  # Verifica se é um ano válido
            released_year = int(released_year)
        else:
            continue  # Ignora a linha se o ano não estiver presente ou não for válido

        # Encontrar o campo de streams corretamente
        streams = None
        for campo in campos:
            if campo.isdigit():
                # Verifica se o campo é um número grande, presumindo que streams seja um número grande
                if len(campo) > 6:  # Supõe que streams tenha pelo menos 7 dígitos
                    streams = int(campo)
                    break

        if streams is None:
            continue  # Ignorar esta linha se não pudermos encontrar o número de streams

        if 2012 <= released_year <= 2022:
            if released_year not in musicas_por_ano:
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
            elif streams > musicas_por_ano[released_year][3]:
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

# Transformar o dicionário em uma lista ordenada de acordo com os anos
top_songs = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano.keys())]

# Imprimir a lista final das músicas mais tocadas de cada ano
print(top_songs)
