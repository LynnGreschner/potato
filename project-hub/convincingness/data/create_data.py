import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'text': ['Regenwuermer sind sehr resilient.', 'Regenwürmer sind einfach krasse Tiere.', 'Irgendwas mit Evolution.', 'Regenwürmer sind Aliens.'],
    'id': ['Regenwurm1', 'Regenwurm2', 'Regenwurm3', 'Regenwurm4'],
})

# Save the DataFrame to a TSV file
df.to_csv('toy_worm.tsv', sep='\t', index=False)
