import wandb

def log_artifact(dir='amora-pyg/merged'):
    with wandb.init(project="ATP-1", job_type="update-dataset") as run:
        artifact = wandb.Artifact(name="training_output", type="dataset")

        artifact.add_dir(dir)
        run.log_artifact(artifact)

def download_artifact():
    run = wandb.init(project="ATP-1", job_type="download-dataset", tags=["latest"])
    artifact = run.use_artifact("training_output:latest")
    artifact_dir = artifact.download()
    print(artifact_dir)

    run.finish()
    
    return artifact_dir

def show_sample_txt_from_ds(data_set_path="./last_run_prepared/701123de2d8265eb65694b58cc962a1d/"):
    from datasets import Dataset
    from transformers import AutoTokenizer
    
    tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-6b")
    
    dataset = Dataset.load_from_disk(data_set_path)

    df = dataset.to_pandas()
    
    # LOG.info(f'# of processing items: {len(df)}')

    for row in df.head(2).itertuples():
        print('---')
        decoded_text = tokenizer.decode(row.input_ids)
        print(decoded_text)

if __name__ == "__main__":
    log_artifact()
    # download_artifact()
    # show_sample_txt_from_ds()
