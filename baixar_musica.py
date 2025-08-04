import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import os
import threading

def baixar_musica():
    url = entrada_url.get()
    pasta_destino = filedialog.askdirectory(title="Escolha a pasta para salvar")
    
    if not url or not pasta_destino:
        messagebox.showerror("Erro", "URL e pasta de destino são obrigatórios.")
        return

    botao.config(state='disabled')
    status.set("Baixando...")

    def download():
        try:
            opcoes = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': 'C:\\ffmpeg\\bin\\ffmpeg.exe'  # Caminho completo no Windows
            }

            with yt_dlp.YoutubeDL(opcoes) as ydl:
                ydl.download([url])

            status.set("Download concluído!")
            messagebox.showinfo("Sucesso", "Música baixada com sucesso!")
        except Exception as e:
            status.set("Erro ao baixar")
            messagebox.showerror("Erro", str(e))
        finally:
            botao.config(state='normal')

    threading.Thread(target=download).start()

# GUI
janela = tk.Tk()
janela.title("YouTube MP3 Downloader")
janela.geometry("400x200")
janela.resizable(False, False)

tk.Label(janela, text="Insira a URL do vídeo:").pack(pady=10)

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack()

botao = tk.Button(janela, text="Baixar Música", command=baixar_musica, bg="#4CAF50", fg="white")
botao.pack(pady=10)

status = tk.StringVar()
status.set("Aguardando URL...")
tk.Label(janela, textvariable=status).pack()

janela.mainloop()
