from pathlib import Path

# “Bottykins” turns bot into a warm, grandma-like pet name with the joke built in.
# Unlike “Robot,” “Alexa,” or “Siri,” it sounds personal, playful, and freshly coined.
WORD = "Bottykins"


def main():
    try:
        encoded = WORD.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ValueError("entry must be valid UTF-8") from error

    if not 1 <= len(WORD) <= 30:
        raise ValueError("entry must contain 1 to 30 characters")
    if not WORD or any(character.isspace() for character in WORD):
        raise ValueError("entry must be a single word with no whitespace")

    encoded.decode("utf-8")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(encoded)


if __name__ == "__main__":
    main()
