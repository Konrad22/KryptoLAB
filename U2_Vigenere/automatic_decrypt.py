import functions as func
import sys

def main():
    text = sys.argv[1]
    output = sys.argv[2]
    f = func.read(text)
    list_index_of_coincidence = []
    list = []
    key = ""
    for i in range(100):
        index = 0
        list = func.partition_text(f, i + 1)
        for j in range(len(list)):
            index = index + func.index_of_coincidence_text(list[j])
        index = index/len(list)
        list_index_of_coincidence.append(index)

    tolerance = max(list_index_of_coincidence) - 0.01
    likely_key_lengths = [i+1 for i,v in enumerate(list_index_of_coincidence) if v > tolerance]
    count_divisors = [0] * max(likely_key_lengths)
    for key_length in likely_key_lengths:
        count_divisors = func.get_and_count_divisors(count_divisors, key_length)

    likely_key_length = count_divisors.index(max(count_divisors)) + 1

    while(likely_key_length not in likely_key_lengths):
        count_divisors[likely_key_length - 1] = 0
        likely_key_length = count_divisors.index(max(count_divisors)) + 1

    #print(likely_key_lengths)

    #print(likely_key_length)
    #Häufigkeitsanalyse gibt falschen Schlüssel aus, am Donnerstag schauen ob richtig geschrieben
    list_text_partition_by_key = func.partition_text(f, likely_key_length)
    for text_part in list_text_partition_by_key:
        k_part = func.frequency_analysis(text_part)
        key = key +  func.transform_number_to_letter(k_part)
    f = key + '\n' + func.decrypt_text_key(f,key)
    func.write(output, f)

main()

#gibt zu großen Schlüssel aus, wie am besten den kleinsten nenner finden