import tinysegmenter as ts

# print(' | '.join(ts.tokenize(u"私の名前は中野です")))
#
# print(ts.tokenize("私の名前は中野です"))

text = "Hi. I'm testing\nsome\nstufff\n"

print(text)

text = text.replace("\n", '')

print(text)