import sys
import mcb185 

path = sys.argv[1]
orf_min_length = sys.argv[2]

def list_of_starts(seq, frame):
	starts = [] 
	w = 3 
	if frame == 1:
		for i in range(0, len(seq) -w +1, w):
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1)
	if frame == 2:
		for i in range(1, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1)
	if frame == 3:
		for i in range(2, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1)
	return starts

def list_of_stops(seq, frame):
	stops = [] 
	w = 3 
	if frame == 1:
		for i in range(0, len(seq) -w +1, w):
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3)
	if frame == 2:
		for i in range(1, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3)
	if frame == 3:
		for i in range(2, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3)
	return stops
    
def best_start_stop(starts, stops):
	cds_dict = {} 
	prev_stop = 0
	for stop in stops:
		best_start = float('inf')
		for start in starts:
			if start > prev_stop and start < stop and start < best_start:
				best_start = start
		prev_stop = stop  
		if best_start == float('inf'): 
			continue
		else:
			cds_dict[best_start] = stop

	for start in starts:
		if start > stops[-1]:
			cds_dict[start] = ' to the end of seq'
			return cds_dict
	return cds_dict	

def orf_filter(cds_dict, orf_min_length, seq):
	filtered_dict = {} 
	for start, stop in cds_dict.items():
		if type(stop) == int:
			length = int(stop) - int(start) + 1 
			if length >= int(orf_min_length): 
				filtered_dict[start] = stop 
		elif type(stop) == str:
			length = len(seq) - int(start) + 1
			if length >= int(orf_min_length):
				filtered_dict[start] = len(seq)

	return filtered_dict


cds_all_frames = {} 


seq_length = 0

for i in range(1, 4):
	for defline, seq in mcb185.read_fasta(path):
		seq_length = len(seq)
		starts = list_of_starts(seq, i)
		stops = list_of_stops(seq, i)
		cds = best_start_stop(starts, stops)
		cds = orf_filter(cds, orf_min_length, seq)
		cds_all_frames[i] = cds 

for i in range(1, 4):
	for defline, seq in mcb185.read_fasta(path):
		seq = mcb185.anti_seq(seq) 
		starts = list_of_starts(seq, i)
		stops = list_of_stops(seq, i)
		cds = best_start_stop(starts, stops)
		cds = orf_filter(cds, orf_min_length, seq)
		cds_all_frames[-i] = cds 

print('frame\tCDS\tstart\tstop')

for frame_number, cds_in_frame in cds_all_frames.items(): 
	cds_number = 1
	for start, stop in cds_in_frame.items():
		if frame_number < 0:
			adj_start = seq_length-stop 
			adj_stop = seq_length-start
			print(f'{frame_number}\t{cds_number}\t{adj_start}\t{adj_stop}')
		elif frame_number > 0:
			print(f'{frame_number}\t{cds_number}\t{start}\t{stop}')
		cds_number += 1