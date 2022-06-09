class AddressFixer():
    """Class that exchange every backlash with -> in given path"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.fp_list = []
        self.arrow = "_"
        self.slash = "/"
        self.slash_index = []

    def address_converter(self):   # Funkcja do konwersji adresu strony do nazwy pliku (zamiana slashy na strzały)

        for letter in self.file_path:    #pętla tworząca listę ściężki z stringa
            self.fp_list.append(letter)

        for i in range(len(self.fp_list)):   #pętla tworząca listę indeksów slashy w ścieżce

            if self.fp_list[i] == self.slash:
                self.slash_index.append(i)

        for i in range(0, len(self.slash_index)):   #pętla zamieniająca slashe na strzałki
            insert_slash = self.slash_index[i]
            self.fp_list[insert_slash] = self.arrow

        self.fixed_file_path = str("".join(self.fp_list))
        self.fixed_file_path = self.fixed_file_path.replace(chr(34),"")
        self.fixed_file_path = self.fixed_file_path.replace(":", ";")
        self.fixed_file_path = self.fixed_file_path.replace(chr(92), "-bs-")
        self.fixed_file_path = self.fixed_file_path.replace("*", "-str-")
        self.fixed_file_path = self.fixed_file_path.replace("?", "-q-")
        self.fixed_file_path = self.fixed_file_path.replace(chr(74), "-brcl-")
        self.fixed_file_path = self.fixed_file_path.replace(chr(76), "-brcr-")
        self.fixed_file_path = self.fixed_file_path.replace(chr(174), "-ln-")
        return self.fixed_file_path

# path = SlashChanger("https://www.pythoncheatsheet.org/#Handling-File-and-Directory-Paths")
# fixed_path = path.address_converter()
# print(fixed_path)