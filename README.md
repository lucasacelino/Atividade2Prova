# Documentação.
Pergunta: Quais endpoints são fornecidos pelo serviço REST
O endpoint abaixo cria um novo relatório de todos os alunos salvos. 
    @app.post('/relatorio')
    def relatorio_post():

        //Recebe os dados da requisição
        request_data = request.json

        //Cria a instânica da classe RelatorioSchema
        schema = RelatorioSchema()
        try:

            // Carrega os dados do objeto e faz deserialização, ou seja, os dados que vieram como json são convertidos em um dicionário
            result = schema.load(request_data)

            // o método dumps serializa os dados de result transformando o conjunto de dados em Json 
            data_now_json_str = dumps(result)

            // response data recebe os dados que serão cadastrados no relatório
            response_data = cadastrarRelatorio(data_now_json_str)

        //Se o tipos dos dados informados na requisição forem de um tipo diferente dos quais formam criados na classe, lança a exceção ValiationError
        except ValidationError as err:
            return jsonify(err.messages), 400
        // retorna os dados que foram cadastrados.
        return jsonify(response_data), 200

Endpoint abaixo cria um novo aluno>
    @app.post('/aluno')
    def aluno_post():

        //Recebe os dados da requisição
        request_data = request.json

         //Cria a instânica da classe AlunoSchema
        schema = AlunoSchema()
        try:

            // Carrega os dados do objeto e faz deserialização, ou seja, os dados que vieram como json são convertidos em um dicionário
            result = schema.load(request_data)

            // o método dumps serializa os dados de result transformando o conjunto de dados em Json
            data_now_json_str = dumps(result)

            /Se o tipos dos dados informados na requisição forem de um tipo diferente dos quais formam criados na classe, lança a exceção ValiationError
            response_data = cadastrarAluno(data_now_json_str)

        //Se o tipos dos dados informados na requisição forem de um tipo diferente dos quais formam criados na classe, lança a exceção ValiationError
        except ValidationError as err:
            return jsonify(err.messages), 400

        // retorna os dados que foram cadastrados.
        return jsonify(response_data), 200

Pergunta: Como os dados são manipulados e persistidos? Você sugere alguma forma mais eficiente de persistir essas informações? Aponte no código e comente a forma de manipulação e sugestões.
    Resposta: Os dados são persistidos(salvados) em uma lista e isso é ruim porque quando fecha aplicação, os dados que estavam na lista, são perdidos. Sim, há uma melhor maneira de persistir os dados, utilizando uma conexão com banco de dados. Meu ponto de melhoria, primeiro: criar as tabelas dos respetivos modelos, como no exemplo: Aluno e Relatório. posteriormente, atribuiria as minhas funções de conexão aos arquivos onde irem manipular os endpoints.


Pergunta: Explique, passo-a-passo, através de comentários no código como funciona a validação dos dados através da biblioteca do marshmallow.
    Resposta: 
    class AlunoSchema(Schema):
    // É atribuido ao atributo o tipo de dado que se espera ser salvo. Neste caso, o tipo do dado é deve ser um inteiro e é obrigatório
    idade = fields.Integer(required=True)
    disciplina = fields.String(required=True)

    // Se o dado informado não for do tipo esperado ou não for informado, é lançada a exceção ValidationError. 
    except ValidationError as err:
        return jsonify(err.messages), 400

Pergunta: Defina quais JSON que devem ser fornecidos nas entradas dos endpoints? Como é possível chegar a essa conclusão? Adicione comentário antes de cada endpoint informando o formato da dado de entrada.
    no endpoint /relatorio, deve ser fornecido o seguite Json: 
        [
            {
                "idade": 34,
                "disciplina": "Programação Web"
            }
        ]

    No Endpoint /aluno, deve ser fornecido o seguinte Json:
        [
            "titulo": "Aluno matriculado em TSI",
            "criacao": 23/11/24,
            "aluno": {
                "idade": 34,
                "disciplina": "Programação Web"
            }
        ]