import csv

def csv_plot_3d_or_2d(x, y, z=z, csv_name='surface_plot_3d.csv', single_plot=False):
	"""
	writes a csv file with the x, y and if given z values obtained from the laplace object

	:param x: x coordinate values
	:type x: array_like
	:param y: y coordinate values
	:type y: array_like
	:param z: Optional, z coordinate values
	:type z: array_like
	:param csv_name: Default 'surface_plot_3d.csv' 
	                 name of the csv file
	:type csv_name: str
	:param single_plot: plot in 2d
	:type single_plot: bool
	"""


	
	with open(csv_name, 'w', newline="") as csv_file:


		if single_plot:

			fieldnames = ["x", "y"]

			key_x, key_y = zip(fieldnames)

		else:

			fieldnames = ["x", "y", "z"]

			key_x, key_y, key_z = zip(fieldnames)


		
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')


		csv_writer.writeheader()


		
		if not single_plot:

			for x, y, z in zip(x, y, z):

				row = {key_x[0]: x, key_y[0]: y, key_z[0]: z}

				csv_writer.writerow(row)

		else:

			for x, y in zip(x, y):

				row = {key_x[0]: x, key_y[0]: y}

				csv_writer.writerow(row)