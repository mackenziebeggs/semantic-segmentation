import os
import pandas as pd

def make_dataset_folder(folder):
    """
    Create Filename list for images in the provided path

    input: path to directory with *only* images files
    returns: items list with None filled for mask path
    """
    items = os.listdir(folder)
    items = [(os.path.join(folder, f), '') for f in items]
    items = sorted(items)
   
    pth = "/gpfs/fs0/scratch/l/leil/rbeggs/data/aecon/RGB_2_LiDAR_TESTING/Markham_3A_00000_ImageListLocation.csv"
    x = pd.read_csv(pth)
    fnames = x['ImageName']

    items_lst = []
    for x in items:
        fname = x[0].split("/")[-1]
        if fname in set(fnames):
            items_lst.append((x[0], ''))
    
    del items
    items = items_lst#[100:]
    print(f'Found {len(items)} folder imgs')
    
    """
    orig_len = len(items)
    rem = orig_len % 8
    if rem != 0:
        items = items[:-rem]

    msg = 'Found {} folder imgs but altered to {} to be modulo-8'
    msg = msg.format(orig_len, len(items))
    print(msg)
    """

    return items
