from ibl_pipeline import ephys
from ibl_pipeline.plotting import ephys as ephys_plotting
import datajoint as dj
from tqdm import tqdm


dj.config['safemode'] = False

for key in tqdm((ephys.ProbeInsertion & ephys_plotting.SpikeAmpTime).fetch('KEY')):
    (ephys_plotting.SpikeAmpTime & key).delete()
    ephys_plotting.SpikeAmpTime.populate(key, suppress_errors=True)
