from db import db
class Producto(db.Model):
  __tablename__ = "Producto"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255), nullable=False, unique=True)
  precio_publico = db.Column(db.DECIMAL(10, 2), nullable=False)
  id_tipo_producto = db.Column(db.Integer, db.ForeignKey('TipoProducto.id'), nullable=False)

  tipo_producto = db.relationship("TipoProducto")

# Métodos getter
def get_id(self):
    return self.id

def get_nombre(self):
    return self.nombre

def get_precio_publico(self):
    return self.precio_publico

def get_id_tipo_producto(self):
    return self.id_tipo_producto

def get_tipo_producto(self):
    return self.tipo_producto