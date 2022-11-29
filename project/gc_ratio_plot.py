import random
from matplotlib import pyplot as plt


def get_gc_ratio(genomic_data: str) -> int:
    ratio = (genomic_data.count('G') + genomic_data.count('C')) / len(genomic_data)
    return int(100 * ratio)


def plot_gc_content(genomic_data: str, step: int = 100, image_file_name: str = 'gc_content'):
    windows = [genomic_data[i:i+step] for i in range(0, len(genomic_data), step)]
    genome_positions = []
    gc_ratios = []
    for i, window in enumerate(windows):
        genome_positions.append((i + 1) * step)
        gc_ratios.append(get_gc_ratio(window))

    plt.plot(genome_positions, gc_ratios)
    plt.title('GC-content distribution')
    plt.xlabel('Genome position')
    plt.ylabel('GC-content(%)')
    # plt.show()
    plt.savefig(f'images/{image_file_name}.png')
    plt.clf()


if __name__ == '__main__':
    sars_genomic_data = ''
    with open('data/genomic.fna') as f:
        for line in f.readlines():
            sars_genomic_data += line.strip()

    plot_gc_content(sars_genomic_data, image_file_name='sars_cov')

    random_genomic_data = ''.join(random.choice('CGTA') for _ in range(5000))
    plot_gc_content(random_genomic_data, 50)
