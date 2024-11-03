import sys
import subprocess

def install_dependencies():
    # Verifica se o Python está instalado
    if sys.executable is None:
        print("Python não está instalado ou não foi encontrado.")
        sys.exit(1)

    # Instalar as dependências globalmente
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--upgrade"], check=True)
        print("Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao instalar as dependências.")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
