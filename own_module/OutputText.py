def outputText(outputFileName, outputText):
    f = open(outputFileName, 'w')
    try:
        for i in range(0, len(outputText)):
            print(i)
            print(outputText[i])
            f.write(outputText[i] + "\n")
    except:
        print('error')
    finally:
        f.write("\n")
        f.close()
