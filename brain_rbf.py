# Inputs:
# 5 for first antennae, i.e. antennae_angles[0]
# 0: Object detection, 1 if detected 0 if not
# 1: R 0 - 1
# 2: G 0 - 1
# 3: B 0 - 1
# 4: Object detection 2...
from funcs import gaussian as gauss
from funcs import transfer

class BrainRBF(object):
	"""docstring for Brain"""
	G_INPUTNODES = 8
	G_TOTAL_CONNECTIONS = 36 # 12 calls * 3 genes
	G_GENES_NEEDED = G_TOTAL_CONNECTIONS + 3
	G_REGION_SIZE = 3

	def __init__(self, genes=None):
		if genes is not None:
			self.import_genes(genes)

	def think(self, data):
		self.gene_index = 0
		rbf = self.rbf

		if data[0] == 0 and data[4] == 0:
			return (0.005, 0)
		
		else:
			if data[0] == 1:
				left = (rbf(data[1]) + rbf(data[2]) + rbf(data[3]),
					rbf(data[1]) + rbf(data[2]) + rbf(data[3]))
			else:
				self.gene_index += self.G_TOTAL_CONNECTIONS / 2
				left = (0,0)

			if data[4] == 1:
				right = (rbf(data[5]) + rbf(data[6]) + rbf(data[7]),
					rbf(data[5]) + rbf(data[6]) + rbf(data[7]))
			else:
				right = (0,0)

			return (transfer(left[0] + right[0]), transfer(left[1] + right[1]))

	def rbf(self, data):
		self.gene_index += 3
		return self.genes[self.gene_index-3] * gauss(data, (self.genes[self.gene_index - 2] + 1) / 2, (self.genes[self.gene_index - 1] + 1) / 2)
	
	# assuming that the last three genes are not used
	def import_genes(self, genes):
		#self.genes = genes[0:-3]
		self.genes = genes

	def diagnose(self):
		print "No diagnosis for RBF yet"
