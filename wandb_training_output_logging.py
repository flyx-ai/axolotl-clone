import wandb

def log_artifact(dir='amora-pyg'):
    with wandb.init(project="ATP-1", job_type="update-dataset") as run:
        artifact = wandb.Artifact(name="training_output", type="dataset")

        artifact.add_dir(dir)
        run.log_artifact(artifact)


if __name__ == "__main__":
    log_artifact()
