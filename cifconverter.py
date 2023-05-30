import pymol2

infile = "/Users/yashravipati/Downloads/PDBBind_processed/830c/830c_combined.cif"
with pymol2.PyMOL() as pymol:
     pymol.cmd.load(infile,'myprotein')
     pymol.cmd.save(infile.replace('.cif', '.pdb'), selection='myprotein')