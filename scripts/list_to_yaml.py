import sys


def list_to_yaml(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        domains = [f"+.{line.strip()}" for line in file if line.strip()]
    yaml_content = "payload:\n" + "\n".join(f"  - {domain}" for domain in domains)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(yaml_content)
    print(f"Processed YAML file saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    list_to_yaml(input_file, output_file)
