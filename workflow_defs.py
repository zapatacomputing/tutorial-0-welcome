import orquestra.sdk.v2.dsl as sdk
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import Tuple

THIS_IMPORT = sdk.GitImport(
    repo_url="git@github.com:zapatacomputing/tutorial-0-welcome.git",
    git_ref="linreg",
)

@sdk.task(source_import=THIS_IMPORT, n_outputs=2)
def generate_data(size: int, a: float, b: float) -> Tuple[np.ndarray, np.ndarray]:
    """Generate samples of two variables that are correlated."""
    x = np.arange(size)
    y = a * x + 5 * np.random.random(size) + b
    return (x.reshape(-1, 1), y.reshape(-1, 1))


@sdk.task(source_import=THIS_IMPORT)
def train_model(x, y) -> LinearRegression:
    """Fit a linear regression."""
    model = LinearRegression()
    model.fit(x, y)
    return model


@sdk.workflow
def linreg_demo():
    """Workflow that generates random samples and fits them using a linear
    regression."""

    size = 20
    a = 1
    b = 4
    x, y = generate_data(size, a, b)
    model = train_model(x, y)
    return [x, y, model]