from app import db

class UnidadeDeSaude(db.Model):
    __tablename__ = 'unidades_de_saude'

    id = db.Column(db.Integer, primary_key=True)
    capsi = db.Column(db.String(20))
    abrangencia = db.Column(db.String(100))
    endereco = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    uf = db.Column(db.String(2))
    contato = db.Column(db.String(100))
    ramais = db.Column(db.String(50))
    contato2 = db.Column(db.String(50))
    email = db.Column(db.String(50))
    isFullTime = db.Column(db.Boolean)
    alcoolDrogas = db.Column(db.Boolean)
    transtornoGrave = db.Column(db.Boolean)
    criancaAdolescente = db.Column(db.Boolean)
    observacao = db.Column(db.String(200)) 

    def to_dict(self):
        return {
            'id': self.id,
            'capsi': self.capsi, 
            'abrangencia': self.abrangencia,
            'endereco': self.endereco,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'uf': self.uf,
            'contato': self.contato,  
            'ramais': self.ramais,
            'contato2': self.contato2,
            'email': self.email,
            'isFullTime': self.isFullTime,
            'alcoolDrogas': self.alcoolDrogas,
            'transtornoGrave': self.transtornoGrave,
            'criancaAdolescente': self.criancaAdolescente,
            'observacao': self.observacao 
        }
