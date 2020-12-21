import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import getpass
import os
from os import listdir
import shutil

root = tk.Tk()
root.title("Organizar")


class MoveFile:
    def __init__(self):
        self.pastaorigem = ''
        self.pastadestino = ''
        self.executaveis_extensoes = ['exe', 'dll', 'jnlp', 'bat', 'msi']
        self.pdfs_extensoes = ['pdf', 'txt', 'log']
        self.imagens_extensoes = ['jpg', 'png', 'gif', 'jpeg', 'bmp', 'tiff', 'psd', 'exif', 'raw', 'eps', 'svg', 'webp']
        self.winrar_extensoes = ['zip', 'arj', 'cab', 'rar', 'tar', 'z', 'gz', 'taz', 'tgz', '7z']
        self.word_extensoes = ['doc', 'docm', 'docx', 'dot', 'dotm', 'odt', 'rtf', 'wps', 'xml', 'xps', 'xls', 'xlsx', 'ppt',
                          'pps', 'pptx', 'log']
        self.somvideo_extensoes = ['mp3', 'wav', 'mid', 'avi', 'mpg', 'wmv', 'mov', 'webm', 'mp4', 'mpeg']
        self.mydirs = ['PDF', 'Documentos do Word', 'Imagens', 'Winrar', 'Executaveis', 'Outros', 'Som e Video']

    def pasta_origem(self):
        self.pastaorigem = filedialog.askdirectory(initialdir="/", title='Select a Directory')
        myOrigem['text'] = f'Pasta de Origem: {self.pastaorigem}'


    def pasta_destino(self):
        if self.pastaorigem == '':
            response = messagebox.showerror('Error!','Por Favor, selecione a pasta de origem primeiro!')
        else:
            self.pastadestino = filedialog.askdirectory(initialdir="/", title='Select a Directory')
            myDestino['text'] = f'Pasta de Destino: {self.pastadestino}'

    def executar_programa(self):
        if self.pastadestino != '':
            response = messagebox.askyesno('Executando Programa', f'Voce está pegando os arquivos da pasta:\n{self.pastaorigem}\nPara organizar em:\n{self.pastadestino}\nÉ isso mesmo que deseja?')
            if response == 1:
                # Verificando se as pastas em 'MYDIRS' existem
                for directory in listdir(self.pastadestino):
                    if os.path.isdir(f'{self.pastadestino}/{directory}'):
                        if directory in self.mydirs:
                            self.mydirs.remove(directory)

                # Criando as pastas caso ainda não existam
                while self.mydirs:
                    for pastas in self.mydirs:
                        os.mkdir(f'{self.pastadestino}/{pastas}')
                        self.mydirs.remove(pastas)

                # Arquivos do PATH indicado pelo usuário
                for file in listdir(self.pastaorigem):
                    if file == 'desktop.ini':
                        file = ''

                    if os.path.isfile(self.pastaorigem + '/' + file):
                        formato_arquivo = file.split('.')

                        if formato_arquivo[-1].lower() in self.executaveis_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Executaveis/{file}')
                        elif formato_arquivo[-1].lower() in self.pdfs_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/PDF/{file}')
                        elif formato_arquivo[-1].lower() in self.imagens_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Imagens/{file}')
                        elif formato_arquivo[-1].lower() in self.winrar_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Winrar/{file}')
                        elif formato_arquivo[-1].lower() in self.word_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Documentos do Word/{file}')
                        elif formato_arquivo[-1].lower() in self.somvideo_extensoes:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Som e Video/{file}')
                        else:
                            shutil.move(f'{self.pastaorigem}/{file}', f'{self.pastadestino}/Outros/{file}')
            else:
                pass
        else:
            response2 = messagebox.showerror('Error!', 'Por Favor, selecione a pasta de destino!')



move_file = MoveFile()

# ---------------------- ORIGEM
frame = tk.LabelFrame(root, text="Selecione a pasta que deseja organizar", padx=15, pady=15)
frame.grid(row=0, padx=10, pady=10)

button_origem = tk.Button(frame, text="Pasta de Origem", command=move_file.pasta_origem)

button_origem.pack(expand=True, fill='both')

# ---------------------- DESTINO
frame2 = tk.LabelFrame(root, text="Selecione onde deseja organizar", padx=15, pady=15)
frame2.grid(row=1, padx=10, pady=10, sticky=tk.W+tk.E)

button_destino = tk.Button(frame2, text="Pasta de Destino", command=move_file.pasta_destino)
button_destino.pack(expand=True, fill='both')

# ---------------------- RESULTADO
button_executar = tk.Button(root, text='Executar Programa', command=move_file.executar_programa)
button_executar.grid(row=2, padx=10, pady=10, sticky=tk.E + tk.W)

myOrigem = tk.Label(root, text=f'Pasta de Origem: ')
myOrigem.grid(row=3)

myDestino = tk.Label(root, text=f'Pasta de Destino: ')
myDestino.grid(row=4)


root.mainloop()
