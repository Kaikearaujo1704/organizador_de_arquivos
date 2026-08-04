import os
from datetime import datetime


class Relatorio:

    def __init__(self):

        self.pasta_relatorios = "relatorios"

        if not os.path.exists(self.pasta_relatorios):
            os.makedirs(self.pasta_relatorios)

        self.arquivo = os.path.join(
            self.pasta_relatorios,
            "ultimo_relatorio.txt"
        )

    def salvar(self, dados):

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            arquivo.write("=" * 40 + "\n")
            arquivo.write("RELATÓRIO DE ORGANIZAÇÃO\n")
            arquivo.write("=" * 40 + "\n\n")

            arquivo.write(
                f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            )

            arquivo.write(f"Total de arquivos: {dados['total']}\n")
            arquivo.write(f"Tempo: {dados['tempo']} segundos\n\n")

            arquivo.write("Arquivos por categoria:\n\n")

            for categoria, quantidade in dados["categorias"].items():

                arquivo.write(
                    f"{categoria}: {quantidade} arquivo(s)\n"
                )

    def mostrar(self):

        if not os.path.exists(self.arquivo):

            print("Nenhum relatório encontrado.")
            return

        with open(self.arquivo, "r", encoding="utf-8") as arquivo:

            print(arquivo.read())
