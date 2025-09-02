import os
import shutil
import subprocess
from pathlib import Path

def remove_directories(directories, user, root):
	for directory_str in directories:
		target_dir_user = Path(user, directory_str)
		if target_dir_user.exists():
			shutil.rmtree(target_dir_user)
			print(f"Diretório removido: {target_dir_user}")
		target_dir_root = Path(root, directory_str)
		if target_dir_root.exists():
			shutil.rmtree(target_dir_root)
			print(f"Diretório removido: {target_dir_root}")

def create_symlinks():
    """
    Cria links simbólicos de /root/.local/bin para /usr/bin.
    É necessário executar este script com privilégios de root (sudo).
    """
    source_dir = Path("/root/.local/bin/")
    dest_dir = Path("/usr/bin")
    files_to_link = [
        "buildozer",
        "buildozer-remote",
        "cygdb",
        "cython",
        "cythonize",
        "virtualenv"
    ]

    # A verificação de UID não funciona no Windows, mas é uma boa prática para scripts Linux.
    try:
        if os.geteuid() != 0:
            print("Aviso: Este script precisa ser executado como root (ou com sudo) para criar links em /usr/bin.")
    except AttributeError:
        print("Aviso: Não foi possível verificar o UID. Certifique-se de executar com privilégios de administrador se necessário.")

    if not source_dir.is_dir():
        print(f"Erro: Diretório de origem '{source_dir}' não encontrado.")
        return

    if not dest_dir.is_dir():
        print(f"Erro: Diretório de destino '{dest_dir}' não encontrado.")
        return

    print(f"Criando links simbólicos de '{source_dir}' para '{dest_dir}'...")

    for filename in files_to_link:
        src_file = source_dir / filename
        dest_file = dest_dir / filename

        if not src_file.is_file():
            print(f"  Aviso: Arquivo de origem '{src_file}' não encontrado. Pulando.")
            continue

        print(f"  Linkando {src_file} -> {dest_file}")
        try:
            # Se o link/arquivo já existir, removemos para evitar erro.
            if dest_file.exists() or dest_file.is_symlink():
                print(f"    Destino '{dest_file}' já existe. Removendo para recriar.")
                dest_file.unlink()

            os.symlink(src_file, dest_file)
            print(f"    Link simbólico '{dest_file}' criado com sucesso.")
        except OSError as e:
            print(f"    Erro ao criar link simbólico para '{filename}': {e}")
        except Exception as e:
            print(f"    Um erro inesperado ocorreu: {e}")

    print("\nProcesso de criação de links simbólicos concluído.")

def run_buildozer_clean():
    """
    Executa o comando 'buildozer android clean' no diretório do projeto.
    É necessário executar este script com privilégios de root (sudo).
    """
    command = ['/root/.local/bin/buildozer', 'android', 'clean']
    working_dir = '/home/user/JogoS/tower-defense'

    print(f"Executando comando: '{' '.join(command)}' em '{working_dir}'")

    # A verificação de UID não funciona no Windows, mas é uma boa prática para scripts Linux.
    try:
        if os.geteuid() != 0:
            print("Aviso: Este script precisa ser executado como root (ou com sudo) para executar o buildozer.")
    except AttributeError:
        print("Aviso: Não foi possível verificar o UID. Certifique-se de executar com privilégios de administrador se necessário.")

    try:
        # Usando subprocess.run para executar o comando
        result = subprocess.run(
            command,
            cwd=working_dir,
            capture_output=True,
            text=True,
            check=True  # Lança uma exceção se o comando retornar um código de erro
        )
        print("\n--- Saída do Buildozer ---")
        print(result.stdout)
        print("--------------------------")
        print("\nComando 'buildozer android clean' executado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O comando '{command[0]}' ou o diretório '{working_dir}' não foi encontrado.")
    except subprocess.CalledProcessError as e:
        print("\n--- Erro ao executar o Buildozer ---")
        print(f"Código de saída: {e.returncode}")
        print("\nSaída padrão (stdout):")
        print(e.stdout)
        print("\nSaída de erro (stderr):")
        print(e.stderr)
        print("------------------------------------")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

def check_file_existence(source_file, directories, user_paths):
    """
    Verifica se o arquivo de origem existe em alguma das hierarquias de diretórios.
    """
    if not source_file.is_file():
        print(f"Erro: Arquivo de origem '{source_file.name}' não encontrado no diretório atual.")
        return

    print(f"Verificando a existência de '{source_file.name}' nos diretórios de destino...")
    found_count = 0
    total_checks = 0

    for base_path in user_paths:
        for directory_str in directories:
            total_checks += 1
            # Path() lida com caminhos que começam com './' ou não.
            target_path = Path(base_path) / directory_str / source_file.name
            if target_path.is_file():
                print(f"  [ENCONTRADO] em: {target_path}")
                found_count += 1
            else:
                print(f"  [NÃO ENCONTRADO] em: {target_path}")

    print("-" * 20)
    if found_count > 0:
        print(f"Resumo: Arquivo encontrado em {found_count} de {total_checks} locais verificados.")
    else:
        print("\nResumo: Arquivo não foi encontrado em nenhum dos diretórios de destino.")

# run_buildozer_clean()

# create_symlinks()

# O script assume que 'longintrepr.h' está no mesmo diretório de execução.
# Se não for o caso, especifique o caminho completo para o arquivo de origem.
# Exemplo: source_file = Path("/caminho/completo/para/longintrepr.h")
# source_file = Path("/home/user/JogoS/tower-defense/longintrepr.h")
source_file = Path("longintrepr.h")

# Estes caminhos parecem ser para um ambiente Linux (como o WSL).
# Se executado no Windows, as pastas serão criadas na raiz da unidade atual (ex: C:\home\user\...)
directories = [
	"JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include",
	".buildozer/android/platform/android-ndk-r25/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include",
    ".buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include",
	"JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/tower_defense/arm64-v8a/include/python3.1",
    "JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/tower_defense/armeabi-v7a/include/python3.1",
	"JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni/SDL/include",
	"JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/Include",
	"JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/native-build"
]

buildozer = '.buildozer'
jogo = 'JogoS/tower-defense'
user = '/home/user'
root = '/root'
user_paths = [user, root]

directories2 = [
	os.path.join(user, buildozer),
	# os.path.join(root, buildozer),
	os.path.join(user, jogo, buildozer)
]

# check_file_existence(source_file, directories, user_paths)

# remove_directories(directories2, user, root)

# Verifica se o arquivo de origem existe antes de começar.
if not source_file.is_file():
	print(f"Erro: Arquivo de origem '{source_file}' não encontrado.")
else:
	print(f"Iniciando a cópia do arquivo '{source_file.name}'...")
	for directory_str in directories:
		try:
			# Cria a hierarquia de diretórios. 'exist_ok=True' evita erro se o diretório já existir.,
			target_dir = Path(user, directory_str)
			print('1-----------------------------------------------------------------------------------')
			target_dir.mkdir(parents=True, exist_ok=True)
			shutil.copy2(source_file, target_dir)
			print(f"Diretório verificado/criado: {target_dir}")
			print('2-----------------------------------------------------------------------------------')

			# Copia o arquivo preservando metadados
			print('4-----------------------------------------------------------------------------------')
			print(f"Arquivo '{source_file.name}' copiado para {target_dir}")

		except Exception as e:
			print(f"Erro ao criar diretório ou copiar arquivo para {target_dir}: {e}")
	print("\nProcesso concluído.")
