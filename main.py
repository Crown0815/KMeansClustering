import filereader
import filewriter
import kmeans as clstr
import matplotlib.pyplot as plt


file_reader = filereader.FileReader("places.txt")
data_vector = file_reader.read_file_to_data_points()

kmeans = clstr.KMeans(data_vector, 3)
# kmeans.run()

cluster_centers = kmeans.clusters
clusters = kmeans.cluster_points(cluster_centers)

plt.plot(cluster_centers.get_values(1), cluster_centers.get_values(2), 'x')

kmeans.run()

cluster_centers = kmeans.clusters
clusters = kmeans.cluster_points(cluster_centers)
plt.plot(clusters[0].get_values(1), clusters[0].get_values(2), 'bo')
plt.plot(clusters[1].get_values(1), clusters[1].get_values(2), 'ro')
plt.plot(clusters[2].get_values(1), clusters[2].get_values(2), 'go')
plt.plot(cluster_centers.get_values(1), cluster_centers.get_values(2), 'w*')

indexed = kmeans.cluster_numbered_index(cluster_centers)
file_writer = filewriter.FileReader("results.txt", " ")
file_writer.write_data_clusters_to_file(indexed)

plt.show()





