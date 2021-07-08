def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 31:
        return [28, 30, 31]
    if lastNumberOfDays == 30:
        return [31]
    if lastNumberOfDays == 28:
        return [31]

