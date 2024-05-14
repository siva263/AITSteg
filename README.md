## Features
- Protect your invisible secret using passwords
- Cryptographically secure by encrypting the invisible secret using AES-256-CTR encryption and decryption.
- Uses Invisible characters in unicode characters that works everywhere in the web - Tweets, Gmail, WhatsApp, Telegram, Instagram, Facebook, and many more!
- Completely invisible, uses Zero Width Characters instead of white spaces or tabs.
- The secret message which is encrpted using password can be embedded in the cover message by the sender and extracted from the cover message and decrypted using the same password by the receiver.

<br>

## Functions implemented
- Embed algorithm: To embed the secret message into the cover message by converting it into invisible zero width unicode characters.
- Extract algorithm: To extract the secret message from the cover message by converting it back into ascii characters from invisible zero width unicode characters.
- AES-encryption: We take password for encrypting the secret message before embeding it,the key for encryption is generated from the password based key derivation function PBKDF2.
- AES-decryption: For decrpytion,we need to pass the same password used while encryption since AES-256 is a symmetric cipher.

#### Installation
Install the dependency for AES by running:
```html  
    pip install pycryptodomex
```

#### Run using Command Prompt
Clone the repository and run the following commands-
```html
    set FLASK_ENV=development
    set FLASK_APP=app.py
    flask run
```

###             Tech stack
`Backend` : Python3,Flask  <br>
`Frontend` : Html,CSS  <br>


