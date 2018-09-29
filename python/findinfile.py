# find_in_file module.
# Has methods that allow the finding and organization of data found in
# php files.

# Finds methods in a PHP file given a PATH, and returns a
# sensible dictionary with what it found.

import os
import sys

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

def find_usage(path, needle, result=[]):
    try:
        dirlist = os.listdir(path)

        for fname in dirlist:
            filepath = path + os.sep + fname

            if os.path.isfile(filepath):
                if is_invalid_file_name(fname):
                    continue

                with open(filepath, 'rt') as f:
                    for num, line in enumerate(f,1):
                        if line.find(needle) > -1:
                            resultline = filepath + ":" + str(num) + ":    " + line
                            resultline = resultline.strip()
                            result.append(resultline)
            else:
                find_usage(filepath, needle, result)

        return result
    except:
        print("\n\n" + path + " Errored out:", sys.exc_info()[0])

def is_invalid_file_name(fname):
    acceptedfiles = [
            '.php',
            '.txt'
            ]

    for ext in acceptedfiles:
        if ext in fname:
            return False

    return True
