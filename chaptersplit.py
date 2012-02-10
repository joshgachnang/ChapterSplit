import os
import subprocess

# Install pdftk first!!!!

# File format:

# Original_File_Name.pdf
# New_File_Base_ (Will have section name and .pdf attached)
# New file name, page_start page_end

# Example:
# SuperBook.pdf
# SuperBook_
# Chapter 1, 1 15

# Another example using multiple sections (for example, chapter 1 plus chapter 1 answers)
# SuperBook.pdf
# SuperBook_
# Chapter 1, 1 15, 1004 1006

def split(filename):
	if not os.path.exists(filename):
		raise IOError("Sections file %s doesn't exist." % filename)
	with open(filename, 'r') as f:
		lines = f.readlines()
		original_filename = lines[0].strip()
		new_filename = lines[1].strip()
		if new_filename == None or original_filename == None:
			raise SyntaxError("Original filename or new filename incorrect")
		if not os.path.exists(original_filename.strip()):
			raise IOError("Original file %s doesn't exist." % original_filename)
		
		for line in lines[2:]:
			section_name = line.strip().split(',')[0].replace(' ', '_')
			command = 'pdftk %s cat ' % original_filename
			for section in line.strip().split(',')[1:]:
				command += section.strip().replace(' ', '-')
				command += ' '
			command += 'output %s%s.pdf' % (new_filename, section_name)
			print "Creating%s%s.pdf" % (new_filename, section_name)
			subprocess.call(command, shell=True)