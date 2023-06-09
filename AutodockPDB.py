import subprocess
from vina import Vina
import sys, time, os
import pymol
import numpy

v = Vina(sf_name='vina', cpu = 6, seed = 12345)

# v.set_receptor('/Users/yashravipati/Downloads/PDBBind_processed/1a4g/1a4g_protein_processed.pdb.pdbqt')

# v.set_ligand_from_file('/Users/yashravipati/Downloads/PDBBind_processed/1a4g/1a4g_ligand.mol2.pdbqt')
# v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])
root_dir = "/Users/yashravipati/Downloads/PDBBind_processed"



def dock_vina(receptor_file, ligand_file, name, center):
    v.set_receptor(receptor_file)
    v.set_ligand_from_file(ligand_file)
    v.compute_vina_maps(center=center, box_size=[30,30,30])
    try:
        v.dock(exhaustiveness=16, n_poses=1, max_evals=500000)
    except:
        print("Error")
    v.write_poses("/Users/yashravipati/Downloads/VinaOutputs/" + name, n_poses=1, overwrite=True)

i = 0
for subdir, dirs, files in os.walk(root_dir):
    i+=1
    if i<350:
        continue
    struct = subdir[len(root_dir):]
    filename = root_dir + struct + "/" + struct + "_protein_processed.pdb"
    if(struct == ""):
        continue
    center = numpy.genfromtxt(filename, skip_header=1, usecols=[6, 7, 8])
    center = center.mean(axis=0)
    try:
        print(struct)
        dock_vina(root_dir + struct + "/" + struct + "_protein_processed.pdb.pdbqt", root_dir + struct + "/" + struct + "_ligand.mol2.pdbqt", struct, center)
    except:
        continue

# x = 0
# for dirpath, dirnames, filenames in os.walk(root_dir):
#     for filename in filenames:
#         if filename.endswith(".pdbqt"):
#             # Check if the file is a receptor or a ligand
#             if "protein" in filename:
#                 receptor_file = os.path.join(dirpath, filename)
#                 x += 1
#             elif "ligand" in filename:
#                 ligand_file = os.path.join(dirpath, filename)
#                 x += 1
#                 # Dock the receptor and ligand
#             if x == 2:
#                 print(receptor_file + "\n" + ligand_file) 
#                 x=0
#                 try:
#                     dock_vina(receptor_file, ligand_file)
#                 except:
#                     print(f"Docking failed for {ligand_file} with {receptor_file}, skipping\n")
#                     pass
