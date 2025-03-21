import sys
import gzip
import mcb185
import itertools

def kmer_finder(seq, k):
	kmers = {}
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1
	
	rev_comp = mcb185.anti_seq(seq)
	for i in range(len(rev_comp) -k +1):
		kmer = rev_comp[i:i+k]
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1 
	return kmers

def kmer_checker(kmers_dict, k):
	possible_kmers = 4**k
	found_kmers = len(list(kmers_dict.keys()))
	if possible_kmers == found_kmers: return False
	else: return True 

def check_kmer_until_missing(seq):
	missing_kmer_list = []
	missing = False
	k = 1
	while missing == False:
		kmer_dict = kmer_finder(seq, k)
		missing = kmer_checker(kmer_dict, k)
		if missing == True:
			for nts in itertools.product('ACGT', repeat=k):
				kmer = ''.join(nts)
				if kmer not in kmer_dict.keys():
					missing_kmer_list.append(kmer)
		k += 1
	return missing_kmer_list

def kmer_checker(path):
	with gzip.open(path, 'rt') as file:
		for defline, seq in mcb185.read_fasta(path):
			final_missing_kmer = check_kmer_until_missing(seq)
			print(defline)
			for missing_k in final_missing_kmer:
				print(missing_k)


path = sys.argv[1]
kmer_checker(path)
