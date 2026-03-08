import os # biblioteca para manipulação de arquivos e diretórios
import shutil # biblioteca para operações de arquivos de alto nível, como mover arquivos

pastaDownloads = os.path.join(os.path.expanduser('~'),"Downloads")

# Dicionário para mapear extensões de arquivos a suas respectivas pastas
Categorias = {
    "Imagens":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
    "Videos":      [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Audios":      [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"],
    "Documentos":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Planilhas":   [".xls", ".xlsx", ".csv", ".ods"],
    "Apresentacoes": [".ppt", ".pptx", ".odp"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programas":   [".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"],
    "Codigos":      [".py", ".js", ".html", ".css", ".java", ".cpp", ".json"],
}

def descobrirCategoria(extensao):
    for categoria, extensoes in Categorias.items(): # percorre o dicionário de categorias e suas extensões
        if extensao in extensoes:# verifica se a extensão do arquivo está na lista de extensões da categoria
            return categoria
        
    return "Diversos" # se a extensão do arquivo não corresponder a nenhuma categoria

def organizarArquivos():
    
    if not os.path.exists(pastaDownloads):
        print(f"A pasta {pastaDownloads} não existe.")
        return

    print(f"Organizando arquivos na pasta: {pastaDownloads}")

    arquivosMovidos = 0
    arquivosIgnorados = 0

    for arquivos in os.listdir(pastaDownloads): # percorre os arquivos na pasta downloads
        
        caminhoCompleto = os.path.join(pastaDownloads, arquivos) # obtém o caminho do arquivo

        if os.path.isdir(caminhoCompleto): #ignora pastas
            arquivosIgnorados += 1
            continue

        extensao = os.path.splitext(arquivos)[1] # obtém a extensão do arquivo (parte após o último ponto)

        categoria = descobrirCategoria(extensao) # descobre a categoria do arquivo com base na extensão

        pastaDestino = os.path.join(pastaDownloads, categoria)  # caminho da pasta de destino para a categoria do arquivo

        if os.path.isfile(pastaDestino):
            pastaDestino += "_Pasta" # se já existir um arquivo com o mesmo nome da pasta, adiciona um sufixo para evitar conflitos
            print(f"⚠️ Conflito de nome, renomeando pasta para: {pastaDestino}")

        os.makedirs(pastaDestino, exist_ok=True) # cria a pasta de destino se ela não existir

        destinoCompleto = os.path.join(pastaDestino, arquivos) # caminho completo do arquivo de destino


        if os.path.exists(destinoCompleto): # verifica se a pasta de destino existe
            print (f"⚠️ Já existe , pulando: {arquivos}")
            arquivosIgnorados += 1
            continue

        shutil.move(caminhoCompleto, pastaDestino) # move o arquivo para a pasta de destino
        print(f"✅ {arquivos} -> {categoria}")
        arquivosMovidos += 1

    print(f"\n🎉 Concluído!")
    print(f"   Arquivos movidos:   {arquivosMovidos}")
    print(f"   Ignorados/pastas:   {arquivosIgnorados}")


if __name__ == "__main__":
    organizarArquivos()
        
        

