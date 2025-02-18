import argparse

from tmdl_format_column_names.replace_column_name import rename_columns


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        "--quote-columns",
        action="store_true",
    )
    args = parser.parse_args()

    for filename in args.filenames:

        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            new_content = rename_columns(
                content=content,
                quote_columns=args.quote_columns,
            )

            # Write the updated content back to the file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(new_content)

        except FileNotFoundError as e:
            print(f"Error processing file '{filename}': {e}")


if __name__ == "__main__":
    main()
