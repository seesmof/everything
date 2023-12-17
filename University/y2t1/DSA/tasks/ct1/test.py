class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverseMapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def buildFrequencyDict(self, text):
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def buildHeap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def mergeNodes(self):
        while len(self.heap) > 1:
            child = heapq.heappop(self.heap)
            mergeWith = heapq.heappop(self.heap)

            merged = self.HeapNode(None, child.freq + mergeWith.freq)
            merged.left = child
            merged.right = mergeWith

            heapq.heappush(self.heap, merged)

    def _buildCodesHelper(self, root, currentCode):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = currentCode
            self.reverseMapping[currentCode] = root.char
            return

        self._buildCodesHelper(root.left, currentCode + "0")
        self._buildCodesHelper(root.right, currentCode + "1")

    def buildCodes(self):
        root = heapq.heappop(self.heap)
        currentCode = ""
        self._buildCodesHelper(root, currentCode)

    def getEncodedText(self, text):
        encodedText = ""
        for char in text:
            encodedText += self.codes[char]
        return encodedText

    def padEncodedText(self, encodedText):
        extraPadding = 8 - len(encodedText) % 8
        for i in range(extraPadding):
            encodedText += "0"

        paddingInfo = "{0:08b}".format(extraPadding)
        encodedText = paddingInfo + encodedText
        return encodedText

    def getByteArray(self, paddedEncodedText):
        if len(paddedEncodedText) % 8 != 0:
            console.log("Encoded text not padded properly", log_locals=True)
            exit(0)

        b = bytearray()
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i : i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        outputPath = fileName + ".bin"

        with open(filePath, "r+") as file, open(outputPath, "wb") as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.buildFrequencyDict(text)
            self.buildHeap(frequency)
            self.mergeNodes()
            self.buildCodes()

            encodedText = self.getEncodedText(text)
            paddedEncodedText = self.padEncodedText(encodedText)

            b = self.getByteArray(paddedEncodedText)
            output.write(bytes(b))

        return outputPath

    def removePadding(self, paddedEncodedText):
        paddedInfo = paddedEncodedText[:8]
        extraPadding = int(paddedInfo, 2)

        paddedEncodedText = paddedEncodedText[8:]
        encodedText = paddedEncodedText[: -1 * extraPadding]

        return encodedText

    def decodeText(self, encodedText):
        currentCode = ""
        decodedText = ""

        for bit in encodedText:
            currentCode += bit
            if currentCode in self.reverseMapping:
                character = self.reverseMapping[currentCode]
                decodedText += character
                currentCode = ""

        return decodedText

    def decompress(self, filePath):
        fileName, fileExtension = os.path.splitext(filePath)
        outputPath = fileName + "_decompressed.txt"

        with open(filePath, "rb") as file, open(outputPath, "w") as output:
            bitString = ""

            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bitString += bits
                byte = file.read(1)

            encodedText = self.removePadding(bitString)
            decodedText = self.decodeText(encodedText)

            output.write(decodedText)

        return outputPath
