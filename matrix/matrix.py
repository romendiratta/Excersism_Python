class Matrix(object):

    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")
        self.columns = []


    def row(self, index):
        return " ".join(self, self.rows[index-1])

    def column(self, index):
        pass
