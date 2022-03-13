# cypher-encryption.py
Python script to encrypt and decrypt data using dual level of custom defined, random auto-generated key and reference tables.

## Fetching the repo
- Download cypher-encryption [.zip](https://github.com/kxnyshk/cypher-encryption.py/archive/refs/heads/master.zip)
- Unzip the folder.
- Open the [_./dist/cypher/_](https://github.com/kxnyshk/cypher-encryption.py/tree/master/dist/cypher) folder.
- Run the [cypher.exe](https://github.com/kxnyshk/cypher-encryption.py/blob/master/dist/cypher/cypher.exe) application.

## How to use
- Enter your Identity as asked, to proceed further.
- Wait for Cypher.py while it initializes the program for you.

- After Initializing:
  - `Press A`: If you already posess a reference and key to cypher your data.
  - `Press N`: If you want to generate a new reference and key.

- In case, you choose `A`, you will be asked to enter your Reference, Key and the Cyphered data to further proceed to decypher it.

- In case, you chose `N`, you will be asked for:
  - `(N)ew Key`: Generates a New Key and Refrence for your data, to get encrypted.
  - `(G)et Key`: Prints the generated Key and Reference.
  - `(E)ncrypt`: Starts the Encryption process for your data.
  - `(D)ecrypt`: Starts the Decryption process for your data.

- At any time, when you are in the Menu, you can:
  - `Press V`:  To view all the contents of the menu.
  - `Press -1`: To terminate the program.
