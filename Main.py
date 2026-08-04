import os
from organizador import Organizador
from relatorio import Relatorio


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("=" * 45)
    print("organizador de arquivos")
    print("=" * 45)
    print("1 - Organizar uma pasta")
    print("2 - Ver último relatório")
    print("3 - Sair")
    print("=" * 45)


def main():

    relatorio = Relatorio()

    while True:

        limpar_tela()
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            pasta = input("\nDigite o caminho da pasta:\n> ")

            if not os.path.exists(pasta):
                print("\nPasta não encontrada.")
                input("\nPressione ENTER...")
                continue

            organizador = Organizador(pasta)

            dados = organizador.organizar()

            relatorio.salvar(dados)

            print("\nOrganização concluída!")

            input("\nPressione ENTER...")

        elif opcao == "2":

            limpar_tela()

            relatorio.mostrar()

            input("\nPressione ENTER...")

        elif opcao == "3":

            print("\nAté mais!")
            break

        else:

            print("\nOpção inválida.")
            input("\nPressione ENTER...")


if __name__ == "__main__":
    main()
