from owlready2 import *

def criar_ontologia():
    onto = get_ontology("http://example.org/diagnostico.owl")

    with onto:
        class Doenca(Thing): pass
        class Sintoma(Thing): pass

        class hasSymptom(Doenca >> Sintoma): pass

        febre = Sintoma("febre")
        tosse = Sintoma("tosse")
        coriza = Sintoma("coriza")

        gripe = Doenca("Gripe")
        resfriado = Doenca("Resfriado")

        gripe.hasSymptom = [febre, tosse]
        resfriado.hasSymptom = [coriza]

    onto.save("diagnostico.owl")  
    print("Ontologia criada e salva como 'diagnostico.owl'")
    return onto

def carregar_ontologia():
    return get_ontology("diagnostico.owl").load()

def buscar_na_ontologia(sintomas):
    onto = carregar_ontologia()
    resultados = set()

    for sintoma in sintomas:
        sintoma_inst = onto.search_one(iri=f"*{sintoma.lower()}")
        if sintoma_inst:
            for doenca in onto.Doenca.instances():
                if sintoma_inst in doenca.hasSymptom:
                    resultados.add(doenca.name)

    return list(resultados)
