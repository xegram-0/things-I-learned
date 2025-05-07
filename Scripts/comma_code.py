
def commaString(inputString:str):
    returnString:str = ''
    # The length adjustment is for the 2nd-to-last and the last element
    for i in range(len(inputString)-1):
        if i == (len(inputString) - 2):
            returnString += inputString[i] + ' and ' + inputString[i+1]
            return returnString
        else:
            # Use '+=' here, not '+' only
            # Would result in None or just the last 'and cats'
            returnString += inputString[i] + ', '

def main():
    spam:list = ['apples', 'bananas', 'tofu', 'cats']
    resultString:str = commaString(spam)
    print(resultString)

if __name__=='__main__':
    main()