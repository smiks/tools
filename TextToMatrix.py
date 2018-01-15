class TextToMatrix:
    """
        Converts text to matrix.
        Names of columns are unique words that appear in a text,
        values of columns are frequencies of previously mentioned words.
    """

    def __init__(self):
        self.union_of_words = set()
        self.matrix_titles = []
        self.list_of_texts = []
        self.text_tokens = []
        self.matrix_titles = []
        self.matrix = []

    def _clean(self):
        """
            Re-initialize union of words and list of words.
            Useful when user is adding text after already generating matrix.
        :return:
        """
        self.union_of_words = set()
        self.matrix_titles = []

    def add_text(self, text, force_lower=True):
        """
        If matrix is already generated it will be purged.

        :param text: text to be added in a matrix.
        :param force_lower: if True, all words will be in lower case.
        :return:
        """

        if force_lower:
            text = text.lower()

        if len(text) > 0:
            self.list_of_texts.append(text)

        if len(self.matrix_titles):
            self._clean()

    @staticmethod
    def _tokenize(text):
        import re
        clean = [" ", ",", ";", ".", ":", "?", "!", "(", ")"]
        tokens = []
        regex = r"^[a-zA-ZšŠčČžŽ]+"
        for word in text.split():
            for c in clean:
                word = word.strip(c)

            m = re.match(regex, word)
            if m is not None:
                word = m.group()
            tokens.append(word)

        print("TOKENS: ", tokens)
        return tokens

    def _generate_union(self):
        for text in self.list_of_texts:
            words = TextToMatrix._tokenize(text)
            self.text_tokens.append(words)
            self.union_of_words |= set(words)

        self.matrix_titles = list(self.union_of_words)

    def prepare(self):
        self._generate_union()
        return self

    def generate_matrix(self):
        for tokens in self.text_tokens:
            tmp = []
            for title in self.matrix_titles:
                cnt = tokens.count(title)
                tmp.append(cnt)

            self.matrix.append(tmp)

    def print_matrix(self):
        print(self.matrix)
        print('\t'.join(self.matrix_titles))
        for m in self.matrix:
            print('\t'.join(map(str, m)))

    def write_to_file(self, filename):
        """
            Tries to store matrix in tab separated format.
            If matrix is successfully stored in a file function returns True
            otherwise False.
        :param filename:
        :return:
        """

        try:
            open(filename, 'w').close()
            with open(filename, 'a') as file:
                file.write('\t'.join(self.matrix_titles) + '\n')
                for e, m in enumerate(self.matrix):
                    endln = ""
                    if e+1 < len(self.matrix):
                        endln = "\n"
                    file.write('\t'.join(map(str, m)) + endln)
        except:
            return False

        return True


if __name__ == "__main__":
    t2m = TextToMatrix()

    text1 = "This is text number one."
    text2 = "This is text number two!"

    t2m.add_text(text1, classes=[1, 2])
    t2m.add_text(text2, classes=[0, 3])

    t2m.prepare().generate_matrix()

    t2m.add_class_title("CA")
    t2m.add_class_title("CB")

    t2m.print_matrix(description_row=True)
    t2m.write_to_file("test", description_row=True)

    """
        Output example:

        text	this	one	is	two	number	CA	CB
        c	c	c	c	c	c	class	class
        1	1	1	1	0	1	1	2
        1	1	0	1	1	1	0	3
    """
