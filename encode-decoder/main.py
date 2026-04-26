import argparse
from encoder import base64_enc, base32_enc, hex_enc, url_enc
from detector.detect import detect_format


def main():
    parser = argparse.ArgumentParser(description="Multi-format Encoder/Decoder")

    parser.add_argument("action", choices=["encode", "decode", "detect", "interactive"])
    parser.add_argument("format", nargs="?", help="base64 | base32 | hex | url")
    parser.add_argument("input", nargs="?", help="Input string")

    args = parser.parse_args()

    # ------------------ INTERACTIVE ------------------
    if args.action == "interactive":
        while True:
            data = input("Enter text (or 'exit'): ")
            if data.lower() == "exit":
                break
            print("Detected:", detect_format(data))
        return

    # ------------------ DETECT (FIXED) ------------------
    if args.action == "detect":
        # handle both cases:
        # python main.py detect data
        # python main.py detect format data
        data = args.input if args.input else args.format

        if not data:
            print("❌ Please provide input to detect")
            return

        print("Detected:", detect_format(data))
        return

    # ------------------ VALIDATION ------------------
    if not args.format or not args.input:
        print("❌ Format and input required")
        return

    fmt = args.format.lower()
    data = args.input

    # ------------------ ENCODE ------------------
    if args.action == "encode":
        if fmt == "base64":
            print(base64_enc.encode(data))
        elif fmt == "base32":
            print(base32_enc.encode(data))
        elif fmt == "hex":
            print(hex_enc.encode(data))
        elif fmt == "url":
            print(url_enc.encode(data))
        else:
            print("❌ Unsupported format")

    # ------------------ DECODE ------------------
    elif args.action == "decode":
        if fmt == "base64":
            print(base64_enc.decode(data))
        elif fmt == "base32":
            print(base32_enc.decode(data))
        elif fmt == "hex":
            print(hex_enc.decode(data))
        elif fmt == "url":
            print(url_enc.decode(data))
        else:
            print("❌ Unsupported format")


if __name__ == "__main__":
    main()
