count = 0
with open("spotify-2023.csv","r", encoding='latin-1') as spotify_data:
    for linha in spotify_data:
        print(linha, end="")
        count += 1
        if count == 5:
            break
print("-"*110)
print("\n"*5)

def linha_valida(linha):
    if linha[0].startswith('"') and linha[0].endswith('"'):
        return True
    else:
        return False
musicas_por_ano = {}
with open("spotify-2023.csv","r", encoding='latin-1') as spotify_data:
    count = 0
    for linha in spotify_data:
        campos = linha.strip().split(',')
        if linha_valida(campos):
            continue
        track_name = campos[0].strip('"')
        artist_name = campos[1].strip('"')
        released_year = campos[3].strip('"')
        if released_year and released_year.isdigit():  
            released_year = int(released_year)
        else:
            continue 
        
        streams = None
        for campo in campos:
            if campo.isdigit():
                if len(campo) > 6:
                    streams = int(campo)
                    break
        if streams is None:
            continue

        if 2012 <= released_year <= 2022:
            if released_year not in musicas_por_ano:
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
            elif streams > musicas_por_ano[released_year][3]:
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

top_songs = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano.keys())]
print(top_songs)