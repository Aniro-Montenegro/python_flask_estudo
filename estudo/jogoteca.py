from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Resident Evil', 'RPG', 'Playstation')
    jogo3 = Jogo('Final Fight', 'RPG', 'Nintendo')
    listaJogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


app.run()
