if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

python RMSD.py "/Users/yashravipati/Downloads/PDBBind_processed/456c/456c_combined.pdb" "/Users/yashravipati/Downloads/PDBBind_processed/456c/456c_docked.pdbqt"