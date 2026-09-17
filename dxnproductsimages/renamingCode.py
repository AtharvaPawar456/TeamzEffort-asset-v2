import os


def renameAllFiles(folderPath):
    """
    Renames all files inside a folder sequentially.

    Input:
        folderPath (str): Target directory path

    Working:
        - Iterates through all files
        - Renames each file to file_<number> with original extension
    """
    try:
        files = sorted(os.listdir(folderPath))
        fileCounter = 1
        # fileCounter = 112

        for fileName in files:
            oldPath = os.path.join(folderPath, fileName)

            if not os.path.isfile(oldPath):
                continue

            _, extension = os.path.splitext(fileName)
            newFileName = f"file_{fileCounter}{extension}"
            newPath = os.path.join(folderPath, newFileName)

            os.rename(oldPath, newPath)
            fileCounter += 1

        print(f"Renamed {fileCounter - 1} files in '{folderPath}' successfully.")

    except Exception as error:
        print(f"Error: {error}")


folderList = [
    # "dxn-2in1",
    # "dxn-butterfly-pea",

    # "dxn-breakfast-cookies",
    # "dxn-coconut-oil",
    # "dxn-coconut-sugar",
    # "dxn-cordyceps-cereals",
    # "dxn-cordyceps-coffee",
    # "dxn-cordyceps-tablets",
    # "dxn-GL",
    # "dxn-linzhi-3-in-1-coffee",
    # "dxn-lions-mane",
    # "dxn-mongra-safron",
    # "dxn-moringa",
    # "dxn-morinzhi-juice",
    # "dxn-morinzhi-powder",
    # "dxn-multiflora-honey",
    # "dxn-panax-ginseng",
    # "dxn-pink-salt",
    # "dxn-radish-salt",
    # "dxn-raw-hing",
    # "dxn-red-chilli-powder",
    # "dxn-RG",
    # "dxn-roselle-juice",
    # "dxn-roselle-tablet",
    # "dxn-shatavari-kalpa",
    # "dxn-shilajit",
    # "dxn-sitopan",
    # "dxn-turmeric-powder",
    # "dxn-zhi-mocha"
    
    "dxn-ganoderma"
    
]

# for folder in folderList:
#     renameAllFiles(folder)


files = os.listdir("dxn-breakfast-cookies")
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-soap/shorts/"
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort-asset-v2/refs/heads/main/dxnproductsimages/dxn-breakfast-cookies/"



for fileName in files:
    print(f"'{tempPath}{fileName}',")



# https://github.com/AtharvaPawar456/TeamzEffort/blob/main/static/dxnproductsimages/dxn-tooth-paste/file_64.mp4
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tooth-paste/file_64.mp4





"""


"""