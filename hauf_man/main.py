import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_code_mapping(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node.char is not None:
        mapping[node.char] = code
    else:
        build_code_mapping(node.left, code + "0", mapping)
        build_code_mapping(node.right, code + "1", mapping)

    return mapping

def huffman_encoding(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1

    huffman_tree = build_huffman_tree(freq_table)
    code_mapping = build_code_mapping(huffman_tree)

    encoded_text = ''.join(code_mapping[char] for char in text)
    return encoded_text, huffman_tree

def huffman_decoding(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    encoded_text, huffman_tree = huffman_encoding(user_input)
    print("Encoded text:", encoded_text)

    decoded_text = huffman_decoding(encoded_text, huffman_tree)
    print("Decoded text:", decoded_text)
