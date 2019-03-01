class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):

        # base case, if self is None, terminate recursive
        if not self:
            return

        # if self has value invoke cb with current value
        cb(self.value)

        if self.left:
            self.left.depth_first_for_each(cb)
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):

        store = []
        store.append(self)

        while len(store) > 0:

            current = store.pop(0)

            cb(current.value)

            # add child Node if exist
            if current.left is not None:
                store.append(current.left)
            if current.right is not None:
                store.append(current.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value


l = BinarySearchTree(5)

arr = []


def cb(x): return arr.append(x)


l.insert(3)
l.insert(4)
l.insert(10)
# l.insert(9)
# l.insert(11)


# l.depth_first_for_each(cb)
l.breadth_first_for_each(cb)
print(arr)
# [5, 3, 10, 4, 9, 11])
