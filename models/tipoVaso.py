from db import db
class TipoVaso(db.Model):
  __tablename__ = "TipoVaso"

  id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255), nullable=False, unique=True)
  descripcion = db.Column(db.String(255))

  # Métodos getter
  def get_id(self):
      return self.id

  def get_nombre(self):
      return self.nombre

  def get_descripcion(self):
      return self.descripcion