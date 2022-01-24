# Desafio 9.3 Media do Aluno
#
# Classe Aluno possui os atributos:
# - Nome => string - Status => Aprovado ou Não Aprovado (booleano) - Nota1 => float - Nota2
# => float - Media => float
#
#  Classe também possui um método:
# - Mostrar Informações (mostrar_informacoes) => Fala o nome do aluno e se ele foi aprovado ou
# não - Calcular Média (calcular_media) => Calcula e retorna a média do aluno - Inserir Nota
# (inserir_nota) => Adiciona valor nas notas do aluno (2 parâmetros de nota)
# 
# Regras:
# - Para passar ele precisa de 6 - Nome será enviado no construtor - Nota1 e Nota2 será enviado por
# parâmetro => Inserir Nota

class Aluno(object):
    status = False

    def __init__(self, nome):
        self.nome = nome

    def inserir_notas(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_info(self):
        status = (self.calcular_media() >= 6)
        if (status):
            print(f"O aluno {self.nome} foi aprovado")
        else:
            print(f"O aluno {self.nome} não foi aprovado")