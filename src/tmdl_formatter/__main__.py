import argparse

from tmdl_formatter.measures.sorting import extract_measures, replace_measures, sort_measures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print(args)

    # for filename in args.filenames:
    #     with open(filename, "r") as file:
    #         content = file.read()

    #     # Extract measures from the file
    #     measures = extract_measures(content=content)

    #     # Sort the measures
    #     sorted_measures = sort_measures(measures=measures)

    #     # Replace the measures in the file
    #     new_content = replace_measures(content=content, measures=sorted_measures)

    #     # Write the updated content back to the file
    #     with open(filename, "w") as file:
    #         file.write(new_content)


if __name__ == "__main__":
    main()
