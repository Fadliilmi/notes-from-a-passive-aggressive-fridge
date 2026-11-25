from pathlib import Path

NOTE = "You've opened me nine times tonight and chosen nothing; the rendang is now in a committed relationship with the yogurt."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(NOTE, encoding="utf-8")


if __name__ == "__main__":
    main()
