import matplotlib.pyplot as plt
import numpy as np

""" x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained")
ax1.plot(x, y, label="Kurve")
ax1.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
ax1.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
ax1.legend(loc="best")

ax2.plot(x, y, label="Kurve")
ax2.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
ax2.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
ax2.legend(loc="best")
#fig.savefig("build/plot.pdf") """




#Lineare Regression
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16

# load data
x, y = np.genfromtxt("daten.txt", unpack=True)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, "k.", label="example data")
ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")




x_plot = np.linspace(0, 20)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, "k.", label="Messwerte")
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label="Lineare Regression",
    linewidth=1,
    color="tab:orange",
)

ax.legend()
ax.set(xlabel=r"$\Delta x$", ylabel=r"$\symbf{F}(N)$");



fig.savefig("build/plot.pdf")









""" #Curve fit

#includs curve fit
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp


def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unc.correlated_values(popt, pcov)


def f(x, a, b):
    return a * x + b


# Generate data
#length = 100
#x = np.linspace(0,3 * np.pi, length)
#rng = np.random.default_rng(seed=42)
#y1 = rng.normal(0.0, 0.2, length)
#y2 = np.abs(rng.normal(0.0, 0.2, length))

y = f(x, 1, 1) 



# Solution
x, y_0 = np.genfromtxt("daten.txt", unpack=True)
#y = unp.uarray(y_0, y_err)
params = ucurve_fit(f, x, y)
print("a * x + b")
for char, p in zip("ab", params):
    print(f"{char} = {p}")

fig = plt.figure(layout="constrained")
ax = fig.add_subplot()
#ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
ax.plot(x, f(x, *unp.nominal_values(params)), label="Fit")
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
ax.legend()
#plt.savefig("loesung.pdf")
fig.savefig("build/plot.pdf")
# end solution
# def ucurve_fit(f, x, y, **kwargs):
#     …
#     … = scipy.optimize.curve_fit(…, **kwargs)
#     … """



""" import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import uncertainties as unp
import uncertainties.unumpy as unp

# Define the curve fitting function
def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unp.correlated_values(popt, pcov)

# Define the linear function to fit
def f(x, a, b):
    return a * x + b

# Generate data
length = 100
x = np.linspace(0, 3 * np.pi, length)
rng = np.random.default_rng(seed=42)
y0 = f(x, 1, 1)  # True values
y_err = 0.2 * np.ones(length)  # Error for each data point
y = unp.uarray(y0 + rng.normal(0.0, 0.2, length), y_err)  # Noisy measurements

# Save generated data (optional, if you want to use a file)
# np.savetxt("daten.txt", np.column_stack([x, unp.nominal_values(y), y_err]), header="x\ty\ty_err")

# Solution
# x, y_0, y_err = np.genfromtxt("daten.txt", unpack=True)
# y = unp.uarray(y_0, y_err)  # Uncomment if reading from file
params = ucurve_fit(f, x, y)
print("a * x + b")
for char, p in zip("ab", params):
    print(f"{char} = {p}")

# Plotting results
fig = plt.figure(layout="constrained")
ax = fig.add_subplot()
ax.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt=".", label="Data")
ax.plot(x, f(x, *unp.nominal_values(params)), label="Fit", color='red')
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], ["0", "π", "2π", "3π"])
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title('Curve Fitting with Uncertainties')
fig.savefig("build/plot.pdf")
plt.show() """






""" import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generate synthetic data
np.random.seed(0)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # Features (independent variable)
y = 4 + 3 * X + np.random.randn(100, 1)  # Target variable (dependent variable)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print the coefficients
print(f"Intercept: {model.intercept_[0]}")
print(f"Coefficient: {model.coef_[0][0]}")

# Visualize the results
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Fitted Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.show() """
