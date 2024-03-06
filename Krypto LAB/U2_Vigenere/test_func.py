import functions as func

def main():
    #text = "Kryptotext_TAG.txt"
    #text1 = func.read(text)
    #text3 = text1[0:50]
    #print(text3)
    #text1 = text1.translate({ord(i): None for i in '., ÄÖÜ'})

#    list_index_of_coincidence = []
#
 #   for i in range(4):
  #      index = 0
   #     list = func.partition_text(text1, i + 1)
    #    for j in range(len(list)):
     #       index = index + func.index_of_coincidence_text(list[j])
      #  index = index / len(list)
       # list_index_of_coincidence.append(index)
    #print(list_index_of_coincidence)

#    list_index_of_coincidence = []
#
 #   for i in range(4):
  #      index = 0
   #     list = func.partition_text(text3, i + 1)
    #    for j in range(len(list)):
     #       index = index + func.index_of_coincidence_text(list[j])
      #  index = index / len(list)
       # list_index_of_coincidence.append(index)
    #print(list_index_of_coincidence)
    #text = "AAAAABCDD"
    #numbers = func.count_letters(text)
    #most_common = func.most_common_letter(numbers)
    #print(numbers)
    #print(most_common)
    #print(func.frequency_analysis(text))
    text = "Klartext_TAG.txt"
    text1 = func.read(text)
    list_text_partition_by_key = func.partition_text(text1, 3)
    for text_part in list_text_partition_by_key:
        frequency_letters = func.count_letters(text_part)
        index_most_common_letter = func.most_common_letter(frequency_letters)
    text = "Kryptotext_TAG.txt"
    text1 = func.read(text)
    list_text_partition_by_key = func.partition_text(text1, 3)
    for text_part in list_text_partition_by_key:
        text_part = func.decrypt_text_key(text_part, 'T')
        frequency_letters = func.count_letters(text_part)
        index_most_common_letter = func.most_common_letter(frequency_letters)

main()