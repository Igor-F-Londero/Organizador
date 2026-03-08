Organizador de Downloads
Script Python que organiza automaticamente os arquivos da pasta Downloads, movendo cada arquivo para uma subpasta de acordo com seu tipo.

🚀 Como usar

Clone ou baixe o arquivo Organizador.py
Abra o terminal na pasta do projeto
Execute:

bashpython Organizador.py
O script irá organizar automaticamente sua pasta ~/Downloads.

📂 Categorias
PastaExtensõesImagens.jpg .jpeg .png .gif .bmp .svg .webp .heicVideos.mp4 .mov .avi .mkv .wmv .flvAudios.mp3 .wav .aac .ogg .flac .m4aDocumentos.pdf .doc .docx .txt .odt .rtfPlanilhas.xls .xlsx .csv .odsApresentacoes.ppt .pptx .odpCompactados.zip .rar .7z .tar .gzProgramas.exe .msi .dmg .pkg .deb .apkCodigos.py .js .html .css .java .cpp .jsonDiversosQualquer outro tipo

⚙️ Requisitos

Python 3.6 ou superior
Bibliotecas utilizadas: os e shutil (já incluídas no Python, sem instalação necessária)


🛡️ Tratamento de erros

Pastas existentes são ignoradas automaticamente
Arquivos duplicados no destino são pulados (sem sobrescrita)
Conflito de nome (arquivo com o mesmo nome de uma categoria) é detectado e reportado no terminal
Arquivos sem extensão ou de tipo desconhecido vão para a pasta Diversos


💡 Exemplo de saída
Organizando arquivos na pasta: /home/igor/Downloads

✅ relatorio.pdf → Documentos/
✅ foto_viagem.jpg → Imagens/
✅ musica.mp3 → Audios/
⚠️  arquivo.zip já existe, pulando...
✅ script.py → Codigos/

🎉 Concluído!
   Arquivos movidos:   4
   Ignorados/pastas:   1

🔧 Personalização
Para adicionar uma nova categoria, edite o dicionário Categorias no início do arquivo:
pythonCategorias = {
    # ...categorias existentes...
    "eBooks": [".epub", ".mobi"],  # ← nova categoria
}
