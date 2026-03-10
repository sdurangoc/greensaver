import mariadb
from fastapi import FastAPI

app = FastAPI()

# Conexión a MariaDB
DB_HOST = "localhost"
DB_NAME = "greensaver"
DB_USER = "root"
DB_PASWD = ""

try:
    conn = mariadb.connect(
        user=DB_USER,
        password=DB_PASWD,
        host=DB_HOST,
        port=3306,
        database=DB_NAME
    )
    cursor = conn.cursor(dictionary=True)  # devuelve resultados como dict
except mariadb.Error as e:
    print(f"Error conectando a MariaDB: {e}")

# ------------------- CRUD USUARIOS -------------------
@app.get("/usuarios")
async def get_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

@app.post("/usuarios")
async def insert_usuario(nombre: str, ciudad: str, consumo_mensual: float):
    cursor.execute("INSERT INTO usuarios (nombre, ciudad, consumo_mensual) VALUES (?, ?, ?)",
                   (nombre, ciudad, consumo_mensual))
    conn.commit()
    return {"message": "Usuario insertado"}

@app.put("/usuarios/{id}")
async def update_usuario(id: int, nombre: str, ciudad: str, consumo_mensual: float):
    cursor.execute("UPDATE usuarios SET nombre=?, ciudad=?, consumo_mensual=? WHERE id=?",
                   (nombre, ciudad, consumo_mensual, id))
    conn.commit()
    return {"message": "Usuario actualizado"}

@app.delete("/usuarios/{id}")
async def delete_usuario(id: int):
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()
    return {"message": "Usuario eliminado"}

# ------------------- CRUD PROVEEDORES -------------------
@app.get("/proveedores")
async def get_proveedores():
    cursor.execute("SELECT * FROM proveedores")
    return cursor.fetchall()

@app.post("/proveedores")
async def insert_proveedor(nombre_empresa: str, contacto: str, telefono: str, direccion: str, tipo_equipo: str):
    cursor.execute("INSERT INTO proveedores (nombre_empresa, contacto, telefono, direccion, tipo_equipo) VALUES (?, ?, ?, ?, ?)",
                   (nombre_empresa, contacto, telefono, direccion, tipo_equipo))
    conn.commit()
    return {"message": "Proveedor insertado"}

@app.put("/proveedores/{id}")
async def update_proveedor(id: int, nombre_empresa: str, contacto: str, telefono: str, direccion: str, tipo_equipo: str):
    cursor.execute("UPDATE proveedores SET nombre_empresa=?, contacto=?, telefono=?, direccion=?, tipo_equipo=? WHERE id=?",
                   (nombre_empresa, contacto, telefono, direccion, tipo_equipo, id))
    conn.commit()
    return {"message": "Proveedor actualizado"}

@app.delete("/proveedores/{id}")
async def delete_proveedor(id: int):
    cursor.execute("DELETE FROM proveedores WHERE id=?", (id,))
    conn.commit()
    return {"message": "Proveedor eliminado"}

# ------------------- CRUD PANELES -------------------
@app.get("/paneles")
async def get_paneles():
    cursor.execute("SELECT * FROM paneles")
    return cursor.fetchall()

@app.post("/paneles")
async def insert_panel(modelo: str, potencia_w: float, precio: float, proveedor_id: int):
    cursor.execute("INSERT INTO paneles (modelo, potencia_w, precio, proveedor_id) VALUES (?, ?, ?, ?)",
                   (modelo, potencia_w, precio, proveedor_id))
    conn.commit()
    return {"message": "Panel insertado"}

@app.put("/paneles/{id}")
async def update_panel(id: int, modelo: str, potencia_w: float, precio: float, proveedor_id: int):
    cursor.execute("UPDATE paneles SET modelo=?, potencia_w=?, precio=?, proveedor_id=? WHERE id=?",
                   (modelo, potencia_w, precio, proveedor_id, id))
    conn.commit()
    return {"message": "Panel actualizado"}

@app.delete("/paneles/{id}")
async def delete_panel(id: int):
    cursor.execute("DELETE FROM paneles WHERE id=?", (id,))
    conn.commit()
    return {"message": "Panel eliminado"}

# ------------------- CRUD INVERSORES -------------------
@app.get("/inversores")
async def get_inversores():
    cursor.execute("SELECT * FROM inversores")
    return cursor.fetchall()

@app.post("/inversores")
async def insert_inversor(potencia_kw: float, voltaje: str, precio: float, proveedor_id: int):
    cursor.execute("INSERT INTO inversores (potencia_kw, voltaje, precio, proveedor_id) VALUES (?, ?, ?, ?)",
                   (potencia_kw, voltaje, precio, proveedor_id))
    conn.commit()
    return {"message": "Inversor insertado"}

@app.put("/inversores/{id}")
async def update_inversor(id: int, potencia_kw: float, voltaje: str, precio: float, proveedor_id: int):
    cursor.execute("UPDATE inversores SET potencia_kw=?, voltaje=?, precio=?, proveedor_id=? WHERE id=?",
                   (potencia_kw, voltaje, precio, proveedor_id, id))
    conn.commit()
    return {"message": "Inversor actualizado"}

@app.delete("/inversores/{id}")
async def delete_inversor(id: int):
    cursor.execute("DELETE FROM inversores WHERE id=?", (id,))
    conn.commit()
    return {"message": "Inversor eliminado"}

# ------------------- CRUD BATERIAS -------------------
@app.get("/baterias")
async def get_baterias():
    cursor.execute("SELECT * FROM baterias")
    return cursor.fetchall()

@app.post("/baterias")
async def insert_bateria(capacidad_kwh: float, tipo: str, precio: float, proveedor_id: int):
    cursor.execute("INSERT INTO baterias (capacidad_kwh, tipo, precio, proveedor_id) VALUES (?, ?, ?, ?)",
                   (capacidad_kwh, tipo, precio, proveedor_id))
    conn.commit()
    return {"message": "Batería insertada"}

@app.put("/baterias/{id}")
async def update_bateria(id: int, capacidad_kwh: float, tipo: str, precio: float, proveedor_id: int):
    cursor.execute("UPDATE baterias SET capacidad_kwh=?, tipo=?, precio=?, proveedor_id=? WHERE id=?",
                   (capacidad_kwh, tipo, precio, proveedor_id, id))
    conn.commit()
    return {"message": "Batería actualizada"}

@app.delete("/baterias/{id}")
async def delete_bateria(id: int):
    cursor.execute("DELETE FROM baterias WHERE id=?", (id,))
    conn.commit()
    return {"message": "Batería eliminada"}

# ------------------- CRUD CALCULOS SISTEMA -------------------
@app.get("/calculos")
async def get_calculos():
    cursor.execute("SELECT * FROM calculos_sistema")
    return cursor.fetchall()

@app.post("/calculos")
async def insert_calculo(usuario_id: int, panel_id: int, inversor_id: int, bateria_id: int,
                         paneles_necesarios: int, inversor_kw: float, bateria_kwh: float, costo_total: float):
    cursor.execute("""INSERT INTO calculos_sistema 
        (usuario_id, panel_id, inversor_id, bateria_id, paneles_necesarios, inversor_kw, bateria_kwh, costo_total) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (usuario_id, panel_id, inversor_id, bateria_id, paneles_necesarios, inversor_kw, bateria_kwh, costo_total))
    conn.commit()
    return {"message": "Cálculo insertado"}

@app.put("/calculos/{id}")
async def update_calculo(id: int, usuario_id: int, panel_id: int, inversor_id: int, bateria_id: int,
                         paneles_necesarios: int, inversor_kw: float, bateria_kwh: float, costo_total: float):
    cursor.execute("""UPDATE calculos_sistema SET usuario_id=?, panel_id=?, inversor_id=?, bateria_id=?, 
        paneles_necesarios=?, inversor_kw=?, bateria_kwh=?, costo_total=? WHERE id=?""",
        (usuario_id, panel_id, inversor_id, bateria_id, paneles_necesarios, inversor_kw, bateria_kwh, costo_total, id))
    conn.commit()
    return {"message": "Cálculo actualizado"}

@app.delete("/calculos/{id}")
async def delete_calculo(id: int):
    cursor.execute("DELETE FROM calculos_sistema WHERE id=?", (id,))
    conn.commit()
    return {"message": "Cálculo eliminado"}

# ------------------- REPORTE GENERAL -------------------
@app.get("/greensaver/report")
async def reporte_general():
    sql = """
    SELECT 
        u.nombre,
        p.modelo AS panel,
        i.potencia_kw AS inversor,
        b.capacidad_kwh AS bateria,
        c.paneles_necesarios,
        c.costo_total
    FROM calculos_sistema c
    JOIN usuarios u ON c.usuario_id = u.id
    JOIN paneles p ON c.panel_id = p.id
    JOIN inversores i ON c.inversor_id = i.id
    JOIN baterias b ON c.bateria_id = b.id
    """
    cursor.execute(sql)
    return cursor.fetchall()

@app.get("/")
async def root():
    return {"message": "Bienvenido a Green Saber API 🚀"}