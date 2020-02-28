


def load_data():
    data = 'ALL_AML_data.txt'
    gene = 'ALL_AML_genes.txt'
    samples = 'ALL_AML_samples.txt'

    # Processes Sample Info
    with open(samples, 'r') as samples_file:
        text = samples_file.read()
    sample_names = text.split()

    # Process Gene Info
    gene_info = []
    with open(gene, 'r') as gene_in_file:
        raw_gene = gene_in_file.readlines()[1:]
    gene_des = {}
    gene_names = []
    for line in raw_gene:
        line = line.strip()
        line = line.split('\t')
        gene_names.append(line[0])
        name = line[0]
        des = line[1]
        gene_des[name] = des

    
    # Process Data File 
    with open(data, 'r') as data_file:
        raw_data = data_file.read()
    formatted_data = []
    data_lines = raw_data.strip().split('\n')

    for line in data_lines:
        element_vals = line.strip().split('\t')
        element_num = []
        for val in element_vals:
            v = float(val)
            element_num.append(v)
        formatted_data.append(element_num)


    
    return sample_names, gene_names, gene_des, formatted_data