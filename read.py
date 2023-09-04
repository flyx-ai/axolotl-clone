import pyarrow as pa

# Load Arrow file
# reader = pa.ipc.RecordBatchFileReader('./cache-a1d4979879391701_00007_of_00012.arrow')

# # Convert to Pandas DataFrame for readability
# data_frame = reader.read_pandas()

# # Print DataFrame
# print(data_frame)
import pyarrow.dataset as ds

directory = './701123de2d8265eb65694b58cc962a1d'

# Load Arrow dataset
dataset = ds.dataset(directory, format='parquet')

# Convert to Pandas DataFrame for readability
data_frame = dataset.to_table().to_pandas()

# Print DataFrame
print(data_frame)