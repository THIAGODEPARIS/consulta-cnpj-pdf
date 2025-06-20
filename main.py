from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Configurações de diretório
PASTA_CNPJ = r"C:\CNPJ"
templates = Jinja2Templates(directory="templates")

# Rota para página inicial
@app.get("/", response_class=HTMLResponse)
def tela_principal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para buscar PDF por CNPJ
@app.get("/busca-pdf")
def buscar_pdf(cnpj: str):
    caminho_pdf = os.path.join(PASTA_CNPJ, f"{cnpj}.pdf")

    if not os.path.isfile(caminho_pdf):
        raise HTTPException(status_code=404, detail="PDF não encontrado.")

    return FileResponse(caminho_pdf, media_type="application/pdf", filename=f"{cnpj}.pdf")

# Montar arquivos estáticos (como a logo)
app.mount("/static", StaticFiles(directory="static"), name="static")
