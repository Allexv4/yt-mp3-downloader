# 📻 YouTube MP3 Downloader

Um script Python simples e seguro para baixar músicas do YouTube diretamente no seu computador em formato MP3, sem depender de sites suspeitos ou cheios de anúncios.

---

## 🎯 Objetivo

- Criado para fins educacionais (aprender Python, GUI com Tkinter e integração com APIs)
- Alternativa confiável para baixar músicas sem riscos de vírus ou redirecionamentos maliciosos

---

## 🛠️ Pré-requisitos

- Python 3.8 ou superior ([Download aqui](https://www.python.org/downloads/))
- FFmpeg (utilizado para conversão de áudio)
- Biblioteca [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

---

## 📥 Instalação

### ✅ Passo 1: Instalar o FFmpeg no Windows

1. Baixe o FFmpeg em: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) (versão **essentials**)
2. Extraia o arquivo ZIP em `C:\ffmpeg`
3. Adicione o caminho `C:\ffmpeg\bin` ao **PATH** do sistema:

   - Pressione `Win + R`, digite `sysdm.cpl`
   - Vá em **Avançado → Variáveis de Ambiente → Path → Editar → Novo**
   - Adicione: `C:\ffmpeg\bin`
   - Clique em **OK** e reinicie o terminal

4. Verifique se está instalado corretamente:

   ```bash
   ffmpeg -version
   ```

---

### ✅ Passo 2: Instalar a Biblioteca yt-dlp

Execute no terminal:

```bash
pip install yt-dlp
```

---

### ✅ Passo 3: Gerar Executável (.exe) com PyInstaller

1. Instale o PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:

   ```bash
   pyinstaller --onefile --windowed baixar_musica.py
   ```

3. O arquivo `.exe` será gerado na pasta `dist/` com o nome `youtube_mp3_downloader.exe`

---

## 🚀 Como Usar

1. Execute o script Python ou o arquivo `.exe` gerado
2. Cole a URL do vídeo do YouTube
3. Escolha a pasta de destino do MP3
4. Aguarde o download e a conversão!

---

## ❓ FAQ

**🔧 Preciso mudar o caminho do FFmpeg?**  
Não, desde que você tenha seguido o tutorial e instalado em `C:\ffmpeg`.

**📃 Posso baixar playlists?**  
Sim! Basta colar a URL da playlist que o script cuidará do resto.

**⚠️ Erros comuns:**

- Certifique-se de que o FFmpeg está corretamente adicionado ao **PATH**
- Atualize o yt-dlp, se necessário:

  ```bash
  pip install --upgrade yt-dlp
  ```

---
