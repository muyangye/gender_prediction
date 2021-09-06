lines = open('train.txt', encoding='utf-8').readlines()[1:]
totalMale = totalFemale = 0
characterToSex = {}
for line in lines:
    # Don't need id
    line = line.strip().split(',')
    characters = line[1]
    sex = line[2]
    if (sex == '1'):
        totalMale += 1
    else:
        totalFemale += 1
    for character in characters:
        if (character not in characterToSex):
            characterToSex[character] = {}
        if (sex not in characterToSex[character]):
            characterToSex[character][sex] = 0
        characterToSex[character][sex] += 1
total = totalMale + totalFemale

# We need to calculate P(sex|char)
# Bayes' Theorem tells us that P(sex|char) = P(char|sex) * P(sex) / P(char)
# Note P(char|sex) = number of char in a specific sex / total number of that sex
# And that P(sex) = total number of that sex / total number of all sex
# So P(char|sex) * P(sex) = number of char in a specific sex / total number of all sex

while True:
    print('Please enter the name you want to predict(enter exit to exit): ')
    name = input()
    if (name == 'exit'):
        break
    maleProb = femaleProb = 1
    # Naive Bayes assumes that all events are independent. i.e. P(sex|abc) = P(sex|a) * P(sex|b) * P(sex|c)
    for char in name:
        # P(char) = 1 / number of all chars
        maleProb *= characterToSex[char]['1'] / total / len(characterToSex)
        femaleProb *= characterToSex[char]['0'] / total / len(characterToSex)
    # normalization so that probabilities add up to 1
    finalMaleProb = maleProb / (maleProb + femaleProb) * 100
    finalFemaleProb = femaleProb / (maleProb + femaleProb) * 100
    print('The chance that guy is male is: ' + str(finalMaleProb) + '%')
    print('The chance that guy is female is: ' + str(finalFemaleProb) + '%')