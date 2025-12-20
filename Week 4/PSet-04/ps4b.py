# Problem Set 4B
# Name: Luciano
# Collaborators:
# Time Spent: x:xx

import string

# words.txt 파일에서 유효한 단어 리스트를 로드하기 위한 전역 변수 (테스트용)
# 이 변수는 `load_words`가 호출될 때 채워집니다.
# 주의: 이 파일은 실행 환경에 words.txt가 있다고 가정합니다.
WORDLIST_FILENAME = 'words.txt'


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): 로드할 단어 목록이 포함된 파일 이름

    Returns: 유효한 단어 목록. 단어는 소문자로 이루어진 문자열입니다.

    단어 목록의 크기에 따라 이 함수를 완료하는 데 시간이 걸릴 수 있습니다.
    '''
    print("Loading word list from file...")
    # inFile: file
    try:
        # 파일 열기 시도
        with open(file_name, 'r') as inFile:
            # wordlist: list of strings
            wordlist = []
            for line in inFile:
                wordlist.extend([word.lower() for word in line.split(' ')])
            print("  ", len(wordlist), "words loaded.")
            return wordlist
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Returning an empty list.")
        return []
    except Exception as e:
        print(f"An error occurred while loading words: {e}. Returning an empty list.")
        return []


def is_word(word_list, word):
    '''
    대소문자 및 구두점을 무시하고 단어가 유효한 단어인지 판단합니다.

    word_list (list): 딕셔너리에 있는 단어 목록.
    word (string): 가능한 단어.

    returns: word_list에 단어가 있으면 True, 아니면 False

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    # 단어 주변의 구두점과 공백을 제거합니다.
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    '''
    story.txt 파일에서 전체 내용을 읽어 암호화된 문자열로 반환합니다.
    '''
    try:
        f = open("story.txt", "r")
        story = str(f.read())
        f.close()
        return story
    except FileNotFoundError:
        print(f"Error: The file 'story.txt' was not found. Returning a placeholder.")
        return "This is a placeholder story for testing purposes."


# wordlist는 전역에서 로드하여 Message 클래스 인스턴스에 전달됩니다.
# 실제 실행 환경에서는 이 부분을 주석 처리하고, 대신 Message 클래스 안에서 load_words()가 호출되도록 해야 할 수 있습니다.
# 여기서는 `if __name__ == '__main__':` 블록에서 로드하도록 구현하겠습니다.

### END HELPER CODE ###


class Message(object):
    ### 인스턴스 초기화 ###
    def __init__(self, text):
        '''
        Message 인스턴스를 초기화합니다.

        text (string): 메시지 텍스트
        self.message_text (string): 초기화 시 제공된 메시지 텍스트
        self.valid_words (list): load_words를 사용하여 로드된 단어 목록
        '''
        self.message_text = text
        # 일반적으로 load_words는 한 번만 호출되도록 외부에서 처리되지만,
        # 문제 요구사항을 따라 인스턴스마다 로드한다고 가정합니다.
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### Getter 메서드 ###
    def get_message_text(self):
        '''
        message_text 속성을 반환합니다.
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        유효한 단어 리스트의 사본을 반환합니다.
        '''
        # 리스트의 변경을 방지하기 위해 사본을 반환합니다.
        return self.valid_words[:]

    ### 핵심 암호화/복호화 도구 ###
    def build_shift_dict(self, shift):
        '''
        주어진 shift 값에 따라 암호화에 사용할 딕셔너리를 구축합니다.
        대문자와 소문자 알파벳만 이동하며, 다른 문자는 변경되지 않습니다.

        shift (integer): 0에서 25 사이의 정수.

        returns: 암호화에 사용할 딕셔너리
        '''
        shift_dict = {}

        # 소문자 처리
        lower_case = string.ascii_lowercase
        for i in range(26):
            original_char = lower_case[i]
            # (i + shift) % 26 으로 쉬프트 인덱스 계산
            shifted_char = lower_case[(i + shift) % 26]
            shift_dict[original_char] = shifted_char

        # 대문자 처리
        upper_case = string.ascii_uppercase
        for i in range(26):
            original_char = upper_case[i]
            # (i + shift) % 26 으로 쉬프트 인덱스 계산
            shifted_char = upper_case[(i + shift) % 26]
            shift_dict[original_char] = shifted_char

        # 알파벳이 아닌 문자는 딕셔너리에 포함할 필요가 없으며,
        # apply_shift에서 처리됩니다.
        return shift_dict

    def apply_shift(self, shift):
        '''
        메시지 텍스트에 주어진 shift를 적용하여 암호화된 텍스트를 반환합니다.

        shift (integer): 0에서 25 사이의 정수.

        returns: 암호화된 문자열
        '''
        shifted_text = []
        shift_dict = self.build_shift_dict(shift)

        for char in self.message_text:
            if char in shift_dict:
                # 딕셔너리에 있는 알파벳이면 쉬프트 적용
                shifted_text.append(shift_dict[char])
            else:
                # 딕셔너리에 없는 (공백, 구두점 등) 문자면 그대로 유지
                shifted_text.append(char)

        return "".join(shifted_text)


class PlaintextMessage(Message):
    '''
    암호화될 메시지를 나타내는 Message 하위 클래스입니다.
    PlaintextMessage 객체는 시프트 값과, 그에 따른 암호화 딕셔너리 및
    암호화된 메시지 텍스트를 가집니다.
    '''

    def __init__(self, text, shift):
        '''
        PlaintextMessage 인스턴스를 초기화합니다.

        text (string): 메시지 텍스트
        shift (integer): 시프트 값 (0에서 25 사이의 정수)

        self.shift (integer): 시프트 값
        self.encrypting_dict (dict): 암호화 딕셔너리
        self.message_text_encrypted (string): 암호화된 메시지 텍스트
        '''
        # Message의 생성자를 호출하여 text와 valid_words를 설정합니다.
        Message.__init__(self, text)

        self.shift = shift
        # shift에 따른 암호화 딕셔너리 구축
        self.encrypting_dict = self.build_shift_dict(shift)
        # shift를 적용하여 암호화된 메시지 텍스트 계산
        self.message_text_encrypted = self.apply_shift(shift)

    ### Getter 메서드 ###
    def get_shift(self):
        '''
        self.shift 속성을 반환합니다.
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        암호화 딕셔너리의 복사본을 반환합니다.
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        암호화된 메시지 텍스트를 반환합니다.
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        shift 값을 변경하고 이에 따라 encrypting_dict와
        message_text_encrypted를 업데이트합니다.

        shift (integer): 새로운 시프트 값 (0에서 25 사이의 정수)

        returns: None
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    '''
    복호화될 메시지를 나타내는 Message 하위 클래스입니다.
    CiphertextMessage 객체는 복호화될 메시지 텍스트만 가집니다.
    '''

    def __init__(self, text):
        '''
        CiphertextMessage 인스턴스를 초기화합니다.

        text (string): 암호화된 메시지 텍스트

        self.message_text (string): 초기화 시 제공된 암호화된 메시지 텍스트
        self.valid_words (list): 유효한 단어 목록
        '''
        # Message의 생성자를 호출합니다.
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        암호화된 텍스트를 복호화하는 가장 좋은 시프트(shift)를 찾습니다.
        가장 좋은 시프트는 복호화된 메시지에서 가장 많은 수의 유효한
        영어 단어를 생성하는 시프트입니다.
        (shift가 0일 때 가장 많은 유효 단어를 생성하는 경우가 발생할 수 있습니다.)

        returns: 튜플 (best_shift, decrypted_message)
                 best_shift는 가장 많은 유효 단어를 생성한 시프트 값이고,
                 decrypted_message는 해당 시프트로 복호화된 문자열입니다.
        '''
        word_list = self.get_valid_words()
        best_shift = 0
        max_valid_words = -1
        decrypted_message = ""

        # 가능한 모든 shift (0부터 25)를 시도합니다.
        for shift in range(26):
            # 복호화 시프트는 (26 - shift) 입니다.
            # apply_shift 메서드를 사용하면, 복호화는 26 - shift 만큼 암호화하는 것과 같습니다.
            decryption_shift = 26 - shift

            # 주어진 shift로 메시지 복호화 시도
            decrypted_text = self.apply_shift(decryption_shift)

            # 복호화된 텍스트에서 유효한 단어의 개수를 계산합니다.
            words = decrypted_text.split(' ')
            valid_word_count = 0
            for word in words:
                if is_word(word_list, word):
                    valid_word_count += 1

            # 현재까지의 최대 유효 단어 수와 비교합니다.
            if valid_word_count > max_valid_words:
                max_valid_words = valid_word_count
                best_shift = shift  # 이 shift는 암호화 시의 shift (0~25)를 의미합니다.
                decrypted_message = decrypted_text

        return (best_shift, decrypted_message)


if __name__ == '__main__':
    # words.txt 파일을 로드하여 Message 클래스에서 사용할 수 있도록 합니다.
    # Note: 이 코드를 실행하기 전에 words.txt 파일이 동일 폴더에 있어야 합니다.

    # -----------------------------------------------------------------
    # PlaintextMessage 테스트
    # -----------------------------------------------------------------
    print("\n--- PlaintextMessage 테스트 ---")

    # Example test case (PlaintextMessage)
    test_text1 = 'Hello World!'
    shift1 = 4
    plaintext1 = PlaintextMessage(test_text1, shift1)

    # 기대 출력: 'Lipps Asvph!' (H->L, e->i, l->p, o->s. W->A, r->s, l->p, d->h)
    expected_output1 = 'Lipps Asvph!'

    print(f"Original Text: {test_text1}")
    print(f"Shift Value: {shift1}")
    print(f"Expected Output: {expected_output1}")
    print(f"Actual Encrypted Text: {plaintext1.get_message_text_encrypted()}")
    print("-" * 30)

    # Change Shift Test
    new_shift = 10
    plaintext1.change_shift(new_shift)

    # 기대 출력: 'Rovvy Gybvn!' (H->R, e->o, l->v, o->y. W->G, o->y, r->b, l->v, d->n)
    expected_output2 = 'Rovvy Gybvn!'

    print(f"Original Text: {test_text1}")
    print(f"New Shift Value (Changed): {new_shift}")
    print(f"Expected Output: {expected_output2}")
    print(f"Actual Encrypted Text: {plaintext1.get_message_text_encrypted()}")
    print("-" * 30)

    # Custom test case (PlaintextMessage)
    test_text3 = "Python is Fun."
    shift3 = 7
    plaintext3 = PlaintextMessage(test_text3, shift3)

    # 기대 출력: 'Wfawvu pz Mah.' (P->W, y->f, t->a, ...)
    print(f"Original Text: {test_text3}")
    print(f"Shift Value: {shift3}")
    print(f"Actual Encrypted Text: {plaintext3.get_message_text_encrypted()}")
    print("-" * 30)

    # -----------------------------------------------------------------
    # CiphertextMessage 테스트
    # -----------------------------------------------------------------
    print("\n--- CiphertextMessage 테스트 ---")

    # Example test case (CiphertextMessage)
    # 'jgnnq'는 shift=2로 암호화된 'hello'입니다. (h->j, e->g, l->n, l->n, o->q)
    # 따라서 복호화 시프트는 26 - 2 = 24가 최적입니다.
    ciphertext_text2 = 'jgnnq'
    ciphertext2 = CiphertextMessage(ciphertext_text2)
    decrypted_shift2, decrypted_text2 = ciphertext2.decrypt_message()

    print(f"Encrypted Text: {ciphertext_text2}")
    # 원본 shift는 2였으므로, 복호화가 성공적으로 이루어졌다면 원본 shift를 반환해야 합니다.
    print(f"Expected Output (Original Shift, Decrypted Text): (2, 'hello')")
    print(f"Actual Output: ({decrypted_shift2}, '{decrypted_text2}')")
    print("-" * 30)

    # Custom test case (CiphertextMessage)
    # 위에서 암호화한 'Wfawvu pz Mah.'를 복호화 시도 (shift=7로 암호화됨)
    ciphertext_text4 = plaintext3.get_message_text_encrypted()  # 'Wfawvu pz Mah.'
    ciphertext4 = CiphertextMessage(ciphertext_text4)
    decrypted_shift4, decrypted_text4 = ciphertext4.decrypt_message()

    print(f"Encrypted Text: {ciphertext_text4}")
    print(f"Expected Output (Original Text): {test_text3}")
    print(f"Actual Output: ({decrypted_shift4}, '{decrypted_text4}')")
    print("-" * 30)

    # =================================================================
    # TODO: 실제 스토리 해독
    # =================================================================
    print("\n--- 실제 스토리 해독 ---")

    encrypted_story = get_story_string()
    story_cipher = CiphertextMessage(encrypted_story)

    # 최적의 shift 값을 찾아 스토리를 해독한다.
    best_shift, unencrypted_story = story_cipher.decrypt_message()

    print(f"Encrypted Story (Snippet): {encrypted_story[:50]}...")
    print(f"Best shift found: {best_shift}")
    print(f"Unencrypted Story:\n{unencrypted_story}\n")