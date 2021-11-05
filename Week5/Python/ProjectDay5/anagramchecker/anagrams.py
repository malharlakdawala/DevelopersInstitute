from anagramchecker import Anagramchecker

def main():
    input_menu_item = input("""
            i-> Input Keyword
            x-> Exit    
            """)
    if input_menu_item=="i":
        input_word = input("Input word: ")
        if len(input_word.split()) > 1:
            print("Please enter 1 word only ")
            return main()
        elif not input_word.isalpha():
            print("Enter alphabets only ")
            return main()
        else:
            "".join(input_word)
            input_word = input_word.upper()
            input_word = input_word.lstrip()
            input_word = input_word.rstrip()
            a = Anagramchecker(input_word).get_anagrams()
            a=", ".join(a)
            print(f"The anagram for {input_word} is {a}")
            return main()

    else: exit()

main()
