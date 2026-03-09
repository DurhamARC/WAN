#!/bin/bash

# Generic options:

#SBATCH --account=bddur45   # Run job under project <project>
#SBATCH --time=23:30:00        # Run for a max of 59 minutes

# Node resources:
# (choose between 1-4 gpus per node)

#SBATCH --partition=gpu # Choose either "gpu", "test" or "infer" partition type
#SBATCH --nodes=1        #!/bin/bash -l

#SBATCH --job-name=compareWANs
#SBATCH -o job_gpu-%j.out
#SBATCH -e job_gpu-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

time python ./compareWANSnoprint.py

echo "end of job"
