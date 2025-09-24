class Midia:
    def __init__(self,titulo:str,duracao_seg:int):
        self.titulo=titulo
        self.duracao_seg=duracao_seg

    def exibir(self):
        print(f"Titulo {self.titulo} com {self.duracao_seg} segundos.")

    def __str__(self):
        return f"{self.titulo}"

class Musica(Midia):
    def __init__(self,titulo,duracao_seg,artista):
        super().__init__(titulo,duracao_seg)
        self.artista=artista

    def exibir(self):
        print(f"Titulo {self.titulo} é uma música de {self.artista} com {self.duracao_seg} segundos.")

class Video(Musica):
    def __init__(self,titulo,duracao_seg,artista,resolucao):
        super().__init__(titulo,duracao_seg,artista)
        self.resolucao=resolucao

    def exibir(self):
        print(f"Titulo {self.titulo} é um vídeo de {self.artista} com {self.duracao_seg} segundos e com {self.resolucao} de resolução.")


musica1=Musica("titulo1",120,"artista1")
musica2=Musica("titulo2",180,"artista2")
video1=Video("titulo3",360,"artista3",1920)
video2=Video("titulo4",280,"artista4",720)

dicionario={"musicas":[] ,"videos":[]}

dicionarios_midia:dict[str, list[Midia]] = {"musicas":[], "videos":[]}
dicionarios_midia["musicas"].append(musica1)
dicionarios_midia["musicas"].append(musica2)
dicionarios_midia["videos"].append(video1)
dicionarios_midia["videos"].append(video2)


#print(dicionarios_midia) # dicionarios dá valores estranhos desta forma 

for item in dicionarios_midia.values():
    for midia in item:
        midia.exibir()