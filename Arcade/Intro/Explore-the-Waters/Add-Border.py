def addBorder(picture):

    bordered = list()
    border = "*"*(len(picture[0])+2)
    bordered.append(border) 

    for i in picture:
        bordered.append(f"*{i}*")
    bordered.append(border) 
       
    return bordered
