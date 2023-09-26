# Given 
1. File: path, size
2. Directories: Collection<File> no nested hierarchy

# Expected
Report: Total size of all files: lookup all files mapped to directories as well as unmapped
TopK Collections by size: sorted by size collection of directories(TreeSet)

# Scratchpad
Map
filename to size

Map
collectionname collectionsize


file1.txt(size: 100)
file2.txt(size: 200) in collection "collection1"
file3.txt(size: 200) in collection "collection1"
file4.txt(size: 300) in collection "collection2"
file5.txt(size: 100)

Top K collections based on size

FileEvent
	name
	size
	taggedToCollection
 
FileCollection implements Comparable
	Set<Files> files;
	int totalSize;

	// add File and update totalSize


FileEventMetricsCalculator
	SortedSet<FileCollection> publishTopKCollections(List<FileEvent> fileEvents) {
		SortedSet<FileCollection> sortedFileCollections = new SortedSet<>();
		

	}

FileEvent
	Name, Size, tagToCollection


