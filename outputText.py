def outputText(OutputFileName, OutputText[]):
    f = open(OutputFileName, 'w')
    for i in range(1, len(OutputText)):
        f.write(OutputText[i])

    f.close()
