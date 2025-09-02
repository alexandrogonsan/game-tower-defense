import os; import shutil
from pathlib import Path

diretorios = [
	"/JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include",
	"/.buildozer/android/platform/android-ndk-r25/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include",
	"/JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/python-installs/tower_defense/arm64-v8a/include/python3.1",
	"/JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds/sdl2/jni/SDL/include",
	"/JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/Include",
	"/JogoS/tower-defense/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/native-build"
]

root = '/home/user'
aux = 'longintrepr.h.copy.py.folder'
arquivo = 'longintrepr.h'
print(root)
print(arquivo)

for diretorio in diretorios:
	print(diretorio)
	print('1..............................................................................')
	current_path = os.path.join(root, aux, diretorio)
	print('2..............................................................................')
	os.makedirs(current_path, exist_ok=True)
	print('3..............................................................................')
	try:
		aux2 = os.path.join(root, diretorio, arquivo)
		print('1', aux2)
		aux3 = os.path.join(current_path, arquivo)
		print('2', aux3)
		shutil.copy(aux2, aux3)
		print(f"Arquivo copiado para {diretorio}")
	except FileNotFoundError:
		print(f"Erro: Arquivo {arquivo} não encontrado")
	except Exception as e:
		print(f"Erro ao copiar arquivo para {diretorio}: {e}")
