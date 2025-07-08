from app.database import crear_tablas, SessionLocal, Comprador, Deudor

crear_tablas()
db = SessionLocal()

if not db.query(Comprador).first():
    db.add_all([
        Comprador(id=1, nombre="Ana", total_compras=1200),
        Comprador(id=2, nombre="Luis", total_compras=3000),
        Comprador(id=3, nombre="Marta", total_compras=2500),
    ])

if not db.query(Deudor).first():
    db.add_all([
        Deudor(id=1, nombre="Carlos", monto_adeudado=500),
        Deudor(id=2, nombre="Luis", monto_adeudado=1500),
        Deudor(id=3, nombre="Elena", monto_adeudado=750),
    ])

db.commit()
db.close()
