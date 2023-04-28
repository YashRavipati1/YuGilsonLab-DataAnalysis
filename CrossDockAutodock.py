#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# My first example with AutoDock Vina in python
#
import os
import subprocess
from vina import Vina


v = Vina(sf_name='vina', cpu = 6, seed = 12345)

# v.set_receptor('/Users/yashravipati/Downloads/PDBBind_processed/1a4g/1a4g_protein_processed.pdb.pdbqt')

# v.set_ligand_from_file('/Users/yashravipati/Downloads/PDBBind_processed/1a4g/1a4g_ligand.mol2.pdbqt')
# v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])

def dock_vina(receptor_file, ligand_file):
    v.set_receptor(receptor_file)
    v.set_ligand_from_file(ligand_file)
    v.compute_vina_maps(center=[-12, 0, -12], box_size=[30, 30, 30])
    v.dock(exhaustiveness=32, n_poses=10, max_evals=1000000000)
    v.write_poses("/Users/yashravipati/Downloads/PDBbind-CrossDocked-Refined/dataset/%d/%s/%s_prot/%s_docked.pdbqt" % (i, struct, struct, struct), n_poses=1, overwrite=True)

root_dir = "/Users/yashravipati/Downloads/PDBbind-CrossDocked-Refined/dataset/"

struct = "5d21"
i = 10

dock_vina("/Users/yashravipati/Downloads/PDBbind-CrossDocked-Refined/dataset/%d/%s/%s_prot/%s_p.pdbqt" % (i, struct, struct, struct), "/Users/yashravipati/Downloads/PDBbind-CrossDocked-Refined/dataset/%d/%s/%s_prot/%s_l.pdbqt" % (i, struct, struct, struct))

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
