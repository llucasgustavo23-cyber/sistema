# app/security/crypto.py
import base64
import hmac
from hashlib import pbkdf2_hmac
from secrets import token_bytes

# Parâmetros recomendados (equilíbrio entre segurança e performance)
ALGO = "sha256"
ITERATIONS = 210_000
SALT_LEN = 16  # 128 bits
DK_LEN = 32    # 256 bits

def hash_password(password: str) -> tuple[str, str, int, str]:
    """
    Retorna (algo, salt_b64, iterations, hash_b64).
    Armazene no banco: algo, iterations, salt, hash.
    """
    if isinstance(password, str):
        password = password.encode("utf-8")
    salt = token_bytes(SALT_LEN)
    dk = pbkdf2_hmac(ALGO, password, salt, ITERATIONS, dklen=DK_LEN)
    return (
        ALGO,
        base64.b64encode(salt).decode("ascii"),
        ITERATIONS,
        base64.b64encode(dk).decode("ascii"),
    )

def verify_password(password: str, algo: str, salt_b64: str, iterations: int, hash_b64: str) -> bool:
    if isinstance(password, str):
        password = password.encode("utf-8")
    salt = base64.b64decode(salt_b64)
    expected = base64.b64decode(hash_b64)
    dk = pbkdf2_hmac(algo, password, salt, int(iterations), dklen=len(expected))
    # Comparação em tempo constante
    return hmac.compare_digest(dk, expected)