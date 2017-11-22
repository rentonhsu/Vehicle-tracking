import os

def getFiles(root, extensions):
    assert root and extensions, 'Please provide the root folder that you want to look into, ' \
                                'and the file extensions you\'re interested in.'
    output_list = []

    if isinstance(extensions, (list, tuple)):
        isExtensionMatch = lambda x, ext : True in [x.endswith(extension) for extension in ext]
        extensionTypes = 'Multiple'

    elif type(extensions) == str:
        isExtensionMatch = lambda x : x.endswith(extensions)
        extensionTypes = 'Single'

    for dirPath, dirNames, fileNames in os.walk(root):
        for fileName in fileNames:
            if extensionTypes == 'Multiple':
                if isExtensionMatch(fileName, extensions):
                    output_list.append(os.path.join(dirPath, fileName))
            elif extensionTypes == 'Single':
                if isExtensionMatch(fileName):
                    output_list.append(os.path.join(dirPath, fileName))

    return output_list

print(len(getFiles(r'C:\Users\User\Desktop\0721修改之圖文', ['.jpg', '.png'])))

