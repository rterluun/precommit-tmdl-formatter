import argparse
from os import path as os_path

from tmdl_format_column_names.replace_column_name import rename_columns
from tmdl_format_column_names.replace_column_name_references import (
    get_column_names,
    rename_column_names_in_measure_file,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        "--quote-columns",
        dest="quote_columns",
        action="store_true",
    )
    parser.add_argument(
        "--no-quote-columns",
        dest="quote_columns",
        action="store_false",
    )
    parser.add_argument(
        "--ignore-columns-starting-with",
        dest="ignore_columns_starting_with",
        default=None,
    )

    parser.add_argument(
        "--preserved-words",
        dest="preserved_words",
        default=None,
    )
    args = parser.parse_args()

    for filename in args.filenames:

        try:
            directory_name = os_path.dirname(filename)

            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            new_content = rename_columns(
                content=content,
                quote_columns=args.quote_columns,
                ignore_columns_starting_with=args.ignore_columns_starting_with,
                preserved_words=args.preserved_words,
            )

            column_names = get_column_names(content=new_content)

            # Write the updated content back to the file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(new_content)

            # Update the measures file
            try:
                measures_file = os_path.join(directory_name, "_measures.tmdl")

                with open(measures_file, "r", encoding="utf-8") as file:
                    measures_content = file.read()

                new_measures_content = rename_column_names_in_measure_file(
                    content=measures_content,
                    column_names=column_names,
                )

                with open(measures_file, "w", encoding="utf-8") as file:
                    file.write(new_measures_content)

            except FileNotFoundError as e:
                print(f"Error opening measures file: {e}")
                continue

        except FileNotFoundError as e:
            print(f"Error processing file '{filename}': {e}")


if __name__ == "__main__":
    main()
