@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/crear_usuario", response_class=HTMLResponse)
def form_usuario(request: Request):
    return templates.TemplateResponse("crear_usuario.html", {"request": request})

@app.post("/procesar_usuario")
async def procesar_usuario(
    email: str = Form(...), nombre: str = Form(...), password: str = Form(...),
    extrovertido: int = Form(...), aventurero: int = Form(...), cultural: int = Form(...),
    tipo: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()
    # Hash password (simple, usa bcrypt real)
    password_hash = password  # TODO: hash
    perfil = {"extrovertido": extrovertido, "aventurero": aventurero, "cultural": cultural}
    cursor.execute(
        "INSERT INTO usuarios (email, password_hash, nombre, perfil_tags, tipo) VALUES (%s, %s, %s, %s, %s)",
        (email, password_hash, nombre, str(perfil).replace("'", '"'), tipo)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"mensaje": "Usuario creado con perfil!"}

@app.get("/crear_evento", response_class=HTMLResponse)
def form_evento(request: Request):
    return templates.TemplateResponse("crear_evento.html", {"request": request})

@app.post("/procesar_evento")
async def procesar_evento(
    lugar_id: int = Form(...), titulo: str = Form(...), descripcion: str = Form(None),
    fecha_inicio: str = Form(...), fecha_fin: str = Form(...), capacidad: int = Form(None),
    es_masivo: bool = Form(False), nft_cantidad: int = Form(0),
    cultural: int = Form(0), sostenible: int = Form(0)
):
    db = get_db()
    cursor = db.cursor()
    es_masivo_val = 1 if es_masivo else 0
    tags = {"cultural": cultural, "sostenible": sostenible}
    cursor.execute(
        "INSERT INTO eventos (lugar_id, titulo, descripcion, es_masivo, capacidad, fecha_inicio, fecha_fin, perfil_tags, nft_cantidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (lugar_id, titulo, descripcion, es_masivo_val, capacidad, fecha_inicio, fecha_fin, str(tags).replace("'", '"'), nft_cantidad)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"mensaje": "Evento creado!"}