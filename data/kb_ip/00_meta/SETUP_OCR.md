# Setup de OCR — Lista 2 (PDF escaneado)

> Documenta como reproduzir a extração de texto da
> `docs/materiais_kb/AULAS/Lista_2_-_Exerccios_de_IP.pdf` (PDF escaneado, 5 páginas).

## Por que OCR?

A Lista 2 não tem camada de texto (`pymupdf.get_text()` retorna 0 chars). É PDF escaneado (imagens). Sem OCR, o conteúdo fica indisponível para o RAG.

## Setup no Windows

### 1. Instalar o binário Tesseract

```powershell
winget install --id UB-Mannheim.TesseractOCR --silent --accept-source-agreements --accept-package-agreements
```

Padrão: instala em `C:\Program Files\Tesseract-OCR\tesseract.exe`.

### 2. Baixar o pacote de português

O instalador winget só vem com `eng` e `osd`. Baixe o `por.traineddata`:

```bash
curl -L -o por.traineddata https://github.com/tesseract-ocr/tessdata_fast/raw/main/por.traineddata
```

Por causa de UAC em `C:\Program Files\Tesseract-OCR\tessdata\`, salve em pasta gravável:

```bash
mkdir -p "$LOCALAPPDATA/Tesseract-OCR"
cp por.traineddata "$LOCALAPPDATA/Tesseract-OCR/"
```

### 3. Rodar o OCR

```python
import pymupdf, pytesseract, tempfile, os
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = os.path.join(os.environ["LOCALAPPDATA"], "Tesseract-OCR") + os.sep

pdf = pymupdf.open("docs/materiais_kb/AULAS/Lista_2_-_Exerccios_de_IP.pdf")
textos = []
with tempfile.TemporaryDirectory() as tmp:
    for i, page in enumerate(pdf):
        pix = page.get_pixmap(dpi=300)
        img = os.path.join(tmp, f"p{i+1}.png")
        pix.save(img)
        # psm 6 = assume bloco de texto uniforme (melhor p/ exercícios)
        txt = pytesseract.image_to_string(img, lang="por", config="--psm 6")
        textos.append(txt)

Path("data/_extracao/AULAS/Lista_2_-_Exerccios_de_IP.txt").write_text(
    "\n\n===PAGE_BREAK===\n\n".join(textos), encoding="utf-8"
)
```

**Importante**: NÃO use `pytesseract.image_to_string` com `tesseract_cmd` apontando para
o binário padrão em uma sessão PowerShell onde `tesseract` não está no PATH — o
wrapper Python pode falhar. Sempre passe o caminho absoluto e configure `TESSDATA_PREFIX`
apontando para a pasta onde está o `por.traineddata`.

## Verificação

```python
import pymupdf
d = pymupdf.open("docs/materiais_kb/AULAS/Lista_2_-_Exerccios_de_IP.pdf")
chars = sum(len(p.get_text()) for p in d)
print(f"chars no PDF original: {chars}")  # esperado: 0 (escaneado)
```

```python
txt = Path("data/_extracao/AULAS/Lista_2_-_Exerccios_de_IP.txt").read_text(encoding="utf-8")
print(f"chars extraídos: {len(txt)}")  # esperado: ~6000 (5 páginas)
print("Estruturas de Decisão" in txt)  # True
```

## Saída esperada

6028 chars em UTF-8 limpo. Exemplos de strings que aparecem corretamente:

- "Estruturas de Decisão e Repetição em Algoritmos"
- "LISTA 2 DE EXERCÍCIOS"
- "SE/ENTÃO", "REPITA/ATÉ"
- "Exercício 1: Triângulo ou não Triângulo"

## Quando refazer

- Se adicionar nova lista escaneada em `docs/materiais_kb/AULAS/`
- Se o `por.traineddata` for atualizado (versão do modelo melhora com o tempo)
- Se o `tesseract` for desinstalado/reinstalado em outra pasta (ajustar `tesseract_cmd`)

## Arquivos relacionados

- `data/_extracao/AULAS/Lista_2_-_Exerccios_de_IP.txt` — saída do OCR
- `data/kb_ip/02_aulas/Lista_2___Exerccios_de_IP.md` — versão com frontmatter para indexação
- `docs/materiais_kb/AULAS/Lista_2_-_Exerccios_de_IP.pdf` — fonte original escaneada