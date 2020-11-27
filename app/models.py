from app import db

#class Thing(db.Model):
#	id = db.Column(db.Integer(), primary_key=True)

#	def __repr__(self):
#		return "<Thing {}>".format(self.id)

class Atributos(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	nome = db.Column(db.String())
	descricao = db.Column(db.String())
	tipo_atributo_id = db.Column(db.String())

	def __repr__(self):
		return "<SihColumn {}>".format(self.id)


#db.create_all()

