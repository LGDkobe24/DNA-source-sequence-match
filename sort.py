import time

def r_sort(sources, R1, R2):
	fin_r1 = open(R1,'r')
	fin_r2 = open(R2,'r')
	cnt_ourter = 0
	cnt_inner = 0
	line_rem_r1 = ''
	line_rem_r2 = ''
	for line in fin_r1:
		if cnt_ourter % 4 == 0:
			cnt_inner = 0
			if line_rem_r1 == '':
				pass
			elif source in sources:
				#print '/'.join(target.split('/')[0:-1]) + source + '.txt'
				fout = open(R1.split('.')[0] + '.' + source + '.txt','a')
				fout.write(line_rem_r1)
				fout.close()
				fout = open(R2.split('.')[0] + '.' + source + '.txt','a')
				fout.write(line_rem_r2)
				fout.close()
			line_rem_r1 = ''
			line_rem_r2 = ''
		cnt_ourter = cnt_ourter + 1
		cnt_inner = cnt_inner + 1
		line_rem_r1 = line_rem_r1 + line
		line_rem_r2 = line_rem_r2 + fin_r2.readline()
		if cnt_inner == 2:
			source = line.strip()[0:6]
	fin_r1.close()
	fin_r2.close()

if __name__ == "__main__":
	sources = [u'CTCACA',u'TACTGC',u'ATCAGC',u'CGACTA',u'CGTCAT',u'CTCGAT', \
	u'TAGCAC',u'TCTAGC',u'CACGTA',u'ATGCTC',u'GCTACA',u'GCATCT']
	R1 = '/Users/ff/Desktop/match/R1.txt'
	R2 = '/Users/ff/Desktop/match/R2.txt'
	r_sort(sources, R1, R2)