livros = [
    ["Cem anos de Solidão","Gabriel Garcia Marquez",1997,448],
    ["Crime e Castigo","Fiódor Dostoiévski", 2016,592],
    ["O retrato de Dorian Gray","Oscar Wilde",2018,224],
    ["A hora da estrela","Clarice Lispector",2017,225],
    ["O avesso da pele","Jeferson Tenório",2020,192],
    ["Crônica de uma morte anunciada","Gabriel Garcia Marquez",1981,160],
    ["Quarto de Despejo","Carolina Maria de Jesus",2019,200],
    ["Holocausto Brasileiro","Daniela Arbex",2019,280],
    ["É isto um homem?","Primo Levi",2013,176],
    ["Hamlet","Willian Shakespeare",2015,320]
]


with open('meus_livros.csv','w') as meus_livros:
    meus_livros.write("Título,Autor,Ano de Publicação,Número de Páginas\n")
    for livro in livros[1:]:
        meus_livros.write(",".join(map(str, livro)) + "\n")

