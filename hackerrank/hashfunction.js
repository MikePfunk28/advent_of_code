// Importing 'crypto' module
const crypto = require('crypto'),

    // Returns the names of 
    // supported hash algorithms
    // such as SHA1,MD5
    hash = crypto.getHashes();

// Create hash of SHA1 type
x = "Geek"

// 'digest' is the output 
// of hash function containing
// only hexadecimal digits
hashPwd = crypto.createHash('sha1')
    .update(x).digest('hex');

console.log(hashPwd);




function stringToHash(string) {
    let hash = 0;

    if (string.length === 0) return hash;

    for (const char of string) {
        hash ^= char.charCodeAt(0); // Bitwise XOR operation
    }

    return hash;
}

// String printing in hash
const gfg = "Bitwise XOR operation, I am a question with many words and answers in json.";
console.log(stringToHash(gfg));
