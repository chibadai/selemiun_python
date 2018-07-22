def outputText(outputFileName, outputText):
    f = open(outputFileName, 'w')
    try:
        for i in range(0, len(outputText)):
            f.write(outputText[i] + "\n")
    except:
        print('file write error')
    finally:
        f.write("\n")
        f.close()
