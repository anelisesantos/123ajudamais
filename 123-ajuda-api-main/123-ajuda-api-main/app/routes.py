from flask import abort, jsonify, request, Blueprint, render_template
from flasgger import swag_from
from app.models import UnidadeDeSaude

bp = Blueprint("routes", __name__)

@bp.route('/')
def index():
    html_content = "<html><head><title>api 123 ajuda</title></head><body><h1>123 ajuda</h1></body></html>"
    return render_template('index.html')

@bp.route('/unidades_de_saude', methods=['GET', 'POST'])
@swag_from('unidades.yml')
def get_unidades():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        abrangencia = data.get('abrangencia')
        uf = data.get('uf')
        isFullTime = data.get('isFullTime')
        alcoolDrogas = data.get('alcoolDrogas')
        transtornoGrave = data.get('transtornoGrave')
        criancaAdolescente = data.get('criancaAdolescente')

    else:
        abrangencia = request.args.get('abrangencia')
        uf = request.args.get('uf')
        isFullTime = request.args.get('isFullTime')
        alcoolDrogas = request.args.get('alcoolDrogas')
        transtornoGrave = request.args.get('transtornoGrave')
        criancaAdolescente = request.args.get('criancaAdolescente')

    # if not UnidadeDeSaude.query.filter_by(abrangencia=abrangencia).first():
    #     abort(400, "A 'abrangencia' fornecida não está na nossa base.")
 

    # query = UnidadeDeSaude.query.filter_by(abrangencia=abrangencia)
    query = UnidadeDeSaude.query

    if abrangencia:
        query = query.filter(UnidadeDeSaude.abrangencia.ilike(f"%{abrangencia}%"))
    if uf:
        query = query.filter(UnidadeDeSaude.uf.ilike(f"%{uf}%"))
    if isFullTime:
        query = query.filter(UnidadeDeSaude.isFullTime.ilike(f"%{isFullTime}%"))
    if alcoolDrogas:
        query = query.filter(UnidadeDeSaude.alcoolDrogas.ilike(f"%{alcoolDrogas}%"))
    if transtornoGrave:
        query = query.filter(UnidadeDeSaude.transtornoGrave.ilike(f"%{transtornoGrave}%"))
    if criancaAdolescente:
        query = query.filter(UnidadeDeSaude.criancaAdolescente.ilike(f"%{criancaAdolescente}%"))



    unidades = query.all()

    resultados = []
    for unidade in unidades:
        resultados.append({
            'id': unidade.id,
            'nome': unidade.capsi,
            'endereco': unidade.endereco,
            'abrangencia': unidade.abrangencia,
            'bairro': unidade.bairro,
            'cidade': unidade.cidade,
            'uf': unidade.uf,
            'contato': unidade.contato,
            'contato2': unidade.contato2,
            'ramais': unidade.ramais,
            'email': unidade.email,
            'isFullTime': unidade.isFullTime,
            'alcoolDrogas': unidade.alcoolDrogas,
            'transtornoGrave': unidade.transtornoGrave,
            'criancaAdolescente': unidade.criancaAdolescente,
            'observacao': unidade.observacao
        })

    return jsonify(resultados)

@bp.route('/unidades_de_saude/id/<int:id>', methods=['GET'])
@swag_from('unidades.yml')
def listar_unidade_de_saude(id):
    unidade_por_id = UnidadeDeSaude.query.filter_by(ID=id).first()
    return jsonify(unidade_por_id.to_dict())
