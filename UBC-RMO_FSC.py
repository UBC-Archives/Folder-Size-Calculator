#Folder Size Calculator
#Version: 1.1
#https://recordsmanagement.ubc.ca
#https://www.gnu.org/licenses/gpl-3.0.en.html

inputfile = open('input.txt', 'r', encoding='utf-8').read()
inputfilelines = inputfile.split('\n')

with open('output.txt', 'w', encoding='utf-8') as outputfile:
    for i in inputfilelines:
        isplit = i.split('\t')
        if isplit[1] == '-':
            foldersize = 0
            for j in inputfilelines[inputfilelines.index(i) + 1:]:
                if j.startswith(isplit[0]+'\\'):
                    if j.split('\t')[1]=='-':
                        foldersize += 0
                    else:
                        foldersize += int(j.split('\t')[1])
            outputfile.write(isplit[0] + '\t' + str(foldersize/1048576) + '\n')
        else:
            outputfile.write(isplit[0] + '\t' + str(int(isplit[1])/1048576) + '\n')
print('Done!')
input('Press any key to exit ...')
