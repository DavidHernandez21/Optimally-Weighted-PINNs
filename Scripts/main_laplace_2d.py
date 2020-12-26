import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from NeuralNetwork import NeuralNetwork
from PDEs.Laplace_2d import Laplace_2d
from Enums import ActivationFunction, TrainMode
from csv_writter.write_csv_for_plotting import csv_plot_3d_or_2d
from utilities.plotting import savefig


def main():
    # Create Neural Network
    network = NeuralNetwork(inputDimension=2, hiddenLayers=[20, 20, 20, 20], activationFunction=ActivationFunction.Tanh)

    # Load weights
    # network.LoadWeights(path)

    # Create PDE
    laplace = Laplace_2d(frequency=6 * np.pi, network=network)

    # Train
    # laplace.Train(trainMode=TrainMode.DefaultAdaptive, iterations=20000)
    # laplace.Train(trainMode=TrainMode.OptimalAdaptive, iterations=20000)
    laplace.Train(trainMode=TrainMode.MagnitudeAdaptive, iterations=20000)

    # Store weights
    # network.SaveWeights(path)

    laplace.ComputeL2Error()
    laplace.ComputeMaxError()

    # region Plots
    # Surface plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x, y, z = laplace.GetInteriorPlotData(pointCount=5000, tensor=network.yInt, x=[(0, 1), (0, 1)])
    csv_plot_3d_or_2d(x, y, z=z, csv_name='surface_plot_3d.csv')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$u$")

    # Boundary conditions
    color = next(ax._get_lines.prop_cycler)['color']
    x, y, z = laplace.GetBoundaryPlotData(pointCount=1000, tensor=network.boundaryCondition, x=[(0, 1), (0, 1)])
    csv_plot_3d_or_2d(x, y, z=z, csv_name='boundary_plot_3d.csv')
    ax.plot3D(x[0], y[0], z[0], color=color, label="Boundary Condition")
    for i in range(1, len(x)):
        ax.plot3D(x[i], y[i], z[i], color=color)
        
    savefig("figures/surface_plot")

    # Single boundary plot
    plt.figure()
    x, y = laplace.GetInteriorPlotData(pointCount=1000, tensor=network.yInt, x=[(0, 1), 0.25])
    csv_plot_3d_or_2d(x, y, csv_name='interior_plot_2d.csv', single_plot=True)
    plt.plot(x, y, label="Approximated Solution")

    # Boundary conditions
    x, y = laplace.GetBoundaryPlotData(pointCount=1000, tensor=network.boundaryCondition, x=[(0, 1), 0.25])
    csv_plot_3d_or_2d(x, y, csv_name='boundary_plot_2d.csv', single_plot=True)
    plt.scatter(x, y, label="Boundary Condition")

    plt.xlabel("$x_1$")
    plt.ylabel("$u$")
    plt.legend()
    
    savefig("figures/single_boundary_plot")

    plt.show()
    # endregion

    # Cleanup
    network.Cleanup()
