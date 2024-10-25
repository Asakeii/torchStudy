
def parse_fasta_to_lists(fasta_file_path):
    odd_lines = []
    even_lines = []
    with open(fasta_file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 0:  # Python索引从0开始，所以奇数行实际上是偶数索引
                odd_lines.append(line)
            else:
                even_lines.append(line)
    return odd_lines, even_lines

def save_lines_to_file(lines, output_file_path):
    with open(output_file_path, 'w') as file:
        file.writelines(lines)

# def main():
#     # 替换为你的FASTA文件的实际路径
#     fasta_file_path = r'C:\Users\21651\Downloads\Archaea_results_rep_seq.fasta'
#
#     # 解析FASTA文件并将奇数行和偶数行分别保存到两个列表中
#     odd_lines, even_lines = parse_fasta_to_lists(fasta_file_path)
#
#     # 定义输出文件的路径
#     odd_file_path = 'odd_lines.fasta'
#     even_file_path = 'even_lines.fasta'
#
#     # 将奇数行保存到一个新文件
#     save_lines_to_file(odd_lines, odd_file_path)
#
#     # 将偶数行保存到另一个新文件
#     save_lines_to_file(even_lines, even_file_path)
#
#     print(f"Odd lines saved to {odd_file_path}")
#     print(f"Even lines saved to {even_file_path}")


def extract_cluster_ids_from_fasta(fasta_file_path):
    cluster_ids = []
    with open(fasta_file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                parts = line.strip().split('|')
                if len(parts) > 3:
                    cluster_id = parts[-1].strip()
                    cluster_ids.append(cluster_id)
    return cluster_ids


def save_cluster_ids(cluster_ids, output_file_path):
    with open(output_file_path, 'w') as file:
        for cluster_id in cluster_ids:
            file.write(cluster_id + '\n')


def main():
    # 替换为你的.fasta文件的实际路径
    fasta_file_path = 'odd_lines.fasta'
    cluster_ids = extract_cluster_ids_from_fasta(fasta_file_path)

    # 定义输出文件的路径
    output_file_path = 'cluster_ids.txt'

    # 将聚类编号保存到一个新文件
    save_cluster_ids(cluster_ids, output_file_path)

    print(f"Cluster IDs have been saved to {output_file_path}")


if __name__ == "__main__":
    main()
