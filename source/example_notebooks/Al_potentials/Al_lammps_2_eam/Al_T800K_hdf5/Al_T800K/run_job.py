import sys
from pyiron_base.objects.job.wrapper import JobWrapper

debug = False
job = JobWrapper(working_directory='/cmmc/u/mpt13/PyIron_data/website/pyiron_docs/source/example_notebooks/Al_potentials/Al_lammps_2_eam/Al_T800K_hdf5/Al_T800K',
                 job_id= 779481 ,
                 debug=False )
job.run()
