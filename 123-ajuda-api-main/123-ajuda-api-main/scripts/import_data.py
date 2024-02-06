import csv
import os
import sys

# Adicione o caminho para o diretório raiz do projeto (onde estão app e scripts)
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)


from app import db
from scripts.create_tables import create_table
from app.models import UnidadeDeSaude

def import_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            unidade = UnidadeDeSaude(
                capsi=row['capsi'],
                abrangencia=row['abrangencia'],
                endereco=row['endereco'],
                bairro=row['bairro'],
                cidade=row['cidade'],
                uf=row['uf'],
                contato=row['contato'],
                ramais=row['ramais'],
                contato2=row['contato2'],
                email=row['email'],
                isFullTime=row['isFullTime'] == 'true',
                alcoolDrogas=row['alcoolDrogas'] == 'true',
                transtornoGrave=row['transtornoGrave'] == 'true',
                criancaAdolescente=row['criancaAdolescente'] == 'true',
                observacao=row['observacao']
            )
            db.session.add(unidade)

    db.session.commit()

if __name__ == "__main__":
    csv_file_path = '/123-ajuda-api/data/UnidadesDeSaude.csv'
    create_table() 
    import_csv(csv_file_path)
