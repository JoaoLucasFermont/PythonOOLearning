class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property

    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.duracao} min, {self.likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.tempordas = temporadas

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.tempordas} temporadas, {self.likes} likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
toc = Serie('todo mundo odeia o cris', 2005, 4)
spiderman = Filme('Spider Man 3', 2020, 200)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
toc.dar_likes()
toc.dar_likes()
toc.dar_likes()
spiderman.dar_likes()
spiderman.dar_likes()
spiderman.dar_likes()

filmes_e_series = [vingadores,atlanta,toc,spiderman]
minha_platlist = Playlist('minha playlist', filmes_e_series)

print(f'Tamanho playlist {len(minha_platlist)}')

for programa in minha_platlist:
    print(programa)
