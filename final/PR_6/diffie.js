function getKey() {
    const p = BigInt(document.getElementById("txtP").value);
    const g = BigInt(document.getElementById("txtG").value);

    const a = 6n;  // Alice's private key
    const b = 15n; // Bob's private key

    // Public keys
    const A = modPow(g, a, p); // Alice sends this to Bob
    const B = modPow(g, b, p); // Bob sends this to Alice

    // Shared secrets
    const AS = modPow(B, a, p); // Alice computes
    const BS = modPow(A, b, p); // Bob computes

    document.getElementById("txtASecret").value = AS.toString();
    document.getElementById("txtBSecret").value = BS.toString();
}

// Modular exponentiation function: (base^exp) % mod
function modPow(base, exp, mod) {
    let result = 1n;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2n === 1n) {
            result = (result * base) % mod;
        }
        exp = exp / 2n;
        base = (base * base) % mod;
    }
    return result;
}
