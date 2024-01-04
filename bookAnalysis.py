# Vital Nyabashi       4/07/2023
# Com S Lab 12
# Assignment:BookAnalysis.py

def analyzeBook(filename):
    with open(filename,'r', encoding="utf8") as f:
        count = {}
        for line in f:
            for word in line.split():
                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')

                # ignore case
                word = word.lower()

                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def outputAnalysis(count, title):
    keys_sorted= sorted(count.keys())
    filename = f"{title}_analysis.txt"
    try:
    # save the word count analysis to a file
        with open(filename,'w') as out:
            for word in keys_sorted :
                out.write(word + " " + str(count[word]))
                out.write('\n')
        return True
    except Exception as e:
        print(f"Error occured while writing to file {filename}: {e}")
        return False


def main():
    filename= "C:/Users/vital/OneDrive/Desktop/COM S 127 WORK FOLDER/The Project Gutenberg eBook of A ne.txt"
    count_dict = analyzeBook(filename)
    success = outputAnalysis(count_dict, "A new name")
    print("Did the output succeed?:", success)


if __name__ == "__main__":
    main()
