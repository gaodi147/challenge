
def hex_xor(hexstring1,hexstring2):
    return "".join([chr(int(x,16)^int(y,16)).encode('hex')[1] for (x,y) in zip(hexstring1,hexstring2)])


if __name__=='__main__':
    hexstring1='1c0111001f010100061a024b53535009181c'
    hexstring2='686974207468652062756c6c277320657965'
    #746865206b696420646f6e277420706c6179
    print hex_xor(hexstring1,hexstring2)