def reverse_vowels(input_str):
    # Convert the string to a list of characters
    char_list = list(input_str)
    
    # Define a set of vowels for checking
    vowels = set("AEIOUaeiou")
    
    # Initialize pointers
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Find the next vowel from the left
        while left < right and char_list[left] not in vowels:
            left += 1
        
        # Find the next vowel from the right
        while left < right and char_list[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        # Move the pointers inward
        left += 1
        right -= 1
    
    # Reconstruct the string from the modified list of characters
    reversed_str = ''.join(char_list)
    
    return reversed_str

# Example usage:
input_str = input()
result = reverse_vowels(input_str)
print(result)  # Output: "Holle, Werld!"
