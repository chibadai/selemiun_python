import sys
sys.path.append("./own_module")
# import OutputText_sample
from own_module import OutputText

def main():
    OutputFileName = 'test.txt'
    testArray = ['1', '2', '3', '4', '5']
    # sample()
    OutputText.outputText(OutputFileName, testArray)

if __name__ == '__main__':
    main()
