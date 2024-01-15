from newsscraper.constants import DATES_MAPPER


def standardize_data(string_data: str) -> str:
    # Ene 13, 2024
    # Remove all special characters
    string_data = "".join(
        [chr for chr in string_data if chr.isalnum() or chr.isspace()]
    )
    month, day, year = string_data.upper().split()
    month = DATES_MAPPER[month]
    return f"{year}-{month}-{day}"
