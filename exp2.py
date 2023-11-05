# Frequency Analysis
Text = input("Enter text : ")

length = len(Text)

for char in Text:
    count = 0
    for char_check in Text:
        if(char_check == char):
            count += 1
        else:
            continue
    frequency = (count*100)/length
    print(char," = ",frequency)