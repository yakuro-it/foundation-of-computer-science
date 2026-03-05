import base64
import binascii
from urllib.parse import quote, unquote
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ascii_bytes_view(s: str) -> list[int]:
    return list(s.encode("utf-8"))

def demo_base64(data: bytes) -> tuple[str, str]:
    enc = base64.b64encode(data).decode("ascii")
    dec = base64.b64decode(enc).decode("utf-8")
    return enc, dec

def demo_hex(data: bytes) -> tuple[str, str]:
    enc = binascii.hexlify(data).decode("ascii")
    dec = binascii.unhexlify(enc).decode("utf-8")
    return enc, dec

def demo_url_encoding(s: str) -> tuple[str, str]:
    enc = quote(s, safe="")
    dec = unquote(enc)
    return enc, dec

def build_mime_message_preview(sender: str, receiver: str) -> str:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Demo: Base64 inside MIME (protected by TLS in real SMTP)"

    body = MIMEText(
        "This is a demo email body.\n"
        "In real email, attachments can be Base64 encoded for transport.\n"
        "TLS protects the channel during SMTP transmission.",
        "plain"
    )
    msg.attach(body)
    return msg.as_string()

if __name__ == "__main__":
    sample_text = "Confidential report: StudentID=1001 & Fee=20.50"
    sample_bytes = sample_text.encode("utf-8")

    print("=== TASK 1: Encoding Format Demonstration ===\n")

    print("Original text:")
    print(sample_text)
    print("\nASCII/UTF-8 bytes view:")
    print(ascii_bytes_view(sample_text))

    b64_enc, b64_dec = demo_base64(sample_bytes)
    print("\n--- Base64 ---")
    print("Encoded:", b64_enc)
    print("Decoded:", b64_dec)

    hex_enc, hex_dec = demo_hex(sample_bytes)
    print("\n--- Hexadecimal ---")
    print("Encoded:", hex_enc)
    print("Decoded:", hex_dec)

    url_enc, url_dec = demo_url_encoding(sample_text)
    print("\n--- URL Encoding ---")
    print("Encoded:", url_enc)
    print("Decoded:", url_dec)

    print("\n=== MIME Message Preview (conceptual SMTP + Base64 usage) ===")
    print(build_mime_message_preview("sender@example.com", "receiver@example.com"))
