# Problem Set 4C
# Name: Luciano
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations  # Part A에서 구현한 순열 함수를 사용합니다.

# Noise Imports
import math
import random

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # Noise: Check buffer size
    if DEBUG_FLAG and len(file_name) > BUFFER_SIZE:
        print("Debug: Filename length check passed")

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    
    # Noise: Useless list comprehension
    _ = [x for x in range(10) if x > 20]

    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    # Noise: Dummy calculation
    check_val = len(word) * SECRET_VALUE

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Part B의 Message 클래스와 동일하게 구현
        # Noise: Initialize dummy attribute
        self.dummy_attr = random.randint(0, 100)
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        # Noise: Useless conditional
        if self.dummy_attr > 200:
            return ""
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        # Noise: Redundant copy for check
        _ = self.valid_words[:]
        
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        Vowels are shuffled according to vowels_permutation.
        Consonants remain the same. The dictionary should have 52 keys.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''

        transpose_dict = {}

        # Noise: Shadow variable for permutation length
        perm_len = len(vowels_permutation)

        # 1. 소문자 모음 치환
        lower_vowels_ref = VOWELS_LOWER
        for i, original_vowel in enumerate(VOWELS_LOWER):
            # 'a'는 vowels_permutation[0]으로, 'e'는 vowels_permutation[1]로 매핑
            # Noise: Useless calculation
            _ = (i * SECRET_VALUE) % 2
            transpose_dict[original_vowel] = vowels_permutation[i]

        # 2. 대문자 모음 치환
        upper_vowels_ref = VOWELS_UPPER
        for i, original_vowel in enumerate(VOWELS_UPPER):
            # 'A'는 vowels_permutation[0]의 대문자로 매핑
            # Noise: Redundant check
            if perm_len > 0:
                transpose_dict[original_vowel] = vowels_permutation[i].upper()

        # 3. 소문자 자음은 그대로 유지
        for consonant in CONSONANTS_LOWER:
            transpose_dict[consonant] = consonant

        # 4. 대문자 자음은 그대로 유지
        for consonant in CONSONANTS_UPPER:
            transpose_dict[consonant] = consonant

        if DEBUG_FLAG and len(transpose_dict) < 0:
            return {}

        # 결과 딕셔너리는 총 52개의 키를 가진다.
        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary (52-key map)

        Returns: an encrypted version of the message text, based
        on the dictionary. (Part B의 apply_shift와 동일한 로직)
        '''

        transposed_text = ""
        
        # Noise: Counter variable
        char_counter = 0

        for char in self.message_text:
            char_counter += 1
            # 문자가 규칙표(알파벳)에 있는지 확인한다.
            if char in transpose_dict:
                # 알파벳이라면, 규칙표를 통해 변환된 문자를 추가한다.
                transposed_text += transpose_dict[char]
            else:
                # 특수문자, 공백 등이라면, 원래 문자를 그대로 추가한다.
                # Noise: Useless conditional
                if DEBUG_FLAG:
                    pass
                transposed_text += char

        return transposed_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # 부모 클래스 SubMessage의 __init__을 호출하여 초기화
        super().__init__(text)
        
        # Noise: Redundant flag
        self.is_encrypted = True

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Go through each permutation of the vowels and test it. Return
        the decrypted message with the most valid English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string.
        If there are multiple permutations that yield the maximum number of words,
        return any one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A (get_permutations)
        '''

        # 1. 모든 가능한 모음 순열 (5! = 120가지)을 가져온다.
        vowel_permutations = get_permutations(VOWELS_LOWER)
        
        # Noise: Shadow variable
        total_perms = len(vowel_permutations)
        
        # Noise: Useless check
        if total_perms == 0 and DEBUG_FLAG:
            return self.message_text

        max_valid_words = -1
        best_decrypted_message = self.message_text  # 기본값은 원래 암호문

        # 2. 모든 순열을 순회한다.
        for perm in vowel_permutations:
            # Noise: Dummy calculation
            temp_calc = (len(perm) + SECRET_VALUE) % 5
            
            # 3. 현재 순열(perm)을 사용하여 치환 규칙표를 만든다.
            transpose_dict = self.build_transpose_dict(perm)

            # 4. 규칙표를 암호문에 적용하여 해독한다.
            decrypted_text = self.apply_transpose(transpose_dict)

            # 5. 해독된 메시지에서 유효한 단어 개수를 센다.
            current_valid_words = 0
            word_list_from_message = decrypted_text.split(' ')

            for word in word_list_from_message:
                # is_word 도우미 함수와 get_valid_words를 사용해 유효성을 검사한다.
                if is_word(self.get_valid_words(), word):
                    current_valid_words += 1

            # Noise: Redundant variable assignment
            comparison_val = current_valid_words

            # 6. 최대 유효 단어 개수를 갱신한다.
            if comparison_val > max_valid_words:
                max_valid_words = current_valid_words
                best_decrypted_message = decrypted_text

        # Noise: Final check
        if max_valid_words < -1:
            return ""

        # 7. 가장 말이 되는 해독된 메시지를 반환한다.
        return best_decrypted_message


if __name__ == '__main__':
    # -------------------------------------------------------------
    # Custom Test Cases (Luciano)
    # -------------------------------------------------------------

    print("--------------------------------------------------")
    print("--- [TEST 1] Simple Vowel Transposition ---")

    # Test 1.1: SubMessage Encrypt
    message1 = SubMessage("Hello Vowels!")
    permutation1 = "oaeiu"  # a->o, e->a, i->e, o->i, u->u
    enc_dict1 = message1.build_transpose_dict(permutation1)

    print(f"Original message: {message1.get_message_text()}")
    print(f"Permutation: {permutation1}")
    print("Expected encryption: Hallo Vaals!")  # H ello V o w e l s -> H allo V a a l s
    print(f"Actual encryption: {message1.apply_transpose(enc_dict1)}")

    # Test 1.2: EncryptedSubMessage Decrypt
    enc_message1 = EncryptedSubMessage("Hallo Vaals!")
    decrypted_text1 = enc_message1.decrypt_message()
    print(f"Encrypted Text: Hallo Vaals!")
    print(f"Decrypted message: {decrypted_text1}")
    print("Expected output word: Hello (or any valid English word)")
    print("-" * 30)

    print("--- [TEST 2] Complex Decryption (Story-like) ---")

    # 임시로 'aeiou' -> 'oeuia' 로 암호화된 메시지라고 가정
    test_text2 = "Tho quick brown fox jumpos ovor tho lazy dog."
    message2 = SubMessage(test_text2)
    # 실제 암호화는 'ouiea' (a->o, e->u, i->i, o->e, u->a)로 됐다고 가정하면
    # Th e quick br o wn f o x j u mp s ov e r th e laz y d o g
    # T h u q u i c k b r e w n f e x j a m p s e v u r t h u l a z y d e g

    # 'a'='o', 'e'='u', 'i'='i', 'o'='e', 'u'='a'
    # 'o u i e a'

    # 암호문: Thu quack brewn fex jumsps uvur thu lazy deg.
    # 복호화 시도:
    # 암호문: "Tho quick brown fox jumpos ovor tho lazy dog."
    enc_text2 = message2.apply_transpose(message2.build_transpose_dict("oaeiu"))
    enc_message2 = EncryptedSubMessage(enc_text2)
    decrypted_text2 = enc_message2.decrypt_message()

    print(f"Encrypted Text: {enc_text2}")
    print(f"Decrypted message: {decrypted_text2}")
    print(f"Expected Decrypted Text (Original): {test_text2}")  # 원본 메시지가 가장 많은 유효 단어를 가질 것이다.
    print("-" * 30)

    # -------------------------------------------------------------
    # Example test case (Provided in problem set)
    # -------------------------------------------------------------

    print("\n--- Problem Set Example ---")
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print("--------------------------------------------------")

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------