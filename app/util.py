from app import db


def getValoresPossiveis(column):
    query = 'Select distinct "' + column.strip() + '" from public."SIH"'
    result = db.engine.execute(query)
    return result





def formatCid(cidList):
    cidList = cidList.split(",")

    cidListNew = ""

    for c in cidList:
        if (cidListNew == ""):
            cidListNew = "'"+c+"'"
        else:
            cidListNew = cidListNew+",'" + c + "'"

    return cidListNew



