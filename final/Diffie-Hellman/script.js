function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function checkPrime() {
    const p = parseInt(document.getElementById("prime").value);
    if (isPrime(p)) {
        document.getElementById("primeMessage").innerText = `${p} is a prime number.`;
        document.getElementById("generatorSection").style.display = "block";
    } else {
        document.getElementById("primeMessage").innerText = `${p} is not a prime number. Enter a valid prime.`;
        document.getElementById("generatorSection").style.display = "none";
    }
}

function isPrimitiveRoot(g, p) {
    let results = new Set();
    for (let i = 1; i < p; i++) {
        results.add(Math.pow(g, i) % p);
    }
    return results.size === p - 1;
}

function checkGenerator() {
    const g = parseInt(document.getElementById("generator").value);
    const p = parseInt(document.getElementById("prime").value);
    
    if (isPrimitiveRoot(g, p)) {
        document.getElementById("generatorMessage").innerText = `${g} is a valid generator for ${p}.`;
        document.getElementById("usersSection").style.display = "flex";
    } else {
        document.getElementById("generatorMessage").innerText = `${g} is NOT a valid generator for ${p}. Try another.`;
        document.getElementById("usersSection").style.display = "none";
    }
}

let alicePublicKey, bobPublicKey;

function computePublicKey(user) {
    const p = parseInt(document.getElementById("prime").value);
    const g = parseInt(document.getElementById("generator").value);
    const privateKey = parseInt(document.getElementById(user + "Private").value);

    if (privateKey >= p) {
        alert(`Private key must be less than ${p}`);
        return;
    }

    const publicKey = Math.pow(g, privateKey) % p;
    document.getElementById(user + "Public").innerText = `Public Key: ${publicKey}`;

    if (user === "alice") alicePublicKey = publicKey;
    else bobPublicKey = publicKey;

    if (alicePublicKey && bobPublicKey) {
        document.getElementById("sharePublicKeySection").style.display = "block";
    }
}

function sharePublicKeys() {
    document.getElementById("bobPublicOnAlice").innerText = bobPublicKey;
    document.getElementById("alicePublicOnBob").innerText = alicePublicKey;
    document.getElementById("shareKeySection").style.display = "block";
}

function computeSecretKey() {
    const p = parseInt(document.getElementById("prime").value);
    const alicePrivateKey = parseInt(document.getElementById("alicePrivate").value);
    const bobPrivateKey = parseInt(document.getElementById("bobPrivate").value);

    const aliceSharedSecretKey = Math.pow(bobPublicKey, alicePrivateKey) % p;
    const bobSharedSecretKey = Math.pow(alicePublicKey, bobPrivateKey) % p;

    document.getElementById("aliceSharedKey").innerText = aliceSharedSecretKey;
    document.getElementById("bobSharedKey").innerText = bobSharedSecretKey;
}
