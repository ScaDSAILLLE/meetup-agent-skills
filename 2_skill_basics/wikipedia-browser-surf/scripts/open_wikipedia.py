#!/usr/bin/env python3
import argparse
import os
import platform
import subprocess
from urllib.parse import quote_plus


def build_url(topic: str | None, language: str) -> str:
    lang = (language or "en").strip().lower()
    if not lang.isalpha() or len(lang) < 2 or len(lang) > 8:
        lang = "en"

    if not topic:
        return (
            "https://www.wikipedia.org"
            if lang == "en"
            else f"https://{lang}.wikipedia.org/"
        )

    return (
        f"https://{lang}.wikipedia.org/wiki/Special:Search?search={quote_plus(topic)}"
    )


def open_in_desktop_browser(url: str) -> None:
    system = platform.system().lower()
    in_wsl = "microsoft" in platform.release().lower() or bool(
        os.getenv("WSL_DISTRO_NAME")
    )

    if system == "windows" or in_wsl:
        subprocess.run(["cmd.exe", "/C", "start", "", url], check=False)
        return
    if system == "darwin":
        subprocess.run(["open", url], check=False)
        return

    subprocess.run(["xdg-open", url], check=False)


def run(topic: str | None, language: str) -> None:
    target = build_url(topic, language)
    open_in_desktop_browser(target)
    print(f"Opened in default browser: {target}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Open Wikipedia in the default browser"
    )
    parser.add_argument("--topic", help="Topic to search on Wikipedia", default=None)
    parser.add_argument(
        "--lang",
        default="en",
        help="Wikipedia language code, e.g. en, de, fr. Default: en",
    )

    args = parser.parse_args()
    run(topic=args.topic, language=args.lang)


if __name__ == "__main__":
    main()
