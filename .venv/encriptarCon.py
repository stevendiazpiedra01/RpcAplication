import chilkat2

crypt = chilkat2.Crypt2()
crypt.CryptAlgorithm = "des"
crypt.CipherMode = "cbc"
crypt.KeyLength = 64
crypt.PaddingScheme = 0
crypt.EncodingMode = "hex"
ivHex = "0001020304050607"
crypt.SetEncodedIV(ivHex,"hex")
keyHex = "0001020304050607"
crypt.SetEncodedKey(keyHex,"hex")