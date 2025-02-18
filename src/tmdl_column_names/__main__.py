import argparse

from tmdl_column_names.replace_column_name import rename_columns


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    for filename in args.filenames:

        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            new_content = rename_columns(content=content)

            # Write the updated content back to the file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(new_content)

        except FileNotFoundError as e:
            print(f"Error processing file '{filename}': {e}")


if __name__ == "__main__":
    main()
