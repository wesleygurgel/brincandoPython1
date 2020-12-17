# TODO MOVER ARQUIVOS DE SUAS RESPECTIVAS EXTENSÕES PARA PASTAS DO SEU TIPO.
# TODO 1. VERIFICAR SE AS PASTAS EXISTEM:
"""
1. PDF's
2. Executaveis
3. Imagens
4. Winrar
5. Documentos do Word
6. Outros
"""
import getpass
import os
from os import listdir
import shutil

mypath = input(
    'Digite o PATH da pasta que deseja organizar!\nExemplo: C:/Users/wesleygurgel/Downloads\n'
    '- Preste atenção nas Barras, elas são assim "/" e não assim "\\"\nSeu path: ')
username = getpass.getuser()
# mypath = 'C:/Users/wesleygurgel/Downloads'
usuario_logado = 'C:/Users/' + username
mydirs = ['PDF', 'Documentos do Word', 'Imagens', 'Winrar', 'Executaveis', 'Outros', 'Som e Video']

# EXTENSOES ARQUIVOS
executaveis_extensoes = ['exe', 'dll', 'jnlp']
pdfs_extensoes = ['pdf', 'txt']
imagens_extensoes = ['jpg', 'png', 'gif', 'jpeg', 'bmp', 'tiff', 'psd', 'exif', 'raw', 'eps', 'svg', 'webp']
winrar_extensoes = ['zip', 'arj', 'cab', 'rar', 'tar', 'z', 'gz', 'taz', 'tgz', '7z']
word_extensoes = ['doc', 'docm', 'docx', 'dot', 'dotm', 'odt', 'rtf', 'wps', 'xml', 'xps', 'xls', 'xlsx', 'ppt', 'pps']
somvideo_extensoes = ['mp3', 'wav', 'mid', 'avi', 'mpg', 'wmv', 'mov', 'webm']

# Verificando se as pastas em 'MYDIRS' existem
for file in listdir(usuario_logado + '/Downloads'):
    if os.path.isdir(usuario_logado + '/Downloads/' + file):
        if file in mydirs:
            mydirs.remove(file)

# Criando as pastas caso ainda não existam
while mydirs:
    for pastas in mydirs:
        os.mkdir(usuario_logado + '/Downloads/' + pastas)
        mydirs.remove(pastas)

# Arquivos do PATH indicado pelo usuário
for file in listdir(mypath):
    if file == 'desktop.ini':
        file = ''

    if os.path.isfile(mypath + '/' + file):
        formato_arquivo = file.split('.')

        if formato_arquivo[-1] in executaveis_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Executaveis/{file}')
        elif formato_arquivo[-1] in pdfs_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/PDF/{file}')
        elif formato_arquivo[-1] in imagens_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Imagens/{file}')
        elif formato_arquivo[-1] in winrar_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Winrar/{file}')
        elif formato_arquivo[-1] in word_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Documentos do Word/{file}')
        elif formato_arquivo[-1] in somvideo_extensoes:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Som e Video/{file}')
        else:
            shutil.move(f'{mypath}/{file}', f'{usuario_logado}/Downloads/Outros/{file}')
