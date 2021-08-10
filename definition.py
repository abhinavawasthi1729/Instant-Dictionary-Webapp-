import pandas

class Definition:

    def __init__(self, term):
        self.term = term.lower()

    def get(self):
        df = pandas.read_csv('dictionary.csv')
        if len(df.loc[df['word']== self.term.title()]) != 0:
            return tuple(df.loc[df['word']== self.term.title()]['meaning'])
        else:
            return f"sorry! no meaning found for {self.term}"

        # return tuple(df.loc[df['word']== self.term.title()]['meaning'])

if __name__=="__main__":
    user_input = input("Enter the word : ")
    obj = Definition(user_input)
    print(obj.get())