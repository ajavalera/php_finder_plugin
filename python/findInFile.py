# findInFile module.
# Has methods that allow the finding and organization of data found in
# php files.

# Finds methods in a PHP file given a PATH, and returns a
# sensible dictionary with what it found.
def methods(filePath):

    with open(filePath) as f:
        data = f.read()

    lineList = data.split("\n")

    publicMethods    = []
    privateMethods   = []
    staticMethods    = []
    protectedMethods = []
    lineNumber       = 1 # There is no line 0 you nincapoop

    for line in lineList:
        line = line.strip()
        line = line + ":" + str(lineNumber)

        if "public function" in line:
            publicMethods.append(line)
        elif "private function" in line:
            privateMethods.append(line)
        elif "static function" in line:
            staticMethods.append(line)
        elif "protected function" in line:
            protectedMethods.append(line)

        lineNumber += 1

    return {
            "public": sorted(publicMethods),
            "private": sorted(privateMethods),
            "static": sorted(staticMethods),
            "protected": sorted(protectedMethods)
            }
