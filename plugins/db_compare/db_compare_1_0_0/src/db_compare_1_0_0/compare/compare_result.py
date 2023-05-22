class CompareResult:
    def __init__(self, marked, left, right):
        self.marked = marked
        self.left = left
        self.right = right

    def dict(self):
        return dict(marked=self.marked, left=self.left, right=self.right)

    @staticmethod
    def create(marked, left, right):
        if marked == "equal":
            return CompareResult(marked, left, right)
        if marked == "insert":
            return CompareResult(marked, ["缺失"], right)
        if marked == "delete":
            return CompareResult(marked, left, ["缺失"])
        if marked == "replace":
            return CompareResult(marked, left, right)