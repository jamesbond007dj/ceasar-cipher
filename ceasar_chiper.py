import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()
import random

'''
This is short way to write alphebet, i find it from geekforce web side
'''
alp = [chr(x) for x in range(ord('a'), ord('z')+1)]

print(alp)

def encrypt(plain, key):
    encrypted_pin = ''

    for char in plain:
        if char in alp:
            letter = alp[(alp.index(char.lower())+key)%len(alp)]
            encrypted_pin += letter
        else:
            encrypted_pin += char


    return encrypted_pin

def decrypt(encoded, key):
    return encrypt(encoded, -key)

def decrypt_others(plain):
    def english_words(list_of_words):
        correct_word = 0
        for plain in list_of_words:
            if plain in word_list:
                correct_word += 1
        if correct_word/len(list_of_words) >= 0.5:
            return True
        return False
    for key in range(len(alp)):
        encrypted_other = encrypt(plain, (-1*(key)))
        decrypted_other = english_words(encrypted_other.split(' '))
        if decrypted_other:
            return encrypted_other


if __name__ == '__main__':
    pins = [
        'i take vocation to fifty states at once'
    ]
    chris = """jargtdqnke vcpigpv cpf fgtkxcvkxg\nkv jcu c uvtwevwtg xgta ukoknct vq ukioqkf hwpevkqp. jqygxgt, vjku vkog vjg hwpevkqp ku fghkpgf cu (-1, + 1). vjg cfxcpvcig qxgt vjg ukioqkf hwpevkqp ku vjcv kvu fgtkxcvkxg ku oqtg uvggr, yjkej ogcpu kv ecp igv oqtg xcnwg. vjku ogcpu vjcv kv yknn dg oqtg ghhkekgpv dgecwug kv jcu c ykfgt tcpig hqt hcuvgt ngctpkpi cpf itcfkpi."""
    print ('CODED TEXT FROM CHRIS:' , chris)
    decrypted_chris = decrypt_others(chris)
    print ('DECRYPTED TEXT OF CHRIS:', decrypted_chris)

for  pin in pins:
    key = random.randint(1,26)
    print('MY PLAIN PIN:', pin)
    encrypted_pin = encrypt(pin, key)
    print('MY ENCRYPTED PIN:', encrypted_pin)
    decrypted_pin = decrypt(encrypted_pin, key)
    print('MY DECRYPTED PIN:', decrypted_pin)




