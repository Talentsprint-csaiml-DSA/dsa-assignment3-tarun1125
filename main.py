import heapq 

def calculate_frequencies(text):
    freq_dict = {}
    for char in text:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1
    return freq_dict

def huffman_codes(string):
    freq_dict = calculate_frequencies(string)

    heap = [[freq, [sym, ""]] for sym, freq in freq_dict.items()]

    heapq.heapify(heap)

    while len(heap)>1:
        first_low = heapq.heappop(heap)
        second_low = heapq.heappop(heap)

        for pair in first_low[1:]:
            pair[1] = '0' + pair[1]

        for pair in second_low[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [first_low[0] + second_low[0]] + first_low[1:] + second_low[1:])

    huffman_tree = heap[0][1:]
    huffman_dict = {sym: code for sym, code in huffman_tree}
    encoded_string = ''.join(huffman_dict[char] for char in string)

    return encoded_string
        