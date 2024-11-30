from database.db_operations import buscar_doencas_por_sintomas
from ontology.ontology_operations import criar_ontologia, buscar_na_ontologia

ontologia = criar_ontologia()

sintomas_usuario = list(set(['febre', 'tosse']))
#sintomas_usuario = list(set(['febre', 'tosse', 'dor no peito']))

resultados_db = buscar_doencas_por_sintomas(sintomas_usuario)

resultados_onto = buscar_na_ontologia(sintomas_usuario)

def combinar_resultados(resultados_db, resultados_onto):
    combinados = {}
    for doenca, descricao, relevancia in resultados_db:
        combinados[doenca] = {
            'descricao': descricao,
            'relevancia': relevancia,
            'ontologia': False
        }

    for doenca in resultados_onto:
        if doenca in combinados:
            combinados[doenca]['ontologia'] = True
        else:
            combinados[doenca] = {'descricao': 'Nada encontrado', 'relevancia': 0, 'ontologia': True}

    return combinados

resultados_combinados = combinar_resultados(resultados_db, resultados_onto)

print("\nResultados finais:")
for doenca, dados in resultados_combinados.items():
    print(f"Doença: {doenca}")
    print(f"Descrição: {dados['descricao']}")
    print(f"Relevância: {dados['relevancia']}")
    print(f"Encontrado na Ontologia: {dados['ontologia']}")
    print("---")
