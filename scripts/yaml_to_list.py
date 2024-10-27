import sys

import yaml


def yaml_to_list(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    domains = [item.lstrip("+.") for item in data.get("payload", [])]
    with open(output_file, "w", encoding="utf-8") as file:
        for domain in domains:
            file.write(f"{domain}\n")
    print(f"Processed List file saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    yaml_to_list(input_file, output_file)
