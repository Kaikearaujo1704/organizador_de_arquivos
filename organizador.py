import os
import shutil
import time


class Organizador:

    def __init__(self, pasta):

        self.pasta = pasta

        self.tipos = {

            ".png": "Imagens",
            ".jpg": "Imagens",
            ".jpeg": "Imagens",
            ".gif": "Imagens",
            ".bmp": "Imagens",
            ".webp": "Imagens",

            ".mp4": "Videos",
            ".mkv": "Videos",
            ".avi": "Videos",
            ".mov": "Videos",

            ".mp3": "Musicas",
            ".wav": "Musicas",

            ".pdf": "PDF",

            ".doc": "Word",
            ".docx": "Word",

            ".xls": "Excel",
            ".xlsx": "Excel",

            ".ppt": "PowerPoint",
            ".pptx": "PowerPoint",

            ".zip": "Compactados",
            ".rar": "Compactados",
            ".7z": "Compactados",

            ".py": "Python",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C",

            ".txt": "Texto"
        }

    def organizar(self):

        inicio = time.time()

        total = 0

        movidos = {}

        for arquivo in os.listdir(self.pasta):

            caminho = os.path.join(self.pasta, arquivo)

            if os.path.isdir(caminho):
                continue

            nome, extensao = os.path.splitext(arquivo)

            extensao = extensao.lower()

            if extensao in self.tipos:

                destino = self.tipos[extensao]

            else:

                destino = "Outros"

            pasta_destino = os.path.join(self.pasta, destino)

            if not os.path.exists(pasta_destino):

                os.makedirs(pasta_destino)

            novo_caminho = os.path.join(pasta_destino, arquivo)

            try:

                shutil.move(caminho, novo_caminho)

                total += 1

                if destino not in movidos:
                    movidos[destino] = 0

                movidos[destino] += 1

            except Exception as erro:

                print(f"Erro ao mover {arquivo}: {erro}")

        fim = time.time()

        tempo = round(fim - inicio, 2)

        return {

            "total": total,
            "tempo": tempo,
            "categorias": movidos

        }
