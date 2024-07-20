from db import db
class Ingrediente(db.Model):
  __tablename__ = "Ingrediente"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255), nullable=False, unique=True)
  precio = db.Column(db.DECIMAL(10, 2), nullable=False)
  calorias = db.Column(db.Integer, nullable=False)
  inventario = db.Column(db.Integer, nullable=False)
  es_vegetariano = db.Column(db.Boolean, nullable=False)
  tipo = db.Column(db.String(255), nullable=False)
  sabor = db.Column(db.String(255))
  volumen = db.Column(db.DECIMAL(10, 2))
  id_tipo_vaso = db.Column(db.Integer, db.ForeignKey('TipoVaso.id'))
  tipo_vaso = db.relationship("TipoVaso")

   # Métodos getter
def get_id(self):
    return self.id

def get_nombre(self):
    return self.nombre

def get_precio(self):
    return self.precio

def get_calorias(self):
    return self.calorias

def get_inventario(self):
    return self.inventario

def get_es_vegetariano(self):
    return self.es_vegetariano

def get_tipo(self):
    return self.tipo

def get_sabor(self):
    return self.sabor

def get_volumen(self):
    return self.volumen

def get_id_tipo_vaso(self):
    return self.id_tipo_vaso

def get_tipo_vaso(self):
    return self.tipo_vaso

def abastecer(self, cantidad):
    """Reabastece la cantidad del ingrediente."""
    self.inventario += cantidad
    db.session.commit()

def usar(self, cantidad):
    """Usa la cantidad del ingrediente."""
    if self.inventario >= cantidad:
        self.inventario -= cantidad
        db.session.commit()
        return True
    return False

@property
def es_sano(self):
    return self.calorias < 100 or self.es_vegetariano