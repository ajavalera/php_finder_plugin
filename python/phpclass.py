#PhpClass entity

class PhpClass:

    path = ""
    namespace = ""
    classname = ""
    fullnamespace = ""
    methods = []
    attributes = []
    content = []

    def __init__(self, path):
        self.path = path
        with open(path) as f:
            for n, line in enumerate(f, 1):
                self.content.append(line)

        self.SetNamespace()
        self.SetClassName()
        self.SetFullNamespace()

    def SetNamespace(self):
        for line in self.content:
            if 'namespace' in line:
                namespace = line.replace("namespace ","")
                namespace = namespace.replace(";", "")
                self.namespace = namespace.rstrip()
                break

    def SetClassName(self):
        for line in self.content:
            if 'class' in line:
                linelist= line.split("class")
                self.classname = linelist[1].rstrip()

                linelist2 = self.classname.split(" ")
                self.classname = linelist2[1].rstrip()
                self.classname = self.classname.replace(" ", "")
                break

    def SetFullNamespace(self):
        self.fullnamespace = self.namespace + '\\' + self.classname
