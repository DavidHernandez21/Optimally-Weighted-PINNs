# import matplotlib
# matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rc
from Scripts.main_laplace_2d import main as main_laplace_2d
from Scripts.main_laplace_nd import main as main_laplace_nd


print(matplotlib.rcParams['backend'])
plt.rcParams.update({'font.size': 16})
plt.rcParams['figure.figsize'] = [10, 7]
rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})


main_laplace_2d()


# main_laplace_nd()
