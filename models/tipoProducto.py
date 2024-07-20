from db import db
class TipoProducto(db.Model):
  __tablename__ = "TipoProducto"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre_tipo_producto = db.Column(db.String(50), nullable=False, unique=True)
  descripcion_tipo_producto = db.Column(db.String(db.Text), nullable=False)

    # Métodos getter
def get_id(self):
    return self.id

def get_nombre_tipo_producto(self):
    return self.nombre_tipo_producto

def get_descripcion_tipo_producto(self):
    return self.descripcion_tipo_producto