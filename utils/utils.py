def queryId(dataList : list , id : int):
    for idx , item in enumerate(dataList):
        if item.get('id') == id:
            return item
    return None