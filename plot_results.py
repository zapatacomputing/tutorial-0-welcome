
import matplotlib.pyplot as plt
from orquestra.runtime import QERuntime, RayRuntime
from orquestra.runtime import QERuntime
from orquestra.runtime._config import read_config


# replace with workflow ID returned from submit command
WORKFLOW_ID = "linreg-demo-gie4c-r000"

################# Setup Connection to Local Container #######################
# runtime = RayRuntime('.')
# workflow_results = runtime.get_workflow_run_outputs(WORKFLOW_ID)


################# Setup Connection to Remote Cluster #######################
# replace with URL of your remote cluster
CONFIG_NAME = "remote"
runtime = QERuntime.from_runtime_configuration(
    project_dir=".",
    config=read_config(CONFIG_NAME),
)

# retrieve the results
workflow_results = runtime.get_workflow_run_outputs_non_blocking(WORKFLOW_ID)


# Plot the data and the linear regression
x = workflow_results[0]
y = workflow_results[1]
model = workflow_results[2]

plt.style.use('orquestra')
plt.plot(x, y)
predicted_y = model.predict(x)
plt.plot(x, predicted_y)
plt.title("a: {:.2f}, b: {:.2f}".format(model.coef_[0][0], model.intercept_[0]))
plt.savefig("plot.png")