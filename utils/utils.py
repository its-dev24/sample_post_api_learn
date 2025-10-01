def queryId(dataList : list , id : int):
    for idx , item in enumerate(dataList):
        if item.get('id') == id:
            return idx , item
    return 0 ,None