
class Directory:
    def __init__(self, name):
        self.dir_name = name
        self.dir = []
        self.files_size = 0
        self.prev = None
        self.total = 0
        self.total_result = 0

    def add_dir(self, dir_name):
        self.dir.append(Directory(dir_name))

    def go_back(self):
        return self.prev

    def goto_dir(self, dir_name):
        for dir in self.dir:
            if dir.dir_name == dir_name:
                dir.prev = self
                return dir
        return None

    def add_file(self, file_size):
        self.files_size += file_size

    def get_total_size(self):
        total_size = 0
        total_size += self.files_size
        for dir in self.dir:
            total_size += dir.get_total_size()

        return total_size

    def print_dirs(self):
        for dir in self.dir:
            dir.print_dirs()
        size = self.get_total_size()
        if size <= 100000:
            print(size)

