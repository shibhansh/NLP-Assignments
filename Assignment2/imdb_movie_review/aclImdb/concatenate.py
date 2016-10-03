import glob

read_files = glob.glob("train/neg/*.txt")

with open("train_neg.txt", "wb") as outfile:
	for f in read_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
		outfile.write("\n")

outfile.close()
read_files = glob.glob("train/pos/*.txt")

with open("train_pos.txt", "wb") as outfile:
	for f in read_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
		outfile.write("\n")

outfile.close()
read_files = glob.glob("test/neg/*.txt")

with open("test_neg.txt", "wb") as outfile:
	for f in read_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
		outfile.write("\n")

outfile.close()
read_files = glob.glob("test/pos/*.txt")

with open("test_pos.txt", "wb") as outfile:
	for f in read_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
		outfile.write("\n")

outfile.close()